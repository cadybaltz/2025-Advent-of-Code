"""
cadybaltz
12/08/2025
AoC 2025 Day 8
Part 1: 00:15:25
Part 2: 00:17:46
"""

def distance(a, b):
    # straight line distance formula
    # https://en.wikipedia.org/wiki/Euclidean_distance
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2) ** 0.5


def pt_1_solution(input, num_connections=1000):
    
    # map of index to coordinates
    inputs = {}

    # map of index pairs to the distance between them
    distances = {}

    # map of input index to the circuit group it is in
    input_to_grouping = {}
    # map of circuit group to the list of input indices
    grouping_to_inputs = {}

    total = len(input)
    
    # first, just parse input
    for i in range(len(input)):
        x,y,z = input[i].strip().split(",")

        inputs[i] = (int(x), int(y), int(z))

        # to start, each box is its own circuit group
        input_to_grouping[i] = i
        grouping_to_inputs[i] = [i]
    
    # compute distances between all pairs
    for x in range(total):
        for y in range(x+1,total):
            if x != y:
                dist = distance(inputs[x], inputs[y])
                distances[(x,y)] = dist

    sorted_distances = sorted(distances.items(), key=lambda item: item[1])

    # perform the desired number of connections
    for indices, dist in sorted_distances[:num_connections-1]:
        a,b = indices
        group_a_id = input_to_grouping[a]
        group_b_id = input_to_grouping[b]

        # if the two boxes are in different circuit groups, join the groups (move all B boxes to the A group)
        if group_a_id != group_b_id:
            for input in grouping_to_inputs[group_b_id]:
                input_to_grouping[input] = group_a_id
                grouping_to_inputs[group_a_id].append(input)

            # remove the old group
            del grouping_to_inputs[group_b_id]
            

    # sort groupings based on count
    sorted_groupings = dict(sorted(grouping_to_inputs.items(), key=lambda item: len(item[1]), reverse=True))

    result = 1

    # get three largest groupings and multiply sizes
    for val in list(sorted_groupings.values())[:3]:
        result *= len(val)

    return result


def pt_2_solution(input):
    # map of index to coordinates
    inputs = {}

    # map of index pairs to the distance between them
    distances = {}

    # map of input index to the circuit group it is in
    input_to_grouping = {}
    # map of circuit group to the list of input indices
    grouping_to_inputs = {}

    total = len(input)
    
    # first, just parse input
    for i in range(len(input)):
        x,y,z = input[i].strip().split(",")

        inputs[i] = (int(x), int(y), int(z))

        # to start, each box is its own circuit group
        input_to_grouping[i] = i
        grouping_to_inputs[i] = [i]
    
    # compute distances between all pairs
    for x in range(total):
        for y in range(x+1,total):
            if x != y:
                dist = distance(inputs[x], inputs[y])
                distances[(x,y)] = dist

    sorted_distances = sorted(distances.items(), key=lambda item: item[1])

    # (part 2) keep going through the distances in order until there is only one group
    for indices, dist in sorted_distances:
        a,b = indices
        group_a_id = input_to_grouping[a]
        group_b_id = input_to_grouping[b]

        # if the two boxes are in different circuit groups, join the groups (move all B boxes to the A group)
        if group_a_id != group_b_id:
            for input in grouping_to_inputs[group_b_id]:
                input_to_grouping[input] = group_a_id
                grouping_to_inputs[group_a_id].append(input)

            # remove the old group
            del grouping_to_inputs[group_b_id]

            # (part 2) if group A contains all inputs, return the produce of the x coords of the boxes you just connected
            if len(grouping_to_inputs[group_a_id]) == total:
                return inputs[a][0] * inputs[b][0]

if __name__ == '__main__':
    filename = "input.txt"
    input = open(filename, "r")

    lines = input.readlines()
    print("Part 1: " + str(pt_1_solution(lines)))
    print("Part 2: " + str(pt_2_solution(lines)))