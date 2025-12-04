def accessible_rolls(grid):

    num_rows = len(grid)
    num_cols = len(grid[0])

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    ]

    new_grid = [row[:] for row in grid]
    accessible_count = 0

    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == '@':
                neighbor_count = 0
                for di, dj in directions:
                    i2 = i + di
                    j2 = j + dj
                    if 0 <= i2 < num_rows and 0 <= j2 < num_cols:
                        if grid[i2][j2] == '@':
                            neighbor_count += 1
                if neighbor_count < 4:
                    new_grid[i][j] = 'x'
                    accessible_count += 1

    return new_grid, accessible_count

def main():

    grid = []
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            if line:  
                grid.append(list(line))

    i = 1
    result = 0
    while True:
        new_grid, accessible_count = accessible_rolls(grid)

        if accessible_count == 0:
            break

        grid = new_grid
        print(f"\nAccessible rolls in iteration {i}: {accessible_count}\n")
        result += accessible_count

    for row in new_grid:
        print(''.join(row))

    print(f"\nAccessible rolls: {result}\n")

if __name__ == '__main__':
    main()