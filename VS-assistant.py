from errno import ENOMSG
import pyttsx3 #pip install pyttsx3 = text data into speech
import datetime
import speech_recognition as sr
import smtplib
#from Secrets import senderemail, epwd, to 
import pyautogui
import webbrowser as wb
from time import sleep
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard
import wikipedia
import os
import pyjokes
import time as tt
import psutil
from nltk.tokenize import word_tokenize 

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def getvoices(voice):
    voices = engine.getProperty('voices')
    if voice==1:
        engine.setProperty('voice',voices[0].id)
        speak("hello this is ramanan")
    if voice==2:
        engine.setProperty('voice', voices[1].id)
        speak("Hello this is Amanda")  


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("Today's date is")
    speak(day)
    speak(month)
    speak(year)


def greeting():
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    elif hour>=18 and hour<=24:
        speak("Good Evening")


def wishme():
  speak("Welcome Abhijit")
  #date()
  #greeting()
  speak("How may I help you")


def takeCommandCmd():
    query=input("How can I help you?")
    return query


def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language="en-IN" )
        print(query)
    except Exception as e:
        print(e)
        speak("Could you repeat that please?")
        return "None"
    return query


# def sendEmail():
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(senderemail, epwd)
#     server.sendmail(senderemail, to, 'hello this is a test')
#     server.close
# sendEmail()


def sendWhatsapp(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(5)
    pyautogui.press('enter')


def searchgoogle():
    speak("What should I search for")
    search = takeCommandMic()
    wb.open('https://www.google.com/search?q='+search)


def news():
    newsapi =  NewsApiClient(api_key='')#add api key
    speak("What news do you want")
    topic = takeCommandMic()
    data = newsapi.get_top_headlines(q=topic,language='en',page_size=5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak(f'{x}{y["description"]}')
    speak("thats all")


def textspeech():
    text = clipboard.paste()
    print(text)
    speak(text)


def screenshot():
    name_img = tt.time()
    name_img = f'C:\\Users\\abhij\\Desktop\\Virtual Assistant Test\\screenshot\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at "+ usage+"percent")
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent+"percent")


if __name__ == "__main__":
    getvoices(2)
    wishme()
    while True:
        query=takeCommandMic().lower()

        if 'hello amanda' in query:
            speak("Hello")

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'message' in query:
            user_name ={
                'David':''#add number
            }
            try:
                speak("Who do you want to send the message to")
                name = takeCommandMic()
                phone_no = user_name[name]
                speak("what is your message")
                message = takeCommandMic()
                sendWhatsapp(phone_no,message)
                speak("message sent")
            except Exception as e:
                print(e)
                speak("Please try again")
        
        elif 'wikipedia' in query:
            speak("Searching..")
            query = query.replace ("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)


        elif 'search' in query:
            searchgoogle()

        elif 'youtube' in query:
            speak("what should I search for")
            topic=takeCommandMic()
            pywhatkit.playonyt(topic)

        elif 'weather' in query:
            url = "http://api.openweathermap.org/data/2.5/weather?q=thiruvananthapuram&appid=//your api key"
            #url="https://api.openweathermap.org/data/weather?q=trivandrum&units=imperial&appid="
            res = requests.get(url)
            data = res.json()
            weather = data['weather'] [0] ['main']
            temp = data['main']['temp']
            desp = data['weather'][0]['description']
            temp = round((temp-32)*5/9)
            speak('Temperature:{}'.format(temp))
            speak('Weather is{}'.format(desp))

        elif 'news' in query:
            news()

        elif 'text' in query:
            textspeech()

        elif 'open' in query:
            os.system('explorer C://{}'.format(query.replace('Open','')))

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'screenshot' in query:
            screenshot()

        elif 'remind' in query:
            speak("What should I remind you")
            data = takeCommandMic()
            speak("Okay reminding you to do the following"+ data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close

        elif 'remember' in query:
            speak("You asked me to remember that")
            remember= open('data.txt','r')
            speak(remember.read())

        elif 'cpu' in query:
            cpu()

        elif 'offline'in query:
            speak("Okay Byeeee")
            quit()

