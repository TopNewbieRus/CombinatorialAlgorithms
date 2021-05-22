n = int(input())
adjacency = []
for i in range(n):
	inp = [int(j) for j in input().split()]
	adjacency.append([i for i in range(len(inp)) if inp[i] == 1])
color = {k: 0 for k in range(1, n + 1)}

visited = []

def is_bipartate(vertex):
	stack = [vertex]
	color[vertex] = 1
	while len(stack) > 0:
		current = stack.pop(-1)
		visited.append(current)
		for neighbor in adjacency[current]:
			if color[neighbor] != 0 and color[neighbor] == color[current]:
				return False
			if color[neighbor] == 0:
				color[neighbor] = -color[current]
				stack.append(neighbor)
	return True

result = is_bipartate(0)
if not result:
	print("N")
else:
	print("Y")
	part_1 = [k + 1 for k in color.keys() if color[k] == 1]
	part_1.sort()
	part_2 = [k + 1 for k in color.keys() if color[k] == -1]
	part_2.sort()
	if 1 not in part_1:
		part_1, part_2 = part_2, part_1
	print(*part_1, end=" 0 \n")
	print(*part_2, end=" 0 \n")