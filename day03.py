"""
cadybaltz
12/03/2025
AoC 2025 Day 3
Part 1: 00:02:13
Part 2: 00:33:58
"""

def pt_1_solution(input):
    result = 0

    # brute force solution - checking all pairs of two digits (in order based on string position)
    for line in input:
        max = 0
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                substr = line[i] + line[j]
                if int(substr) > max:
                    max = int(substr)
        result += max

    return result


def pt_2_solution(input):
    result = 0

    for line in input:
        line = line.strip()
        joltage = []
        remaining = line

        # find 12 digits by greedily finding the largest digit possible with enough remaining digits
        while len(joltage) < 12:
            if len(joltage) < 11:
                # attempt to find the largest digit first
                for w in range(9, -1, -1):
                    index = remaining.find(str(w))

                    # you must have at least 12 - [digits so far] remaining after this digit
                    if index != -1 and (index <= len(remaining) - (12 - len(joltage))):
                        joltage.append(remaining[index])
                        remaining = remaining[index+1:]
                        break
            else:
                # for the last digit, just find the largest remaining digit anywhere in the remaining substring
                for w in range(9, -1, -1):
                    index = remaining.find(str(w))
                    if index != -1:
                        joltage.append(remaining[index])
                        break

        result += int(''.join(joltage))

    return result

if __name__ == '__main__':
    filename = "input.txt"
    input = open(filename, "r")

    lines = input.readlines()
    print("Part 1: " + str(pt_1_solution(lines)))
    print("Part 2: " + str(pt_2_solution(lines)))