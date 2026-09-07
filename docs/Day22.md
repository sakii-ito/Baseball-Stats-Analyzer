📅 Day21 - Add OPS to Player Statistics

# Goal

Add OPS to the baseball statistics application and calculate it using cumulative OBP and SLG.

---

# Completed

- Added an OPS column to the SQLite players table
- Added OPS calculation using cumulative OBP and SLG
- Added OPS display to the Player Stats detail page
- Added OPS display to Player History
- Fixed the SQLite table migration for the new OPS column
- Tested OPS calculation and display successfully
- Pushed the completed changes to Git

---

# What I Learned

Today, I learned that `CREATE TABLE IF NOT EXISTS` does not add new columns to an existing SQLite table.
I learned how to use `ALTER TABLE ... ADD COLUMN` to add a new column to an existing database table without deleting the existing data.
I also learned that the number of values in an SQL `INSERT` statement must match the number of placeholders.

---

# Files Updated

- app.py
- index.html
- player.html

---

# Git Commit

- Add OPS stats

---

# Reflection

Today, I added OPS to the Baseball Stats Analyzer.
OPS is calculated by adding OBP and SLG, and the application now recalculates OPS using the player's cumulative statistics.
I also displayed OPS on both the Player Stats detail page and Player History.
The application now provides AVG, OBP, SLG, and OPS, making the player statistics more complete.

---

# Next Goal

- Create a Player Leaderboard
- Rank players by OPS
- Display player rankings
- Add sorting for player statistics