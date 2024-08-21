# TEXT BASED CHAT BOT USING PYTHON:


import time

# Function to get the current time
def get_current_time():
    return time.ctime()

# Dictionary to store key and value pairs
questions = {
    "hey": "Hi there! How can I assist you today?",

    "what is your name": "I'm Haider's chatbot.",

    "how are you": "I'm doing great, thank you! How about you?",

    "i am good": "That's wonderful to hear! How can I help you today?",

    "what is the time": get_current_time(),

    "quit": "Goodbye! Have a great day!"
}

# Function to get a response from the chatbot
def get_response(user_input):
    return questions.get(user_input.lower(), "I'm sorry, I didn't understand that. Can you please rephrase?")

# Main function to run the chatbot
def chatbot():
    print("WELCOME TO CHATBOT SIR! :)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: " + questions["quit"])
            break
        response = get_response(user_input)
        print("Chatbot: " + response)

# Run the chatbot
chatbot()


















