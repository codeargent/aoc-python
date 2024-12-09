def main():
    with open('input.txt', 'r') as file:
        content = file.read().split('\n')

        antennas = {}
        for i in range(len(content)):
            for j in range(len(content[i])):
                char = content[i][j]
                if char == '.':
                    continue

                if char not in antennas:
                    antennas[char] = []

                antennas[char].append((i,j))

        antennas_antinodes = set()
        for key in antennas:
            antinodes = get_antinodes(content, antennas[key], set())
            antennas_antinodes |= antinodes
        
        print(len(antennas_antinodes))

def get_antinodes(content, antenna_positions, antinodes_positions = set()):
    antennas_length = len(antenna_positions)
    if antennas_length == 0 or antennas_length == 1:
        return antinodes_positions
    
    antinodes_positions = get_antinodes(content, antenna_positions[1:], antinodes_positions)
    primary_x, primary_y = antenna_positions[0]

    for antenna_x, antenna_y in antenna_positions:
        if (antenna_x, antenna_y) == (primary_x, primary_y):
            continue

        direction_x, direction_y = (antenna_x - primary_x, antenna_y - primary_y)

        first_pos = (primary_x - direction_x, primary_y - direction_y)
        second_pos = (antenna_x + direction_x, antenna_y + direction_y)

        if if_position_exists(content, first_pos) != '':
            antinodes_positions.add(first_pos)
        
        if if_position_exists(content, second_pos) != '':
            antinodes_positions.add(second_pos)

    return antinodes_positions

def if_position_exists(content, position):
    i, j = position
    try:
        if i < 0 or j < 0:
            raise

        return content[i][j]
    except:
        return ''

if __name__ == '__main__':
    main()