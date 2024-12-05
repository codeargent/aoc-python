import re

def main():
    with open("input.txt", "r") as file:
        content = file.read()

        mul_sum = 0
        for match in re.finditer(r"mul\((\d*),(\d*)\)", content):
            mul_sum += int(match.group(1)) * int(match.group(2))
        
        print(mul_sum)

if __name__ == "__main__":
    main()