# Rule-Based Chatbot (Python)

A simple **rule-based chatbot** built using Python that responds to user messages using **predefined rules**, `if-elif-else` conditions, and basic **pattern matching (regex)**.

---

## Features

Greeting responses (Hi / Hello / Hey)  
Good Morning responses (GM / Morning)  
Bot introduction (Your name)  
User name detection (`my name is ...`)  
Current time response  
Current date response  
Day in week response (Today is Monday/Tuesday...)  
Help & support response  
Feature list response  
Exit responses (bye / exit / quit / good night / gn etc.)

---

## Technologies Used

- Python 3.x
- `re` module (Regex)
- `datetime` module


## How to Run

1. Clone the repository:
```bash
git clone https://github.com/SaiDeepthi-22/CHATBOT-WITH-RULE-BASED-RESPONSES
```
```bash
cd CHATBOT-WITH-RULE-BASED-RESPONSES
```
```bash
python main.py
```
### Sample Conversation
Rule-Based Chatbot is running! Type 'bye' to exit.
You: hi
Bot: Hello! :) How can I help you today?
You: what day is today
Bot: Today is Friday
You: time
Bot: The current time is 09:10 PM
You: gn
Bot: Goodbye! Have a great day!
### How It Works
The chatbot cleans user input using:
- lowercasing
- trimming spaces
- removing punctuation
- Then it checks conditions like:
greetings
time/date/day queries
user name extraction using regex
exit keywords
If no rule matches, it gives a fallback response.
### Supported Keywords
Greetings:
hi, hello, hey, hii, hola

Morning:
good morning, gm, morning

Exit:bye, goodbye, exit, quit, gn, good night, goodnight
### Future Improvements 
- Add multiple jokes using random
- Add calculator support (add/sub/mul/div)
- GUI using Tkinter
- Store chat history in a text file
### Author
Samatham Sai Deepthi