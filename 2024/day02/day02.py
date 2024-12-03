def isSafe(report):
	levels = list(map(int, report.split()))

	increasing = all(levels[i] < levels[i+1] for i in range(len(levels)-1))
	decreasing = all(levels[i] > levels[i+1] for i in range(len(levels)-1))

	validDiff = all(1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))

	if (increasing or decreasing) and validDiff:
		return True
	
	# Part 2
	for i in range(len(levels)):
		newLevels = levels[:i] + levels[i+1:]
		increasing = all(newLevels[j] < newLevels[j + 1] for j in range(len(newLevels) - 1))
		decreasing = all(newLevels[j] > newLevels[j + 1] for j in range(len(newLevels) - 1))
		valid_difference = all(1 <= abs(newLevels[j] - newLevels[j + 1]) <= 3 for j in range(len(newLevels) - 1))
		if (increasing or decreasing) and valid_difference:
			return True
		
	return False

def main():
	with open('input.txt') as f:
		lines = f.readlines()

	totalSafe = 0

	for line in lines:
		line = line.strip()
		if line:
			if isSafe(line):
				totalSafe += 1

	print(f'Total safe: {totalSafe}')

if __name__ == '__main__':
	main()