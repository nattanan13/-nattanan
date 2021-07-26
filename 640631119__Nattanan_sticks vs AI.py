print("The Stick in the Pile Game")
player2 = str(input("What's your name? : "))
sticks = int(input("How many sticks in the pile? : "))

while True:
  print("There are " + str(sticks) + " sticks in the pile ")

#player1 (AI)

  import random 
  take1 = random.randint(1, 2)
  if take1 <= sticks:
    sticks = sticks - take1
    print("I take " + str(take1) + " stick, there are "
          + str(sticks) + " sticks in the pile. ")
  if sticks == 0:
    print("Computer takes the last stick.")
    print("YOU WON")
    break

#player2 (people)

  while True:
    take2 = int(input("How many sticks you will take? (1 or 2): "))
    if take2 > 2:
      print("No! you can't take more than 2 sticks!!")
    elif take2 <= 0:
      print("No! you can't take more less than 1 stick!")
    elif take2 > sticks:
      print("There are no enough sticks to take")
    elif take2 == 1 or take2 == 2:  
      break
  sticks = sticks - take2
  
  if sticks == 0:
    print(player2, "takes the last stick.")
    print("I WON (Python won) ")
    break
print("bonus")


