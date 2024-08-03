# montyhallproblem

> Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?

It's intuitive to believe that it doesn't matter if you choose to switch or stay from your original choice, the probability should be 50/50 right? By employing a simple Monte Carlo study, we can easily demonstrate that switching from your initial choice converges to a win rate of 66.66%, highlighting that this is much more advantageous than staying with your original choice.

![monty_hall_fig](https://github.com/user-attachments/assets/bf00497b-a80e-43fa-bf29-503ac949de09)

# usage

1. Ensure python3 is installed

2. Clone this repository, `cd` into it, and install packages `pip3 install -r requirements.txt` (you can install these packages in a virtual environment if you wish)

3. Use script `python3 main.py` or optionally `python3 main.py -r 100000` to adjust the number of simulation trials
