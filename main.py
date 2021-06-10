import random 

number = random.randint(1, 20)
no_of_guesses = 0

name = input("Hello! What would be your good name?: ")

print("Well, hello " + name + "! I am thinking of a number between 1-20. Can you guess it?")
guess = int(input())

while no_of_guesses < 6:
  if guess < number:
    print("Nope. Your guess was lesser than the number.")
    guess = int(input())
    no_of_guesses += 1
  elif guess > number:
    print("You're wrong. Your guess is too high.")
    guess = int(input())
    no_of_guesses += 1
  elif guess == number:
    print("You got it! " + str(number) + " was the right number! You got it in " + str(no_of_guesses) + " tries!")
    break

if no_of_guesses >= 6:
  print("Whoops. You did not get it in 6 tries. The number was " + str(number))