📅 Day20 - Add Cumulative Player Stats

# Goal

Make the baseball statistics app update existing players instead of creating duplicate player records.

---

# Completed

- Added At Bats, Hits, Singles, Doubles, Triples, Walks, and Home Runs to the players database
- Added a check to find an existing player by name
- Added cumulative updates for existing players
- Added cumulative calculation for AVG
- Added cumulative calculation for OBP
- Added cumulative calculation for SLG
- Updated the saved AVG, OBP, and SLG after cumulative calculations
- Tested the feature successfully with the same player entered multiple times

---

# What I Learned

Today, I learned how to check whether a player already exists in a SQLite database.
I learned how to use SELECT to find an existing player and UPDATE to add new statistics to the player's previous totals.
I also learned how to retrieve the updated statistics and recalculate AVG, OBP, and SLG using the cumulative data.

---

# Files Updated

- app.py
- players.db

---

# Git Commit

- Add cumulative player stats update
- Update cumulative player stats and recalculate batting metrics

---

# Reflection

Today, I added an important feature to my baseball statistics app.
The app can now recognize an existing player and add new batting data to their previous statistics instead of creating a duplicate player.
AVG, OBP, and SLG are also recalculated using the cumulative statistics.
I successfully tested the feature with the same player multiple times and confirmed that the statistics are updated correctly.

---

# Next Goal

- Improve the Player Stats detail page
- Display detailed cumulative statistics for each player
- Make the Player Stats page more useful and baseball-like