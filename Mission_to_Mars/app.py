# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo


# Import the code used to scrape the web pages
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# Connect to database; it is created if not already available
#mars_data = mongo.db.mars_data

# Drops collection if available to remove duplicates
#db.team.drop()


# Route to render index.html template using data from Mongo
@app.route('/')
def index():
	
	mars_info = mongo.db.mars_info.find_one()
	return render_template("index.html", mars_info=mars_info)

@app.route('/scrape')
def scrape():
	mars_info = mongo.db.mars_info
	mars_data = scrape_mars.scrape_info()
	mars_info.update({}, mars_data, upsert=True)
	
	return redirect("/", code=302)

if __name__ == "__main__":
	app.run(debug=True)



# create route that renders index.html template
#@app.route("/")
#def index():

    #teams = list(db.team.find())
    #print (teams)
    #return render_template("index.html", team="teams")

# Bonus add a new route
#@app.route("/bonus")
#def bonus():

    #return render_template("bonus.html")


#if __name__ == "__main__":
   # app.run(debug=True)
