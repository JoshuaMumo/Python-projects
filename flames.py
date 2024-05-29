#simple FLAMES game
def remove_common_chars(name1, name2):
    common_chars = set(name1) & set(name2)
    common_count = {char: min(name1.count(char), name2.count(char)) for char in common_chars}
    for char, count in common_count.items():
        name1 = name1.replace(char, '', count)
        name2 = name2.replace(char, '', count)
    return name1, name2
def get_remaining_count(name1, name2):
    name1, name2 = remove_common_chars(name1, name2)
    remaining_chars = name1 + name2
    return len(remaining_chars)
def get_flames_result(remaining_count):
    flames = ["F", "L", "A", "M", "E", "S"]
    while len(flames) > 1:
        remove_index = (remaining_count - 1) % len(flames)
        flames.pop(remove_index)
    return flames[0]
def main():
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")
    remaining_count = get_remaining_count(name1, name2)
    result = get_flames_result(remaining_count)
    print("Relationship result:", result)
if __name__ == "__main__":
    main()