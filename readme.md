# Abstract
A performance point system is a way of evaluating and ranking players' skill based on plays they have made on specific maps or quotes by calculating specific plays' worth in points and weighting them. Points are determined by 2 factors, the score (wpm) on the map (text) and the star rating (difficulty) of the map (text). Total points are then calculated for each player by sorting their top 400 or so plays (by points) from highest to lowest, weighing them by making each play worth a smaller percentage of the original points as the position gets farther down, and adding up the weighted values. Someone's total points would be what determines their position like on the current cr leaderboard.

# Star Ratings
Syndric with the help of me (dubs) created the star rating algorithm. It takes a lot of different variables into account to determine a star rating, and with all the current english texts, the highest rated text is currently text 1526 with a star rating of 13.01 (rounded) and the lowest is text 115 with a star rating of 1.06, although there are only 13 texts with a star rating of less than 3. The algorithm at a high level takes into consideration 3 main topics which is length (52%), density (28%), and obscurity (20%). Density is the amount of stuff in it like length of words, punctuation, numbers, capital letters, etc, which are all worth their own respective amounts. Obscurity is how obscure the combination of letters are.

# Point Calculations
To calculate points with a given wpm and text (see score.py) you use the following equation where 33 is a constant value that Syndric and I determined so the top score would be around 600-700 points.
```py
33 * star * curve(wpm)
```
The curve function will output a number anywhere from 0 to 6 (if you can get past 300 wpm that is) based on the wpm using the curve below (x axis is wpm, y axis is multiplier).
![Multiplier Curve](/curve.png)

# Total Score Calculations
To calculate someone's total points (see total_points.py), you first need to sort them from highest to lowest points. Then you trim the amount of plays you're calculating down to their top 300 (you could also use their top 200-250 considering top players would lose less than 50 total points, but any more than 300 is redundant). You then weigh each play's points using the following equation, where n is the placement of the play, starting at 1 for the highest. You then add up all the weighted values to get their total points.
```py
points * (0.97 ** (n-1))
```

# Naming
Conventionally, in games with similar systems, the points are called pp for performance points. So, for example, you would say that the highest pp play was done by joshu and is worth 667pp. However, Aevistar doesn't think it's a good idea to use this naming system, so we have thought of a few other options. There's tp (typing points), kp (keymash points), and mp (mash points), although a few vocal users in #general like tp the best because it looks like toilet paper.

# Data
You can contact Syndric for the most recent star rating data or for the algorithm if it would be easier in the future to calculate for new texts.
