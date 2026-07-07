from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    average = None
    if request.method == "POST":
        
        player = request.form["player"]
        at_bats = int(request.form["at_bats"])
        hits = int(request.form["hits"])
        
        if at_bats> 0:
            average = round(hits / at_bats, 3)
        else:
            average = "Cannot divide by 0"
        
    return render_template("index.html", average=average)

if __name__ == "__main__":
    app.run(debug=True)