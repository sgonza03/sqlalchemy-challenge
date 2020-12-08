import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo = True)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitations<br/>"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/start"
    )


@app.route("/api/v1.0/precipitations")
def precipitations():
    # Design a query to retrieve the last 12 months of precipitation data and plot the results
    max_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    max_date = max_date[0]

    # Calculate the date 1 year ago from today
    year_ago = dt.datetime.strptime(max_date, "%Y-%m-%d") - dt.timedelta(days=366)
    
    # Perform a query to retrieve the data and precipitation scores
    results_precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year_ago).all()

    # Convert list of tuples into normal list
    precipitation_dict = dict(results_precipitation)

    return jsonify(precipitation_dict)


@app.route("/api/v1.0/stations")
def stations():
    # Query stations
    results_stations =  session.query(Measurement.station).group_by(Measurement.station).all()

    # Convert list of tuples into normal list
    stations_list = list(np.ravel(results_stations))

    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    ###
    
@app.route("/api/v1.0/start")
def start():
    # 

if __name__ == '__main__':
    app.run(debug=True)
