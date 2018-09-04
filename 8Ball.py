import random
import time
import sys
responses = ["Yes", "No", "Maybe", "The odds are in your favor", "It is certain", "Cannot predict now", "Cheese = death", "Don't count on is", "Very doubtful", "Most likely"]

print("Welcome, I am the MAGIC 8 BALL!!!!!!!")

time.sleep(1)

cont = input("Would you like to continue? If so just say [yes] uwu, if not say [no] -_-")
while cont != 'yes':
    cont = print("Goodbye:(")
    sys.exit()
    

time.sleep(1)

name = input("Thank you for continuing with me UWU. What is your name?")
print("Well, hello %s!" % name)

time.sleep(1)

quest = input("Ask me a question, anything at all.")

time.sleep(2)
print("Hmmmm")
time.sleep(2)

print(random.choice(responses))


     



      
            


































































































