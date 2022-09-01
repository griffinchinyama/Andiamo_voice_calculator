import pyttsx3

voiceEngine = pyttsx3.init()

voiceEngine.setProperty("rate", 150)
voiceEngine.say("5-67")
voiceEngine.runAndWait()


class Speak:

    def __init__(self, textmsg):
        self.txt = textmsg

    def printname(self):
        voiceEngine.setProperty("rate", 150)
        voiceEngine.say("2-4")
        voiceEngine.runAndWait()


# Use the Person class to create an object, and then execute the printname method:
