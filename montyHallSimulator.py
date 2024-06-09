# Random package to generate random number
import random
import sys

# Generate a random number using Random Package 
def generateRandomInRange(start,end):
    return random.randint(start,end)

# Function to simulate Monty Hall Problem
def simulate_monty_hall(num_simulations):
    switch_wins = 0
    stay_wins = 0

    for _ in range(num_simulations):
        # Generate a random number between 0 and 2 
        # Place the prize behind one of the three doors
        car_position = generateRandomInRange(0, 2)
        
        # Contestant randomly picks one of the three doors
        contestant_choice = generateRandomInRange(0, 2)
        
        # Host opens one of the doors not picked by the contestant and not having the car
        possible_doors = [0, 1, 2]
        possible_doors.remove(contestant_choice)
        if car_position in possible_doors:
            possible_doors.remove(car_position)
        door_opened_by_host = random.choice(possible_doors)
        
        # Determine the door to switch to
        remaining_doors = [0, 1, 2]
        remaining_doors.remove(contestant_choice)
        remaining_doors.remove(door_opened_by_host)
        door_to_switch = remaining_doors[0]

        # Check if switching wins
        if door_to_switch == car_position:
            switch_wins += 1
        
        # Check if staying wins
        if contestant_choice == car_position:
            stay_wins += 1

    print(f"Out of {num_simulations} simulations:")
    print(f"Switching wins: {switch_wins} times")
    print(f"Staying wins: {stay_wins} times")
    print(f"Probability of winning by switching: {switch_wins / num_simulations:.2f}")
    print(f"Probability of winning by staying: {stay_wins / num_simulations:.2f}")


# Run the simulator with a desired number of simulations
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python monty_hall_simulator.py <num_simulations>")
        sys.exit(1)
    
    try:
        num_simulations = int(sys.argv[1])
        simulate_monty_hall(num_simulations)
    except ValueError:
        print("Please enter a valid integer for the number of simulations.")
        sys.exit(1)