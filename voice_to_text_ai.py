# Voice to Text
# pip install SpeechRecognition
# pip install pocketsphinx
import speech_recognition as sr
def Voice_To_Text():
    recognizer = sr.Recognizer()
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)
    # recognize speech using Sphinx
    text_result = recognizer.recognize_sphinx(audio)
    return text_result
if __name__ == "__main__":
    output = Voice_To_Text()
    if output:
        print("Transcribed Text:")
        print(output)