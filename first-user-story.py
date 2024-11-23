from common import *

us='''
* Complex US: Maintain Consistency (US6)

   As a:  Hotel Provider
 I want:  To lower prices of all rooms of a hotel with a specific provider
So That:  I can ensure the information reflects newest prices
'''

print(us)

# need to change everything below
# change_in_price: positive means new_price = original price + change_in_price,
#                  negative means new_price = original price - change_in_price

def show_changed_prices( hotel_id, provider_id, change_in_price ):

    cols = ''

    tmpl =  f'''
SELECT 
  FROM Provisions as p
       JOIN Hotel_Provider as hp ON p.provider_id = hp.provider_id
       JOIN Hotel as h on h.hotel_id = p.hotel_id
 WHERE p.hotel_id = %s and p.provider_id = %s
'''
    cmd = cur.mogrify(tmpl, (hotel_name, change_in_price))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    pp(rows)
    show_table( rows, cols) 

show_comment_bug_feature( 5 )

# show enough to demonstrate that you've made the changes
# need the join to make it complex, so use hotel_name
# prices of rooms before
# prices of rooms after
# cheapest nightly rate before
# cheapest nightly rate after
