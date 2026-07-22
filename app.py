from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect("players.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS players(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player TEXT,
    average TEXT,
    obp TEXT,
    slg TEXT
    )
    """)
conn.commit()

@app.route("/", methods=["GET", "POST"])
def home():
    average = ""
    obp = ""
    slg = ""
    
    player = ""
    at_bats = ""
    hits = ""
    walks = ""
    home_runs = ""
    
    error = ""
    
    if request.method == "POST":
        
        player = request.form["player"]
        at_bats = request.form["at_bats"]
        hits = request.form["hits"]
        
        singles = request.form["singles"]
        doubles = request.form["doubles"]
        triples = request.form["triples"]
        
        walks = request.form["walks"]
        home_runs = request.form["home_runs"]
        
        if int(hits) > int(at_bats):
            error = "Hits cannot be greater than At Bats."
            average = ""
            obp = ""
            
        elif int(at_bats) > 0:
            average = f"{int(hits) / int(at_bats):.3f}"
            
            if int(at_bats) + int(walks) > 0:
                obp = f"{(int(hits) + int(walks)) / (int(at_bats) + int(walks)):.3f}"
                
            else:
                obp = "Cannot divide by 0"
                
        else:
            average = "Cannot divide by 0"
            obp = "Cannot divide by 0"
            
        if int(at_bats) > 0:
            total_bases = (
                int(singles)
                + int(doubles) * 2
                + int(triples) * 3
                + int(home_runs) * 4
            )
            slg = f"{total_bases / int(at_bats):.3f}"
        
        else:
            slg = "Cannot divide by 0"

    cursor.execute("""
                   INSERT INTO players (player, average, obp, slg)
                   VALUES (?, ?, ?, ?)
                   """, (player, average, obp, slg))
    conn.commit()
    
    cursor.execute("SELECT player, average, obp, slg FROM players")
    players = cursor.fetchall()
    
    return render_template(
        "index.html", 
        average=average,
        obp=obp,
        slg=slg,
        players=players,
        
        player=player,
        at_bats=at_bats,
        hits=hits,
        
        walks=walks,    
        home_runs=home_runs,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)