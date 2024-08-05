#This code creates a simple Flask web application that allows users to guess a random number between 0 and 9.
#The application provides feedback on whether the guessed number is too high, too low, or correct,
#displaying a corresponding message and GIF.


from flask import Flask
import random

# Generate a random number between 0 and 9
random_number = random.randint(0, 9)
print(random_number)

# Create a Flask application instance
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

# Define the route for guessing the number
@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
