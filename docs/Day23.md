📅 Day23 - Create and Improve the Player Leaderboard

# Goal

Create a Player Leaderboard that ranks players by OPS and displays their batting statistics clearly.

---

# Completed

- Added a Player Leaderboard page
- Added a `/leaderboard` route in Flask
- Retrieved player statistics from the SQLite database
- Sorted players by OPS in descending order
- Added AVG, OBP, SLG, and OPS to the leaderboard
- Added ranking numbers and medals for the top 3 players
- Added a View Leaderboard button to the main page
- Added a Back to Home button to the leaderboard page
- Improved the leaderboard layout and adjusted the width
- Tested the leaderboard successfully
- Pushed the completed changes to Git

---

# What I Learned

Today, I learned how to create a separate leaderboard page using Flask and SQLite.
I learned how to use SQL `ORDER BY` to sort player statistics and `CAST` to compare numeric values stored as text.
I also learned how to use Jinja2 `loop.index` to display ranking numbers automatically.
In addition, I learned how CSS `width` and `max-width` can be used to control the size of a page and create a more balanced layout.

---

# Files Updated

- app.py
- templates/index.html
- templates/leaderboard.html

---

# Git Commit

- Improve leaderboard layout

---

# Reflection

Today, I created a Player Leaderboard for the Baseball Stats Analyzer.
Players are now ranked by OPS, and their AVG, OBP, SLG, and OPS can be compared on one page.
I also added navigation buttons between the main page and the leaderboard.
By adjusting the width and layout, I was able to make the leaderboard easier to view and more balanced.
The application now feels more like a real baseball statistics website.

---

# Next Goal

- Improve the Player Leaderboard

- Add more useful ways to compare player statistics

- Improve the overall UI and user experience