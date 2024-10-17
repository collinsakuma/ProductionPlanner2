from app import app
from models import db, Machine, Operation, Route, Item

if __name__ == '__main__':

    with app.app_context():
        print('Starting seed...')
        # clear previous tables before seeding

        Machine.query.delete()
        Operation.query.delete()
        Route.query.delete()
        Item.query.delete()

        print('Seeding Finished...')