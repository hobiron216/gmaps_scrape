# save this as app.py
from flask import Flask, request
from google_maps_by_keyword import scrape
from google_maps_by_radius import scrape_paid
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/tes")
@cross_origin(supports_credentials=True)
def hello():
    radius = request.args.get('radius')
    longitude  = request.args.get('longitude')
    latitude = request.args.get('latitude')
    category = request.args.get('category')

    error = ''
    if not radius :
        error = "field radius should be exist"
    elif not longitude:
        error = "field longitude should be exist"
    elif not latitude:
        error = "field latitude should be exist"
    elif not category:
        error = "field category should be exist"

    if error :
        response = {
            "success" : False,
            "error" : error,
        }

        return response
    else :
        response = {
            "success": True,
            "error": error,
        }

        return response

@app.route("/scrape")
@cross_origin(supports_credentials=True)
def crawl():
    keyword = request.args.get('keyword')
    category = request.args.get('category')
    languange = 'en'

    error = ''
    if not keyword :
        error = "field keyword should be exist"
    elif not category:
        error = "field category should be exist"

    if error :
        response = {
            "success" : False,
            "error" : error,
        }

        return response
    else :
        data = scrape(keyword, languange, category)
        response = {
            "success": True,
            "error": error,
            "data" : data
        }
        return response

@app.route("/scrape_paid")
@cross_origin(supports_credentials=True)
def crawl2():
    lat = request.args.get('lat')
    long = request.args.get('long')
    radius = request.args.get('radius')
    category = request.args.get('category')

    error = ''
    if not lat :
        error = "field lat should be exist"
    elif not long:
        error = "field long should be exist"
    elif not category:
        error = "field category should be exist"
    elif not radius:
        error = "field radius should be exist"

    if error :
        response = {
            "success" : False,
            "error" : error,
        }

        return response
    else :
        data = scrape_paid(lat, long, radius, category)
        response = {
            "success": True,
            "error": error,
            "data" : data
        }
        return response

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000, host='0.0.0.0')
