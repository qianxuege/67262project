from common import *

def select_table( tablename ):
        tmpl =  f'''
    SELECT *
    FROM {tablename}
    '''
        cmd = cur.mogrify(tmpl, (tablename,))
        print_cmd(cmd)
        cur.execute(cmd)
        rows = cur.fetchall()
        pp(rows)
        show_table( rows) 

def show_all():
    tables = ["Hotel_Provider", "Hotel", "Provision", "Room"]
    for i in range(len(tables)):
        select_table(tables[i])

show_all()
