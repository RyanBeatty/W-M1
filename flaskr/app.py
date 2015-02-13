
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
    req = request.form
    print("hi")
    print(req)
    info = {}
    quote = postmates.delivery_quote(req['pickup_address'], req['dropoff_address'])
    info['quote_id'] = quote['id']
    info['pickup_name'] = req.getlist('pickup_name')[0]
    info['pickup_address'] = req.getlist('pickup_address')[0]
    print(req.getlist('pickup_phone_number'))
    info['pickup_phone_number'] = req.getlist('pickup_phone')[0]
    info['dropoff_name'] = req.getlist('dropoff_name')[0]
    info['dropoff_phone_number'] = req.getlist('dropoff_phone')[0]
    info['dropoff_address'] = req.getlist('dropoff_address')[0]
    info['manifest'] = req.getlist('manifest')[0]
    delivery = postmates.delivery_place(info)
    return render_template("delivery.html", backgroundInfo = info, deliveryObject = delivery)

@app.route("/test")
def test():
    print(type(request.args))
    return "test"

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
