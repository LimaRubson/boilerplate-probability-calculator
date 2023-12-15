# Probability Calculator

This is the boilerplate for the Probability Calculator project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator

# My collaboration in the project:

## Hat Experiment Simulation
This repository contains a Python implementation of a simple experiment involving drawing colored balls from a hat. The experiment is designed to estimate the probability of drawing a specific group of colors from the hat.

## Hat Class
The Hat class represents a hat containing balls of different colors. The colors and quantities are specified during the initialization of the hat. The draw method simulates drawing a specified number of balls from the hat without replacement.

## Experiment Function
The experiment function simulates the experiment by repeatedly drawing balls from a hat and checking if the drawn group matches an expected group of colors. It takes the following parameters:

## hat: An instance of the Hat class representing the initial configuration of the hat.
expected_balls: A dictionary specifying the expected group of colors and their respective quantities.
num_balls_drawn: The number of balls to draw in each experiment.
num_experiments: The total number of experiments to perform.

The function returns the estimated probability of the expected group of colors being drawn based on the number of successful experiments.

## Example Usage
```python
# Example Hat with 5 blue, 4 red, and 2 green balls
hat = Hat(blue=5, red=4, green=2)

# Expected group: 1 red ball and 2 green balls
expected = {"red": 1, "green": 2}

# Number of balls drawn in each experiment
num_drawn = 4

# Number of experiments to run
num_exp = 10000

# Run the experiment and print the estimated probability
probability = experiment(hat, expected, num_drawn, num_exp)
print(f"Estimated Probability: {probability}")
