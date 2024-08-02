import random
import matplotlib.pyplot as plt

def pick_a_door() -> str:
    doors = ["A", "B", "C"]
    random_index = random.randrange(0, 3)
    return doors[random_index]


def generate_winning_door() -> list:
    choices = {
        "A": False,
        "B": False,
        "C": False
    }

    random_index = random.choice(list(choices.keys()))
    choices[random_index] = True
    return choices


def reveal_losing_door(choices: list, choice: str) -> str:
    for door, value in choices.items():
        if value is False and door != choice:
            return door


def simulate(runs: int):
    iter = 0
    wins = 0
    attempts = 0
    track_win_rate = []
    while iter < runs:
        iter += 1
        choice = pick_a_door()
        choices = generate_winning_door()
        losing_door = reveal_losing_door(choices, choice)
        print(f"You chose {choice}. Door {losing_door} has a goat behind it and you choose to stay")

        if choices[choice] == True:
            wins += 1
            attempts += 1
            win_rate = round((wins / attempts) * 100, 10)
            track_win_rate.append(win_rate)
        else:
            attempts += 1
            win_rate = round((wins / attempts) * 100, 10)
            track_win_rate.append(win_rate)
    
    return track_win_rate


def plot_win_rate(data):
    plt.plot(data)
    plt.title("Monty Hall Problem - win rate when keeping initial choice")
    plt.xlabel("Number of Trials")
    plt.ylabel("Win rate %")

    plt.show()


def main():
    data = simulate(runs=1000)
    plot_win_rate(data)


if __name__ == "__main__":
    main()