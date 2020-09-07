def is_fruit(fruit_check):
    fruit_list = ["banana", "apple", "pear", "peach"]
    fruit_check = fruit_check.strip(" ")
    fruit_check = fruit_check.rstrip("s")
    fruit_exists = fruit_check.lower() in fruit_list
    return fruit_exists


if __name__ == "__main__":
    fruit_name = input("Enter a fruit: ")
    if is_fruit(fruit_name):
        print("Yes, this is a fruit.")
    else:
        print("No, this is not a fruit.")
