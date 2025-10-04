# A simple AI chatbot with a friendly personality
import json
import random

# Load responses from JSON
with open("responses.json", "r") as file:
    responses = json.load(file)



print ("FriendlyBot: Hi! Type 'exit'to end the chat. ")


def respond(user_input):
    user_input = user_input.lower()

    if user_input in ["hi", "hello", "hey"]:
     return random.choice(responses["greeting"])

    elif "how are you" in user_input:
        return "I'm feeling great, thanks for asking! How about you?"

    elif "help" in user_input:
        return random.choice(responses["help"])

    elif user_input.startswith(("bye", "goodbye", "see you")):
        return random.choice(responses["farewell"])

    else:
        return random.choice(responses["unknown"])
    






