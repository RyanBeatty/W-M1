
from flask import Flask, render_template, request
import rss_scraper
import postmates
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

@app.route("/item_info",methods=["GET"])
def item_info():
    info = rss_scraper.getItemData(request.args.get("url","http://auburn.craigslist.org/zip/4877117310.html"))
    return json.dumps(info)

@app.route("/delivery_quote",methods=["GET"])
def delivery_quote():
    pickup = request.args.get("pickup_address", '')
    dropoff = request.args.get("dropoff_address", '')
    if not pickup or not dropoff:
        return json.dumps({})
    quote = postmates.delivery_quote(pickup, dropoff)
    return json.dumps(quote)

@app.route("/delivery_progress",methods=["POST"])
def delivery_progress():
    info = {}
    quote = postmates.delivery_quote(request.form['pickup_address'], request.form['dropoff_address'])
    info['quote_id'] = quote['id']
    print(info)
    info['pickup_name'] = request.form['pickup_name']

    info['pickup_address'] = request.form['pickup_address']
    print("HIIII")
    info['pickup_phone_number'] = request.form['pickup_phone_number']

    info['dropoff_name'] = request.form['dropoff_name']
    info['dropoff_phone_number'] = request.form['dropoff_phone_number']
    info['dropoff_address'] = request.form['dropoff_address']
    info['manifest'] = request.form['manifest']
    delivery = postmates.delivery_place(info)
    return render_template("delivery.html", deliveryObject = delivery)

@app.route("/test")
def test():
    print(type(request.args))
    return "test"

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
