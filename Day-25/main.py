# # Open File and read lines into a list
# with open("weather_data.csv") as weather_file:
#     weather_list = (weather_file.readlines())
# print(weather_list)


# # Extracting a column of data from csv using csv class
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)


# Using Pandas library
# import pandas
# data = pandas.read_csv("weather_data.csv")

# # print(type(data))
# # print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# #
# # average = sum(temp_list) / len(temp_list)
# # print(average)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
#
# # Get Data in columns
# print(data["condition"])
# print(data.condition)


# # Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = (monday_temp * 9/5) + 32

# # Create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("save_dict_data.csv")
import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_count_dict = {
    "Fur Color": ["grey", "cinnamon", "black"],
    "Count": [0, 0, 0]
}

# unique_color_list = squirrel_data["Primary Fur Color"].unique()

for squirrel_color in squirrel_data["Primary Fur Color"]:
    if squirrel_color == "Gray":
        squirrel_count_dict["Count"][0] += 1
    if squirrel_color == "Cinnamon":
        squirrel_count_dict["Count"][1] += 1
    if squirrel_color == "Black":
        squirrel_count_dict["Count"][2] += 1

print(squirrel_count_dict)
squirrel_count_data = pandas.DataFrame(squirrel_count_dict)
squirrel_count_data.to_csv("squirrel_count.csv")
