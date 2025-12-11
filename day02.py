"""
cadybaltz
12/02/2025
AoC 2025 Day 2
Part 1: 00:05:07
Part 2: 00:15:29
"""

# simple brute force solution
def pt_1_solution(input):
    result = 0

    ranges = input[0].split(',')

    # check each range
    for curr in ranges:
        start_str, end_str = curr.split('-')
        start = int(start_str)
        end = int(end_str)

        # check each possible ID
        for x in range(start, end + 1):
            id = str(x)

            # an only ID can only have two matching halves if its length is even (ignore rounding math)
            if len(id) % 2 == 0:
                # check if first half of substring equals second half
                mid = len(id) // 2
                first = id[:mid]
                second = id[mid:]
                if first == second:
                    result += x

    return result

# brute force solution with a bit of pruning
def pt_2_solution(input):
    result = 0

    ranges = input[0].split(',')

    # check each range
    for curr in ranges:
        start_str, end_str = curr.split('-')
        start = int(start_str)
        end = int(end_str)

        # check each possible ID
        for x in range(start, end + 1):
            id = str(x)

            # only possible to duplicate a substring until the halfway point of the string
            # check all possible substring lengths up to the midpoint
            for length in range(1, int(len(id) / 2) + 1):

                # split the string into substrings of the given length
                first_substring = id[0:length]

                # check that all the substrings of this length are equal (break if not)
                all_equal = True
                for i in range(0, len(id), length):
                    if id[i:i + length] != first_substring:
                        all_equal = False
                        break
                    
                if all_equal:
                    result += x
                    # move to the next ID
                    break
    return result

if __name__ == '__main__':
    input = open("input.txt", "r")

    lines = input.readlines()
    print("Part 1: " + str(pt_1_solution(lines)))
    print("Part 2: " + str(pt_2_solution(lines)))