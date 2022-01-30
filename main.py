from flask import Flask, render_template, url_for
import datetime
app = Flask(__name__)

@app.route("/")
def home_page():
    current_year = datetime.datetime.now().year
    return render_template("index.html", year=current_year)

@app.route("/portfolio")
def portfolio():
    current_year = datetime.datetime.now().year
    return render_template("portfolio.html",year=current_year)

@app.route("/analysis")
def analysis():
    current_year = datetime.datetime.now().year
    return render_template("analysis.html",year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
