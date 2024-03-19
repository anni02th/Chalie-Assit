import speech_recognition as sr
import pyttsx3
from openai import OpenAI

# Initialize OpenAI API
api_key = "sk-api"     """add your API key"""
client = OpenAI(api_key=api_key)

# Function to get user input via voice
def record_voice_and_get_input():
    r = sr.Recognizer()
    engine = pyttsx3.init()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand what you said."

# Function to ask GPT-3 and get response
def ask_gpt(input_text):
    if "what's your name" in input_text.lower() or "your name" in input_text.lower():
        return "I'm Charlie, created by Aniket."
    elif "thanks for the help" in input_text.lower() or "thanks" in input_text.lower():
        return "You're welcome! If you have any more questions or need assistance, feel free to ask. To close, press Control + C."
    else:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a general purpose chatbot"},
                {"role": "user", "content": input_text}
            ]
        )
        return completion.choices[0].message.content

# Function to respond via speech
def respond_with_voice(response):
    engine = pyttsx3.init()
    engine.say(response)
    engine.runAndWait()

# Main loop for listening to user input and responding
def main():
    try:
        while True:
            user_input_text = record_voice_and_get_input()
            print("You said:", user_input_text)
            response = ask_gpt(user_input_text)
            print("Response:", response)
            respond_with_voice(response)
    except KeyboardInterrupt:
        print("\nClosing the assistant. Thanks for intearcting with Charlie!")

if __name__ == "__main__":
    main()
