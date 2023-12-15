import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = [color for color, quantity in balls.items() for _ in range(quantity)]

    def draw(self, num_balls):
        drawn_balls = random.sample(self.contents, min(num_balls, len(self.contents)))
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Check if the drawn balls match the expected group
        drawn_group = {color: drawn_balls.count(color) for color in expected_balls.keys()}
        if drawn_group == expected_balls:
            successful_experiments += 1

    probability = successful_experiments / num_experiments
    return probability
