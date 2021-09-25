from googletrans import Translator

def translate(text):
    translator = Translator()
    translation = translator.translate(text=text, dest ='te') #te means telugu
    return translation.text