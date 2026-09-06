from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"name": "Aero Smart Watch", "price": "$149", "tag": "Best Seller", "emoji": "⌚"},
    {"name": "Nova Headphones", "price": "$199", "tag": "New", "emoji": "🎧"},
    {"name": "Pulse Speaker", "price": "$89", "tag": "Trending", "emoji": "🔊"},
    {"name": "Luma Lamp", "price": "$79", "tag": "Popular", "emoji": "💡"},
]


@app.route("/")
def index():
    return render_template("index.html", products=products)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
