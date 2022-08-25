# Abstract
A performance point system is a way of evaluating and ranking players' skill based on plays they have made on specific maps or quotes by calculating specific plays' worth in points and weighting them. Points are determined by 2 factors, the score (wpm) on the map (text) and the star rating (difficulty) of the map (text). Total points are then calculated for each player by sorting their top 400 or so plays (by points) from highest to lowest, weighing them by making each play worth a smaller percentage of the original points as the position gets farther down, and adding up the weighted values. Someone's total points would be what determines their position like on the current cr leaderboard.

# Star Ratings
Syndric with the help of me (dubs) created the star rating algorithm. It takes a lot of different variables into account to determine a star rating, and with all the current english texts, the highest rated text is currently text 1526 with a star rating of 14.05 (rounded) and the lowest is text 1622 with a star rating of 2.96. The algorithm at a high level takes into consideration 3 main topics which is length (45%), density (28%), and obscurity (27%). Density is the amount of stuff in it like length of words, punctuation, numbers, capital letters, etc, which are all worth their own respective amounts. Obscurity is how obscure combinations of letters are.

# Point Calculations
To calculate points with a given wpm and text (see score.py) you use the following equation where 35 is a constant value that Syndric and I determined so the top score would be around 600-700 points.
```py
35 * star * curve(wpm)
```
The curve function will output a number anywhere from 0 to 7 (if you can get past 300 wpm that is) based on the wpm using the curve below (x axis is wpm, y axis is multiplier).
![WPM Curve](/wpm_curve.png)

# Total Score Calculations
To calculate someone's total points (see total_points.py), you first need to sort them from highest to lowest points. Then you trim the amount of plays you're calculating down to their top 300 (you could also use their top 200-250 considering top players would lose less than 50 total points, but any more than 300 is redundant). You then weigh each play's points using the following equation, where n is the placement of the play, starting at 1 for the highest. You then add up all the weighted values to get their total points.
```py
points * (0.97 ** (n-1))
```

# Accuracy
For calculations, the star ratings should go to at least 4 decimal places. For displaying on the website, they should only go to 2 decimals. For points, they should also only go to 2 decimals for both calculations and displaying on the webiste.

# Naming
Conventionally, in games with similar systems, the points are called pp for performance points. So, for example, you would say that the highest pp play was done by joshu and is worth 649pp. We have thought of a few other options. There's tp (typing points), kp (keymash points), and mp (mash points). However, I think calling them performance points is better because it is more descriptive and alliteration is good.

# Valid texts
English quotes that are **enabled** (keyword) are the only texts that should be "ranked" for having points be calculated for them. This does not include dictionary.

# Data
You can contact Syndric for differently formatted star rating data or for the algorithm if it would be easier in the future to calculate for new texts automatically.
Example calculated data for players' scores and total point leaderboards are in the [data](/data) folder.

# Website Design Changes
To accommodate for adding a performance point system and to make the user experience both more enjoyable and informative, there are a few things I think would be simple to add but effective for the aforementioned reasons.
## Star Ratings
Star ratings of maps should be displayed on
- the countdown/in-game screen next to either the "leave" button or the ping display.
- the end screen after finishing a map, possibly next to contributor
- the text leaderboard info bar, possibly under contributor
- possibly on the matches (and top scores) tab for each text
- possibly on replay pages where general information is displayed
## Point displays
Performance points for a given play should be displayed on
- its own column on text leaderboards (end screen, and leaderboard pages)
- its own column on the matches page
- its own column on the top scores page (with the weighted value in brackets next to it ex. 320tp [280])
- possibly on the end screen of a text below wpm or somewhere similar
- on replay pages where general information is displayed
## Profile changes
- next to "general, matches, achievements, tournaments" possibly between general and matches, there should be a "top scores" tab or something similar, that is like the matches tab, except the placement on the left is your placement for the text leaderboard itself (side note, it would be nice if the card itself linked to the text leaderboard for both the matches and top scores tabs)
- a new rectangle in the general tab that displays information like highest point play, total points, and rank
(another side note, it would be nice if all text leaderboards had a link to the replay if one is available)

# Extras
There should be systems to be able to easily do the following:
- Update the star rating of one or multiple texts and update everyone (that has a score on the changed text(s))'s performance points, personal pp leaderboards, and the main pp leaderboard
