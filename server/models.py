from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

from config import db


class Machine(db.Model, SerializerMixin):
    __tablename__ = 'machines'

    id = db.Column(db.Integer, primary_key=True)
    machine_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())