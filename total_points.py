"""Calculate a player's total points."""

# List of their top plays in order (real values will be to 2 decimal places)
example_points = [210, 200, 190, 180, 170, 160, 155, 140, 122, 120, 110, 109, 108, 107, 106, 103, 102, 102, 101, 100, 99]

weighted_points = []

# n is the placement, points is the current item in the list
for n, points in enumerate(example_points):
    n += 1 # placement should start at 1; enumerate starts at 0
    weighted = points * .97**(n-1)
    weighted_points.append(weighted)

# Adds weighted points together
total_points = sum(weighted_points)

print(round(total_points, 2)) # >>> 2196.18 (rounded)

# As opposed to

print(sum(example_points)) # >>> 2794
