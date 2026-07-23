📅 Day11 - Fix SLG Calculation and Display Player History

## Goal
Fix the SLG calculation and display player history using data stored in the SQLite database.

---

## Completed
- Added Singles, Doubles, and Triples inputs
- Fixed the SLG calculation using Total Bases
- Saved player data to the SQLite database
- Loaded player history from the SQLite database
- Displayed player history on the web page
- Fixed SQLite and Jinja2 syntax errors
- Successfully tested the updated application

---

## What I Learned
Today, I learned how to calculate SLG correctly using Singles, Doubles, Triples, and Home Runs.

I learned that SLG is calculated using Total Bases divided by At Bats, rather than simply dividing Home Runs by At Bats.

I also learned how to save player data to an SQLite database and retrieve the stored data using an SQL SELECT query.

When displaying the data in the HTML template, I learned that data retrieved from SQLite using fetchall() is returned as tuples, so I can access each value using indexes such as p[0], p[1], p[2], and p[3].

During testing, I also found and fixed small syntax errors in the SQL query and Jinja2 template.

---

## Files Updated
- app.py
- templates/index.html
- players.db

---

## Git Commit
Fix SLG calculation and display player history from SQLite

---

## Reflection
Today, I successfully fixed the SLG calculation and connected the Player History feature to the SQLite database.
I also learned how important testing and debugging are when developing a web application.
By fixing errors step by step, I better understood how Flask, SQLite, SQL queries, and Jinja2 work together.
My baseball statistics app is becoming more like a real application with persistent player data.

---

## Next Goal
- Add validation to check whether Hits matches the total number of Singles, Doubles, Triples, and Home Runs
- Improve input validation and error handling
- Improve the Player History UI
- Continue improving the SQLite database functionality