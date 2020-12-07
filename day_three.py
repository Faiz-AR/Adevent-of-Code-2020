# Input can be found here: https://adventofcode.com/2020/day/3/input

with open("input.txt") as f:
    input_test = []
    for line in f:
        input_test.append(line.rstrip())

def move(roadmap,right,down):
    column_index = 0
    row_index = 0
    lane_length = len(roadmap[0])
    trees = 0

    while True:
        column_index = (column_index + right) % lane_length
        row_index += down

        #Check if at bottom lane
        if row_index >= len(roadmap):
            break
        
        current = roadmap[row_index][column_index]
        #Check for trees
        if current == '#':
            trees+=1

    return trees

print(f'[PART 1] No of trees: {move(input_test,3,1)}')
print(f'[PART 2] No of trees: {move(input_test,1,1)*move(input_test,3,1)*move(input_test,5,1)*move(input_test,7,1)*move(input_test,1,2)}')