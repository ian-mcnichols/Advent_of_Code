combos_a = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,

    "B X": 1,
    "B Y": 5,
    "B Z": 9,

    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

combos_b = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,

    "B X": 1,
    "B Y": 5,
    "B Z": 9,

    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}


def cheat_elf(part=1):
    study_guide = open("elf_input.txt", "r")
    if part == 1:
        combos = combos_a
    elif part == 2:
        combos = combos_b
    else:
        print("it's a 2 part challenge. pick one.")
    total_points = 0
    for line in study_guide.readlines():
        points = combos[line.strip()]
        total_points += points
    study_guide.close()
    print("Your score:", total_points)


cheat_elf(1)
