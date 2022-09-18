# pip install  pyttsx3    ###pyttsx3 is a text-to-speech conversion library in Python .
# pip install  speech_recognition   ## speech recognition, the process of understanding the words that are spoken by human beings.
# pip install  pyaudio   ## the cross-platform audio I/O library.
# pip install  wikipedia


import pyttsx3    
import speech_recognition as sr
import wikipedia
import webbrowser
import keyword
from tabulate import tabulate

d = [ ["Fariha", 'Khan', 6],   #LIST
     ["Kinza", 'Mushtaq', 13], 
     ["Naveen", 'Nizam', 29]]

print(tabulate(d, headers=["Name", "L.Name", "Roll_no."]))


# init pyttsx
#speech engines based on your operating system:
##sapi5 for Window , nsss for MacOS ,espeak for Linux
engine = pyttsx3.init("sapi5")   
voices = engine.getProperty("voices")  ## voices use for male or female by default male

engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice


def speak(audio):
    engine.say(audio)  ##Lines the command to talk an expression.
    engine.runAndWait()   ##locks while handling all current lined orders


def take_command():
    r = sr.Recognizer()  
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1   ##as the loudness of the audio files
        audio = r.listen(source)   ##listen() method which puts the server into listen mode
    try: 
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        ##  Recognizer_google function uses Google’s free web search API.
        print("User said:" + query + "\n")
        speak('you said' + query)
        
    except Exception as e:
        print(e)
        speak("I didnt understand")
        return "None"
    return query


if __name__ == '__main__':

    speak("Faakina assistance activated ")
    speak("How can i help you")
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            webbrowser.open('https://en.wikipedia.org/wiki/' + results)
        elif 'calculator' in query:
            class calculator():
                def __init__(self,x,y):
                  self.x=x
                  self.y=y
            
                def add(self):
                  print("Sum :",self.x+self.y)
            
                def subtraction(self):
                  print("Subtraction :",self.x-self.y)  
            
                def multiplication(self):
                  print("Multiplication :",self.x*self.y)
                def table(self):
                  for i in range(1, 11):
                    print(self.x , 'x', i, '=', self.x*i)

            n1=calculator(197,4) # object 
            n1.table()
            n1.add()
            n1.subtraction()
            n1.multiplication()
        elif 'show keyword' in query:
            print(keyword.kwlist)
        elif 'who are you' in query:
            speak("I am Faakina. voice controlled  virtual assistant")
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.open('https://web.whatsapp.com')
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
        elif 'wait' in query:
            speak('OK! I am waiting')
        elif 'sleep' or 'stop' in query:
            exit(0)
