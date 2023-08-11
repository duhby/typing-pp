"""Calculate a player's total points."""

# List of their top plays in order (real values will be to 2 decimal places)
example_points = [200 for _ in range(50)]

weighted_points = []

# n is the placement, points is the current item in the list
for n, points in enumerate(example_points):
    n += 1  # placement should start at 1; enumerate starts at 0
    weighted = points * 0.97 ** (n - 1)
    weighted_points.append(weighted)

# Adds weighted points together
total_points = sum(weighted_points)

print(round(total_points, 2))  # >>> 5212.9

# As opposed to

print(sum(example_points))  # >>> 10_000
