import pyttsx3

speaker = pyttsx3.init()
text = "Welcome to my Home"
speaker.say(text)
speaker.runAndWait()
