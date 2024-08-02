import argparse
import random
import matplotlib.pyplot as plt


def parse_args():
    parser = argparse.ArgumentParser(description="Script to demonstrate and prove the Monty Hall problem")
    parser.add_argument(
        "--runs", "-r",
        type=int,
        default=1000,
        help="Number of simulations to run"
    )
    return parser.parse_args()


def pick_a_door() -> str:
    return random.choice(["A", "B", "C"])


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


def simulate(runs: int) -> list:
    iter = 0
    wins = 0
    attempts = 0
    win_rate_history = []
    while iter < runs:
        iter += 1
        choice = pick_a_door()
        choices = generate_winning_door()
        losing_door = reveal_losing_door(choices, choice)

        if choices[choice] == True:
            wins += 1
            attempts += 1
            win_rate = round((wins / attempts) * 100, 10)
            win_rate_history.append(win_rate)
        else:
            attempts += 1
            win_rate = round((wins / attempts) * 100, 10)
            win_rate_history.append(win_rate)
    return win_rate_history


def plot_win_rate(data: list):
    plt.plot(data)
    plt.title("Monty Hall Problem - win rate when keeping initial choice")
    plt.xlabel("Number of Trials")
    plt.ylabel("Win rate %")
    plt.show()


def main():
    args = parse_args()
    data = simulate(runs=args.runs)
    plot_win_rate(data)


if __name__ == "__main__":
    main()