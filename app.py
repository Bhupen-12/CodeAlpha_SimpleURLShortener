import random
import string

from flask import Flask, request, jsonify, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(1000), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)


with app.app_context():
    db.create_all()


def generate_code(length=6):
    characters = string.ascii_letters + string.digits

    while True:
        code = ''.join(random.choice(characters) for _ in range(length))

        if not URL.query.filter_by(short_code=code).first():
            return code


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/shorten", methods=["POST"])
def shorten():
    data = request.get_json() or request.form

    long_url = data.get("url")

    if not long_url:
        return jsonify({"error": "URL is required"}), 400

    code = generate_code()

    new_url = URL(
        original_url=long_url,
        short_code=code
    )

    db.session.add(new_url)
    db.session.commit()

    return jsonify({
        "short_url": request.host_url + code
    })


@app.route("/<code>")
def redirect_url(code):
    url = URL.query.filter_by(short_code=code).first()

    if not url:
        return jsonify({"error": "URL not found"}), 404

    return redirect(url.original_url)


if __name__ == "__main__":
    app.run(debug=True)