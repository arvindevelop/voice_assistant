import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)  //further if want then remove this command
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir, Please tell me how may i help you")

def takeCommand():
    #it takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        #print(e)
        print("You are not audible clearly, Please say that again")
        return "none"
    return query

def sendEmail(to,content):
     server = smtplib.SMTP('smtp.gmail.com',587)
     server.ehlo()
     server.starttls()
     server.login('arvinddevelop@gmail.com', 'arvi9471')
     server.sendmail('aks7631353674@gmail.com' ,to, content)
     server.close()

if __name__ == "__main__":
    #speak("Arvind is a good boy")
    wishMe()
    #takeCommand()
    while True:
        query = takeCommand().lower()

        # Logic for executing task based on query
        if 'wikipedia' in query:

            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
           webbrowser.open("youtube.com")

        elif 'open google' in query:
           webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
           webbrowser.open("stackoverflow.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            print(f" The time is {strTime}")
            speak(f'Sir, the time is {strTime}')

        elif 'open code' in query:
            codePath= "C://Users//aks76//AppData//Local//Programs//Microsoft VS Code//Code.exe"
            os.startfile(codePath)

        elif 'who are you' in query:
            speak('i am Jarvis assistant and work for Arvind ')

        elif 'who is sonu' in query:
            speak('sonu is my friend')

        elif 'who is anand' in query:
            speak('Anand is Arvind brother')

        elif 'who is harshit' in query:
            speak('harshit is Arvind friend')


        elif 'do you believe in god' in query:
            speak('Yes, because my developer is equivalent to god to me.')
        elif 'email to arvind' in query:
             try:
                 speak('what should i say ?')
                 content = takeCommand()
                 to = 'psclancer@gmail.com'
                 sendEmail(to,content)
                 speak("Email has been sent")
             except Exception as e:
                 #print(e)
                 speak("sorry Arvind  , email was not sent")
        elif 'ok go' in query:
            exit()
            
