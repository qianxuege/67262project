from common import *

us='''
* Complex US: Maintain Consistency (US6)

   As a:  Kayak’s website Manager
 I want:  Lower prices of all rooms in the hotel given a specific hotel name
So That:  I can ensure the information reflects newest prices
'''

print(us)

# need to change everything below
# change_in_price: positive means new_price = original price + change_in_price,
#                  negative means new_price = original price - change_in_price
#name = user input hotel name
def show_changed_prices( hotel_name, change_in_price):

    cols = ''

    tmpl =  f'''
    UPDATE Room 
           SET nightly_rate = nightly_rate + %s
     WHERE room_number IN 
      (SELECT r.room_number
          FROM Room as r
          JOIN Hotel as h on h.hotel_id = r.hotel_id
        WHERE h.hotel_name = %s)
'''
    cmd = cur.mogrify(tmpl, (change_in_price, hotel_name))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    pp(rows)
    show_table( rows, cols) 

show_changed_prices("Kinzie Hotel", 100)

# show enough to demonstrate that you've made the changes
# need the join to make it complex, so use hotel_name
# prices of rooms before
# prices of rooms after
# cheapest nightly rate before
# cheapest nightly rate after
