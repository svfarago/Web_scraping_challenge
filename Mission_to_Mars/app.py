from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection to database, mars_app
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Route for index.html template pulling data from Mongo
@app.route("/")
def index():

    # Find one record of data from the mars mongo database
    destination_data = mongo.db.mars.find_one()

    # Return template and data
    return render_template("index.html", mars=destination_data)


# Route that will trigger the scrape function
# Note: Caution if running too frequenty it may cause Windows to lock you out for 10 min.
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    # Run the scrape function to retrieve mars table data in dictionary format
    mars_data = scrape_mars.scrape_all()
    print(mars_data)

    # Update the Mongo database collection (mars table) using update and upsert=True
    mars.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")
    

if __name__ == "__main__":
    app.run(debug=True)