import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone()

def listen():
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("\n🎤 Speak now...")
        audio = recognizer.listen(source)
    return recognizer.recognize_google(audio)
