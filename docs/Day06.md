# 📅 Day06 - Add On-Base Percentage (OBP)

## Goal
Add a new baseball statistic by calculating On-Base Percentage (OBP)

---

## Completed
- Added a new input field for Walks
- Received Walks data in Flask
- Calculated On-Base Percentage (OBP)
- Displayed the OBP result on the webpage
- Fixed an 'UnboundLocalError' by initializing variables

---

## What I Learned
### Walks
walks are included when calculating On-Base Percentage.
ex: Walks = 2

### On-Base Percentage (OBP)
OBP measures how often a player reaches base.
Formula
(Hits + Walks) ÷ (At Bats + Walks)

### Variable Initialization
Variables should be initialized before they are used.
ex: obp = None
    walks = ""

### Multiple Result
Flask can send multiple values to HTML using 'render_template()'.
ex: return render_template(
    "index.html",
    average=average,
    obp=obp
)

---

## Files Updated
- app.py
- templates/index.html

---

## Git Commit
Add On-Base Percentage calculation

---

## Reflection
Today I added a new baseball statistic to my application.
I learned how to add a new input field, calculate a new value, and display it on the webpage.
I also fixed an error by initializing variables before using them.

---

## Next Goal
Improve the webpage design and add more baseball statistics such as OPS.
