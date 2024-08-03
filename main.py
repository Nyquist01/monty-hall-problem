import argparse
import random
import matplotlib.pyplot as plt


def parse_args():
    parser = argparse.ArgumentParser(description="A script to prove the Monty Hall problem using a Monte Carlo approach")
    parser.add_argument(
        "--runs", "-r",
        type=int,
        default=10000,
        help="Number of simulations to run (default: 10,000)"
    )
    return parser.parse_args()


def generate_winning_door() -> dict:
    choices = {
        "A": False,
        "B": False,
        "C": False
    }

    winning_door = random.choice(list(choices.keys()))
    choices[winning_door] = True
    return choices


def pick_a_door() -> str:
    return random.choice(["A", "B", "C"])


def reveal_losing_door(choices: dict, choice: str) -> str:
    for door, value in choices.items():
        if value is False and door != choice:
            return door


def switch_door(choices: dict, initial_choice: str, revealed_door: str) -> str:
    for door in choices.keys():
        if door != initial_choice and door != revealed_door:
            return door


def simulate(runs: int, switch: bool) -> list:
    wins = 0
    trials = 0
    win_rate = []
    while trials < runs:
        choices = generate_winning_door()
        initial_choice = pick_a_door()
        revealed_door = reveal_losing_door(choices, initial_choice)

        if switch:
            final_choice = switch_door(choices, initial_choice, revealed_door)
        else:
            final_choice = initial_choice

        if choices[final_choice]:
            wins += 1

        trials += 1
        win_rate.append(round((wins / trials) * 100, 10))

    return win_rate


def plot_win_rate(switch_data: list, stay_data: list, ):
    plt.plot(switch_data, label="switch")
    plt.plot(stay_data, label="stay")
    plt.title("Monty Hall Problem - win rate for staying and switching strategies")
    plt.xlabel("Number of Trials")
    plt.ylabel("Win rate %")
    plt.legend()
    plt.show()


def main():
    args = parse_args()
    switch_data = simulate(runs=args.runs, switch=True)
    stay_data = simulate(runs=args.runs, switch=False)
    plot_win_rate(switch_data, stay_data)


if __name__ == "__main__":
    main()