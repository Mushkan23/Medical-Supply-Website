import re
import random


class Brain:
    def __init__(self, intents):
        self.intents = intents

    def get_response(self, user_message):
        error_message = "sorry, i didn't  understand"
        if not user_message:
            return error_message

        user_message = user_message.lower()
        intent = self.get_intent(user_message)

        if intent:
            response = random.choice(intent["responses"])
        else:
            response = error_message
        return response

    def get_intent(self, user_message):
        for intent in self.intents.get("intents"):
            for pattern in intent["patterns"]:            
                if re.search(pattern.lower(), user_message):
                    return intent

