def main():
    with open("input2.txt", "r") as file:
        content = file.read().split()

        print(sum(blink(rock, 75) for rock in content))

Results = {}
def blink(rock, counter):
    if (rock, counter) in Results:
        return Results[(rock, counter)]

    if counter == 0:
        return 1

    if rock == '0':
        res = blink('1', counter - 1)
    elif len(rock) % 2 == 0:
        first_rock = rock[:len(rock) // 2]
        second_rock = str(int(rock[len(rock) // 2:]))
        
        res = blink(first_rock, counter - 1) + blink(second_rock, counter - 1)
    else:
        res = blink(str(int(rock) * 2024), counter - 1)
    
    Results[(rock, counter)] = res
    return res
    

if __name__ == '__main__':
    main()