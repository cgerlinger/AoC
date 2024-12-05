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

def main():
	filename = 'input.txt'
	rules, updates = parseFile(filename)
	graph = buildGraph(rules)

	validUpdates = [update for update in updates if isValidUpdate(graph, update)]
	middlePages = [findMiddle(update) for update in validUpdates]
	result = sum(middlePages)

	print(f'Result: {result}')

if __name__ == "__main__":
	main()