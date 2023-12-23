import random
import SpeechRecognition as sr

def greet():
    responses = ["Hello! How can I assist you today?", "Greetings! What can I do for you?", "Hi there! How can I help you?"]
    return random.choice(responses)

def respond(user_input):
    greetings = ['hello', 'hi', 'hey', 'greetings']
    farewells = ['bye', 'goodbye', 'see you', 'take care']
    
    if any(word in user_input.lower() for word in greetings):
        return greet()
    elif any(word in user_input.lower() for word in farewells):
        return "Goodbye! Take care."
    else:
        return "I'm sorry, I don't understand that command."

if __name__ == "__main__":
    recognizer = sr.Recognizer()

    print("Welcome to Jarvis-like Assistant!")

    while True:
        print("Type or speak your command:")
        
        user_input = input("You (type): ")

        if user_input.lower() in ['exit', 'quit', 'goodbye']:
            break

        # If user doesn't type, try speech recognition
        if not user_input:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)

            try:
                user_input = recognizer.recognize_google(audio)
                print("You (voice):", user_input)
            except sr.UnknownValueError:
                print("Sorry, I could not understand your audio.")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

        response = respond(user_input)
        print("Jarvis:", response)
