
from gtts import gTTS
import speech_recognition as sr
import os 
import webbrowser
import smtplib

def TalkToMe(audio):
    print(audio)
    tts = gTTS(text=audio,lang='en')
    tts.save(audio.mps)
    os.system('mpg123 audio.mp3')

def myCommand():
    r = sr.Recogizer()

    with sr.Microphone() as source:
        print("I am ready for your next command")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:" + command + "\n")
    
    except sr.UnknownValueError:
        assistant(myCommand())

    return command

def assistant(command):

    if 'nike' in command:
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application"
        url = "https://www.nike.com/"
        webbrowser.get(chrome_path).open(url)

        if "What\'s up" in command:
            TalkToMe("Just doing my job")
        
        if "email" in command:
            TalkToMe("who is the recipient")
            recipient = myCommand()
            
            if "bella" in recipient:
                TalkToMe("What should I say")
                content = myCommand()
                
                #init gmail SMTP
                mail = smtplib.SMTP("smtp.gmail.com", 587)

                #identity to server
                mail.ehlo()

                #encrypt session
                mail.starttls()

                #login
                mail.login("Username", "Password")

                #send message
                mail.sendmail("PERSON NAME","Email address",content)

                #close mail connection
                mail.close

                TalkToMe("Email sent")

TalkToMe("I am ready for your next command")

while True:
    assistant(myCommand())

            