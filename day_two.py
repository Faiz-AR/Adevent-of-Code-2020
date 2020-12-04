# Input can be found here: https://adventofcode.com/2020/day/2/input


with open("input.txt") as file_in:
    input_test = []
    for line in file_in:
        input_test.append(line)

def info(a):
    index_of_colon = a.find(':')
    index_of_hyphen = a.find('-')
    l = a[index_of_colon-1]
    p = a[index_of_colon+2:]
    p_one = int(a[:index_of_hyphen])
    p_two = int(a[index_of_hyphen+1:index_of_colon-2])

    return (l,p,p_one,p_two)

valid_passwords = 0
counter = 1

for i in input_test:
    letter,password,pos_one,pos_two = info(i)
    print(f'Password {counter}')
    if password[pos_one-1] == letter or password[pos_two-1] == letter:
        if password[pos_one-1] == letter and password[pos_two-1] == letter:
            print(f'Invalid : {password}')
        else:
            print(f'Valid : {password}')
            valid_passwords+=1
    else:
        print(f'Invalid : {password}')

    counter+=1
    print('')

print(f'Valid passwords: {valid_passwords}')


    