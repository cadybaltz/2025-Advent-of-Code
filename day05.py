"""
cadybaltz
12/11/2025
AoC 2025 Day 5
Part 1: 00:37:26 (self-timed, completed late)
Part 2: 00:45:37 (self-timed, completed late)
"""

def parse_input(input):
    ranges = {}
    all_mins = []
    finished_ranges = False

    ids = []

    for x in range(len(input)):
        if input[x] == "\n":
            finished_ranges = True
            continue

        line = input[x].strip()

        if not finished_ranges:
            start = int(line.split("-")[0])
            end = int(line.split("-")[1])
            all_mins.append(start)
            if start in ranges:
                ranges[start] = max(ranges[start], end) # merge smaller range into larger range it's a part of
            else:
                ranges[start] = end

        else:
            ids.append(int(line))

    sorted_mins = sorted(all_mins)

    return ranges, sorted_mins, ids

# optimized solution to check all possible ranges each ID could be in
def pt_1_solution(input):
    result = 0
    ranges, sorted_mins, ids = parse_input(input)
    
    for id in ids:
        x = 0

        # stop iterating once the ranges have gotten too large
        while x < len(sorted_mins) and id >= sorted_mins[x]:
            if id <= ranges[sorted_mins[x]]:
                result += 1
                x = len(sorted_mins)
            x += 1

    return result

# merge all overlapping ranges, then count the size of all non-overlapping ranges
def pt_2_solution(input):
    result = 0
    ranges, sorted_mins, _ = parse_input(input)

    finished_merging = False
    while not finished_merging:
        finished_merging = True
        new_ranges = {}
        new_sorted_mins = []

        x = 0
        while x < len(sorted_mins):
            curr_start = sorted_mins[x]
            curr_end = ranges[curr_start]

            y = x + 1
            done = False
            while y < len(sorted_mins) and not done:
                next_start = sorted_mins[y]
                next_end = ranges[next_start]

                if next_start <= curr_end:
                    curr_end = max(curr_end, next_end)
                    finished_merging = False
                    y += 1
                else:
                    done = True

            new_ranges[curr_start] = curr_end
            new_sorted_mins.append(curr_start)
            x = y

        ranges = new_ranges
        sorted_mins = new_sorted_mins

    for range in ranges:
        result += ranges[range] - range + 1
        
    return result

if __name__ == '__main__':
    filename = "input.txt"
    input = open(filename, "r")

    lines = input.readlines()
    print("Part 1: " + str(pt_1_solution(lines)))
    print("Part 2: " + str(pt_2_solution(lines)))