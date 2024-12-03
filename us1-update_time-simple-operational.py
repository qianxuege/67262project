from common import *

us='''
* Simple US: Update Time (US1)

   As a:  Airline
 I want:  To change the departure and arrival time for a flight 
So That:  I can provide accurate updates to users
'''

print(us)

def show_changed_deparr_times(flight_id):
    #display departure and arrival times before update
    print("before update")
    flight_query = '''
        SELECT f.destination, f.departure_time, f.arrival_time
          FROM Flight as f
         WHERE f.flight_id = %s
    '''