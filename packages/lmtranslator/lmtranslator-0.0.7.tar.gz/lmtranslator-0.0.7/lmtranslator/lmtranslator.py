import textlangid
from processors import TextProcessor
from transformers import pipeline, Pipeline
import torch
import pandas as pd
from datasets import Dataset
from tqdm import tqdm
import logging

logging.basicConfig(level=logging.INFO)

model_name = 'facebook/nllb-200-distilled-600M'
device = "cuda" if torch.cuda.is_available() else "cpu"
if device == "cpu":
    logging.warn("GPU not found. Translations will run on CPU.")
if device == "cuda":
    logging.info("GPU found. Translations will run on GPU.")


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
        if pd.isna(text) or not isinstance(text, str):
            text = ""
        src_lang = textlangid.detect(text)
        self.tokenizer.src_lang = src_lang
        model_inputs = self.tokenizer(text, truncation=True, padding=True, max_length=self.tokenizer.model_max_length, return_tensors="pt").to(self.device)
        model_inputs["forced_bos_token_id"] = self.tokenizer.convert_tokens_to_ids(tgt_lang)

        return model_inputs

    def _forward(self, model_inputs, **kwargs):
        output = self.model.generate(**model_inputs)
        return output

    def postprocess(self, model_output, **kwargs):
        output_text = self.tokenizer.batch_decode(model_output, skip_special_tokens=True)[0]
        postprocessed_text = TextProcessor.postprocess_for_translation(output_text)
        return postprocessed_text

    
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
        
    def translate_df(df: pd.DataFrame, src_col: str, tgt_col: str, tgt_lang: str = "eng_Latn", batch_size: int = 2):
        logging.info("Loading model. This can take a while if not cached.")
        pipe = pipeline("translation", model=model_name, device=device, batch_size=batch_size, pipeline_class=CustomTranslationPipeline)
        logging.info("Model loaded.")

        # Step 1: Clean up all input messages
        logging.info("Preprocessing model input.")
        df[f"{src_col}_clean"] = df[src_col].apply(TextProcessor.preprocess_for_translation)
        
        # Step 2: Check for duplicates in the cleaned column and create a deduplicated temporary DataFrame
        logging.info("Gathering unique input sentences.")
        unique_clean_sentences = df[f"{src_col}_clean"].dropna().unique()
        unique_df = pd.DataFrame({f"{src_col}_clean": unique_clean_sentences})

        # Step 3: Detect the language of the sentences and store it in a temporary column
        logging.info("Detecting language.")
        unique_df[f"{src_col}_lang"] = unique_df[f"{src_col}_clean"].apply(textlangid.detect)
        unique_df["tgt_lang"] = tgt_lang
        
        # Only keep rows where the source language is different from the target language and the cleaned text is longer than 3 characters
        to_translate_df = unique_df[(unique_df[f"{src_col}_lang"] != unique_df["tgt_lang"]) & (unique_df[f"{src_col}_clean"].str.len() > 3)]

        # Step 4: Translate only the sentences where src_lang != tgt_lang
        ds = Dataset.from_pandas(to_translate_df)
        results = []


        logging.info(f"Starting translation on {len(to_translate_df)} unique sentences out of {len(df)}.")
        num_batches = len(ds) // batch_size + (1 if len(ds) % batch_size != 0 else 0)

        for i in tqdm(range(num_batches), total=num_batches):
            start_idx = i * batch_size
            end_idx = min((i + 1) * batch_size, len(ds))
            batch = ds[start_idx:end_idx]

            translations = pipe(batch[f"{src_col}_clean"], tgt_lang=tgt_lang)
            results.extend(translations)

        # Step 5: Map the translations back to the original DataFrame
        logging.info("Mapping translations to original dataframe.")
        translation_map = {sentence: translation for sentence, translation in zip(to_translate_df[f"{src_col}_clean"], results)}
        df[tgt_col] = df[f"{src_col}_clean"].map(lambda x: translation_map.get(x, x))
        df = df.drop(columns=[f"{src_col}_clean"])
        logging.info("Translation finished.")
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
