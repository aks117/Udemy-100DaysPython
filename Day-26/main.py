# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # # Looping through Dictionaries:
# # for (key, value) in student_dict.items():
# #     print(key)
#
# # Loopng through Pandas
# import pandas
#
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
#
# # # Loop through a Data Frame
# # for (key, value) in student_data_frame.items():
# #     print(key)
#
# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     print(row.student)
import pandas
nato_panda = pandas.DataFrame(pandas.read_csv("nato_phonetic_alphabet.csv"))
nato_dict = {row.letter: row.code for (index, row) in nato_panda.iterrows()}

text_input = input("What's your name? ").upper()

for n in text_input:
    print(f"{n} : {nato_dict[n]}")
