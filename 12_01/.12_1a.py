def get_fat_elf():
    elf_file = open("elf_input.txt", "r")
    elf_cals_prev = 0
    elf_cals_curr = 0
    while True:
        new_line = elf_file.readline()
        if not new_line:
            break
        while new_line != "\n":
            elf_cals_curr += int(new_line)
        if elf_cals_curr >= elf_cals_prev:
            elf_cals_prev = elf_cals_curr
    elf_file.close()
    print("Highest calorie count:", elf_cals_curr)


get_fat_elf()
