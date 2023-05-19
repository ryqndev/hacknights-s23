import speech_recognition as sr

def get_audio_snippet():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening... [10 seconds]")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, phrase_time_limit=10)

            text = r.recognize_google(audio)
            return text

    # Catch exceptions and handle them by creating a new instance of the Recognizer interface.
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        r = sr.Recognizer()
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        r = sr.Recognizer()
        