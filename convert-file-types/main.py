import json
show_data = []

with open("television_shows.txt", "r") as file:
    for line in file:
        show_data.append(line)

with open("best_shows.json", "w") as file:
    json.dump( show_data, file)