"""File to define Bear class."""


class Bear:
    age: int
    hunger_score: int

    def __init__(self):
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Increment the bear's age by 1 day"""
        self.age += 1
        self.hunger_score = -1
        return None

    def eat(self, num_fish: int):
        """Increase Hunger Score by number of fish eaten"""
        self.hunger_score += num_fish
