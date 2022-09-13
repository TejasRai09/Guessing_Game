import random
EASY = 10
HARD = 5
def compare(x,y):
  if x == y:
    return 0
  if x != y:
    return 1
Actual_number = random.randint(1,100)
n = input("TELL ME THE DIFFICULTY LEVEL, \n For hard type 'HARD' \n For easy type 'EASY'")

if n == "HARD":
  n = HARD
else:
  n = EASY
Game_over = False
while not Game_over and n >0:
  guessed_number = int(input("Make a guess"))
  count = compare(guessed_number,Actual_number)
  
  if count == 0:
    print("YOU WIN")
    Game_over = True
  elif count == 1 and guessed_number > Actual_number:
    print("TOO HIGH")
  else:
    print("TOO LOW")
  n -= 1
  if n == 1:
      print("IT IS YOUR LAST CAHNCE")
  elif n == 0:
      print("YOU LOOSE")
  
