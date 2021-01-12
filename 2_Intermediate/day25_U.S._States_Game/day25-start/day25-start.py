# data = []
#
# with open("./weather_data.csv", "r") as weather_data:
#     raw_data = weather_data.readlines()
#     for lines in raw_data:
#         data.append(lines.strip())
#
# print(data)

# with open("./weather_data.csv", "r") as weather_data:
#     data = weather_data.read().splitlines()
#
# print(data)

#
# import csv
#
#
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     temperatures = []
#     for row in data:
#         temp.append(row[1])
#     for _ in temp[1:]:
#         temperatures.append(int(_))
# print(temperatures)


# import csv
#
#
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# import pandas
#
# data = pandas.read_csv("./weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(sum(temp_list)/len(temp_list))
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get data in Columns
# print(data["temp"])
# print(data.temp)

# # Get data in Rows
# print(data[data.day == "Monday"])
# print(data[data.temp == 12])
# print(data[data.condition == "Sunny"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrels.csv")
print(df)
