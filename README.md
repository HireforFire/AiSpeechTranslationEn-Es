**Code: speech_translation.py**

```python
import speech_recognition as sr
import pyttsx3
from transformers import MarianMTModel, MarianTokenizer
from langdetect import detect

r = sr.Recognizer()
tokenizer_es = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-es-en")
model_es = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-es-en")
tokenizer_en = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-es")
model_en = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-es")
tts = pyttsx3.init()

while True:
    with sr.Microphone() as source:
        print("Speak something...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        input_language = detect(text)
        if input_language == "es":
            input_ids = tokenizer_es.encode(text, return_tensors="pt")
            translated_ids = model_es.generate(input_ids)
            translated_text = tokenizer_es.decode(translated_ids[0], skip_special_tokens=True)
            print(f"Translated to English: {translated_text}")
            tts.say(translated_text)
            tts.runAndWait()
        elif input_language == "en":
            input_ids = tokenizer_en.encode(text, return_tensors="pt")
            translated_ids = model_en.generate(input_ids)
            translated_text = tokenizer_en.decode(translated_ids[0], skip_special_tokens=True)
            print(f"Translated to Spanish: {translated_text}")
            tts.say(translated_text)
            tts.runAndWait()
        else:
            print("Unsupported language")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
```

**README.md**

```markdown
# Speech Translation with Text-to-Speech

This repository contains a Python script that demonstrates real-time speech translation using the `speech_recognition`, `transformers`, `pyttsx3`, and `langdetect` libraries. The script allows you to speak in either English or Spanish, and it will translate your speech to the other language while providing an audible response.

## Prerequisites

- Python 3.6 or higher
- `speech_recognition`, `transformers`, `pyttsx3`, `langdetect` libraries: You can install these using pip:

```bash
pip install SpeechRecognition transformers pyttsx3 langdetect
```

## Usage

1. Clone the repository and navigate to the project directory.

```bash
git clone https://github.com/yourusername/speech-translation.git
cd speech-translation
```

2. Run the Python script.

```bash
python speech_translation.py
```

3. Speak into your computer's microphone when prompted. The script will detect the language you spoke in and translate it to the other language.

## How it Works

The script initializes recognizer objects for speech recognition and tokenizer and model objects for machine translation using the `transformers` library. It also sets up a text-to-speech engine using `pyttsx3`.

The main loop continuously listens to your speech input using the default microphone as the audio source. It then uses Google Speech Recognition to convert the speech to text. The script detects the language of the input using `langdetect`.

If the detected language is Spanish (`es`), the script translates the input text to English using the pre-trained `MarianMTModel` and `MarianTokenizer` for Spanish to English translation. The translated text is then spoken out loud using the text-to-speech engine.

If the detected language is English (`en`), the script translates the input text to Spanish using the pre-trained `MarianMTModel` and `MarianTokenizer` for English to Spanish translation. Again, the translated text is spoken using the text-to-speech engine.

If the detected language is neither English nor Spanish, the script will display an "Unsupported language" message.

## Contributing

Contributions to this project are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. Feel free to use and modify the code as per the terms of the license.
```

This condensed version still contains all the necessary information to explain the purpose of the code and how to use it on GitHub. It eliminates some of the detailed explanations while retaining the essential instructions and details.
