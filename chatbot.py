#Creating my own AI

#importing modules
import random
import re
from datetime import datetime


#Starting with a simple chatbot
def chat_bot():
    responses = {
        "hi":"Hi there! \n What can I do for you today?",
        "hello":"Hi there! \n What can I do for you today?",
        "how are you":"I am very well, thank you!",
        "bye":"Happy to have being of help, take care!",
        "what is your name":"I do not have a name yet but I am an AI!",
        "help":"I can chat with you, tell me what you want me to do",
        "time":"The time is:    ",
        "date":"Today's date is:    ",
        "joke":["Why don't scientists trust atoms? Because they make up everything!",
                "What did one wall say to another wall? I'll meet you at the corner!"],
        "weather":"I don't have access to that data yet!",
        "good":"That's great to hear!",
        "bad":"I am sorry to hear that. Is there anything I can help with?"
    }

    user_name = "friend"
    #Adding Conversation Context
    conversation_count = 0

    print("Bot:  Hi there! What can I do for you today?")

    while True:
        user_input =  input("User:  ").lower().strip()
        conversation_count += 1

        #pattern matching - check if any keyword is in the input
        found = False

        #Making an Exit Condition
        if "bye" in user_input:
            break

        elif "time" in user_input:
            current_time = datetime.now().strftime("%H:%M:%S")
            print("Bot: The time is:", current_time)
            print(f"Turn: {conversation_count}")
            found = True

        elif "date" in user_input:
            current_date = datetime.now().strftime("%Y-%m-%d")
            print("Bot:  Today's date is: ", current_date)
            print(f"Turn: {conversation_count}")

        elif "joke" in user_input:
            joke = random.choice(responses["joke"])
            print("Bot:  ", joke)
            print(f"Turn:  {conversation_count}")
            found = True

        elif "my name is" in user_input:
            name_match =  re.search(r"my name is (.+)", user_input)
            if name_match:
                user_name = name_match.group(1).capitalize()
                print(f"Bot:  Nice to meet you, {user_name}!")
                print(f"Turn:  {conversation_count}")
                found = True

        elif "what is my name" in user_input:
            print(f"Bot: Your name is {user_name}, right?")
            print(f'Turn:  {conversation_count}')
            found = True

        else:
            for key in responses:
                if key in user_input and key not in ["time","date","joke"]:
                    if key == "good" and "not good" in user_input:
                     continue #it skips if it is "not good"
                    if key == "bad" and "not bad" in user_input:
                     continue #same as above but "bad"

                    print("Bot: ", responses[key])
                    print(f"Turn: {conversation_count}")
                    found = True
                    break

        if not found:
            print("Bot: I am sorry but I need to be upgraded to understand your prompt")



chat_bot()