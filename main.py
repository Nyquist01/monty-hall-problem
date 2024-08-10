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


class MontyHallProblem():
    def __init__(self, simulations: int):
        self.simulations = simulations
        self.switch_data = []
        self.stay_data = []

    def simulate(self) -> list:
        wins_stay = 0
        wins_switch = 0
        for simulation in range(1, self.simulations):
            winning_door = random.choice(["A", "B", "C"])
            initial_choice = random.choice(["A", "B", "C"])
            remaining_doors = {"A", "B", "C"} - {initial_choice, winning_door} # doors the host can choose to reveal
            reveal_losing_door = random.choice(list(remaining_doors)) # the door the host reveals

            # stay scenario
            if initial_choice == winning_door:
                wins_stay += 1
            # switch scenario
            final_choice = ({"A", "B", "C"} - {initial_choice, reveal_losing_door}).pop()
            if final_choice == winning_door:
                wins_switch += 1

            self.stay_data.append(round((wins_stay / simulation) * 100, 10))
            self.switch_data.append(round((wins_switch / simulation) * 100, 10))
        
        self.plot_win_rate()

    def plot_win_rate(self):
        plt.plot(self.switch_data, label="switch")
        plt.plot(self.stay_data, label="stay")
        plt.title(f"Monty Hall Problem - win rate for staying and switching strategies over {self.simulations} simulations")
        plt.xlabel("Number of Trials")
        plt.ylabel("Win rate %")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    args = parse_args()
    problem = MontyHallProblem(simulations=args.runs)
    problem.simulate()
