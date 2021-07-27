print("The Stick in the Pile Game")
player2 = str(input("What's your name? : "))
sticks = int(input("How many sticks in the pile? : "))
Max_take = int(input("The maximum amount that can be took: "))
import random
while sticks > 0 :
  print("There are " + str(sticks) + " sticks in the pile ")

#player1 (AI)

  if sticks % Max_take+1 == Max_take:
    take1 = 1
    sticks -= take1
    print("I take " + str(take1) + " stick, there are " + str(sticks) + " sticks in the pile. ")
  else:
    take1 = random.randint(1, Max_take)
    sticks -= take1
    print("I take " + str(take1) + " stick, there are " + str(sticks) + " sticks in the pile. ")
  if sticks <= 0:
    print(" AI takes the last stick,")
    print(player2," WON ")
    break
#player2 (people)

  take2 = int(input("How many you will take: "))
  if take2 <= Max_take:
    sticks -= take2
  else: 
    print("No! you can't take more less than 1 stick!")
    take2 = int(input("How many you will take: "))
    sticks -= take2
  if sticks== 0:
    print(player2, "takes the last stick,")
    print("I WON (Python won) ")
    break



