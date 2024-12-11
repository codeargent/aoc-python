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

        groups = []
        temp_group = []
        for index, item in enumerate(filesystem):
            if not len(temp_group):
                if item != -1:
                    temp_group.append(item)
                continue

            if item != temp_group[0]:
                groups.append((index - len(temp_group), temp_group))
                if item != -1:
                    temp_group = [item]
                else:
                    temp_group = []
            else:
                temp_group.append(item)
            
            if index == len(filesystem) - 1:
                groups.append((index - len(temp_group) + 1, temp_group))
        
        groups.reverse()

        for group_index, group in groups:
            group_length = len(group)
            first_free_space_index = None
            for index, item in enumerate(filesystem):
                if index > group_index:
                    break

                if item == -1 and first_free_space_index == None:
                    first_free_space_index = index
                
                if first_free_space_index != None:
                    length = index - first_free_space_index
                    if length == group_length:
                        for i in range(first_free_space_index, index):
                            filesystem[i] = group[0]

                        for i in range(len(group)):
                            filesystem[group_index + i] = -1
                        
                        break

                if item != -1:
                    first_free_space_index = None
        
        checksum = 0
        for index, item in enumerate(filesystem):
            if item != -1:
                checksum += index * filesystem[index]
        
        print(checksum)


if __name__ == '__main__':
    main()