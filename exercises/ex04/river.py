"""File to define River class."""

__author__ = "730549027"

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def view_river(self) -> None:
        """Prints State of River Ecosystem"""

        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        self.day += 1
        for bear in self.bears:
            bear.one_day()
        for fish in self.fish:
            fish.one_day()
        self.bears_eating()
        self.check_hunger()
        self.check_ages()
        self.repopulate_fish()
        self.repopulate_bears()
        self.view_river()

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self):
        surviving_bears = [bear for bear in self.bears if bear.hunger_score >= 0]
        self.bears = surviving_bears

    def check_ages(self):
        surviving_fish = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        self.fish = surviving_fish

        surviving_bears = []
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.bears = surviving_bears

    def remove_fish(self, amount: int) -> None:
        if amount <= 0:
            return
        actual_amount = min(amount, len(self.fish))
        self.fish = self.fish[actual_amount:]
        return None

    def repopulate_fish(self):
        new_fish_count = (len(self.fish) // 2) * 4
        for i in range(new_fish_count):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        new_bears_count = len(self.bears) // 2
        for i in range(new_bears_count):
            self.bears.append(Bear())
        return None

    def one_river_week(self):
        """Simulate one week (7 days) in the river."""
        for i in range(0, 7):
            self.one_river_day()
