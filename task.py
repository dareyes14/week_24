from datetime import datetime, timedelta
import time

user = input("Please enter your name: ")
def name(user):
    Game_Opener

def delay(seconds=1): #delays the output by the given number of seconds for the user to read before the next function starts
    time.sleep(seconds)

def wrong(): #function for when people enter the wrong asnwer
    print("Wrong!")
    delay()
    print("Please play again another time!")
    return False

def game():
    print("Game starting...") #placeholder for future game logic

def time_limit(start_time, limit_seconds=5): 
    return (datetime.now() - start_time).total_seconds() > limit_seconds #returns True if user took longer than the limit

Game_Opener = input(f"Hello {user}, Welcome to the math game! Ready to play? y/n: ")  #game startup info 

if Game_Opener == "y":
    print("Great! Lets begin... ")
    delay()
    print("You will be given multiple questions and you have 5 seconds to type in your number response.")
    delay()
    print("You lose if you can't answer all questions or if you run out of time.")
    delay()

elif Game_Opener == "n":
    print("Please play again another time!")
    quit()

else:
    print("Please type y or n... Restart Program --> ")
    quit()

#game start prompt
Game_Start = input("Are you ready to play? y/n: ")

if Game_Start == "y":
    print("Ready?")
    delay()
    print("3...")
    delay()
    print("2...")
    delay()
    print("1...")
    delay()
    print("Go!")
    delay()
    print(" ")

elif Game_Start == "n":
    print("Please play again another time!")
    quit()

else:
    print("Please type y or n")
    quit()

#list of questions
questions = [
    {"question": "What is 1 + 1?", "answer": "2"},
    {"question": "What is 4 * 7?", "answer": "28"},
    {"question": "What is 50 / 25?", "answer": "2"},
    {"question": "What is 88 + 101?", "answer": "189"},    
    {"question": "What is 1,000 / 10?", "answer": "100"},
    {"question": "What is 32 * 3?", "answer": "96"},
    {"question": "What is 75 * 2?", "answer": "150"},
    {"question": "What is 125 - 80?", "answer": "45"},
    {"question": "What is the square root of 144?", "answer": "12"},
    {"question": "What is -12 + 12?", "answer": "0"}
]

#loop through questions
for q in questions:
    start_time = datetime.now()
    user_answer = input(f"{q['question']} ")

    if time_limit(start_time): #checks time limit
        print("TOO SLOW! :( Please play again another time!")
        quit()

    if user_answer == q ["answer"]: #checks if the answer is correct

        print("Correct!")
    else:
        wrong()
        quit()

print("Congrats, you've completed the game!")