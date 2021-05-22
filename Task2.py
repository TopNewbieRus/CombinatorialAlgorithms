n = int(input())
adjacency = []
for i in range(n):
	inp = [int(j) - 1 for j in input().split()]
	inp.pop(-1)
	adjacency.append(inp)

visited = []
component = []

def bfs(vertex):
	queue = [vertex]
	while len(queue) > 0:
		current = queue.pop(0)	
		visited.append(current)		
		for neighbor in adjacency[current]:
			if neighbor not in visited and neighbor not in queue:
				queue.append(neighbor)


while len(visited) != len(adjacency):
	for vertex in range(len(adjacency)):
		if vertex not in visited:
			component.append(vertex)
			bfs(vertex)

components = []
for root in component:
	visited = []
	bfs(root)
	components.append(visited)
	components[-1].sort()
	for i in range(len(components[-1])):
		components[-1][i] += 1

print(f"Компонент связности: {len(component)}")
for component in components:
	print(*component, sep=" ", end=" 0 \n")