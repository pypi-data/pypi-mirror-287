import textlangid
from processors import TextProcessor
from transformers import pipeline, Pipeline
import torch
import pandas as pd
from datasets import Dataset
from tqdm import tqdm

model_name = 'facebook/nllb-200-distilled-600M'
device = "cuda" if torch.cuda.is_available() else "cpu"

kwargs = {
        'diversity_penalty': 1.2,
        'repetition_penalty': 1.2,
        'num_beams': 4,
        'num_beam_groups': 4,
        'num_return_sequences': 1,
        'do_sample': False,
        'encoder_repetition_penalty': 1.2,
        'no_repeat_ngram_size': 10,
        'early_stopping': True
    } 

class CustomTranslationPipeline(Pipeline):
    DEFAULT_TARGET_LANG = "eng_Latn"

    def _sanitize_parameters(self, **kwargs):
        preprocess_kwargs = {"tgt_lang": kwargs.get("tgt_lang", self.DEFAULT_TARGET_LANG)}
        return preprocess_kwargs, {}, {}

    def preprocess(self, text, tgt_lang=None, **kwargs):
        print(f"Target language: {tgt_lang}")
        # Detect language for each text using textlangid
        src_lang = textlangid.detect(text)
        self.tokenizer.src_lang = src_lang
        model_inputs = self.tokenizer(text, return_tensors="pt").to(self.device)
        model_inputs["forced_bos_token_id"] = self.tokenizer.convert_tokens_to_ids(tgt_lang)

        return model_inputs

    def _forward(self, model_inputs, **kwargs):
        output = self.model.generate(**model_inputs)
        return output

    def postprocess(self, model_output, **kwargs):
        return self.tokenizer.batch_decode(model_output, skip_special_tokens=True)[0]
    
class Translator:
    @staticmethod
    def translate(input_text, batch_size=None):
        source_lang = textlangid.detect(input_text)
        preprocessed_text = TextProcessor.preprocess_for_translation(input_text)
        if len(preprocessed_text) > 3:
            pipe_kwargs = {**kwargs}
            if batch_size is not None:
                pipe_kwargs['batch_size'] = batch_size
            pipe = pipeline('translation', model=model_name, src_lang=source_lang, tgt_lang="eng_Latn", device=device, **kwargs)
            result = pipe(preprocessed_text)
            result = result[0]["translation_text"]
            postprocessed_text = TextProcessor.postprocess_for_translation(result)
            return postprocessed_text
        else:
            return "input text too short"
        
    @staticmethod
    def translate_df(df: pd.DataFrame, src_col: str, tgt_col: str, tgt_lang: str = "eng_Latn", batch_size: int = 2):
        pipe = pipeline("translation", model=model_name, device=device, batch_size=batch_size, pipeline_class=CustomTranslationPipeline)

        ds = Dataset.from_pandas(df)
        results = []

        # Calculate number of batches
        num_batches = len(ds) // batch_size + (1 if len(ds) % batch_size != 0 else 0)

        for i in tqdm(range(num_batches), total=num_batches):
            # Select batch
            start_idx = i * batch_size
            end_idx = min((i + 1) * batch_size, len(ds))
            batch = ds[start_idx:end_idx]
            
            # Translate batch
            translations = pipe(batch[src_col], tgt_lang=tgt_lang)
            results.extend(translations)

        df[tgt_col] = results
        return df
        
    @staticmethod
    def translate_with_llm(input_text, pipe):
        if len(input_text) > 3:
            messages = [
                {"role": "system", "content": 'You are a highly intelligent language model capable of detecting the language of a given text and translating it accurately into English.\nWhen provided with a text, you will:\nIdentify the language of the text.\nTranslate the text into English.\nReturn the translation in JSON format.\nEnsure your translation is as accurate and contextually appropriate as possible.\nIf you encounter any issues, provide the best possible translation.\nFollow this template for your response: {"translation": "<translation here>"}.'},
                {"role": "user", "content": f'Input: "{input_text}"'},
            ]
            
            outputs = pipe(
                messages,
                max_new_tokens=256,
            )

            output = (outputs[0]["generated_text"][-1])
            output = output["content"]
            return output

        else:
            return "input text too short"
        
    @staticmethod
    def load_llm_for_translation():
        # model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"
        model_id = "aifeifei798/DarkIdol-Llama-3.1-8B-Instruct-1.0-Uncensored"

        pipe = pipeline(
            "text-generation",
            model=model_id,
            model_kwargs={"torch_dtype": torch.bfloat16},
            device_map="auto",
        )

        return pipe
