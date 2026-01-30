# Modules
import random
# Variable declarations
#name = input("What is your name: ")
name = "Bob"
# question = input("What is your question: ")
question = "Is the sky blue?"
ball8_q = "Magic 8-ball's answer: "
if question != "":
  final_q = name + " asks " + question
else:
  final_q = ""
answer = ""
random_number = random.randint(1, 9)
# print(random_number)
# Loop function
# Attempted to write this code using cases within if loops
if name != "":  
  if final_q != "":
    match random_number:
      case 1:  
        answer = "Yes - definitely"
        print(final_q)
        print(ball8_q + answer)
      case 2:
        answer = "It is decidedly so"
        print(final_q)
        print(ball8_q + answer)
      case 3:
        answer = "Without a doubt"
        print(final_q)
        print(ball8_q + answer)
      case 4:
        answer = "Reply hazy, try again"
        print(final_q)
        print(ball8_q + answer)
      case 5:
        answer = "Ask again later"
        print(final_q)
        print(ball8_q + answer)
      case 6:
        answer = "Better not tell you now"
        print(final_q)
        print(ball8_q + answer)
      case 7:
        answer = "My sources say no"
        print(final_q)
        print(ball8_q + answer)
      case 8:
        answer = "Outlook not so good"
        print(final_q)
        print(ball8_q + answer)
      case 9:
        answer = "Very doubtful"
        print(final_q)
        print(ball8_q + answer)
  else:
    print("Hey now, you didn't input a question.")
elif name == "" and final_q != "":
  final_q = "Question is: "+ question
  match random_number:
      case 1:  
        answer = "Yes - definitely"
        print(final_q)
        print(ball8_q + answer)
      case 2:
        answer = "It is decidedly so"
        print(final_q)
        print(ball8_q + answer)
      case 3:
        answer = "Without a doubt"
        print(final_q)
        print(ball8_q + answer)
      case 4:
        answer = "Reply hazy, try again"
        print(final_q)
        print(ball8_q + answer)
      case 5:
        answer = "Ask again later"
        print(final_q)
        print(ball8_q + answer)
      case 6:
        answer = "Better not tell you now"
        print(final_q)
        print(ball8_q + answer)
      case 7:
        answer = "My sources say no"
        print(final_q)
        print(ball8_q + answer)
      case 8:
        answer = "Outlook not so good"
        print(final_q)
        print(ball8_q + answer)
      case 9:
        answer = "Very doubtful"
        print(final_q)
        print(ball8_q + answer)
elif name =="" and final_q == "":
  print("Hey now, you didn't input anything, huh.")
