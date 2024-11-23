from common import *

def select_table( tablename, cols ):
        tmpl =  f'''
    SELECT *
    FROM {tablename}
    '''
        cmd = cur.mogrify(tmpl, (tablename,))
        
        cur.execute(cmd)
        rows = cur.fetchall()
        
        show_table(rows, cols) 

def show_all():
    
    tables_dict = {
        "Hotel_Provider": "provider_id provider_name",
        "Hotel": "hotel_id hotel_name location pool rating cheapest_nightly_rate",
        "Provision": "hotel_id provider_id",
        "Room": "room_number hotel_id room_capacity nightly_rate available"
    }
    for table, cols in tables_dict.items():
        print(table)
        select_table(table, cols)

show_all()
