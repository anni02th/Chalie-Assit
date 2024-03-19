import speech_recognition as sr
import pyttsx3
from openai import OpenAI
from gtts import gTTS
from io import BytesIO
from base64 import b64decode
import wave
import subprocess

# Your OpenAI API key
api_key = "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"
client = OpenAI(api_key=api_key)

def getUserInput():
    some_text = input('Hi I am Charlie, How can I help you? \n-> ')
    return some_text

def askGPT():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a general purpose chatbot"},
            {"role": "user", "content": getUserInput()}
        ]
    )
    response_from_chatGPT = completion.choices[0].message.content
    return response_from_chatGPT

# #Save as MP3 file
# def speakNow(content):
#     tts = gTTS(content)
#     tts.save('1.mp3') 
#     subprocess.run(["start", "1.mp3"], shell=True)   #Open MP3 file with the default audio player

def speakNow(content):
    engine = pyttsx3.init()
    engine.say(content)
    engine.runAndWait()
    
wanna_ask_more = 'y'
while wanna_ask_more == 'y':
    ans = askGPT()
    print('Answer: ',ans) 
    speakNow(ans)
    print('-------------- ')
    wanna_ask_more = input("Wanna ask more questions? y/n - ")

r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
