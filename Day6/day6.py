import os, sys

if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
inp = sys.stdin.read().strip()
inp = inp.split('\n')

rows = len(inp); cols = len(inp[0])

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def part1():
	gr, gc, gd = None, None, None
	for r in range(rows):
		for c in range(cols):
			if inp[r][c] in "^>v<":
				gr, gc = r, c
				gd = "^>v<".index(inp[r][c])  # Map direction symbol to index
				break

	# Set to track distinct visited positions
	visited = set()
	visited.add(f"{gr},{gc}")

	# Simulate guard movement
	while True:
		dr, dc = dirs[gd]
		next_row, next_col = gr + dr, gc + dc

		# Check if the next position is outside the grid
		if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
			break  # Guard leaves the grid

		if inp[next_row][next_col] == "#":
			# Obstacle ahead: turn right (clockwise)
			gd = (gd + 1) % 4
		else:
			# Move forward
			gr, gc = next_row, next_col
			visited.add(f"{gr},{gc}")
	
	return len(visited)

def part2():
	# Locate the guard's initial position and direction
	sr, sc, sd = None, None, None
	for r in range(rows):
		for c in range(cols):
			if inp[r][c] in "^>v<":
				sr, sc = r, c
				sd = "^>v<".index(inp[r][c])  # Map direction symbol to index
				break


	# Function to simulate guard movement with an optional extra obstacle
	def eval(obstacle_row, obstacle_col):
		gr, gc, gd = sr, sc, sd
		visited = set()
		visited.add(f"{gr},{gc},{gd}")

		while True:
			dr, dc = dirs[gd]
			next_row = gr + dr
			next_col = gc + dc

			# Check if the next position is outside the grid
			if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
				return False  # Guard exits the grid

			# Treat the additional obstacle as if it's a `#`
			next_cell = (
				"#"
				if (next_row == obstacle_row and next_col == obstacle_col)
				else inp[next_row][next_col]
			)
			if next_cell == "#":
				# Obstacle ahead, turn right
				gd = (gd + 1) % 4
			else:
				# Move forward
				gr = next_row
				gc = next_col

			state = f"{gr},{gc},{gd}"
			if state in visited:
				return True  # Loop detected
			visited.add(state)


	# Count valid positions for the new obstruction
	valid_positions = 0

	for r in range(rows):
		for c in range(cols):
			# Skip positions that are not empty or are the starting position
			if inp[r][c] == "#" or (r == sr and c == sc):
				continue

			# Simulate guard movement with an obstacle at (r, c)
			if eval(r, c):
				valid_positions += 1
	
	return valid_positions

print(part1())
print(part2())
