import random

rand_num = random.randrange(1, 11)

for x in range(3):
   guess = int(input("Guess a number from 1 to 10:"))
   if guess == rand_num:
      print("Correct!")
      break
   elif guess > rand_num:
      print("Too High")
   elif guess < rand_num:
      print("Too Low") 