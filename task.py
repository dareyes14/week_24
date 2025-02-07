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

   
answer = True

    
def wrong(): 
    print("Wrong!")
    delay()
    print("Please play again another time!")
    answer = False
    return answer 



while answer is True:


    q1 = input("What is 1 + 1?: ")
    if q1 == "2":
        print("Correct!")
        delay(3)
    else:
            wrong()


    q2 = input("What is 4 * 7?: ")
    if q2 == "28":
        print("Correct!")
        delay(3)
    else:
            wrong()








Game_Opener = input("Hello, Welcome to the math game! Ready to play? y/n: ") #game start up info


if Game_Opener == "y":

    print("Great! Lets begin... ")
    delay()
    print("You will be given multiple questions and you have 3 seconds to type in your number response. You lose if you can't answer all questions or if you run out of time.")
    delay()
    
   
elif Game_Opener == "n":
        print("Please play again another time!")
        pass 

else:
        print("Please type y or n")

questions = {q1, q2}

Game_Start = input("Are you ready to play? y/n: ")

if Game_Start == "y":
    print("Ready?")
    delay()
    print("3...")
    delay()
    print("2...")
    delay()
    print("1...")
    delay
    print("Go!")
    delay()
    print(" ")

elif Game_Start == "n":
    print("Please play again another time!")

else:
    print("Please type y or n")


for question in questions:
    
    
    
    
    
    while questions == wrong():
return
