import pyttsx3

def text_to_speech():
    engine = pyttsx3.init()
    text = input("Enter the text you want to convert to speech: ")
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    text_to_speech()
