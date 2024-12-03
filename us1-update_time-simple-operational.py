from common import *

us='''
* Simple US: Update Time (US1)

   As a:  Airline
 I want:  To change the departure and arrival time for a flight 
So That:  I can provide accurate updates to users
'''

print(us)

def show_changed_deparr_times(flight_id, new_dep, new_arr):
    #display departure and arrival times before update
    print("before update")
    flight_query = '''
        SELECT f.flight_id, f.destination, f.departure_time, f.arrival_time
          FROM Flight as f
         WHERE f.flight_id = %s
    '''
    cur.execute(flight_query, (flight_id,))
    before_flight_deparr = cur.fetchall()
    show_table(before_flight_deparr, cols = 'Flight_id Destination Departure_Time Arrival_Time')
    
    #Perform the update
    update_query = '''
    UPDATE Flight
       SET departure_time = %s,
           arrival_time = %s
       '''
    cur.execute(update_query, (new_dep, new_arr))
    conn.commit()
    
    #Display departure and arrival times after the change
    print(f"New departure: {new_dep}")
    print(f"New arrival: {new_arr}")
    cur.execute(flight_query, (flight_id,))
    after_deparr = cur.fetchall()
    show_table(after_deparr, cols = 'Flight_id Destination Departure_Time Arrival_Time')
    
#example usage
show_changed_deparr_times(1, '2024-12-07 12:45:37','2024-12-07 09:12:48')