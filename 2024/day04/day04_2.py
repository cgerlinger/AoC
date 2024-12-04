def occurrences(filename):
	with open (filename, "r") as file:
		grid = [line.strip() for line in file.readlines()]

	count = 0
	
	for row in range (1, len(grid) - 1):
		for col in range (1, len(grid[0]) - 1):
			if grid[row][col] == "A":
				if grid[row - 1][col - 1] == "M" and grid[row - 1][col + 1] == "S" and grid[row + 1][col + 1] == "S" and grid[row + 1][col - 1] == "M":
					count += 1
				elif grid[row - 1][col - 1] == "S" and grid[row - 1][col + 1] == "M" and grid[row + 1][col + 1] == "M" and grid[row + 1][col - 1] == "S":
					count += 1
				elif grid[row - 1][col - 1] == "M" and grid[row - 1][col + 1] == "M" and grid[row + 1][col + 1] == "S" and grid[row + 1][col - 1] == "S":
					count += 1
				elif grid[row - 1][col - 1] == "S" and grid[row - 1][col + 1] == "S" and grid[row + 1][col + 1] == "M" and grid[row + 1][col - 1] == "M":
					count += 1

	return count

def main():
	filename = 'input.txt'
	print(occurrences(filename))

if __name__ == "__main__":
	main()