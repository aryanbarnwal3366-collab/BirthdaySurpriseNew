from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/song")
def song():
    return render_template("song.html")

@app.route("/wish")
def wish():
    return render_template("wish.html")

if __name__ == "__main__":
    app.run(debug=True)
