PLACEHOLDER = "[name]"

starting_letter_filepath = "./Input/Letters/starting_letter.txt"
names_filepath = "./Input/Names/invited_names.txt"
ready_to_send_filepath = "./Output/ReadyToSend/"

with open(starting_letter_filepath) as starting_letter_file:
    starting_letter = starting_letter_file.read()

    with open(names_filepath) as names_file:
        # For each name replace the starting letter's placeholder '[name]' with each person's name
        all_names = names_file.readlines()
        # O(n) operation because there is only for loop iterating through each name
        for name in all_names:
            new_letter = starting_letter.replace(
                PLACEHOLDER, name.strip()) + '\n'

            # Writes each new letter as a string separated by '\n' to form new lines into a new file
            with open(f'{ready_to_send_filepath}{name.strip().lower()}_letter.txt', mode="w") as invited_name:
                invited_name.write(new_letter)
