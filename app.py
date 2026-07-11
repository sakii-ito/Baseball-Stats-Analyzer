from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    average = None
    obp = None
    player = ""
    at_bats = ""
    hits = ""
    walks = ""
    error = ""
    
    if request.method == "POST":
        
        player = request.form["player"]
        at_bats = request.form["at_bats"]
        hits = request.form["hits"]
        walks = request.form["walks"]
        
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
        

    return render_template(
        "index.html", 
        average=average,
        obp=obp,
        player=player,
        at_bats=at_bats,
        hits=hits,
        walks=walks,    
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)