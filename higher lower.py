import random
correct_guess = 0
wrong_guess = 0

while True:
  com_num = random.randint(1, 50)
  player_num = int(input("enter a number between 1 - 50: "))

  while player_num != com_num:
    if player_num > com_num:
      print("Too high")
      wrong_guess += 1
    else:
      print("Too low")
      wrong_guess += 1
    player_num = int(input("enter a number between 1 - 50: "))
  else:
    print("Correct Guess, you're awesome!")
    correct_guess += 1

  play_again = input("Play again? (yes/no): ")

  if play_again != "yes":
    break

print("Bye!")
print(str(correct_guess) +" Correct guesses")
print(str(wrong_guess) + " Wrong guesses")
