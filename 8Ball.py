# Modules
import random
# Variable declarations
#name = input("What is your name: ")
name = "Bob"
# question = input("What is your question: ")
question = "Are you my mommy?"
answer = ""
random_number = random.randint(1, 9)
# print(random_number)
# Loop function
if name != "":
  if question != "":
    if random_number == 1:
      answer = "Yes - definitely"
      print(name + " asks: " + question)
      print("Magic 8-Ball's answer: " + answer)
    elif random_number == 2:
      answer = "It is decidedly so"
      print(name + " asks: " + question)
      print("Magic 8-Ball's answer: " + answer)
    elif random_number == 3:
      answer = "Without a doubt"
      print(name + " asks: " + question)
      print("Magic 8-Ball's answer: " + answer)
    elif random_number == 4:
      answer = "Reply hazy, try again"
      print(name + " asks: " + question)
      print("Magic 8-Ball's answer: " + answer)
    elif random_number == 5:
      answer = "Ask again later"
      print(name + " asks: " + question)
      print("Magic 8-Ball's answer: " + answer)
    elif random_number == 6:
      answer = "Better not tell you now"
      print(name + " asks: " + question)
      print("Magic 8-Ball's answer: " + answer)
    elif random_number == 7:
      answer = "My sources say no"
      print(name + " asks: " + question)
      print("Magic 8-Ball's answer: " + answer)
    elif random_number == 8:
      answer = "Outlook not so good"
      print(name + " asks: " + question)
      print("Magic 8-Ball's answer: " + answer)
    elif random_number == 9:
      answer = "Very doubtful"
      print(name + " asks: " + question)
      print("Magic 8-Ball's answer: " + answer)
    else:
      answer = "Error"
      print(answer)
  else:
    print("Hey now, you didn't input a question.")
else:
  if question != "":
    if random_number == 1:
      answer = "Yes - definitely"
      print("Question is: " + question)
      print("Magic 8-Ball's answer: " + answer)
    elif random_number == 2:
      answer = "It is decidedly so"
      print("Question is: " + question)
      print("Magic 8-Ball's answer: " + answer)
    elif random_number == 3:
      answer = "Without a doubt"
      print("Question is: " + question)
      print("Magic 8-Ball's answer: " + answer)
    elif random_number == 4:
      answer = "Reply hazy, try again"
      print("Question is: " + question)
      print("Magic 8-Ball's answer: " + answer)
    elif random_number == 5:
      answer = "Ask again later"
      print("Question is: " + question)
      print("Magic 8-Ball's answer: " + answer)
    elif random_number == 6:
      answer = "Better not tell you now"
      print("Question is: " + question)
      print("Magic 8-Ball's answer: " + answer)
    elif random_number == 7:
      answer = "My sources say no"
      print("Question is: " + question)
      print("Magic 8-Ball's answer: " + answer)
    elif random_number == 8:
      answer = "Outlook not so good"
      print("Question is: " + question)
      print("Magic 8-Ball's answer: " + answer)
    elif random_number == 9:
      answer = "Very doubtful"
      print("Question is: " + question)
      print("Magic 8-Ball's answer: " + answer)
    else:
      answer = "Error"
      print(answer)
  else:
    print("Hey now, you didn't input anything, huh.")

