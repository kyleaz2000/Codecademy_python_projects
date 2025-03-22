#Below is the random integer import function, this needs to be added to make the program run.
import random
#Below is the variable random_number and the random integers that we want imported and the range(parentehses denote that the 1 and 9 are inclusive in the range).

random_number = random.randint(1,9)
#print(random_number)


name = "Katie"
question = " Will I have big boobies?"
answer =""

#Below is the control flow using if/elif statements to determine the output.

if random_number == 1:
  answer = "Yes - Definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  asnwer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"
  
#Below print statement gives a starter to the output so you know who is asking and what is being asked
print(name + " asks:" + question)
print("Magic 8-ball's answer:" + answer)
