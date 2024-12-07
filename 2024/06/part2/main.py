def main():
    with open("input.txt", "r") as file:
        content = file.read().split('\n')

        guard_current_position = None

        for i in range(len(content)):
            for j in range(len(content[i])):
                if content[i][j] == "^":
                    guard_current_position = (i,j)
        
        positions, _ = move_guard(content, guard_current_position)
        positions = list(positions)

        loops = 0
        for i in range(0, len(positions)):
            position = positions[i]

            _, loop = move_guard(content, guard_current_position, False, position)
            if loop:
                loops += 1

        print(loops)

def get_content_value(content, position):
    try:
        if position[0] < 0 or position[1] < 0:
            raise

        return content[position[0]][position[1]]
    except:
        return ''

def switch_movement(current_movement):
    match current_movement:
        case (-1,0):
            return (0,1)
        case (0,1):
            return (1,0)
        case (1,0):
            return (0,-1)
        case (0,-1):
            return (-1,0)

def move_guard(content, guard_current_position, track_positions = True, new_barrier = None):
    ended = False
    loop = False

    movement = (-1,0)
    positions = {guard_current_position}
    movements = set()

    while not ended:
        next_position = (guard_current_position[0] + movement[0], guard_current_position[1] + movement[1])
        next_value = get_content_value(content, next_position)

        if next_value == '':
            ended = True
        elif next_value == "#" or next_position == new_barrier:
            if (guard_current_position, movement) in movements:
                loop = True
                ended = True
            
            movements.add((guard_current_position, movement))
            
            movement = switch_movement(movement)
        else:
            movements.add((guard_current_position, movement))
            guard_current_position = (guard_current_position[0] + movement[0], guard_current_position[1] + movement[1])
            if track_positions:
                positions.add(guard_current_position)
    
    return (positions, loop)

if __name__ == '__main__':
    main()