"""with open("top_10_nba_players.txt", mode="r") as file:
    rankings = file.read()
    print(rankings)"""

# Absolute Path
abs_file_path = "/Users/curlos/Desktop/top_10_nba_players.txt"

with open(abs_file_path, mode="r") as file:
    rankings = file.read()
    print(rankings)

print('----------')

# Relative Path
rel_file_path = "top_10_nba_players.txt"

with open(rel_file_path, mode="r") as file:
    rankings = file.read()
    print(rankings)
