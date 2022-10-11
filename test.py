import json

with open('star_ratings.json', 'r') as file:
    star_ratings = json.load(file)


print(star_ratings['1622'])