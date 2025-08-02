#Creating my own AI

#importing modules
import random
import re
from datetime import datetime
import json
import nltk
from textblob import TextBlob
#Making it more alive, I will have to add more important modules

#Starting with a simple chatbot
#Downloading required nltk data, to be run once
# try:
#     nltk.download('punkt', quiet=True)
#     nltk.download('stopwords', quiet=True)
# except:
#     pass

#Adding a Class

class Chatbot():
    def __init__(self):
        self.responses = {
            "greetings": ["hi", "hello", "hey", "greetings", "good morning", "good afternoon", "how far"],
            "farewells": ["bye", "goodbye", "see you", "farewell", "take care"],
            "wellbeing": ["how are you", "how do    you feel", "how are you doing"],
            "identity": ["what is your name", "who are you", "what are you"],
            "help": ["help", "what can you do", "assist me"],
            "time": ["time", "what time", "current time"],
            "date": ["date", "what date", "today's date", "current date"],
            "jokes": ["joke", "tell me a joke", "make me laugh"],
            "weather": ["weather", "temperature", "forecast"],
            "positive": ["good", "great", "awesome", "excellent", "wonderful"],
            "negative": ["bad", "terrible", "awful", "sad", "depressed"],
            "thanks": ["thank", "thanks", "appreciate"]
        }

        self.jokes_db = [
            "Why did the Nigerian student bring a ladder to school? Because he heard the exams were high level! ",
            "Nigerian parents will say, 'We’re leaving by 5pm' and still be dressing by 7:30pm. Time is just advice to them. ",
            "NEPA took light during a Zoom interview. Candidate said, 'Sorry sir, my country logged me out.' ",
            "Only in Nigeria will you hear, 'I’m 5 minutes away' when the person is still in their bathroom. ",
            "A Nigerian mechanic will fix your car and say 'it’s now brand new' but the steering still has its own plans. ",
            "Nigerians will say 'I'm managing' when they’re clearly living large. Bro, you’re managing G-Wagon? ",
            "A Nigerian wedding isn’t complete until someone shouts 'DJ, increase the volume!' even when the speakers are vibrating walls. ",
            "Nigerian children know it’s over when mom says, 'Continue… I’m watching you.' That’s not a request, it’s judgment day. ",
            "Teacher: What is a verb? Chinedu: It's a doing word, sir. Teacher: Give example. Chinedu: 'To chop'. ",
            "Only in Nigeria will your neighbor shout 'UP NEPA!' like they just won a Grammy."]

        self.username = "Friend"
        self.coversation_count = 0
        self.user_preference = {}
        self.conversation_history = []


    def analyze_sentiment(self, text):
        '''Analyze Sentiment of user input byt checking the polarity value'''
        try:
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            if polarity > 0.1:
                return "positive"
            elif polarity < -0.1:
                return "negative"
            else:
                return "neutral"
        except:
            return "neutral"


    def extract_entities(self, text):
        '''Gets key entities from text'''
        entities = {
            'digits' : re.findall(r'\d+', text),
            'emails' : re.findall(r'\S+@\S', text),
            'urls' : re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
        }
        return entities

    def get_greeting_response(self):
        "Greetings according to the exact time"
        hour = datetime.now().hour
        if 5 <= hour < 12:
            return "Good Morning! What can I do for you?"
        elif 12 <= hour < 17:
            return "Good Afternoon! What can I do for you?"
        elif 17 <= hour < 21:
            return "Good Evening! How can I be of help?"
        else:
            return "Hello! \nWhat can i do for you?"


    def calculate_math(self, text):
        '''It does Basic Math Calculations'''
        #Patterns to search for in user input using regex
        patterns = [
            r'(\d+)\s*\+\s*(\d+)'   #for addition
            r'(\d+)\s*\-\s*(\d+)'   #for subtraction
            r'(\d+)\s*\*\s*(\d+)'   #for multiplication
            r'(\d+)\s*\/\s*(\d+)'   #for division
        ]

        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                try:
                    num1, num2 = map(int, match.groups())
                    if '+' in pattern:
                        return f'{num1} + {num2} = {num1 + num2}'
                    elif '-' in pattern:
                        return f'{num1} + {num2} = {num1 + num2}'
                    elif '*' in pattern:
                        return f'{num1} + {num2} = {num1 + num2}'
                    elif '/' in pattern:
                        if num2 != 0:
                            return f'{num1} ÷ {num2} = {num1 / num2:.2f}'
                        else:
                            return "Can't be divided by Zero!"
                except:
                    pass
            return None


    def process_input(self, user_input):
        '''This will process what the user will ttype in for the machine and,
        cleans it up so it can understand(.lower()) '''
        # self.conversation_count += 1 #try to define this more or just hide the prompt
        self.conversation_history.append({
            'user': user_input, #Remember to check back on this
            'timestamp':datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

        user_input = user_input.lower().strip()

        #Checking for Goodbyes(or it's likes) from the input
        if any(farewell in user_input for farewell in self.responses[f'farewells']):
            return "See you next time!"

        #Checking for math calculations in it's response
        result = self.calculate_math(user_input)
        if result:
            return result

        if "my name is" in user_input:
            name_match = re.search(r'my name is (.+)', user_input)
            if name_match:
                self.user_name = name_match.group(1).capitalize()
                return f"Nice to meet you, {self.user_name}! I'all remember that"

        elif "what is my name" in user_input:
            return f"Your name is {self.user_name}?"

        elif any(time_word in user_input for time_word in self.responses["time"]):
            current_time = datetime.now().strftime("%H:%M:%S")
            return f"The Current time is: {current_time}"

        elif any(date_word in user_input for date_word in self.responses["date"]):
            current_date = datetime.now().strftime("%Y-%m-%d")
            weekday = datetime.now().strftime("%A")
            return f"Today is {weekday}, {current_date}"

        elif any(joke in user_input for joke in self.responses["jokes"]):
            return random.choice(self.jokes_db)

        elif any(greeting in user_input for greeting in self.responses["greetings"]):
            return self.get_greeting_response()

        elif any(wellbeing in user_input for wellbeing in self.responses["wellbeing"]):
            return "I am functioning well, thank you! Now let me help you!"

        elif any(identity in user_input for identity in self.responses["identity"]):
            return "I am your AI assistant, I can't perform all tasks but I can do the basics and chat"

        elif any(thanks in user_input for thanks in self.responses["thanks"]):
            return "You are very welcome! I am happy to help."

        elif any(negative in user_input for negative in self.responses["negative"] ):
            if "not" not in user_input:
                return "I'm sorry to hear that. IS there anything specific I can do to make things better?"


        sentiment = self.analyze_sentiment(user_input)
        if sentiment == "positive": #grabbed from the polarity value
            return "That sounds Positive! I am glad to hear that."
        elif sentiment == "negative":
            return "Your message sounds concerning, how can I help?"

        # entities = self.extract_entities(user_input)
        # if entities['numbers']:
        #     return f"I noticed you mentioned numbers: {','.join(entities['numbers'])}. Do you wish to perform calculations with them?"

        default_responses = [
            f"Intresting stuff, {self.user_name}.Do you mind telling me more?",
            "I am still learning about that topic. Could you explain it differently?",
            "I understand you're saying: " + user_input + ". What other way can I assist you?",
            f"I am here to help, {self.user_name}. What would you like to explore?",
            "That is very thoughtful of you. What else would you like to discuss?",
            "I am processing that information. Is there a specific question I can help with?"
        ]
        return random.choice(default_responses)


    def run(self):
        '''Chat loop'''
        print("*" * 30)
        print(self.get_greeting_response())
        print("Type 'exit' to leave the conversation")
        print()

        while True:
            try:
                user_input = input("You:  ").strip()

                if not user_input:
                    print("Bot:  Sorry I didn't get that. Can you say something?")
                    continue

                response = self.process_input((user_input))

                if response in self.responses["farewells"]:
                    print(f"Bot:  Goodbye, {self.user_name} ! It was great having this conversation with you, come back anytime soon!")
                    # print(f"Conversation Summary:  We
                    break

                else:
                    print(f"Bot:  {response}")
                    print()

            except KeyboardInterrupt:
                print(f"\n\n Bot:Goodbye, {self.user_name}! We had a nice conversation")
                break

            except Exception as e:
                print(f"Bot:  I encountered an issue: {str(e)}. Let's continue our chat!")



if __name__ == "__main__":

    bot = Chatbot()
    bot.run()








