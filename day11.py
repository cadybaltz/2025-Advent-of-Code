"""
cadybaltz
12/11/2025
AoC 2025 Day 11
Part 1: 00:04:19
Part 2: 00:11:49
"""

def parse_input(input):
    inputs_to_outputs = {}
    for line in input:
        values = line.split()
        input = values[0][:-1]
        outputs = []
        for i in range(1, len(values)):
            outputs.append(values[i])
        inputs_to_outputs[input] = outputs
    return inputs_to_outputs


# BFS, storing all complete paths in a set
def pt_1_solution(input):
    inputs_to_outputs = parse_input(input)

    paths = set()

    queue = []
    for val in inputs_to_outputs["you"]:
        queue.append((val, []))
    
    while len(queue) > 0:
        next, path = queue.pop(0)
        new_path = path + [next]

        if next == "out":
            paths.add(tuple(new_path))
        else:
            for val in inputs_to_outputs[next]:
                queue.append((val, new_path))

    return len(paths)

# recursively count paths to "out" with memoization
# only count paths that pass through both "dac" and "fft" (pass in whether they have been seen yet)
def paths_to_out(inputs_to_outputs, start, memo, dac, fft):
    if (start, dac, fft) in memo:
        return memo[(start, dac, fft)]
    
    if start == "out" :
        if dac and fft:
            return 1
        else:
            return 0
    
    if start == "dac":
        dac = True
    if start == "fft":
        fft = True
    
    total_paths = 0
    for next_node in inputs_to_outputs.get(start, []):
        total_paths += paths_to_out(inputs_to_outputs, next_node, memo, dac, fft)
    
    memo[(start, dac, fft)] = total_paths
    return total_paths

def pt_2_solution(input):

    inputs_to_outputs = parse_input(input)

    memo = {}    
    return paths_to_out(inputs_to_outputs, "svr", memo, False, False)

if __name__ == '__main__':
    filename = "input.txt"
    input = open(filename, "r")
    lines = input.readlines()
    print("Part 1: " + str(pt_1_solution(lines)))
    print("Part 2: " + str(pt_2_solution(lines)))