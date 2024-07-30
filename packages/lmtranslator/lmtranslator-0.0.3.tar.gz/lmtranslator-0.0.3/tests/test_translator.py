import lmtranslator

def test_translation():
    translated_text = lmtranslator.translate("Je vais au magazin.")
    assert translated_text == "I'm going to the store."