# List can be found here: https://adventofcode.com/2020/day/1/input

start = 0
loop = True

while loop:
    for i in lst:
        x = i
        for j in lst[start+1:]:
            y = j
            if x + y == 2020:
                first_number = x
                second_number = y
                print(f'First number: {first_number}\nSecond Number: {second_number}')
                multiply = first_number * second_number
                print(f'Multiply both, we get: {multiply}')
                loop = False
            else:
                continue
        start +=1