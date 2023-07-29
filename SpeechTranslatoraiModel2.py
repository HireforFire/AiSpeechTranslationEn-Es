import speech_recognition as sr
import pyttsx3
from transformers import MarianMTModel, MarianTokenizer
from langdetect import detect


# create a recognizer object, a tokenizer object, and a Text-to-speech object
r = sr.Recognizer()
tokenizer_es = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-es-en")
model_es = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-es-en")
tokenizer_en = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-es")
model_en = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-es")
tts = pyttsx3.init()

while True:
    # use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Speak something...")
        # adjust the ambient noise level
        r.adjust_for_ambient_noise(source)
        # listen for audio input from the user
        audio = r.listen(source)
    try:
        # recognize speech using Google Speech Recognition
        text = r.recognize_google(audio)
        input_language = detect(text)
        # translate speech to English if detected language is Spanish
        if input_language == "es":
            input_ids = tokenizer_es.encode(text, return_tensors="pt")
            translated_ids = model_es.generate(input_ids)
            translated_text = tokenizer_es.decode(translated_ids[0], skip_special_tokens=True)
            print(f"Translated to English: {translated_text}")
            # speak the translated text
            tts.say(translated_text)
            tts.runAndWait()
        # translate speech to Spanish if detected language is English
        elif input_language == "en":
            input_ids = tokenizer_en.encode(text, return_tensors="pt")
            translated_ids = model_en.generate(input_ids)
            translated_text = tokenizer_en.decode(translated_ids[0], skip_special_tokens=True)
            print(f"Translated to Spanish: {translated_text}")
            # speak the translated text
            tts.say(translated_text)
            tts.runAndWait()
        else:
            print("Unsupported language")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
