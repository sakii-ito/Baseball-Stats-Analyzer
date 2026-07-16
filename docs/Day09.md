# 📅 Day09 - Player History

## Goal
Save player statistics and display a history of previous calculations.

---

## Completed
- Created a list to store player data
- Used a dictionary to organize player statistics
- Saved new records with append()
- Passed the player list from Flask to HTML
- Displayed player history using a Jinja for loop
- Fixed template errors while building the history feature

---

## What I Learned
### List
A list stores multiple pieces of data.
ex:
'python'
players = []

### Dictionary
A dictionary stores related values using keys.
ex:
'python'
players.append({
    "player": player,
    "average": average,
    "obp": obp,
    "slg": slg
})

### append()
append() adds a new item to the end of a list.
ex:
'python'
players.append(player_data)

### Jinja for Loop
A for loop displays each item in a list.
ex:
'HTML'
{% for p in players %}
<h3>{{ p.player }}</h3>
<p>AVG : {{ p.average }}</p>
{% endfor %}

### Passing a List to HTML
Flask can send an entire list to an HTML template.
ex:
'python'
return render_template(
    "index.html",
    players=players
)

---

## Files Updated
- app.py
- templates/index.html
- static/style.css

---

## Git Commit
Add player history feature

---

## Reflection
Today I learned how to save multiple player records using a list and a dictionary.
I also learned how Flask sends a list to HTML and how Jinja's for loop displays each record.
This made the application feel much more like real baseball statistics website.

---

## Next Goal
Store player history permanently using a database(SQLite).