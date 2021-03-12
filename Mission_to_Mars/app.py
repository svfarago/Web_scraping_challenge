# import necessary libraries
from flask import Flask, render_template
import pymongo

# create instance of Flask app
app = Flask(__name__)

# Create connection variable
conn = "mongodb://localhost:27017"

# Pass connection to pymongo instance
client = pymongo.MongoClient(conn)

# Connect to database; it is created if not already available
db = client.team_db

# Drops collection if available to remove duplicates
db.team.drop()



# create route that renders index.html template
@app.route("/")
def index():

    teams = list(db.team.find())
    print (teams)
    return render_template("index.html", team="teams")

# Bonus add a new route
@app.route("/bonus")
def bonus():

    return render_template("bonus.html")


if __name__ == "__main__":
    app.run(debug=True)
