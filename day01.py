"""
cadybaltz
12/01/2025
AoC 2025 Day 1
Part 1: 00:33:09
Part 2: 00:34:46
"""

def pt_1_solution(lines):
    result = 0
    dial = 50

    for line in lines:
        ch = line[0]
        num = int(line[1:])

        # the dial completes a full rotation
        if num > 99:
            num = num % 100

        if ch == 'L':
            dial -= num
        elif ch == 'R':
            dial += num

        # wrap around logic
        if dial < 0:
            dial = 99 + dial + 1
        if dial > 99:
            dial = dial - 100

        # if dial is at zero at the end of the turn
        if dial == 0:
            result += 1

    return result


def pt_2_solution(lines):
    result = 0
    dial = 50

    for line in lines:
        ch = line[0]
        num = int(line[1:])

        # the dial completes a full rotation
        if num > 99:
            # add one to the result per full rotation
            result += num // 100
            
            num = num % 100

        original_dial = dial
        if ch == 'L':
            dial -= num
        elif ch == 'R':
            dial += num

        if dial == 0:
            result += 1
        elif dial < 0:
            dial = 99 + dial + 1
            if original_dial != 0:
                result += 1
        elif dial > 99:
            dial = dial - 100
            if original_dial != 0:
                result += 1

    return result



if __name__ == '__main__':
    input = open("input.txt", "r")

    lines = input.readlines()
    print("Part 1: " + str(pt_1_solution(lines)))
    print("Part 2: " + str(pt_2_solution(lines)))