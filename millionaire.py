# Who Wants To Be A Millionaire 💰

#This was part of a syntax and name error activity where option3 was missing as well as misspelled operators

score = 0

option1 = 'Fresca'
option2 = 'V8'
option3 = 'Coffee'
option4 = 'A&W'
  
print("For ordering his favorite beverages on demand, LBJ had four buttons installed in the Oval Office labeled 'Coffee', 'Tea', 'Coke', and what?\n")

print("A.", option1)
print("B.", option2)
print("C.", option3)
print("D.", option4)
  
answer = 'a'

if answer == 'A' or answer == 'a': 
  score += 100
  print("\nCorrect!")
else:
  print("\nNope, sorry!")
