import random

rand_num = random.randrange(1, 1001)
guess_var = True
guesses = 0

while guess_var is True:
   guess = int(input("Guess a number from 1 to 1000:"))
   guesses = guesses+1
   print("Guess number:", guesses)
   if guess == rand_num:
      print(guess, "is Correct!")
      break
   elif guess > rand_num:
      print(guess, "is Too High")
   elif guess < rand_num:
      print(guess, "is Too Low")
   