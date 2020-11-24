# Importing needed tools
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping

# Set up Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
   mars_dict = mongo.db.mars_dict.find_one()
   return render_template("index.html", mars=mars_dict)

@app.route("/scrape")
def scrape():
   mars_dict = mongo.db.mars_dict
   mars_data = scraping.scrape_all()
   mars_dict.update({}, mars_data, upsert=True)
   return "Scraping Successful!"

if __name__ == "__main__":
   app.run(host='127.0.0.1',port=5500)