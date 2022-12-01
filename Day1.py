# advent of code 2022 day 1

# function to read the input file, separate by empty lines
def read_input(filename):
    with open(filename) as f:
        return f.read().splitlines()

# add numbers till '' is reached, then add to list and repeat
def add_numbers(input):
    sum = 0
    sum_list = []
    for line in input:
        if line == '':
            sum_list.append(sum)
            sum = 0
        else:
            sum += int(line)
    return sum_list

all_calories = read_input("day1input.txt")

sorted_calories = add_numbers(all_calories)

# return max value in list
print(max(sorted_calories))

# find the top 3 numbers in the list
sorted_calories.sort(reverse=True)
top_three = sorted_calories[:3]

# sum the top 3 numbers
print(sum(top_three))

