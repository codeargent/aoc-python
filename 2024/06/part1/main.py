def main():
    with open("input.txt", "r") as file:
        content = file.read().split('\n')

        guard_current_position = None

        for i in range(len(content)):
            for j in range(len(content[i])):
                if content[i][j] == "^":
                    guard_current_position = (i,j)
        
        ended = False
        positions = {guard_current_position}
        movement = (-1,0)
        while not ended:
            next_position = (guard_current_position[0] + movement[0], guard_current_position[1] + movement[1])
            next_value = get_content_value(content, next_position)

            if next_value == '':
                ended = True
            elif next_value == "#":
                movement = switch_movement(movement)
            else:
                guard_current_position = (guard_current_position[0] + movement[0], guard_current_position[1] + movement[1])
                positions.add(guard_current_position)
        
        print(len(positions))

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

if __name__ == '__main__':
    main()