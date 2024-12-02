import functools


def main():
    with open("input.txt", "r") as file:
        content = file.read().split('\n')
        result = 0
        for line in content:
            result += is_safe(line)
        
        print(result)

def is_safe(line):
    if line == '':
        return 0
    
    values = line.split()

    prev_value = int(values[0])
    order = None
    for i in range(1, len(values)):
        value = int(values[i])

        if value > prev_value and value - 3 <= prev_value and (order == 'asc' or order == None):
            prev_value = value
            order = 'asc'
        elif value < prev_value and value + 3 >= prev_value and (order == 'desc' or order == None):
            prev_value = value
            order = 'desc'
        else:
            return 0
    
    return 1

if __name__ == "__main__":
    main()