"""import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []

    for row in data:
        temp = row[1]
        if temp != 'temp':
            temperatures.append(temp)

    print(temperatures)
"""
import pandas

data = pandas.read_csv("weather_data.csv")
"""
# print(type(data))
# print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
temp_average = sum(temp_list) / len(temp_list)
print(temp_average)

pandas_temp_average = data["temp"].mean()
print(pandas_temp_average)

pandas_temp_max = data["temp"].max()
print(pandas_temp_max)

# Get Data in Columns
print(data["condition"])
print(data.condition)"""

# Get Data in Row
"""pandas_temp_max = data["temp"].max()
data_dict = data.to_dict()
print(data[data.temp == pandas_temp_max])"""

"""monday = data[data.day == "Monday"]
monday_celsius = int(monday.temp)
monday_farenheit = (monday_celsius * 9/5) + 32
print(monday_farenheit)
"""

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data.to_csv("new_data.csv"))
