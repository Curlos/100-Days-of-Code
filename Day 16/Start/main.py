from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Eevee", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Normal", "Water", "Fire"])
table.align = "l"
print(table)