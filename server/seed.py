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

        # seed the machine table
        machine_1 = Machine(
            machine_name = 'endmill_grind_1'
        )
        machine_2 = Machine(
            machine_name = 'endmill_grind_2'
        )
        machine_3 = Machine(
            machine_name = 'endmill_grind_3'
        )