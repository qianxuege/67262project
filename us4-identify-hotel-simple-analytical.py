from common import *

us='''
* Simple US: Identify Hotel (US4)

   As a:  Traveler
 I want:  To see the hotel with the highest rating in my destination 
So That:  I can make sure I have a high-quality place to stay
'''

print(us)

def identify_hotel(destination):
    #filter for hotel with highest rating in destination
    print(f"Hotel with Highest Rating in {destination}")
    hotel_query = '''
        SELECT hotel_name, location, rating
          FROM Hotel
         WHERE TRIM(LOWER(location)) = TRIM(LOWER(%s))
         ORDER BY rating DESC
         LIMIT 1
    '''
    cur.execute(hotel_query, (destination, ))
    best_hotel = cur.fetchall()
    show_table(best_hotel, cols = 'Hotel_name Location Rating')
    
#example usage
identify_hotel("Las Vegas")