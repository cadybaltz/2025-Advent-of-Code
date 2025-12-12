"""
cadybaltz
12/12/2025
AoC 2025 Day 12
Part 1: 00:24:42
Part 2: 00:25:07
"""
import re

# this is not a real solution, but it gave me the right answer
# just check if the total area of all shapes in the region is less than the area of the region
# i was initially trying this approach just to narrow down the search space, i wasn't expecting it to give me the answer...oops!
def pt_1_solution(input):
    result = 0
    presents= {}
    regions = []

    x = 0

    # parse input
    while x < len(input):
        if input[x] == "\n" or input[x].strip() == "":
            x+=1
        elif input[x][1] == ":":
            id = int(input[x][0])
            shape = [input[x+1].strip(), input[x+2].strip(), input[x+3].strip()]
            presents[id] = shape
            x += 4
        else:
            pattern = r'(\d+)x(\d+):\s(\d+)\s(\d+)\s(\d+)\s(\d+)\s(\d+)\s(\d+)'
            match = re.match(pattern, input[x].strip())

            width = int(match.group(1))
            length = int(match.group(2))
            counts = [int(match.group(i)) for i in range(3, 9)]

            regions.append((width, length, counts))
            x+=1
    
    for region in regions:
        width, length, counts = region
        total_boxes = 0
        
        # compute total area of all shapes that you need to place
        for x in range(len(counts)):
            for _ in range(counts[x]):
                shape = presents[x]
                for y in range(len(shape)):
                    for z in range(len(shape[0])):
                        if shape[y][z] == '#':
                            total_boxes += 1

        # check if the total area of shapes will fit in the region
        if total_boxes > width * length:
            continue
        else:
            result += 1
    return result

if __name__ == '__main__':
    filename = "input.txt"
    input = open(filename, "r")

    lines = input.readlines()
    print("Part 1: " + str(pt_1_solution(lines)))