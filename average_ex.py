def my_average(input_list):
    sum = 0;
    for item in input_list:
        sum += int(item)
    average = sum / len(input_list)
    return average
    
    
if __name__ == "__main__":
    print("Enter numbers to include in average.  Hit <Enter> alone when finished.")
    numbers_to_average = list()
    keep_running = True
    while keep_running:
        in_number = input("Enter a number: ")
        if in_number != "":
            numbers_to_average.append(in_number)
        else:
            keep_running = False
    average = my_average(numbers_to_average)
    print("The average is {}".format(average))
    
        