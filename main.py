import re
from datetime import datetime

def clean_text(text):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)  
    return text
def chatbot_response(user_input):
    user_input = clean_text(user_input)
    if user_input in ["hi", "hello", "hey", "hii", "hola"]:
        return "Hello! :) How can I help you today?"
    elif any(word in user_input for word in ["good morning", "gm", "morning"]):
        return "Good morning!  How can I help you today?"
    elif "your name" in user_input:
        return "I am a Rule-Based Chatbot . You can call me ChatBot!"
    elif re.search(r"\bmy name is\b", user_input):
        name = user_input.replace("my name is", "").strip().title()
        return f"Nice to meet you, {name}! "
    elif "time" in user_input:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time} "
    elif "date" in user_input or "dt" in user_input:
        current_date = datetime.now().strftime("%d %B %Y")
        return f"Today's date is {current_date} "
    elif "day in week" in user_input or "what day is today" in user_input or "which day" in user_input:
        today_day = datetime.now().strftime("%A")
        return f"Today is {today_day} "
    elif "help" in user_input or "support" in user_input:
        return "Sure! I can help you with general queries like time, date, greetings, and FAQs. :>"
    elif "what can you do" in user_input or "features" in user_input:
        return ("I am a rule-based chatbot.\n"
                "Greetings\nName interaction\nDate & time\nBasic FAQs\nGoodbye")
    elif user_input in ["bye", "goodbye", "see you", "exit", "quit", "gn", "good night", "gud night", "goodnight"]:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry :( I didn't understand that. Try asking something else!"
print(" Rule-Based Chatbot is running! Type 'bye' to exit.\n")
while True:
    user = input("You: ")
    reply = chatbot_response(user)
    print("Bot:", reply)
    if clean_text(user) in ["bye", "goodbye", "exit", "quit"]:
        break
