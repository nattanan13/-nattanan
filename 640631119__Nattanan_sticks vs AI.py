print("The Stick in the Pile Game")
player2 = str(input("What's your name? : "))
sticks = int(input("How many sticks in the pile? : "))

while sticks > 0 :
  print("There are " + str(sticks) + " sticks in the pile ")

#player1 (AI)

  if sticks ==2 or sticks % 3 == 2:
    take1 = 1
    sticks -= take1
    print("I take " + str(take1) + " stick, there are " + str(sticks) +
          " sticks in the pile. ")
  else:
    take1 = 2
    sticks -= take1
    print("I take " + str(take1) + " stick, there are " + str(sticks) + 
          " sticks in the pile. ")


#player2 (people)

  take2 = int(input("How many you will take (1 or 2): "))
  if take2 == 1 or take2 == 2:
    sticks -= take2
  else: 
    print("Plese take only 1 or 2 stick")
    take2 = int(input("How many you will take (1 or 2): "))
    sticks -= take2

  if sticks == 0:
    print(player2, "takes the last stick,")
    print("I WON (Python won) ")
    break



