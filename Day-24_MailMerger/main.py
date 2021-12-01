# TODO: Create a letter using starting_letter.txt

with open("./Input/Names/invited_names.txt") as names_file:
    for name in names_file:
        # print(name[:-1])
        name = name.strip("\n")
        text = ""
        with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode="w") as letter:
            letter.write(text)
        with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode="a") as letter:
            with open("./Input/Letters/starting_letter.txt") as sample_letter:
                for line in sample_letter:
                    line = line.replace("[name],", f"{name},", 1)
                    letter.write(line)
