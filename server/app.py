from flask import request, session, make_response, render_template

from config import *
from models import Machine, Operation, Route, Item


@app.route('/')
@app.route('/<int:id>')
def index(id=0):
    return render_template("index.html")