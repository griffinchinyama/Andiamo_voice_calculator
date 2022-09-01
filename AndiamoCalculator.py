from tkinter import *
import speech_recognition as sr
import pyttsx3
import threading

#initializing voice recoginition using pyttsx3 package
voiceEngine = pyttsx3.init()
#creating GUI window called rootwindow to hold all buttons and text fields
rootWindow = Tk()  # This is to create a basic window
rootWindow.geometry("612x624")  # this is for the size of the window
rootWindow.resizable(False, False)  # this is to prevent from resizing the window
rootWindow.title("ANDIAMO PVT SECONDARY SCHOOL : VOICE CALCULATOR")

canSpeak = True


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def speak_voice():
    global canSpeak
    canSpeak = True
    if canSpeak:
        voiceEngine.say("Calculator is ready, you can speak")
        voiceEngine.runAndWait()
        speech_calculator()



def mute_voice():
    global canSpeak
    canSpeak = False
    voiceEngine.say("Muted")
    voiceEngine.runAndWait()
    #speech_calculator()


# 'bt_clear' function :This is used to clear
# the input field

def bt_clear():
    global expression
    expression = ""
    input_text.set("")


# speaking before loading
def speak_title():
    voiceEngine.setProperty("rate", 150)
    voiceEngine.say("WELCOME TO ANDIAMO SECONDARY SCHOOL VOICE CALCULATOR")
    voiceEngine.runAndWait()
# 'bt_equal':This method calculates the expression
# present in input field


def bt_equal():
    global expression
    #split_expression = expression.split()
   # for x in split_expression:
        #print(split_expression)
    try:
        result = str(eval(expression))  # 'eval':This function is used to evaluates the string expression directly
        input_text.set(result)
        expression = result
    except:
        voiceEngine.setProperty("rate", 150)
        voiceEngine.say("Error")
        voiceEngine.runAndWait()


expression = ""

# 'StringVar()' :It is used to get the instance of input field

input_text = StringVar()

# Let us creating a frame for the input field

input_frame = Frame(rootWindow, width=312, height=100, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=1)

input_frame.pack(side=TOP)

# Let us create a input field inside the 'Frame'

input_field = Entry(input_frame, font=('arial', 50, 'bold'), textvariable=input_text, width=500, bg="#eee", bd=0,
                    justify=CENTER)

input_field.grid(row=0, column=1)

input_field.pack(ipady=50)  # 'ipady' is internal padding to increase the height of input field

# Let us creating another 'Frame' for the button below the 'input_frame'

btns_frame = Frame(rootWindow, width=100, height=200, bg="#68bee3")

btns_frame.pack()

# first row

clear = Button(btns_frame, text="Clear", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

# second row

seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)

eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)

nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)

multiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                  command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

# third row

four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)

five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)

six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)

minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

# fourth row
one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)

two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)

three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)

plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
              command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

# fourth row
zero = Button(btns_frame, text="0", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(0)).grid(row=4, column=0, padx=1, pady=1)

power = Button(btns_frame, text="power", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click("**")).grid(row=4, column=1, padx=1, pady=1)

point = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)

equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1)

speak = Button(btns_frame, text="SPEAK", fg="black", width=10, height=3, bd=0, bg="#26b51f", cursor="hand2",
               command=lambda: speak_voice()).grid(row=5, column=0, padx=1, pady=1)

mute = Button(btns_frame, text="MUTE", fg="black", width=10, height=3, bd=0, bg="#e3173c", cursor="hand2",
                command=lambda: mute_voice()).grid(row=5, column=2, padx=1, pady=1)


# SPEECH TO TEXT LOGIC
def speech_calculator():
    r = sr.Recognizer()
    with sr.Microphone() as source:
    #print("speak Anything : ")
        audio = r.listen(source)
    counter = 1
    while counter < 2:
        if canSpeak:
            formula = ''
            try:
                text = r.recognize_google(audio)
                formula = str(text)
                print(formula)
                #voiceEngine.say()
                #input_text.set(formula)
                #voiceEngine.runAndWait()
                try:
                    rst = str(eval(text))
                    input_text.set("Answer :"+rst)
                    # print('You said : {}'.format(text))
                    voiceEngine.say("the answer is :" + rst)
                    voiceEngine.runAndWait()
                except:
                    voiceEngine.say("try again")
                # voiceEngine.setProperty("rate", 150)
                #voiceEngine.say("you said " + text)
                #voiceEngine.runAndWait()
            except:
                voiceEngine.say('sorry could not recognize your voice')
                voiceEngine.runAndWait()
        counter = counter+1

rootWindow.after("150",speak_title)
rootWindow.mainloop()
