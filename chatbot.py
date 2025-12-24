import spacy
import random

# Load spaCy model
nlp = spacy.load("en_core_web_md")

# KNOWLEDGE BASE (INTENTS + RESPONSES)
intents = {
    "greeting": {
        "keywords": ["hi", "hello", "hey", "good morning", "good evening"],
        "responses": [
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Hey! Ask me anything."
        ]
    },

    "name": {
        "keywords": ["your name", "who are you", "what are you"],
        "responses": [
            "I am a chatbot created using spaCy NLP!",
            "I'm your NLP assistant.",
        ]
    },

    "purpose": {
        "keywords": ["what can you do", "your purpose", "help me", "how you work"],
        "responses": [
            "I can answer your questions using Natural Language Processing!",
            "My purpose is to assist you and respond based on your input."
        ]
    },

    "goodbye": {
        "keywords": ["bye", "goodbye", "see you", "exit"],
        "responses": [
            "Goodbye! Have a great day!",
            "See you soon!",
        ]
    }
}

# INTENT DETECTION FUNCTION
def get_intent(user_input):
    user_doc = nlp(user_input.lower())

    best_intent = None
    highest_score = 0

    for intent_name, intent_data in intents.items():
        for kw in intent_data["keywords"]:
            score = nlp(kw).similarity(user_doc)
            if score > highest_score:
                highest_score = score
                best_intent = intent_name

    return best_intent if highest_score > 0.55 else None


# CHATBOT LOOP
def chatbot():
    print("Chatbot is ready! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! 👋")
            break
# Detect intent
        intent = get_intent(user_input)

        if intent:
            response = random.choice(intents[intent]["responses"])
            print("Bot:", response)
        else:
            print("Bot: I’m not sure I understood that. Can you rephrase?")

# Run bot
if __name__ == "__main__":
    chatbot()