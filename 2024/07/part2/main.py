def main():
    with open("input.txt", "r") as file:
        content = file.read().split('\n')

        sum = 0
        for line in content:
            result, numbers = line.split(':')
            result = int(result)
            numbers = list(map(int, numbers.split()))
            numbers.reverse()

            possible_results = join_numbers(numbers)
            if result in possible_results:
                sum += result

        print(sum)

def join_numbers(numbers, results = []):
    if len(numbers) == 0:
        return results
    
    number = numbers[0]
    if len(numbers) == 1:
        return [number]

    results = join_numbers(numbers[1:], results)

    new_results = []
    for result in results:
        new_results.append(result + number)
        new_results.append(result * number)
        new_results.append(int(str(result) + str(number)))

    return new_results

if __name__ == '__main__':
    main()