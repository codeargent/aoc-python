def main():
    with open("input.txt", "r") as file:
        content = file.read()

        filesystem = []
        for index, size in enumerate(content):
            size = int(size)
            if index % 2 == 0:
                filesystem.extend([index // 2] * size)
            else:
                filesystem.extend([-1] * size)

        fs_copy = filesystem.copy()
        last_index = len(filesystem)

        checksum = 0
        for i in range(len(filesystem)):
            if filesystem[i] == -1:
                last_item = None

                while len(fs_copy) > i:
                    last_index -= 1
                    popped_item = fs_copy.pop()
                    if popped_item != -1:
                        last_item = popped_item
                        break

                if last_item == None:
                    break
                
                filesystem[last_index] = -1
                filesystem[i] = last_item
            
            checksum += i * filesystem[i]
        
        print(checksum)

if __name__ == '__main__':
    main()