
from flask import Flask, render_template, request
import rss_scraper
import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
	return render_template("index.html")

@app.route("/search", methods=["GET"])
def search():
	site = request.args.get("site", "norfolk")
	term = request.args.get("term", "")
	return render_template("search.html", current_site=site, index_list=rss_scraper.parse_rss_feed(site, term))

@app.route("/item_list", methods=["GET"])
def item_list():
	items = rss_scraper.parse_rss_feed("norfolk")
	return json.dumps(items)



if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')
