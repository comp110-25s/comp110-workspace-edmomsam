"Calculating Cost Of A Tea Party"


__author__: str = "730549027"


def main_planner(guests: int) -> None:
    """Calculate the total number of items and expenses for a tea party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats((guests))))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Calculate the number of tea bags needed for a tea party"""
    return 2 * people


def treats(people: int) -> int:
    """Calculate the number of treats needed for a tea party"""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the total cost needed for a tea party"""
    return float((0.5 * (tea_count)) + (0.75 * (treat_count)))


if __name__ == "__main__":
    main_planner(guests=int(input("How many guest are attending your tea party? ")))
