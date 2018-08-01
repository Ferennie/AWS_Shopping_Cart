import uuid
from flask import Flask, request, jsonify
from flask_restplus import Resource, Api
from flask_restplus import fields
from flask_sqlalchemy import SQLAlchemy

# what's happening
# welcome to flask: http://flask.pocoo.org/
# working with sqlalchemy & swagger:
# http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/

application = Flask(__name__)
api = Api(application)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(application)

# items = []

item = api.model('item', {
    'name': fields.String(required=True, description='item name'),
    'description': fields.String(required=True, description='item description'),
    'price': fields.String(required=True, description='item price'),
    'size': fields.String(required=True, description='item size'),
    'color': fields.String(required=True, description='item color'),
    'availability': fields.String(required=True, description='item availability'),
})

item_id = api.model('item_id', {
    'id': fields.String(readOnly=True, description='unique identifier of an item'),
    'name': fields.String(required=True, description='item name'),
    'description': fields.String(required=True, description='item description'),
    'price': fields.String(required=True, description='item price'),
    'size': fields.String(required=True, description='item size'),
    'color': fields.String(required=True, description='item color'),
    'availability': fields.String(required=True, description='item availability'),
})


class Item(db.Model):
    id = db.Column(db.Text(80), primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    price = db.Column(db.String(80), unique=False, nullable=False)
    size = db.Column(db.String(80), unique=False, nullable=False)
    color = db.Column(db.String(80), unique=False, nullable=False)
    availability = db.Column(db.String(200), unique=False, nullable=False)

    def __repr__(self):
        return '<Rumor %r>' % self.content


def create_item(data):
    id = str(uuid.uuid4())
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    size = data.get('size')
    color = data.get('color')
    availability = data.get('availability')
    itm = Item(id=id, name=name, description=description, price=price, size=size, color=color,
               availability=availability)
    # items.append(itm)
    db.session.add(itm)
    db.session.commit()
    return itm


@api.route("/items")
class Items(Resource):
    def get(self):
        shirt1 = {'Name': 'shirt', 'Description': 'fur', 'Price': 35, 'Size': 2, 'Color': 'black', 'Avail': 'True'}
        db.session.add(shirt1)
        # shirt2 = {'Name': 'pants', 'Description': 'khakis', 'Price': 40, 'Size': 4, 'Color': 'red', 'Avail': 'True'}
        # db.session.add(shirt2)
        # shirt3 = {'Name': 'shoes', ''Description': 'vans', Price': 27, 'Size': 6, 'Color': 'blue', 'Avail': 'True'}
        # db.session.add(shirt3)
        # items.append(shirt3)
        return db.session.query(Item)

    @api.expect(item)
    @api.marshal_with(item_id)
    def post(self):
        new_item = create_item(request.json)
        return Item.query.filter(Item.id == new_item.id).one()


@api.route("/items/<string:clr>")
class ItemColorRoute(Resource):
    # id becomes a method param in this GET
    def get(self, clr):
        # use sqlalchemy to get a rumor by ID
        return Item.query.filter(Item.color == clr)


@api.route("/items/<string:name>")
class ItemNameRoute(Resource):
    # id becomes a method param in this GET
    def get(self, name):
        # use sqlalchemy to get a rumor by ID
        return Item.query.filter(Item.name == name)


@api.route("/items/price/<string:avl>")
class Avail(Resource):
    def get(self, avl):
        clothes = Items.get()
        return [shirt for shirt in clothes if shirt['avl'] == avl]


@api.route("/items/price/<string:prc>")
class ItemPriceRoute(Resource):
    def get(self, prc):
        clothes = Items.get()
        return [shirt for shirt in clothes if str(shirt['prc']) == prc]


@api.route("/items/size/<string:sz>")
class ItemSizeRoute(Resource):
    def get(self, sz):
        clothes = Items.get()
        return [shirt for shirt in clothes if str(shirt['sz']) == sz]


@api.route("/rumor/<string:id>")
class ItemIdRoute(Resource):
    @api.marshal_with(item_id)
    def get(self, id):
        return Item.query.filter(Item.id == id)


def configure_db():
    db.create_all()
    db.session.commit()


# for testing only!
def get_app():
    return application


def main():
    configure_db()
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()
