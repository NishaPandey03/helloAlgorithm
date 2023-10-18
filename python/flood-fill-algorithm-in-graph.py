# Assuming the grid is represented as a 2D list where 0 represents an unvisited cell and 1 represents a visited cell
def flood_fill(grid, row, col, target_color, new_color):
    rows = len(grid)
    cols = len(grid[0])

    # Base cases: Check if the current cell is within the grid and has the target color
    if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != target_color:
        return

    # Change the color of the current cell
    grid[row][col] = new_color

    # Visit the neighboring cells in all four directions
    flood_fill(grid, row - 1, col, target_color, new_color)  # Up
    flood_fill(grid, row + 1, col, target_color, new_color)  # Down
    flood_fill(grid, row, col - 1, target_color, new_color)  # Left
    flood_fill(grid, row, col + 1, target_color, new_color)  # Right

# Example usage
grid = [
    [1, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [1, 1, 0, 0, 1]
]

# Fill the area connected to cell (1, 1) with color 2
flood_fill(grid, 1, 1, 1, 2)

# Print the updated grid
for row in grid:
    print(row)
