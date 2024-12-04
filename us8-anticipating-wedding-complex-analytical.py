from common import *

us='''
* Complex US: Anticipating Wedding (US8)

   As a:  Traveler
 I want:  To find the hotel with the most free rooms in a specific location
So That:  I can make a large group reservation to accommodate guests to my wedding
'''

print(us)

def finding(location):
    print(f"Finding hotel with the most free rooms in {location}...")
    
    query = '''
        SELECT h.hotel_name, h.location, COUNT(r.room_number) AS free_rooms
          FROM Hotel AS h
          JOIN Room AS r ON h.hotel_id = r.hotel_id
         WHERE LOWER(TRIM(h.location)) = LOWER(TRIM(%s))
           AND r.room_available = TRUE
         GROUP BY h.hotel_id, h.hotel_name, h.location
         ORDER BY free_rooms DESC
         LIMIT 1
    '''
    cur.execute(query, (location,))
    result = cur.fetchall()
    
    if result:
        show_table(result, cols="Hotel_name Location Free_Rooms")
    else:
        print(f"No hotels with available rooms found in {location}.")

#example usage
finding("Chicago")
