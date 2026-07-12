# 📅 Day08 - Add Slugging Percentage

## Goal
Add Slugging Percentage (SLG) to the baseball statistics application.

---

## Completed
- Added a Home Runs input field
- Passed the Home Runs value from HTML to Flask
- Calculated Slugging Percentage (SLG)
- Displayed SLG on the result page
- Fixed a form field name error ('home_runs')
- Learned the importance of matching HTML form names with Flask variables

---

## What I Learned
### New Input Field
A new input field can be added by creating an '<input>' element in HTML and receiving its value with 'request.form'.
ex:
'python'
home_runs = request.form["home_runs"]

---

### Slugging Percentage (SLG)
A new statistic can be calculated using values submitted from the form.
ex:
'python'
if int(at_bats) > 0:
    slg = f"{int(home_runs) / int(at_bats):.3f}"

---

### Passing Variables to HTML
New values must also be passed to 'render_template()' so they can be displayed on the webpage.

ex:
'python'
return render_template(
    "index.html",
    slg=slg,
    home_runs=home_runs
)

---

## Files Updated

- app.py
- templates/index.html

---

## Git Commit

Add slugging percentage calculation

---

## Reflection

Today I added a new baseball statistic, Slugging Percentage (SLG), to my Flask application.
I learned how to connect a new HTML input field with Flask and display the calculated result on the webpage.
I also found and fixed an error caused by a mismatched form field name.

---

## 🚀 Next Goal
Store calculated player data and display it as a list.