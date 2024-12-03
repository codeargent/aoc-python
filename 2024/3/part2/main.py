import re

def main():
    with open("input.txt", "r") as file:
        content = file.read()
        
        pattern = r"(?P<dont>don't\(\))|(?P<do>do\(\))|(?P<mul>mul\((?P<first_digit>\d+),(?P<second_digit>\d+)\))"

        mul_sum = 0
        increment = True
        for match in re.finditer(pattern, content):
            if match.group('dont'):
                increment = False
            elif match.group('do'):
                increment = True
            elif match.group('mul') and increment:
                mul_sum += int(match.group('first_digit')) * int(match.group('second_digit'))
        
        print(mul_sum)

if __name__ == "__main__":
    main()
