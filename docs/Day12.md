📅 Day12 - Add input Validation

## Goal
Add input validation to prevent incorrect player data from being caluculated and saved.

---

## Completed
- Added validation for Hits and hit details
- Checked that Hits matches Singles + Doubles + Triples + Home Runs
- Checked that Hits is not greater than At Bats
- Prevented invalid data from being saved to SQLite
- Tested both valid and invalid inputs successfully

---

## What I Learned
Today, I learned how to validate user input before processing and saving data.
I learned how to use conditions to check wheter multiple input values are consistent.
I also learned that invalid data should not be saved to the database.
During testing, I found that data with errors was still being saved to SQLite, so I fixed the code to save data only when there is no error.

---

## Files Updated
- app.py
- players.db

---

## Git Commit
Add input validation

---

## Reflection
Today I learned how important input validation is for preventing incorrect data from being stored in a database.
By testing both valid and invalid inputs, I was able to understand how conditions can be used to control the program flow.
The application is becoming more reliable step by step.

---

## Next Goal
- Improve input validation
- Add more error handling
- Improve the Player History UI