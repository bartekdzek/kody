import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6
lives = int(lives)
print(f"Welcome to the hangman game. You have only {lives} lives!")
word_list = ["orange", "grape", "banana"]
chosen_word = random.choice(word_list)
dlugosc_wyrazu = len(chosen_word)
wyraz = []
for letter in chosen_word:
    wyraz += "_"
print(wyraz)
end_of_game = False
while not(end_of_game):
    guess = input("Podaj litere: ").lower()
    for position in range(dlugosc_wyrazu):
        letter = chosen_word[position]
        if letter == guess:
            wyraz[position] = letter  
        if "_" not in wyraz:
            end_of_game = True
            print("YOU WIN!.")
        elif lives == 1:
            print("You lost")
            end_of_game = True   
    print(wyraz)
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
    print(f"You have {lives} lives left!")






    


