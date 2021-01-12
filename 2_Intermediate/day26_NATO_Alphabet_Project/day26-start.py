# new_list = [new_item for item in list if test]

# number = [1, 2, 3]
# new_number = [n + 1 for n in number]
# print(new_number)
#
# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)
#
# new_list = [n * 2 for n in range(1, 5)]
# print(new_list)
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
#
# upper_names = [name.upper() for name in names if len(name) >= 5]
# print(upper_names)

# new_dict ={new_key:new_value for (key, value) in dict.items() if test}

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score >= 50}
print(passed_students)

