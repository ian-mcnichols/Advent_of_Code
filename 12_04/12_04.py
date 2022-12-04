def get_input():
    elf_file = open("elf_input.txt", "r")
    elf_input = [x.strip() for x in elf_file.readlines()]
    elf_file.close()
    return elf_input


def challenge():
    lines = get_input()
    overlaps = 0
    for line in lines:
        overlap1 = True
        overlap2 = True
        elf1 = line.split(",")[0]
        elf2 = line.split(",")[1]
        elf1_tasks = list(range(int(elf1.split("-")[0]), int(elf1.split("-")[1])+1))
        elf2_tasks = list(range(int(elf2.split("-")[0]), int(elf2.split("-")[1])+1))
        for task in elf1_tasks:
            if task not in elf2_tasks:
                overlap1 = False
        for task in elf2_tasks:
            if task not in elf1_tasks:
                overlap2 = False
        if overlap1 or overlap2:
            overlaps += 1
    print("overlaps:", overlaps)

    return

def challenge2():
    lines = get_input()
    overlaps = 0
    for line in lines:
        overlap1 = False
        overlap2 = False
        elf1 = line.split(",")[0]
        elf2 = line.split(",")[1]
        elf1_tasks = list(range(int(elf1.split("-")[0]), int(elf1.split("-")[1])+1))
        elf2_tasks = list(range(int(elf2.split("-")[0]), int(elf2.split("-")[1])+1))
        for task in elf1_tasks:
            if task in elf2_tasks:
                overlap1 = True
        for task in elf2_tasks:
            if task in elf1_tasks:
                overlap2 = True
        if overlap1 or overlap2:
            overlaps += 1
    print("overlaps:", overlaps)

    return


challenge2()
