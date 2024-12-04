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
                if not char == 'A':
                    continue;

                diagonal_top_left = get_char(content, (i - 1, j - 1))
                diagonal_top_right = get_char(content, (i - 1, j + 1))
                diagonal_bottom_left = get_char(content, (i + 1, j - 1))
                diagonal_bottom_right = get_char(content, (i + 1, j + 1))

                if not diagonal_top_left or not diagonal_top_right or not diagonal_bottom_left or not diagonal_bottom_right:
                    continue

                if diagonal_top_left == "M" and diagonal_top_right == "M" and diagonal_bottom_left == "S" and diagonal_bottom_right == "S":
                    counter += 1
                elif diagonal_top_left == "M" and diagonal_top_right == "S" and diagonal_bottom_left == "M" and diagonal_bottom_right == "S":
                    counter += 1
                elif diagonal_top_left == "S" and diagonal_top_right == "S" and diagonal_bottom_left == "M" and diagonal_bottom_right == "M":
                    counter += 1
                elif diagonal_top_left == "S" and diagonal_top_right == "M" and diagonal_bottom_left == "S" and diagonal_bottom_right == "M":
                    counter += 1

        print(counter)

def get_char(content, indexes):
    try:
        if indexes[0] < 0 or indexes[1] < 0:
            raise

        return content[indexes[0]][indexes[1]]
    except:
        return False

if __name__ == '__main__':
    main()