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

        # seed the machines table
        machine_1 = Machine(
            machine_name = 'endmill_grind_1'
        )
        machine_2 = Machine(
            machine_name = 'endmill_grind_2'
        )
        machine_3 = Machine(
            machine_name = 'endmill_grind_3'
        )

        # seed the operations table
        operation_1 = Operation(
            operation_name = 'endmill grind'
        )
        operation_2 = Operation(
            operation_name = 'cut'
        )
        operation_3 = Operation(
            operation_name = 'edge prep'
        )
        operation_4 = Operation(
            operation_name = 'polish'
        )
        operation_5 = Operation(
            operation_name = ''
        )