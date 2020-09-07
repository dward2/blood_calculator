foods = ["apples", "bananas", "cherries", "donuts", "egglant", "cherries",
         "java"]

amounts = [11, 22, 33, 44, 55, 66]


def get_inventory_of_fruit(fruit_to_check):
    for food, amount in zip(foods, amounts):
        if food == fruit_to_check:
            return amount

    # found_index = foods.index(fruit_to_check)
    # answer1 = amounts[found_index]


if __name__ == "__main__":
    number_of_fruit = get_inventory_of_fruit("cherries")
    more_fruit = number_of_fruit + 5
    print(more_fruit)
    x = True
    print(x)
    y = x + " hello"
