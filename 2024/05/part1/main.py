def main():
    with open('input.txt', 'r') as file:
        content = file.read().split('\n\n')

        rules = []
        pages_lists = []
        for item in content[0].split('\n'):
            temp_rules = item.split('|')
            rules.append((int(temp_rules[0]), int(temp_rules[1])))
        
        for item in content[1].split('\n'):
            pages_lists.append(list(map(int, item.split(','))))

        sum = 0
        for pages_list in pages_lists:
            if is_valid(pages_list, rules):
                sum += pages_list[len(pages_list) // 2]
        
        print(sum)

def is_valid(pages_list, rules):
    pages_with_indexes = {}
    for i in range(len(pages_list)):
        pages_with_indexes[pages_list[i]] = i

    for before, after in rules:
        if before in pages_with_indexes and after in pages_with_indexes:
            if pages_with_indexes[before] > pages_with_indexes[after]:
                return False

    return True

if __name__ == '__main__':
    main()