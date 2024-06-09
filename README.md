# Monty Hall Problem Simulator

This is a Python script that simulates the Monty Hall problem a specified number of times. The script calculates and displays the probabilities of winning if the contestant chooses to switch doors or stay with their initial choice. This simulation helps in understanding the counterintuitive result of the Monty Hall problem, demonstrating that switching doors increases the chance of winning.

## Monty Hall Problem

The Monty Hall problem is a famous probability puzzle named after Monty Hall, the original host of the American television game show *Let's Make a Deal*. The problem is as follows:

1. A contestant is presented with three doors. Behind one door is a car (the prize), and behind the other two doors are goats.
2. The contestant picks one of the three doors.
3. The host, who knows what is behind each door, opens one of the other two doors, revealing a goat.
4. The contestant is then given the option to switch their choice to the other unopened door or stay with their initial choice.
5. The question is: is it to the contestant's advantage to switch their choice?

The correct answer is that the contestant should always switch doors, as this strategy gives them a 2/3 chance of winning the car, compared to a 1/3 chance if they stay with their initial choice.

## How the Simulator Works

This simulator:
1. Randomly places the car behind one of the three doors.
2. Randomly picks a door as the contestant's initial choice.
3. Simulates the host opening one of the remaining doors that does not have the car.
4. Calculates the outcome if the contestant switches to the other unopened door.
5. Repeats this process for a user-specified number of iterations.
6. Outputs the number of wins when switching and staying, along with their respective probabilities.

## Installation

To run this simulator, you need Python installed on your system. You can download Python from the official [Python website](https://www.python.org/).

## Usage

1. Clone or download this repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script using Python with the number of iterations as an argument.

```bash
python monty_hall_simulator.py <num_simulations>
```
# Sample Input
```Text
$ python montyHallSimulator.py 10000
```

# Sample Output
```Text
Out of 10000 simulations:
Switching wins: 6673 times
Staying wins: 3327 times
Probability of winning by switching: 0.67
Probability of winning by staying: 0.33
```

This indicates that out of 10,000 simulations, switching resulted in winning 6673 times, while staying resulted in winning 3327 times. The probabilities are approximately 0.67 for switching and 0.33 for staying.

Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request. You can also open issues for any bugs or suggestions.
