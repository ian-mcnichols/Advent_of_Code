alph = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52
}

def elf_sack():
    count = 0
    input_file = open("elf_input.txt", "r")
    same_items = []
    group = []
    i = 1
    for line in input_file.readlines():
        elf = line.strip()
        group.append(elf)
        if i % 3 == 0:
            print("group:", group)
            for item in group[0]:
                for itemb in group[1]:
                    for itemc in group[2]:
                        if item == itemb and itemb == itemc:
                            same_item = item
            print("same item:", same_item)
            same_items.append(same_item)
            group = []
        i += 1
    input_file.close()
    print(len(same_items))
    for thing in same_items:
        count += alph[thing]
    print('count:', count)


elf_sack()
