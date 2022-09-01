import speech_recognition as sr
import pyttsx3


class Voice2Text:
    voiceEngine = pyttsx3.init()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak Anything : ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            rst = str(eval(text))
            #print('You said : {}'.format(text))
            print("result is :"+rst)

            voiceEngine.setProperty("rate", 150)
            voiceEngine.say("you said "+text)
            voiceEngine.runAndWait()

        except:
            print('sorry could not recognize your voice')
