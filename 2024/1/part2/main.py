def main():
    with open("input.txt", "r") as file:
        content = file.read().split()

        left = content[::2]
        right = content[1::2]

        total_similarity = 0
        for i in range(len(left)):
            total_similarity += int(left[i]) * right.count(left[i])
        
        print(total_similarity)

if __name__ == "__main__":
    main()