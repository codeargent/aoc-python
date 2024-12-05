def main():
    with open("input.txt", "r") as file:
        content = file.read().split('\n')
        result = 0
        for line in content:
            result += is_safe_with_dampener(line)
        
        print(result)

def is_safe(values):
    prev_value = values[0]
    order = None
    for i in range(1, len(values)):
        value = values[i]

        if value > prev_value and value - 3 <= prev_value and (order == 'asc' or order is None):
            prev_value = value
            order = 'asc'
        elif value < prev_value and value + 3 >= prev_value and (order == 'desc' or order is None):
            prev_value = value
            order = 'desc'
        else:
            return 0

    return 1

def is_safe_with_dampener(line):
    if line == '':
        return 0

    values = list(map(int, line.split()))
    
    if is_safe(values):
        return 1

    for i in range(len(values)):
        modified_values = values[:i] + values[i+1:]
        if is_safe(modified_values):
            return 1

    return 0

if __name__ == "__main__":
    main()