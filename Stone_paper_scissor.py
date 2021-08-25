
import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 'stone':
        if you == 'paper':
           return True
        elif you == 'scissor':
           return False
    elif comp == 'scissor':
        if you == 'paper':
           return False
        elif you == 'stone':
           return True
    elif comp == 'paper':
        if you == 'scissor':
           return False
        elif you == 'stone':
           return True

print("Comp turn: Stone Paper or Scissor")
randNo = random.randint(1, 3)
# print(randNo)

if randNo == 1:
    comp = 'stone'
elif randNo == 2:
    comp == 'paper'
elif randNo == 3:
    comp == 'scissor'

you = input("Your turn: Stone Paper or Scissor: ")
a = gameWin(comp, you)

print(f"Computer Chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else: 
    print("You Loose!")