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
                    antennas[char] = set()

                antennas[char].add((i,j))

        antennas_antinodes = set()
        for key in antennas:
            # add antennas positions as antinodes
            antennas_antinodes |= antennas[key]

            antinodes = get_antinodes(content, list(antennas[key]), set())
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

        first_pos_x, first_pos_y = (primary_x - direction_x, primary_y - direction_y)
        first_pos_value = get_content_position(content, (first_pos_x, first_pos_y))
        while first_pos_value != '':
            antinodes_positions.add((first_pos_x, first_pos_y))
            first_pos_x, first_pos_y = (first_pos_x - direction_x, first_pos_y - direction_y)
            first_pos_value = get_content_position(content, (first_pos_x, first_pos_y))
        
        second_pos_x, second_pos_y = (antenna_x + direction_x, antenna_y + direction_y)
        second_pos_value = get_content_position(content, (second_pos_x, second_pos_y))
        while second_pos_value != '':
            antinodes_positions.add((second_pos_x, second_pos_y))
            second_pos_x, second_pos_y = (second_pos_x + direction_x, second_pos_y + direction_y)
            second_pos_value = get_content_position(content, (second_pos_x, second_pos_y))

    return antinodes_positions

def get_content_position(content, position):
    i, j = position
    try:
        if i < 0 or j < 0:
            raise

        return content[i][j]
    except:
        return ''

if __name__ == '__main__':
    main()