# TASK 02
import speech_recognition as sr
import pyttsx3
import pywhatkit
# import datetime

listener= sr.Recognizer()
engine= pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_Command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            # listner.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa',"")
                pywhatkit.playonyt(command)
    
    except:
        pass
    return command

def run_Alexa():
    command=take_Command()
    print(command)
    if "play" in command:
        song=command.replace('play',"")
        talk('Playing' + song)
        print(song)
    # elif 'tell me the time' in command:
    #     time=datetime.datetime.now().strftime('%I:%M %p')
    #     print(time)
    #     talk('Current time is' + time)

run_Alexa()

print('Done')






#TASK 02:
# x=int(input("Till Which Number you want to generate the seriese:"))
# sum,a,b=0,1,1
# f=[]
# f.append(a)
# f.append(b)
# while sum<x:
#    sum=a+b
#    a=b
#    b=sum
#    f.append(sum)
# print(f)

