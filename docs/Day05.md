# 📅 Day05 - Improve User Experience

## Goal
Improve the user interface and make the application easier to use.

---

## Completed
- Improved the CSS design
- Centered the form on the page
- Added a card-style layout
- Styled the input fields and button
- Kept form values after calculation

---

## What I Learned
### CSS
CSS makes a web page look better and easier to use.

### value
The value attribute displays a value inside an input fied.
ex: <input value="{{ player }}">

### User Experience (UX)
Keeping the user's input after submitting a form makes the application easier to use.

### render_template()
Multiple variables can be passed from Python to HTML.
ex: return render_template(
        "index.html",
        player=player,
        at_bats=at_bats,
        hits=hits,
        average=average
)

---

## Files Upated
- app.py
- templates/index.html
- static/style.css

---

## Git Commit
Keep form values after calculation

---

## Reflection
Today I improved the application's user experience.
The form now keeps the user's input after calculation, making it feel more like a real web application.
I also learned how to pass multiple variables from Flask to HTML.

---

## Next Goal
Add new baseball statistics such as On-base Percentage (OBP) or OPS.