def get_fat_elf():
    elf_file = open("../../elf_input.txt", "r")
    highest_elf_cals = 0
    cal_count = 0
    for line in elf_file.readlines():
        if line != "\n":
            cal_count += int(line)
        else:
            if cal_count > highest_elf_cals:
                highest_elf_cals = cal_count
            cal_count = 0
    elf_file.close()
    print("Highest calorie count:", highest_elf_cals)


get_fat_elf()
