
from flask import Flask, render_template
import rss_scraper

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/item_list", methods=["GET"])
def item_list():
	return "hello world"

if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')
