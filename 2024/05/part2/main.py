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
            new_pages_list = pages_list.copy()
            valid = is_valid(new_pages_list, rules)
            was_invalid = False
            while not valid:
                was_invalid = True
                new_pages_list = fix_pages_list(new_pages_list, rules)
                valid = is_valid(new_pages_list, rules)

            if was_invalid:
                sum += new_pages_list[len(new_pages_list) // 2]
        
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

def fix_pages_list(pages_list, rules):
    for i in range(len(pages_list) - 1):
        before = pages_list[i]
        after = pages_list[i + 1]

        if (after, before) in rules:
            pages_list[i] = after
            pages_list[i + 1] = before

    return pages_list
        

if __name__ == '__main__':
    main()