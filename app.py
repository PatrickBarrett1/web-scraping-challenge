from flask import Flask, render_template
from flask_pymongo import PyMongo
import pymongo
from pymongo.mongo_client import MongoClient
from werkzeug.utils import redirect
import scrape_mars

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Initialize PyMongo to work with MongoDBs
#################################################

#app.config['MONGO_DBNAME'] = 'web_scraping'
#app.config['MONGO_URI'] = "mongodb://localhost:27017/web_scraping"
#mongo = PyMongo(app)


mongo_local_connection_string = "mongodb://localhost:27017"
client = pymongo.MongoClient(mongo_local_connection_string)

mongo_db = client.web_scraping
collection = mongo_db.mars_data

#################################################
# Flask Routes
#################################################
#                   default route
@app.route("/")
def index():
    mars = collection.find_one()
    return render_template("./index.html", mars=mars)

# scrape route
@app.route("/scrape")
def scraped_data():
    mars_scrape = scrape_mars.scrape()
    return mars_scrape

if __name__ == "__main__":
    app.run(debug=True)