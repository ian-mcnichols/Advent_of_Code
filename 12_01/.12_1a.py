def get_fat_elf():
    elf_file = open("../../elf_input.txt", "r")
    calorie_counts = []
    cal_count = 0
    for line in elf_file.readlines():
        if line != "\n":
            cal_count += int(line)
        else:
            calorie_counts.append(cal_count)
            cal_count = 0
    elf_file.close()
    calorie_counts.sort()
    calorie_counts = calorie_counts[::-1]
    print("Highest calorie count:", calorie_counts[0])
    print("Second calorie count:", calorie_counts[1])
    print("Third calorie count:", calorie_counts[2])
    print("Sum of 3:", sum(calorie_counts[0:3]))


get_fat_elf()
