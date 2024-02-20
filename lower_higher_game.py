from data import data
import random
score = 0
def increase_score():
    global score
    score += 1
    print(f"Your score is {score}")

print("Welcome to the higher lower game.!")
lose = False

while (lose == False):
    random_number = random.randint(1, len(data))
    random_number2 = random.randint(1, len(data))
    while(random_number2 == random_number):
        random_number2 = random.randint(1, len(data))
       
    caseA = data[random_number]
    caseB = data[random_number2]
    visual_caseA = (caseA['name'], caseA['description'], caseA['country'])
    visual_caseB = (caseB['name'], caseB['description'], caseB['country'])
    followersA = int((caseA['follower_count']))
    followersB = int((caseB['follower_count']))
    print(f"case A = {visual_caseA} \n VS \n case B = {visual_caseB}")
    choice = input("Choose who have more followers? 'A' or 'B' ")
    if choice == 'A' and followersA > followersB:
        print(" \n Correct answer")
        increase_score()
    elif choice == 'B' and followersB > followersA:
        print("Correct answer")
        print(f"Followers A = {followersA} mln, followers B = {followersB} mln")
        increase_score()
    else:
        print("Wrong choice! You lost")
        print(f"Followers A = {followersA} mln, followers B = {followersB} mln")
        print(f"Your score is {score}")
        lose = True





