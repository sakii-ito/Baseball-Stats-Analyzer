# 📅 Day 07 - Add Input validation and Error Handling

## Goal
Improve the application by validating user input and displaying error messages.

---

## Completed
- Added input validation
- Prevented Hits from being greater than At Bats
- Displayed error messages on the webpage
- Learned how to use Jinja2 'if' statements
- Improved the results section with a result card
- Added a hover effect to the button
- Fixed variable initialization by replacing 'None' with empty strings ('""')

---

## What I Learned
### Validation
Validation checks whether user input is correct before processing data.
ex: 
'python'
if int(hits) > int(at_bats):
    error = "Hits cannot be greater than At Bats."

### Error Handling
Error handling improves the user experience by displaying helpful
messages instead of incorrect results.
ex: 
'python'
error = "Hits cannot be greater than At Bats."

### Jinja2 if Statement
Jinja2 can display HTML only when a condition is true.
ex: 
'HTML'
{% if error %}
<p class="error">{{ error }}</p>
{% endif %}

---

### Hover Effect
The ':hover' selector changes an element's style when the mouse pointer is over it.
ex: 
'css'
button:hover {
    background-color: #0056b3;
}

---

### Files Updated
- app.py
- templates/index.html
- static/style.css

---

## Git Commit
Add input validation and error handling

---

## Reflection
Today I improved the application by adding input validation and error handling.
I learned how to display error messages using Jinja2 and improved the user experience by 
preventing invalid input.
I also tested the application with different input values and fixed bugs that
I found during testing.

---

## Next Goal
Add a reset button and continue improving the baseball statics application.