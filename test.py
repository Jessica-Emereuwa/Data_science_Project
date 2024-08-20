# Import necessary packages
import streamlit as st
import speech_recognition as sr
import nltk
from nltk.chat.util import Chat, reflections

# Download nltk resources if not already downloaded
nltk.download('punkt')

# Load the text file and preprocess the data using the chatbot algorithm
# Here you can define your own chatbot responses or use an existing one
pairs = [
    ['hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']],
    ['how are you?', ['I am doing well, thank you!', 'I\'m fine, thanks!', 'All good, thanks for asking!']],
    ['what is your name?', ['I am a chatbot.', 'You can call me a chatbot.']],
    ['bye|goodbye', ['Goodbye!', 'Bye!', 'Take care!']],
]

# Define a function to transcribe speech into text using the speech recognition algorithm
def transcribe_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = r.listen(source)
        st.write("Transcribing...")
        try:
            text = r.recognize_google(audio)
            st.write(f"User said: {text}")
            return text
        except sr.UnknownValueError:
            st.write("Sorry, I couldn't understand the audio.")
            return ""
        except sr.RequestError as e:
            st.write(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

# Modify the chatbot function to take both text and speech input
def chatbot(input_text):
    chat = Chat(pairs, reflections)
    return chat.respond(input_text)

# Create a Streamlit app
def main():
    st.title("Speech-enabled Chatbot")
    option = st.radio("Select input type:", ("Text", "Speech"))

    if option == "Text":
        user_input = st.text_input("You:", "")
        if st.button("Send"):
            response = chatbot(user_input.lower())
            st.text_area("Chatbot:", value=response, height=200, max_chars=None, key=None)
    elif option == "Speech":
        if st.button("Start Recording"):
            text = transcribe_speech()
            if text:
                response = chatbot(text.lower())
                st.text_area("Chatbot:", value=response, height=200, max_chars=None, key=None)

if __name__ == "__main__":
    main()
