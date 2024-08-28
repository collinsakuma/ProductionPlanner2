from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

from config import db


class Machine(db.Model, SerializerMixin):
    __tablename__ = 'machines'

    id = db.Column(db.Integer, primary_key=True)
    machine_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    operations = db.relationship('Operation', backref='machine')

class Operation(db.MOdel, SerializerMixin):
    __tablename__ = 'operations'

    serialize_rules = ('-machine')

    id = db.Column(db.Integer, primary_key=True)
    operation_name = db.Column(db.String)
    machine_id = db.Column(db.Integer, db.ForeignKey('machines.id'))

    route_operations = db.relationship('RouteOperation', backref='operation')

class Route(db.Model, SerializerMixin):
    __tablename__ = 'routes'

    id = db.Column(db.Integer, primary_key=True)
    # item_id = db.Column(db.Integer)

    # items = db.relationship('Item', backref='route')
    route_operations = db.relationship('RouteOperation', backref='route')

class Item(db.Model, SerializerMixin):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String)
    route_id = db.Column(db.Integer, db.ForeignKey('routes.id'))

    serialize_rules = ('-route')

class RouteOperation(db.Model, SerializerMixin):
    __tablename__ = 'route_operations'

    serialize_rules = ('-route', '-operation')

    id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey('routes.id'))
    operation_id = db.Column(db.Integer, db.ForeignKey('operations.id'))