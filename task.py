# math game (3 seconds to snaswer or you lose)
# user response guess
# if correct you move on to the next problem, else lose
#dictionary 1-10 problems
#def the dictionary and call it at the end

from datetime import datetime, timedelta

def delay():   #delays the output by 1 seconds for the user to read before the next function starts
    delay = timedelta(seconds=1)
    endtime = datetime.now() + delay
    while datetime.now() < endtime:
        pass

def game_questions():
    print(Game_Start)


    questions = ["What is 1 + 1?: ",
             "What is 4 * 7?: ",
             "What is 54 - 13?: ",
             "What is 50/25?: ",
             "What is 88 + 101?: ",
             "What is 1,000 / 10?: ",
             "What is  2 * 2?: ",
             "What is that answer * 2?: ",
             "What is that answer * 5?: ",
             "What is that answer *: "]

Game_Start = input("Hello, Welcome to the math game! Ready to play? y/n: ")

if input == "y":
    print("Great! Lets begin... ")
    print("You will be given multiple questions and you have 3 seconds to type in your number response. You lose if you can't answer all questions or if you run out of time.")
    print("Ready?")

elif input == "n":
    print("Please play again another time!")

else:
    print("Please type y or n")





