from common import *

def show_table( tablename ):

        tmpl =  f'''
    SELECT *
    FROM %s
    '''
        cmd = cur.mogrify(tmpl, (tablename,))
        print_cmd(cmd)
        cur.execute(cmd)
        rows = cur.fetchall()
        pp(rows)
        show_table( rows, cols) 

def show_all():
    tables = [Hotel_Provider, Hotel, Provision, Room]
    for table in tables:
        show_table(table)

show_all()
