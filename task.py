# math game (3 seconds to snaswer or you lose)
# user response guess
# if correct you move on to the next problem, else lose
#dictionary 1-10 problems
#def the dictionary and call it at the end
#check system to make sure each problem is correct
#figure out how to call each question and ask in the correct order ("correct!")
#congratulatory system at the end 

# q3 = ["What is 54 - 13?: "]
# q4 = ["What is 50/25?: "]
# q5 = ["What is 88 + 101?: "]
# q6 = ["What is 1,000 / 10?: "]
# q7 = ["What is  32 * 3?: "]
# q8 = ["What is 75 * 2?: "]
# q9 = ["What is 125 - 80-?: "]
# q10 = ["What is the square root of 144?"]

from datetime import datetime, timedelta

def delay():   #delays the output by 1 seconds for the user to read before the next function starts
    delay = timedelta(seconds=1)
    endtime = datetime.now() + delay
    while datetime.now() < endtime:
        pass

def game():
    print(Game_Opener)
    print(Game_Start)

def time():
     if delay > delay(3):
          print("TOO SLOW! :( Please play again another time! ")
          quit()

answer = True

    
def wrong(): 
    print("Wrong!")
    delay()
    print("Please play again another time!")
    answer = False
    return answer 
    


Game_Opener = input("Hello, Welcome to the math game! Ready to play? y/n: ") #game start up info


if Game_Opener == "y":

    print("Great! Lets begin... ")
    delay()
    print("You will be given multiple questions and you have 3 seconds to type in your number response. You lose if you can't answer all questions or if you run out of time.")
    delay()
    
   
elif Game_Opener == "n":
        print("Please play again another time!")
        quit()

else:
        print("Please type y or n... Restart Program --> ")
        quit()

for function in Game_Opener:
    if Game_Opener == False:
        quit()







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

q1 = input("What is 1 + 1?: ")
if q1 == "2":
        print("Correct!")
        time()
     
         
else:
    wrong()
    

q2 = input("What is 4 * 7?: ")
if q2 == "28":
        print("Correct!")

      
        
else:
    wrong()
            
    
questions = [q1, q2]

for question in questions:
    
    if questions == False:
        quit()

    while question == True:
        delay()
        pass



# math game (3 seconds to snaswer or you lose)
# user response guess
# if correct you move on to the next problem, else lose
#dictionary 1-10 problems
#def the dictionary and call it at the end
#check system to make sure each problem is correct
#figure out how to call each question and ask in the correct order ("correct!")
#congratulatory system at the end from datetime import datetime, timedelta


import time

def delay(seconds=1):
    # Delays the output by the given number of seconds for the user to read before the next function starts
    time.sleep(seconds)

def wrong(): 
    print("Wrong!")
    delay()
    print("Please play again another time!")
    return False

def game():
    print("Game starting...")  # Placeholder for future game logic

def time_limit(start_time, limit_seconds=3):
    # Returns True if user took longer than the limit
    return (datetime.now() - start_time).total_seconds() > limit_seconds

# Start of the game
Game_Opener = input("Hello, Welcome to the math game! Ready to play? y/n: ")  # game startup info

if Game_Opener == "y":
    print("Great! Lets begin... ")
    delay()
    print("You will be given multiple questions and you have 3 seconds to type in your number response.")
    delay()
    print("You lose if you can't answer all questions or if you run out of time.")
    delay()

elif Game_Opener == "n":
    print("Please play again another time!")
    quit()

else:
    print("Please type y or n... Restart Program --> ")
    quit()

# Game start prompt
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

# List of questions
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

# Loop through questions

for q in questions:
    start_time = datetime.now()
    user_answer = input(f"{q['question']} ")

    if time_limit(start_time): # Check time limit
        print("TOO SLOW! :( Please play again another time!")
        quit()

    if user_answer == q["answer"]: # Check if the answer is correct

        print("Correct!")
    else:
        wrong()
        quit()

print("Congrats, you've completed the game!")