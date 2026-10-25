"""
1.
Create a Python script called playlist_stats.py that takes a list of daily
 Spotify song play counts (e.g., [120, 135, 150, 200, 120, 90, 200]) and
  calculates the mean (average) number of plays."""


plays = [120, 135, 150, 200, 120, 90, 200]

mean_plays = sum(plays) / len(plays)

print("Mean number of daily plays:", mean_plays)
