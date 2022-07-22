# How to calculate a score for a given play on a text given the words per minute and the star rating of that text

import json

with open('star_ratings.json', 'r') as file:
    star_ratings = json.load(file)


def get_score(wpm, star):
    return 33 * star * curve_multiplier(wpm)


def curve_multiplier(wpm):
    if wpm < 100:
        return wpm * 0.0045
    elif wpm < 140:
        return (wpm * 0.01) - 0.55
    elif wpm < 214:
        return (wpm * 0.0128378) - 0.947297
    else:
        return 0.102232 * (1.01349 ** wpm) # in python, ** is a power


if __name__ == '__main__':
    # Example of the current highest play by joshu
    wpm = 241.90
    star = star_ratings.get('2390') # 2390 is the text id; 7.74325 is the star
    points = get_score(wpm=wpm, star=star)
    print(points) # 667.9644757749904 is the final point value
