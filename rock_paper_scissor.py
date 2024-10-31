import random

ROCK='r'
PAPER='p'
SCISSOR='s'
emojis={ROCK:'🪨',PAPER:'📰',SCISSOR:'✂️'}
choices=(ROCK,PAPER,SCISSOR) # tuple(emojis.key())
# while True:
#   user_choice=input("Rock,Paper or Scissors?(r/p/s):").lower()
#   if user_choice not in choices:
#     print("Invalid choice!")
#     continue

#   computer_choices=random.choice(choices)
#   print(f'you chose {emojis[user_choice]}')
#   print(f'computer chose {emojis[computer_choices]}')

#   if user_choice==computer_choices:
#     print('Tie!')
#   elif (user_choice==ROCK and computer_choices==SCISSOR) or (user_choice==SCISSOR and computer_choices==PAPER) or (user_choice==PAPER and computer_choices==ROCK):
#     print('You win')
#   else:
#     print('You lose')

#   should_continue=input('continue?(y/n):').lower()
#   if should_continue=='n':
#     break
def get_user_choice():
  while True:
    user_choice=input("Rock,Paper or Scissors?(r/p/s):").lower()
    if user_choice in choices:
      return user_choice
    else:
      print("Invalid choice!")

def display_choice(user_choice,computer_choices):
  print(f'you chose {emojis[user_choice]}')
  print(f'computer chose {emojis[computer_choices]}')

def determine_winner(user_choice,computer_choices):
  if user_choice==computer_choices:
    print('Tie!')
  elif (user_choice==ROCK and computer_choices==SCISSOR) or (user_choice==SCISSOR and computer_choices==PAPER) or (user_choice==PAPER and computer_choices==ROCK):
    print('You win')
  else:
    print('You lose')

def play_game():
  while True:
    user_choice=get_user_choice()
    computer_choices=random.choice(choices)
    display_choice(user_choice,computer_choices)
    determine_winner(user_choice,computer_choices)

    should_continue=input('continue?(y/n):').lower()
    if should_continue=='n':
      break
play_game()