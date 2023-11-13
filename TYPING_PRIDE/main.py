
import threading
import time
import random
from fuzzywuzzy import fuzz

def get_sample():
    with open("pride_and_prejudice.txt", "r", encoding="utf-8") as f:
        text = f.read()
        sentences = text.split(".")
        sentence = random.choice(sentences)
        index = text.index(sentence)
        sample = ""
        while len(sample) < 500:
            sample += text[index]
            index += 1
    return sample

def submit_input(submit_event):
    time.sleep(60)
    print("----------\n")
    print("Time's up! Press enter to yet results.\n")
    submit_event.set()

def main():
    submit_event = threading.Event()
    submit_thread = threading.Thread(target=submit_input, args=(submit_event,))
    submit_thread.start()
    start_time = time.time()
    sample = get_sample()
    print(sample)
    print("----------\n")
    print("Starty typing!\n")
    lines = []
    while not submit_event.is_set():
        line = input()
        if line == 'END':
            break
        lines.append(line)
    print("----------\n")
    user_input = '\n'.join(lines).split("Time's up!")[0]
    submit_event.wait()
    end_time = time.time()
    typing_rate = len(user_input) / (end_time - start_time)
    words = user_input.split(" ")
    wpm = (len(words) / (end_time - start_time)) * 60
    print("Results:\n")
    print(f"Characters per second: {typing_rate:.2f}")
    print(f"Words per minute: {wpm:.2f}")
    print(f"Accuracy: {compare_strings(user_input, sample):.2f}")

# Write a function to compare two strings and give a score, between 0 and 1, of how similar they are.
# Need to account for misspellings, extra spaces, etc.

def compare_strings(string1, string2):
    return fuzz.ratio(string1.replace("\n", ""), string2[:len(string1)].replace("\n", ""))

if __name__ == "__main__":
    main()
