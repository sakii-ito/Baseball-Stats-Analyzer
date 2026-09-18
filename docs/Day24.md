📅 Day24 - Add Sorting to the Player Leaderboard

# Goal

Add sorting buttons to the Player Leaderboard so that player statistics can be ranked by AVG, OBP, SLG, or OPS.

---

# Completed

- Added sorting options for AVG, OBP, SLG, and OPS
- Added sorting buttons to the Player Leaderboard
- Connected each button to the Flask `/leaderboard` route
- Used URL parameters to select the sorting statistic
- Highlighted the currently selected sorting option
- Kept the existing leaderboard design and layout
- Tested all four sorting options successfully
- Committed the changes to Git

---

# What I Learned

Today, I learned how to let users change the sorting order of data through buttons on a web page.
I used URL parameters such as `sort=average` and `sort=ops` to tell Flask which statistic should be used for sorting.
I also learned how Flask can receive URL parameters with `request.args.get()` and use them to change the SQL query.
On the HTML side, I used Jinja2 to change the button style depending on the currently selected sorting option.

---

# Files Updated

- app.py
- templates/leaderboard.html

---

# Git Commit

- Add leaderboard sorting

---

# Reflection

Today, I improved the Player Leaderboard by adding sorting functionality.
Users can now compare players based on different batting statistics instead of only viewing the OPS ranking.
The leaderboard is becoming more interactive and useful as a baseball statistics website.
I also learned how Flask, SQL, URL parameters, and Jinja2 can work together to create an interactive feature.

---

# Next Goal

- Improve the Player Leaderboard
- Add more useful player comparison features
- Continue improving the UI and user experience