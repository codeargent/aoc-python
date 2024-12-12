def main():
    with open("input.txt", "r") as file:
        content = file.read().split()

        for _ in range(25):
            content = blink(content)
        
        print(len(content))
    
def blink(content):
    final = []

    for rock in content:
        rock_length = len(rock)
        if rock_length % 2 == 0:
            first_rock = rock[:rock_length // 2]
            second_rock = str(int(rock[rock_length // 2:]))
            
            final.extend([first_rock, second_rock])
        elif rock == '0':
            final.append('1')
        else:
            final.append(str(int(rock) * 2024))
    
    return final 

if __name__ == '__main__':
    main()