import random
import pyttsx3
import pandas as pd
from datetime import datetime
import time
import sys

def speak(word):
    engine = pyttsx3.init()
    engine.setProperty('rate', 100)
    engine.say(word)
    engine.runAndWait()

def random_word(fname):
    # Get a random word from the common words file
    with open(fname, 'r') as f:
        words = f.readlines()
        word = random.choice(words).strip()
        return word

def test(name, fname, num=10):
    # clear terminal
    print('\n'*100)

    start = time.time()
    score = 0

    # Get a list of random words. Words cannot repeat.
    test_words = []
    while len(test_words) < num:
        word = random_word(fname)
        if word not in test_words:

            test_words.append(word)


    #test_words = [random_word() for i in range(num)]
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
    # clear terminal
    print('\n'*100)
    print('\n--- Test Results ---')
    print(f'You scored {score}/{num}\n')

    print('Here are your corrections:')
    for word, spelled in zip(test_words, user_spelling):
        # print feedback, correct and user spelling in a single line!
        if word != spelled:
            print(f'CORRECT: {word}, INCORRECT: {spelled}')

    print('\n')
    
    # Save the score to the test_results.csv file
    test_results = read_test_results()

    time_threshold = 10*num

    if duration < time_threshold:
        factor = time_threshold/duration
        points = 100*score*factor
    else:
        points = 100*score

    print("You have earned {} points!\n".format(int(points)))

    new_row = pd.DataFrame({'name': name, 
                            'correct': score,
                            'incorrect': num-score,
                            'duration': duration,
                            'score': score,
                            'points': int(points),
                            'timestamp': datetime.now()}, index=[0])
    
    test_results = pd.concat([test_results, new_row], ignore_index=True)

    test_results.to_csv('test_results.csv', index=False)


def read_test_results():
    # Read the scoreboard.csv file using pandas
    scoreboard = pd.read_csv('test_results.csv')
    return scoreboard
    
def run(fname, max_word_length=10):
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
            test(name, fname, num=10)

        elif choice == '2':
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == "__main__":
    # get word file from command line
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        run(fname)
    else:
        fname = 'common_words.txt'
        run(fname)