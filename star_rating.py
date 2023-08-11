"""Calculate the star rating of a text."""

import json
import re

with open("combos.json", "r") as file:
    combos = json.load(file)


def get_length(text: str) -> float:
    return 8 - (1.004 ** (550 - len(text)))


def _filter(text: str) -> str:
    """Ignores punctuation and spaces."""
    re.sub(r"\r\n?|\n", " ", text)  # Replace newlines and junk with a space
    text = text.replace("_", "")
    text = text.replace("--", " ")
    text = text.replace("“", '"')
    text = text.replace("”", '"')
    text = text.replace("’", "'")
    text = text.replace('"', "")
    text = text.replace("'", "")
    text = text.replace("(", "")
    text = text.replace(")", "")
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace("/", " ")
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace(";", "")
    text = text.replace(":", "")
    text = text.replace("?", "")
    text = text.replace("!", "")

    return text


def _process(combo: str, prev: str) -> str:
    if re.search(r"[^a-zA-Z ]+", combo):
        return None

    if " " not in combo:
        return combo

    if combo[0:1] == " ":
        return None

    if prev == " ":
        return combo.split(" ")[0]

    return None


def get_obscurity(text: str) -> float:
    text = _filter(text)  # Remove punctuation and special characters
    combo_length = 5  # Change if you use a different combo set (combos.json)

    char_ratings = []
    for i, char in enumerate(text):
        i += 1
        if i >= len(text) - combo_length:
            break

        combo = _process(text[i : i + combo_length], text[i - 1 : i])

        if not combo:
            continue

        new = next((item for item in combos if item["Combo"] == combo), None)

        if not new:
            char_ratings.append(0)
            continue

        a = (
            new["Count"] / 400
        ) ** 0.1  # Change values if you use a different combo set
        char_ratings.append(a)

    # Inverse and map
    obscurity = 25 - (sum(char_ratings) * 14 / len(char_ratings))

    return obscurity


symbol_ratings = [
    (",", 1, True),
    (".", 1, True),  # Ellipsis doesn't get buffed unintentionally
    ("'", 1, True),
    (";", 3, True),
    ("1", 4, False),
    ("2", 4, False),
    ("3", 4, False),
    ("4", 4, False),
    ("5", 4, False),
    ("6", 4, False),
    ("7", 4, False),
    ("8", 4, False),
    ("9", 4, False),
    ("0", 4, False),
    (":", 5, True),
    ("?", 5, True),
    ("!", 5, True),
    ("-", 7, True),
    ("...", 10, True),
    ('"', 20, True),
    ("(", 30, True),
    (")", 30, True),
    ("/", 30, True),
    ("[", 30, True),
    ("]", 30, True),
    ("#", 30, True),
    ("$", 30, True),
    ("%", 30, True),
    ("&", 30, True),
    # Offset capital letter buff
    (" I ", -5, True),
    (" A ", -5, True),
]


def get_density(text: str) -> float:
    score = 0
    # Add points for each capital letter
    freq = len(re.findall(r"[A-Z]", text))
    score += freq * 5

    # Add points for each symbol in the list
    for symbol in symbol_ratings:
        freq = text.count(symbol[0])
        score += freq * symbol[1]

    for i, char in enumerate(text):
        if i == len(text) - 1:
            break

        after = text[i + 1 : i + 2]

        first = next((item for item in symbol_ratings if item[0] == char), None)

        second = next((item for item in symbol_ratings if item[0] == after), None)

        if not first or not second:
            continue

        if first[2] and second[2]:
            if first[0] != second[0]:  # Exclude ellipsis
                score += 10

    # Map
    density = 3.8 * (score / len(text) * 10) ** 0.4

    return density


def get_star(text: str) -> float:
    calc = (
        (0.45 * get_length(text))
        + (0.27 * get_obscurity(text))
        + (0.28 * get_density(text))
    )
    star = calc**1.2
    return star


if __name__ == "__main__":
    # Example of the highest rated text
    # text = "The early \"Dudel-Sack\" gave rise to a number of European, Asian and African folk bagpipes, namely, the Volynka (U.S.S.R.), the Bock (German), the Zukra (North Africa), the Gaita (Portugal and Spain), the Zampogna (Italy), the Cornemuse (France), the Moshug (India), the Zumarah (Egypt), and Flemish, Polish, Greek and Hungarian examples."
    # text = "roll no very give difficult am written stick wire stone join another experience share hurry energy quick receive south rather number past plural point little mountain whole take town south stream loud room answer act year feel with long exercise west body oh does dad science good slave glad is"
    # text = "human beauty count symbol record after group not thank head fill stick use keep around form large slow began divide salt yard proper especially very play took supply inch plain material stand do forward present shout picture him us act one write rope follow ran speed danger tire think clock"
    text = "story cause through speech put liquid while slip safe fact rather like line must add neighbor teeth captain term air class I subtract oil both clean ran shoulder set power real few length believe soft suffix distant bit verb he can gather when post paper bring this some up machine"

    star = get_star(text)
    print(star)  # 14.0480876...
