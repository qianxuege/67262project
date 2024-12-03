from common import *

us='''
* Complex US: Identify Flights (US2)

   As a:  Airline
 I want:  To find the flights with low occupancy (ex <50 passengers) 
So That:  I can lower the price and attract more travelers to book the flight
'''

print(us)

def show_low_occupancies(max_occupancy):
    #filter for flights with low occupancy
    print(f'occupancy threshold: {max_occupancy}')
    flight_query = '''
        SELECT flight_id, destination, departure_time, arrival_time, occupancy
          FROM Flight
         WHERE occupancy <= %s
    '''
    cur.execute(flight_query, (max_occupancy,))
    all_low_occupancies = cur.fetchall()
    show_table(all_low_occupancies, cols = 'Flight_id Destination Departure_Time Arrival_Time Occupancy')
    
#example usage
show_low_occupancies(50)