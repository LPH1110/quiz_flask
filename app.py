from flask import render_template, request, Flask

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def index():
    # your code
    return render_template("start.html", quizzes = [])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')