"""
cadybaltz
12/07/2025
AoC 2025 Day 7
Part 1: 00:05:54
Part 2: 00:54:47
"""

# keep track of all the beams as you go down as a simple array
def pt_1_solution(input):
    result = 0

    beams = []
    for x in input[0].strip():
        if x == 'S':
            beams.append(1)
        else:
            beams.append(0)


    for line in input[1:]:
        next_beams = [0] * len(beams)
        for x in range(len(line.strip())):

            # for every splitter, create two new beams
            if line[x] == '^' and beams[x] > 0:
                result += 1
                
                if x > 1:
                    next_beams[x-1] += 1
                if x < len(line.strip()) - 2:
                    next_beams[x+1] += 1

            # if there is no splitter, just move the beams down
            elif beams[x] > 0:
                next_beams[x] += 1   
        beams = next_beams
    


    return result


memo = {}

def possible_paths(input, row, pos):
    if (row, pos) in memo:
        return memo[(row, pos)]
    
    if len(input) - 1 == row:
        return 1
    
    result = 0
    
    if input[row+1][pos] == '^':
        if pos > 1:
            result += possible_paths(input, row+1, pos-1)

        if pos < len(input[row+1].strip()) - 2:
            result += possible_paths(input, row+1, pos+1)
    else:
        result += possible_paths(input, row+1, pos)
    
    memo[(row, pos)] = result
    return result

def pt_2_solution(input):
    for x in range(len(input[0].strip())):
        if input[0][x] == 'S':

            # I honestly don't know why I need to add 2, but it works
            return possible_paths(input, 0, x) + 2

if __name__ == '__main__':
    input = open("input.txt", "r")
    lines = input.readlines()
    print("Part 1: " + str(pt_1_solution(lines)))
    print("Part 2: " + str(pt_2_solution(lines)))