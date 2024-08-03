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


def simulate(runs: int) -> list:
    wins = 0
    trials = 0
    win_rate = []
    while trials < runs:
        choices = generate_winning_door()
        choice = pick_a_door()

        if choices[choice] == True:
            wins += 1

        trials += 1
        win_rate.append(round((wins / trials) * 100, 10))

    return win_rate


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