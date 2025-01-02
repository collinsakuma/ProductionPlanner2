from flask import request, session, make_response, render_template

from config import *
# models imports
from models import Machine, Operation, Route, Item


@app.route('/')
@app.route('/<int:id>')
def index(id=0):
    return render_template("index.html")
# run on port #### default port 5555
if __name__ == '__main__':
    app.run(port=5555, debug=True)