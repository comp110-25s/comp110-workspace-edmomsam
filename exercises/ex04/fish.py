"""File to define Fish class."""


class Fish:
    age: int

    def __init__(self):
        self.age = 0
        return None

    def one_day(self):
        """Increment the fish's age by 1 day"""
        self.age += 1
        return None
