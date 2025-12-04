"""
cadybaltz
12/04/2025
AoC 2025 Day 4
Part 1: 00:07:50
Part 2: 00:10:53
"""

# copy/paste grid starter code for iterating over all neighbors
def modify_neighbor(grid, val, x, y):
    neighbors = [(-1,-1),(-1,0), (-1,1),(0,-1),(0, 1),(1,-1),(1,0),(1,1)]

    for neighbor in neighbors:
        new_x = x + neighbor[0]
        new_y = y + neighbor[1]
        if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
            # modify the neighbor based on the input val
            grid[new_x][new_y] += val

def solution(input, part_2=False):
    result = 0

    grid = []
    grid_vals = []

    for line in input:
        grid.append(list(line.strip()))
        grid_vals.append([0 for _ in range(len(line.strip()))])
        
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == '@':
                # add a point to each neighbor
                modify_neighbor(grid_vals, 1, x, y)
    
    # part 1: find all rolls with less than four neighbors
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid_vals[x][y] < 4 and grid[x][y] == '@':
                result += 1

    if part_2:
        result = 0

        # continue removing rolls until none were removed in the last round
        added_new = True
        while added_new:
            added_new = False
            
            for x in range(len(grid)):
                for y in range(len(grid[0])):
                    if grid_vals[x][y] < 4 and grid[x][y] == '@':

                        # removing a roll
                        result += 1
                        added_new = True
                        grid[x][y] = '.'

                        # remove a point from each neighbor
                        modify_neighbor(grid_vals, -1, x, y)
                
    return result

if __name__ == '__main__':
    filename = "input.txt"
    input = open(filename, "r")

    lines = input.readlines()
    print("Part 1: " + str(solution(lines)))
    print("Part 2: " + str(solution(lines, part_2=True)))