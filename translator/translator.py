import translators as ts
from pprint import pprint

with open('text.txt', 'r') as text:
    textSrc = text.read()
    translation = ts.google(textSrc)
    print(translation)
    with open('translated_text.txt', 'w') as translatedText:
        translatedText = translatedText.write(translation)

# print(translatedText)