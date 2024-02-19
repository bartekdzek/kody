import random
print("Welcome to the number guessing game!")
level = input("Choose difficulty 'e' - easy 'h' - hard ")
if level == 'e':
    lives = 10
elif level == 'h':
    lives = 5
number = random.randint(1,100)

def live_cut():
    global lives
    lives -= 1

while(lives > 0):
    guess = int(input("Guess the number = "))
    if guess == number:
        print(f"YOU WON number is {number}")
        break
    elif guess > number:
        live_cut()
        print(f"The number is smaller! \n You have {lives} lives left! ")
    elif guess < number:
        live_cut()
        print(f"The number is bigger! \n You have {lives} lives left! ")

if lives == 0:
    print(f"YOU LOSE! The number was {number}")


    


