def main():
    with open("input.txt", "r") as file:
        content = file.read().splitlines()
        content_length = len(content)

        counter = 0
        for i in range(content_length):
            line = content[i]
            line_length = len(line)
            splitted_chars = list(line)

            for j in range(line_length):
                char = splitted_chars[j]
                if not char == 'X':
                    continue;

                horizontal_frontwards = check_word(content, (i, j + 1), (i, j + 2), (i, j + 3))
                horizontal_backwards = check_word(content, (i, j - 1), (i, j - 2), (i, j - 3))

                vertical_frontwards = check_word(content, (i + 1, j), (i + 2, j), (i + 3, j))
                vertical_backwards = check_word(content, (i - 1, j), (i - 2, j), (i - 3, j))

                diagonal_bottom_right = check_word(content, (i + 1, j + 1), (i + 2, j + 2), (i + 3, j + 3))
                diagonal_bottom_left = check_word(content, (i + 1, j - 1), (i + 2, j - 2), (i + 3, j - 3))
                diagonal_top_right = check_word(content, (i - 1, j + 1), (i - 2, j + 2), (i - 3, j + 3))
                diagonal_top_left = check_word(content, (i - 1, j - 1), (i - 2, j - 2), (i - 3, j - 3))

                if horizontal_frontwards:
                    counter += 1

                if horizontal_backwards:
                    counter += 1
                
                if vertical_frontwards:
                    counter += 1
                
                if vertical_backwards:
                    counter += 1
                
                if diagonal_bottom_right:
                    counter += 1

                if diagonal_bottom_left:
                    counter += 1

                if diagonal_top_right:
                    counter += 1
                
                if diagonal_top_left:
                    counter += 1

        print(counter)

def check_word(content, m_indexes, a_indexes, s_indexes):
    try:
        if m_indexes[0] < 0 or m_indexes[1] < 0 or a_indexes[0] < 0 or a_indexes[1] < 0 or s_indexes[0] < 0 or s_indexes[1] < 0:
            raise

        valid_m = content[m_indexes[0]][m_indexes[1]] == 'M'
        valid_a = content[a_indexes[0]][a_indexes[1]] == 'A'
        valid_s = content[s_indexes[0]][s_indexes[1]] == 'S'

        return valid_m and valid_a and valid_s
    except:
        return False

if __name__ == '__main__':
    main()