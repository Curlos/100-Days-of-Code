# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

starting_letter_filepath = "./Input/Letters/starting_letter.txt"
names_filepath = "./Input/Names/invited_names.txt"
ready_to_send_filepath = "./Output/ReadyToSend/"

with open(names_filepath) as file:
    names = file.read()
    print(names)

with open(starting_letter_filepath) as starting_letter_file:
    starting_letter_lines = starting_letter_file.readlines()
    first_line = starting_letter_lines[0].strip()

    with open(names_filepath) as names_file:
        all_names = names_file.readlines()
        print(all_names)
        for name in all_names:
            new_line = first_line.replace('[name]', name.strip()) + '\n'

            with open(f'{ready_to_send_filepath}{name.strip().lower()}_letter.txt', mode="w") as invited_name:
                invited_name.write(new_line)

                for line in starting_letter_lines[1:]:
                    invited_name.write(line)