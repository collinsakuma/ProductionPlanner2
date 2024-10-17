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

        # seed the routes table 
        route_1 = Route(
            sequence = ''
        )

        # seed the items table
        item_1 = Item(
            item_name = 'endmill_1',
            # route_id = '',
            item_length = 50.8,
            item_width = 12.7,
            item_shank_length = 20,
            has_flats = True,
            has_neck = True,
            item_neck_length = 5,
            item_coating = 'C03',
            has_edge_prep = True,
            has_polishing = True
        )