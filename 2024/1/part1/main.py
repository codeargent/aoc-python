def main():
    with open("input.txt", "r") as file:
        content = file.read().split()

        left = content[::2]
        right = content[1::2]

        left.sort()
        right.sort()

        total_distance = 0
        for i in range(len(left)):
            total_distance += abs(int(left[i]) - int(right[i]))

        print(total_distance)

if __name__ == "__main__":
    main()