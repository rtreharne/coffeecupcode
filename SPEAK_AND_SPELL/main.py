import random
import pyttsx3
import pandas as pd
from datetime import datetime
import time

def speak(word):
    engine = pyttsx3.init()
    engine.setProperty('rate', 100)
    engine.say(word)
    engine.runAndWait()

def random_word():
    # Get a random word from the common words file
    with open('common_words.txt', 'r') as f:
        words = f.readlines()
        word = random.choice(words).strip()
        return word

def test(name, num=10):
    start = time.time()
    score = 0
    test_words = [random_word() for i in range(num)]
    user_spelling = []
    feedback = []
    print("Press enter to repeat the word")
    for i, word in enumerate(test_words):
        speak(word)

        while True:
            # ask for user input. If user presses enter, repeat the word
            user_input = input(f'{i+1}. Type your spelling: ')
            if user_input == '':
                speak(word)
            else:
                break

        user_spelling.append(user_input)
        if user_spelling[-1] == word:
            score += 1
            feedback.append('Correct!')
        else:
            feedback.append('Incorrect!')
    end = time.time()
    duration = end - start
    print(f'You scored {score}/{num}')
    print('Here are the correct spellings:')
    for i in range(num):
        print(f'{test_words[i]}: {feedback[i]}')
    
    # Save the score to the test_results.csv file
    test_results = read_test_results()

    time_threshold = 10*num

    if duration < time_threshold:
        factor = time_threshold/duration
        points = 100*score*factor
    else:
        points = 100*score

    new_row = pd.DataFrame({'name': name, 
                            'correct': score,
                            'incorrect': num-score,
                            'duration': duration,
                            'points': int(points),
                            'timestamp': datetime.now()}, index=[0])
    
    test_results = pd.concat([test_results, new_row], ignore_index=True)

    test_results.to_csv('test_results.csv', index=False)


def read_test_results():
    # Read the scoreboard.csv file using pandas
    scoreboard = pd.read_csv('test_results.csv')
    return scoreboard
    
def run():
    # Give user the option to start a test
    print('Welcome to Speak and Spell!')

    

    while True:
        
        # Ask user to enter their name
        name = input('Please enter your name: ')
        name = name.lower().capitalize()

        # Check if name is alpha
        if not name.isalpha():
            print('Please enter a valid name.')
            continue

        print('Press 1 to start a test, or 2 to quit.')

        choice = input('>> ')
        if choice == '1':
            test(name, num=10)

        elif choice == '2':
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == "__main__":
    run()