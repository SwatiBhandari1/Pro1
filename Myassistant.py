import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os




engine=pyttsx3.init("sapi5")   #sapi 5 provides an api to use inbuilt voice of microsoft
voice=engine.getProperty('voices')
#print(voice[0].id) it will give female voice
engine.setProperty('voice',voice[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    """ 
    This function takes 
    the time from
    the system and
    wishes the user .  
    """
    time=datetime.datetime.now().hour
    #print(time)
    if 0<=time and 12>time:
        speak("Good Morning!!!!!!")
    elif 12<=time and 16>time:
        speak("Good Afternoon !!!!!!")
    if 16<=time and 23>time:
        speak("Good evening!!!!!!")
    speak("I am your assistant.....How can i help you")
  
def takeCommand():
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....\n")
            r.pause_threshold=0.5
            audio=r.listen(source)
        try:
            print("Recognizing....\n")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said :{query}")
          
        except Exception as e:
            print("say that again please....")
            return "None"
        return query




if __name__ == '__main__':
    wishMe()
    while(True):
        query=takeCommand().lower()
        
        
        if "wikipedia" in query:
            speak("Searching wikipedia..")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(result)
            print(result)
        elif datetime.datetime.today()==11:
            speak("Happy birthday")
        elif "hello" in query:
            speak("How can i help you?")
        elif "how to exit" in query:
            speak("Say exit.")
        elif "play music" in query:
            print("play music")
            speak("playing music")
            dir='F:\\songs\\my_song'
            songs=os.listdir(dir)
            print(songs)
            os.startfile(os.path.join(dir,songs[0]))
        elif "stack overflow" in query:
            speak("opening stackoverflow")
            wb.open('stackoverflow.com')
   
        elif "google" in query:
            speak("opening google")
            wb.open('google.com')
        elif "youtube" in query:
            speak("opening youtube")
            wb.open('youtube.com')
        elif "facebook" in query:
            speak("opening facebook")
            wb.open('facebook.com')
        elif "what is the time" in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {time}")
        elif "notepad" in query:
            path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Notepad++"
            os.startfile(path)
        elif"android studio" in query:
            d_path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Android Studio"
            os.startfile(d_path)
        elif "you are nice" in query:
            speak("it is my job.")
        
        elif"exit" in query:
            speak("Thank you for using me. Have a nice day")
            exit()
        else:
            speak("Unable to get it please say again")

#end
#in github

























        

