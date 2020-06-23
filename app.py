from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS  
from flask_heroku import Heroku

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= "postgres://farocjhrlgwpay:0251e23f537a3a7852a69de44c48e6a4890df09f250d6143a0280430c768a430@ec2-34-230-231-71.compute-1.amazonaws.c"

db = SQLAlchemy(app)
ma = Marshmallow(app)

heroku = Heroku(app)
CORS(app)



class Month(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.Integer, unique=True, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    daysInMonth = db.Column(db.Integer, nullable=False)
    daysInPreviousMonth = db.Column(db.Integer, nullable=False)
    startDay = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __init__(self,position, month, daysInMonth, daysInPreviousMonth, startDay, year):
        self.position = position
        self.month = month
        self.daysInMonth = daysInMonth
        self.daysInPreviousMonth = daysInPreviousMonth
        self.startDay = StartDay
        self.year = year

class MonthSchema(ma.Schema):
    class Meta:
        fields = ("id", "position", "month", "daysInMonth", "daysInPreviousMonth", "startDay", "year")

month_schema = MonthSchema()
multiple_month_schema = MonthSchema(many=True)       


@app.route("/month/add", methods=["POST"])
def add_month():
    if request.content_type != "application/json":
        return jsonify("Error: Data must be sent as JSON")

    post_data = request.get_json()
    position = post_data.get("position")
    month = post_data.get("month")
    daysInMonth = post_data.get("daysInMonth")
    daysInPreviousMonth = post_data.get("daysInPreviousMonth") 
    startDay = post_data.get("startDay")
    year = post_data.get("year") 

    record = Month(position, month, daysInPreviousMonth, daysInPreviousMonth, startDay, year)
    db.session.add(record)
    db.session.commit()

    return jsonify("Month added syccesfully")

@app.route("/month/get", methods=["Get"])
def get_all_months():
    all_months = db.session.query(Month).all()
    return jsonify(multiple_month_schema.dump(all_months))

if __name__=="__main__":
    app.run(debug=True)




