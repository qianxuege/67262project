from common import *

us='''
* Simple US: Update Availability (US5)

   As a:  Hotel Manager
 I want:  Make a room unavailable to be booked 
So That:  I can accurately assign guests to rooms
'''

print(us)

def show_status_before(hotel_id, room_number):
    #display room's availability status before update
    print("before update")
    room_query = '''
    SELECT h.hotel_id, h.hotel_name, r.room_number, r.room_available
      FROM Hotel as h
      JOIN Room as r ON r.hotel_id = h.hotel_id
     WHERE r.hotel_id = %s AND r.room_number = %s
    '''
    cur.execute(room_query, (hotel_id, room_number))
    rows = cur.fetchall()
    show_table(rows, cols = 'hotel_id hotel_name room_number availability')
    # Extract the hotel name from the query result
    if rows:
        hotel_name = rows[0][1]  # Assuming `hotel_name` is the second column in the result
        print(f'Setting Room {room_number} at {hotel_name} to Unavailable:')
    else:
        print("No matching room found.")
    update_query = '''
    UPDATE Room
    SET room_available = FALSE
    WHERE hotel_id = (
        SELECT h.hotel_id
        FROM Hotel AS h
        WHERE h.hotel_id = %s
    ) 
    AND room_number = %s
    '''
    cur.execute(update_query, (hotel_id, room_number))
    conn.commit()
    
    #display room's availability status after update
    room_query = '''
    SELECT h.hotel_id, h.hotel_name, r.room_number, r.room_available
      FROM Hotel as h
      JOIN Room as r ON r.hotel_id = h.hotel_id
     WHERE r.hotel_id = %s AND r.room_number = %s
    '''
    cur.execute(room_query, (hotel_id, room_number))
    rows = cur.fetchall()
    show_table(rows, cols = 'hotel_id hotel_name room_number availability')
    
#example usage
show_status_before(1, 100)