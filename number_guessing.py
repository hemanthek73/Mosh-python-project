import random

number=random.randint(1,100)
count=0
while True:
  try:
    guess_number=int(input("Guess the number between 1 to 100 :"))
    if number>guess_number:
      print("number is Too Low!")
      
    elif number < guess_number:
      print("number is Too High!")
    else:
       print("congratulations! You guess the number and the number is",number)
       break
  except ValueError:
    print("please enter a valid number")

