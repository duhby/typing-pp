"""Calculate the performance point value of a play."""

import json

with open("star_ratings.json", "r") as file:
    star_ratings = json.load(file)


def get_score(wpm, star):
    return 35 * star * curve_multiplier(wpm)


def curve_multiplier(wpm):
    if wpm < 100:
        return wpm * 0.0045
    elif wpm < 140:
        return (wpm * 0.01) - 0.55
    elif wpm < 214:
        return (wpm * 0.0128378) - 0.947297
    elif wpm >= 214:
        return (wpm * 0.027907) - 4.1721058
    # Old
    # elif wpm < 250.23:
    #     return 0.102232 * (1.01349 ** wpm) # in python, ** is a power
    # else:
    #     return 0.036411 * (1.01768 ** wpm)


if __name__ == "__main__":
    # Example of the current highest play by joshu
    wpm = 241.87
    star = star_ratings.get("1512")  # 1512 is the text id; 8.1722 is the star
    points = get_score(wpm=wpm, star=star)
    print(points)  # 737.31 is the final point value
