import random

print("Welcome to my GUESS THE NUMBER game")
#Generate a random num in imag
imag = random.randint(1,100)
user=0
while user != imag:
  user = int(input("Guess a number between 1 and 100 :-"))
  if user > imag:
    print("Your guess is higher than my number. Try again :- ")
  else:
    print("Your guess is lower than my number. Try again :- ")

print("Congrats! You guessed the right number")  