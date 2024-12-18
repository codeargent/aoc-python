# Load the input map from the file
with open('input.txt', 'r') as file:
    garden_map = [list(line.strip()) for line in file.readlines()]

rows = len(garden_map)
cols = len(garden_map[0])

directions = [
    (-1, 0), # up
    (1, 0), # down
    (0, -1), # left
    (0, 1) # right
]

def flood_fill(x, y, plant_type):
    area = 0
    perimeter = 0
    stack = [(x, y)]
    visited[x][y] = True
    
    while stack:
        cx, cy = stack.pop()
        area += 1
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if garden_map[nx][ny] == plant_type and not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
                elif garden_map[nx][ny] != plant_type:
                    perimeter += 1
            else:
                perimeter += 1
    
    return area, perimeter

# Initialize visited map and calculate total price
visited = [[False for _ in range(cols)] for _ in range(rows)]
total_price = 0

for i in range(rows):
    for j in range(cols):
        if not visited[i][j]:
            plant_type = garden_map[i][j]
            area, perimeter = flood_fill(i, j, plant_type)
            total_price += area * perimeter

print(total_price)
