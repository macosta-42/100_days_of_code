# TO_REPLACE = "[name]"
# names = []
#
# with open("Input/Names/invited_names.txt", "r") as names_file:
#     lines = names_file.readlines()
#     for name in lines:
#         new_name = name.strip()
#         names.append(new_name)
#
# for name in names:
#     with open("Input/Letters/starting_letter.docx", "r") as letter_file:
#         content = letter_file.read()
#         new_content = content.replace(TO_REPLACE, name)
#         with open(f"Output/ReadyToSend/letter_for_{idx}.docx", "w") as new_letter:
#             new_letter.write(new_content)

PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("Input/Letters/starting_letter.docx") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)
