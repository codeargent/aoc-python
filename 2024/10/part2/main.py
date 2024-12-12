def main():
    with open("input.txt", "r") as file:
        content = file.read().split()

        trailheads = []
        for li, line in enumerate(content):
            for ci, char in enumerate(line):
                if char == '0':
                    trailheads.append((li, ci))
        
        total_trails = 0
        for trailhead in trailheads:
            total_trails += find_trails(content, trailhead, 0, [])
        
        print(total_trails)

def find_trails(content, position, counter, reachable_nines):
    if get_value(content, position) != str(counter):
        return

    if counter == 9:
        reachable_nines.append(position)
        return

    directions = [
        (position[0] - 1, position[1]),  # up
        (position[0] + 1, position[1]),  # down
        (position[0], position[1] - 1),  # left
        (position[0], position[1] + 1)   # right
    ]

    for pos in directions:
        find_trails(content, pos, counter + 1, reachable_nines)
    
    return len(reachable_nines)

def get_value(content, pos):
    try:
        if pos[0] < 0 or pos[1] < 0:
            raise

        return content[pos[0]][pos[1]]
    except:
        return ''

if __name__ == '__main__':
    main()