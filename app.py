from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    average = None
    player = ""
    at_bats = ""
    hits = ""
    if request.method == "POST":
        
        player = request.form["player"]
        at_bats = request.form["at_bats"]
        hits = request.form["hits"]
        
        if int(at_bats)> 0:
            average = f"{int(hits) / int(at_bats):.3f}"
        else:
            average = "Cannot divide by 0"
        
    return render_template(
        "index.html", 
        average=average,
        player=player,
        at_bats=at_bats,
        hits=hits    
    )

if __name__ == "__main__":
    app.run(debug=True)