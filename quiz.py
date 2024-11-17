from flask import render_templates, request, Flask

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def index():
    # your code
    return render_templates("start.html", quizzes = [])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')