# List can be found here: https://adventofcode.com/2020/day/1/input

start = 0

while True:
    for i in lst:
        x = i
        for j in lst[start+1:]:
            y = j
            for k in lst[start+2:]:
                z = k
                if x + y + z == 2020:
                    first_number = x
                    second_number = y
                    third_number = z
                    print(f'First number: {first_number}\nSecond Number: {second_number}\nThird Number: {third_number}')
                    multiply = first_number * second_number * third_number
                    print(f'Multiply all, we get: {multiply}')
                    exit()
        start +=1
