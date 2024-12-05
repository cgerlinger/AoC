from collections import defaultdict, deque

def parseFile(filename):
	with open (filename, 'r') as file:
		data = file.read().strip()
	rulesData, updatesData = data.split('\n\n')
	rules = [tuple(map(int, line.split('|'))) for line in rulesData.splitlines()]
	updates = [list(map(int, line.split(','))) for line in updatesData.splitlines()]

	return rules, updates

def buildGraph(rules):
	graph = defaultdict(list)

	for x, y in rules:
		graph[x].append(y)
	return graph

def isValidUpdate(graph, update):
	position = {page: idx for idx, page in enumerate(update)}
	for x in update:
		for y in graph[x]:
			if y in position and position[x] >= position[y]:
				return False
	return True

def findMiddle(update):
	return update[len(update) // 2]

def topologicalSort(graph, update):
	indegree = {node: 0 for node in update}
	for node in update:
		for neighbor in graph[node]:
			if neighbor in indegree:
				indegree[neighbor] += 1

	queue = deque([node for node in update if indegree[node] == 0])
	sorted_list = []

	while queue:
		node = queue.popleft()
		sorted_list.append(node)
		for neighbor in graph[node]:
			if neighbor in indegree:
				indegree[neighbor] -= 1
				if indegree[neighbor] == 0:
					queue.append(neighbor)

	return sorted_list

def main():
	filename = 'input.txt'
	rules, updates = parseFile(filename)
	graph = buildGraph(rules)

	invalidUpdates = [update for update in updates if not isValidUpdate(graph, update)]
	correctedUpdates = [topologicalSort(graph, update) for update in invalidUpdates]
	middlePages = [findMiddle(update) for update in correctedUpdates]
	result = sum(middlePages)

	print(f'Result: {result}')

if __name__ == "__main__":
	main()