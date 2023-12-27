import csv
import datetime
import random
import time
import random
import pygame

def generate_question():
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    return num1, num2

def calculate_score(correct_count, time_taken):
    time_bonus = 50 / time_taken
    return correct_count * time_bonus

def save_to_log(name, correct_count, incorrect_count, score, time):
    """
    'log.csv' has headers: name, correct_count, incorrect_count, score, time, timestamp
    """
    with open("log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, correct_count, incorrect_count, score, time, datetime.datetime.now()])


def update_leaderboard(order_by="score", order="desc"):
    """
    'leaderboard.csv' has headers: name, average_score, best_score, games_played, fastest_time, total_correct, total_incorrect
    """
    with open("log.csv", "r") as file:
        reader = csv.reader(file)
        next(reader) # Skip header row
        rows = list(reader)

    # Calculate average score, best score, fastest time, total correct, total incorrect, and games played
    name_to_score = {}
    name_to_average_score = {}
    name_to_best_score = {}
    name_to_fastest_time = {}
    name_to_total_correct = {}
    name_to_total_incorrect = {}
    name_to_games_played = {}

    for row in rows:
        name = row[0]
        score = float(row[3])
        time_taken = float(row[4])
        correct_count = int(row[1])
        incorrect_count = int(row[2])

        if name in name_to_score:
            name_to_score[name].append(score)
        else:
            name_to_score[name] = [score]

        if name in name_to_best_score:
            name_to_best_score[name] = max(name_to_best_score[name], score)
        else:
            name_to_best_score[name] = score

        if name in name_to_fastest_time:
            if time_taken < name_to_fastest_time[name]:
                name_to_fastest_time[name] = time_taken
        else:
            name_to_fastest_time[name] = time_taken

        if name in name_to_total_correct:
            name_to_total_correct[name] += correct_count
        else:
            name_to_total_correct[name] = correct_count

        if name in name_to_total_incorrect:
            name_to_total_incorrect[name] += incorrect_count
        else:
            name_to_total_incorrect[name] = incorrect_count

        if name in name_to_games_played:
            name_to_games_played[name] += 1
        else:
            name_to_games_played[name] = 1

    # Calculate average score
    name_to_average_score = {name: sum(scores) / len(scores) for name, scores in name_to_score.items()}

    # Write to leaderboard.csv
    with open("leaderboard.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "average_score", "best_score", "games_played", "fastest_time", "total_correct", "total_incorrect"])
        for name in sorted(name_to_average_score, key=name_to_average_score.get, reverse=True):
            writer.writerow([name, name_to_average_score[name], name_to_best_score[name], name_to_games_played[name], name_to_fastest_time[name], name_to_total_correct[name], name_to_total_incorrect[name]])

    # Check if player is at the top of the leaderboard
    if name_to_average_score and name_to_average_score[name] == max(name_to_average_score.values()):
        if correct_count == 10:
            pygame.mixer.init()
            pygame.mixer.music.load("fanfare.mp3")
            pygame.mixer.music.play()
            print("Well done, you got them all correct!")

def play_game():
    name = input("Enter your name: ")
    correct_count = 0
    incorrect_count = 0

    start_time = time.time()

    incorrect_list = []

    for _ in range(10):
        num1, num2 = generate_question()
        answer = int(input(f"What is {num1} * {num2}? "))
        if answer == num1 * num2:
            correct_count += 1
        else:
            incorrect_count += 1
            incorrect_list.append(f"The correct answer to {num1} * {num2} is {num1 * num2}.")

    time_taken = time.time() - start_time
    score = calculate_score(correct_count, time_taken)

    print(f"\nCorrect: {correct_count}")
    print(f"Incorrect: {incorrect_count}")
    print(f"Time taken: {time_taken} seconds")
    print(f"Score: {score}")

    if incorrect_count > 0:
        print("\nIncorrect answers:")
        for incorrect in incorrect_list:
            print(incorrect)

    save_to_log(name, correct_count, incorrect_count, score, time_taken)
    update_leaderboard()

def view_leaderboard():
    with open("leaderboard.csv", "r") as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read and store the headers
        max_lengths = [len(header) for header in headers]  # Calculate maximum lengths for each column
        rows = list(reader)  # Store all rows
        for row in rows:
            for index, value in enumerate(row):
                if value.isdigit():
                    continue
                try:
                    float_value = float(value)
                    if float_value.is_integer():
                        row[index] = str(int(float_value))
                    else:
                        row[index] = f"{float_value:.1f}"
                except ValueError:
                    pass
                max_lengths[index] = max(max_lengths[index], len(row[index]))  # Update maximum lengths
        formatted_headers = [f"{header:<{max_lengths[index]}}" for index, header in enumerate(headers)]  # Align headers
        print("\t".join(formatted_headers))  # Print aligned headers
        for row in rows:
            formatted_row = [f"{value:<{max_lengths[index]}}" for index, value in enumerate(row)]  # Align rows
            print("\t".join(formatted_row))
    

def main():
    while True:
        print("\nOptions:")
        print("1. Play")
        print("2. View Leaderboard")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            view_leaderboard()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
