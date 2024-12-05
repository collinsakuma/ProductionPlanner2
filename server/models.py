from flask_sqlalchemy import SQLAlchemy
# note to fix import
from sqlalchemy_serializer import SerializerMixin  # type: ignore

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

class Route(db.Model, SerializerMixin):
    __tablename__ = 'routes'

    id = db.Column(db.Integer, primary_key=True)
    sequence = db.Column(db.String)

class Item(db.Model, SerializerMixin):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String)
    route_id = db.Column(db.Integer, db.ForeignKey('routes.id'))
    item_length = db.Column(db.Integer)
    item_width = db.Column(db.Integer)
    item_shank_length = db.Column(db.Integer)
    has_flats = db.Column(db.Boolean, default=False) # add defaults ???
    has_neck = db.Column(db.Boolean, default=False)
    item_neck_length = db.Column(db.Integer)
    item_radius = db.Column(db.Integer)
    item_coating = db.Column(db.string) # possibly needs to be its own table
    has_edge_prep = db.Column(db.Boolean, default=False)
    has_polishing = db.Column(db.Boolean, default=False)

    serialize_rules = ('-route')

# class Coating(db.Model, SerializerMixin):
#   __tablename__ = 'coatings'