from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import json
from flask_marshmallow import Marshmallow
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mariadb+pymysql://admin:kcb@localhost:3306/testerml'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class car(db.Model):
    __tablename__ = "cardecision"

    id = db.Column(Integer, primary_key=True, index=True)
    buying = db.Column(String)
    maint = db.Column(String)
    doors = db.Column(String)
    persons = db.Column(String)
    lug_boot = db.Column(String)
    carsafety = db.Column(String)
    decision = db.Column(String)
    carid=db.Column(Integer)

    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    def __init__(self,buying,maint,doors,persons,lug_boot,carsafety,decision,carid):
        self.buying=buying
        self.maint=maint
        self.doors=doors
        self.persons=persons
        self.lug_boot=lug_boot
        self.carsafety=carsafety
        self.decision=decision
        self.carid=carid
    def __repr__(self):
        return '' % self.id
   # db.create_all()

class CarSchema(ma.SQLAlchemyAutoSchema):
    class Meta(ma.SQLAlchemyAutoSchema.Meta):
     model = car
 #   sqla_session = db.session
 #   id = mafields.Number(dump_only=True)
 ##   buying =ma fields.String(required=True)
 #   maint = fields.String(required=True)
 #   doors = fields.String(required=True)
 #   persons = fields.String(required=True)
 #   lug_boot = fields.String(required=True)
 #   carsafety = fields.String(required=True)
 #   decision = fields.String(required=True)
 #   carid = fields.Number(required=True)

@app.route('/cars', methods = ['GET'])
def index():
    get_products = car.query.all()
    car_schema = CarSchema(many=True)
    cars = car_schema.dump(get_products)
    return make_response(jsonify({"car": cars}))

@app.route('/cars', methods = ['POST'])
def create_product():
    data = request.get_json()
    car_schema = CarSchema()
    #product=car_schema.load(json.loads(json.dumps(data)))
    product = car_schema.load(data)
    cars = car_schema.dump(product)
    return make_response(jsonify({"car": cars}),200)

if __name__ == '__main__':
    app.run(debug=True)