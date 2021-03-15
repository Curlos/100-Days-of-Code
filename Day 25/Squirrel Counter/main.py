import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colors = data["Primary Fur Color"].value_counts()
fur_colors_dict = fur_colors.to_dict()
fur_colors_colors = fur_colors.to_dict().keys()
fur_colors_counts = fur_colors.to_dict().values()

data_dict = {
    "Fur Color": fur_colors_colors,
    "Count": fur_colors_counts
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
