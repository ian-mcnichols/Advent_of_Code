import numpy as np

stacks = [['W', 'P', 'G', 'Z', 'V', 'S', 'B'],
          ['F', 'Z', 'C', 'B', 'V', 'J'],
          ['C', 'D', 'Z', 'N', 'H', 'M', "L", 'V'],
          ['B', 'J', 'F', 'P', 'Z', 'm', 'd', 'l'],
          ['h', 'q', 'b', 'j', 'g', 'c', 'f', 'v'],
          ['b', 'l', 's', 't', 'q', 'f', 'g'],
          ['v', 'z', 'c', 'g', 'l'],
          ['g', 'l', 'n'],
          ['c', 'h', 'f', 'j']]

def get_input():
    elf_file = open("elf_input.txt", "r")
    elf_input = [x.strip() for x in elf_file.readlines()]
    elf_file.close()
    return elf_input


def challenge():
    new_stacks = [stack[::-1] for stack in stacks]
    lines = get_input()
    for line in lines:
        amount = int(line.split(" ")[1])
        start = int(line.split(" ")[3]) - 1
        end = int(line.split(" ")[-1]) - 1
        print("stacks:")
        for stack in new_stacks:
            print(stack)
        print("Moving {} from {} to {}".format(amount, start, end))
        for i in range(amount):
            crate = new_stacks[start].pop(-1)
            new_stacks[end].append(crate)
        print("stacks:")
        for stack in new_stacks:
            print(stack)
        print("==================================")
    output = ""
    for stack in new_stacks:
        output += stack[-1].upper()
    print(output)

def challenge2():
    new_stacks = [stack[::-1] for stack in stacks]
    lines = get_input()
    for line in lines:
        amount = int(line.split(" ")[1])
        start = int(line.split(" ")[3]) - 1
        end = int(line.split(" ")[-1]) - 1
        print("stacks:")
        for stack in new_stacks:
            print(stack)
        print("Moving {} from {} to {}".format(amount, start, end))
        crates = []
        for i in range(amount):
            crates.append(new_stacks[start].pop(-1))
        crates = crates[::-1]
        for crate in crates:
            new_stacks[end].append(crate)
        print("stacks:")
        for stack in new_stacks:
            print(stack)
        print("==================================")
    output = ""
    for stack in new_stacks:
        output += stack[-1].upper()
    print(output)


challenge2()
