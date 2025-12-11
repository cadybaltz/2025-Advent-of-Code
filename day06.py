"""
cadybaltz
12/06/2025
AoC 2025 Day 6
Part 1: 6:03 (self-timed, completed late)
Part 2: 27:56 (self-timed, completed late)
"""

def pt_1_solution(input):
    result = 0
    problems = []
    for val in input[0].strip().split():
        problems.append([val])

    for x in range(1,len(input)-1):
        curr_line = input[x].strip().split()
        for y in range(len(curr_line)):
            problems[y].append(curr_line[y])

    symbols = input[len(input)-1].strip().split()
    
    for x in range(len(problems)):
        answer = int(problems[x][0])
        for value in problems[x][1:]:
            if symbols[x] == "*":
                answer = answer * int(value)
            elif symbols[x] == "+":
                answer = answer + int(value)
        result += answer

    return result

def pt_2_solution(input):
    problems = []
    for x in range(len(input[0].split())):
        problems.append([])

    symbols = []
    curr_problem = -1

    for x in range(len(input[len(input)-1])):
        if input[len(input)-1][x] != " ":
            symbols.append(input[len(input)-1][x])
            curr_problem += 1
        if curr_problem >= len(problems):
            break
        number = ""
        for y in range(len(input)-1):
            if input[y][x] != " ":
                number = number + input[y][x]
        if len(number) > 0:
            problems[curr_problem].append(int(number))
            
    result = 0
    for x in range(len(problems)):
        answer = problems[x][0]
        for y in range(1,len(problems[x])):
            if symbols[x] == "*":
                answer = answer * problems[x][y]
            elif symbols[x] == "+":
                answer = answer + problems[x][y]
        result += answer
    return result

if __name__ == '__main__':
    filename = "input.txt"
    input = open(filename, "r")

    lines = input.readlines()
    print("Part 1: " + str(pt_1_solution(lines)))
    print("Part 2: " + str(pt_2_solution(lines)))