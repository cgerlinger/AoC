def occurrences(filename):
	with open (filename, "r") as file:
		grid = [line.strip() for line in file.readlines()]

	directions = [(0, 1), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, -1), (-1, 0)]
	count = 0

	for row in range (len(grid)):
		for col in range (len(grid[0])):
			if grid[row][col] == "X":
				for dx, dy in directions:
					if 0 <= row + 3 * dx < len(grid) and 0 <= col + 3 * dy < len(grid[0]):
						if grid[row + dx][col + dy] == "M" and grid[row + 2 * dx][col + 2 * dy] == "A" and grid[row + 3 * dx][col + 3 * dy] == "S":
							count += 1

	return count

def main():
	filename = 'input.txt'
	print(occurrences(filename))

if __name__ == "__main__":
	main()