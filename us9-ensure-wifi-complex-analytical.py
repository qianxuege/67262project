from common import *

us='''
* Complex US: Ensure Wifi (US9)

   As a:  Traveler
 I want:  Find the average price of a flight with wifi to a specific destination
So That:  I can identify a baseline price to compare to for when I plan to book my trip
'''

print(us)

def find_average_price(destination):
    print(f"Finding the average price of flights with WiFi to {destination}...")
    query = '''
        SELECT AVG(flight_price) AS average_price
          FROM Flight
         WHERE LOWER(TRIM(destination)) = LOWER(TRIM(%s))
           AND wifi = TRUE
    '''
    cur.execute(query, (destination,))
    result = cur.fetchone()
    
    if result and result[0]:
        print(f"The average price of flights with WiFi to {destination} is: ${result[0]:.2f}")
    else:
        print(f"No flights with WiFi found to {destination}.")

# Example Usage
find_average_price("Italy")
