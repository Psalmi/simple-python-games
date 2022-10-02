import random

while True:
  com_num = random.randint(1, 50)
  player_num = int(input("enter a number between 1 - 50: "))

  while player_num != com_num:
    if player_num > com_num:
      print("Too high")
    else:
      print("Too low")
    player_num = int(input("enter a number between 1 - 50: "))
  else:
    print("Correct Guess, you're awesome!")

  play_again = input("Play again? (yes/no): ")

  if play_again != "yes":
    break

print("Bye!")
