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
def show_table(rows, cols):
    if isinstance(cols, str):
        # Ensure cols is a list if it's a string
        cols = cols.split()
    elif not isinstance(cols, list):
        raise ValueError("`cols` must be a string or a list")
    
    # Display the table (Assume this is a placeholder for an actual implementation)
    print(f"{cols}")
    for row in rows:
        print(f"{row}")

def show_changed_prices(hotel_name, change_in_price):
    # Display prices before the change
    print(f"Prices before change for hotel: {hotel_name}")
    before_query = '''
    SELECT r.room_number, r.nightly_rate
      FROM Room AS r
      JOIN Hotel AS h ON h.hotel_id = r.hotel_id
     WHERE LOWER(TRIM(h.hotel_name)) = LOWER(TRIM(%s))
    ORDER BY r.nightly_rate ASC;
    '''
    cur.execute(before_query, (hotel_name,))
    before_prices = cur.fetchall()
    show_table(before_prices, ['Room Number', 'Nightly Rate'])
    
    # Perform the update
    update_query = '''
    UPDATE Room 
       SET nightly_rate = nightly_rate + %s
     WHERE room_number IN 
       (SELECT r.room_number
          FROM Room AS r
          JOIN Hotel AS h ON h.hotel_id = r.hotel_id
         WHERE LOWER(TRIM(h.hotel_name)) = LOWER(TRIM(%s)))
    '''
    cur.execute(update_query, (change_in_price, hotel_name))
    conn.commit()
    
    # Display prices after the change
    print(f"Prices after change for hotel: {hotel_name}")
    cur.execute(before_query, (hotel_name,))
    after_prices = cur.fetchall()
    show_table(after_prices, ['Room Number', 'Nightly Rate'])
    
    # Display the cheapest nightly rates before and after
    if before_prices:
        print(f"Cheapest rate before: {before_prices[0][1]}")
    if after_prices:
        print(f"Cheapest rate after: {after_prices[0][1]}")

# Example usage
show_changed_prices('Kinzie Hotel', 100)


# show enough to demonstrate that you've made the changes
# need the join to make it complex, so use hotel_name
# prices of rooms before
# prices of rooms after
# cheapest nightly rate before
# cheapest nightly rate after
