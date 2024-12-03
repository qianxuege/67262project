from common import *

us='''
* Simple US: Minimize Cost (US3)

   As a:  Student Traveler
 I want:  To find the cheapest three-day period to fly to Italy over spring break
So That:  I can save money as a student
'''

print(us)

# This function gets the flights with departure time between start and end,
# and finds the nday period with the lowest average flight_price.
def show_cheapest_period(start, end, nday, destination):
    assert(nday>0)
    res_col = 'departure_time avg_three_day_price'
    query = '''
      WITH filtered_flights AS (
        SELECT f.flight_id, f.destination, f.flight_price, 
               EXTRACT(DAY FROM f.departure_time) as departure_day,
               f.departure_time, f.arrival_time
          FROM Flight as f
        WHERE LOWER(TRIM(f.destination)) = LOWER(TRIM(%s)) and 
                f.departure_time BETWEEN %s AND %s
      ), 
      day_counts AS (
        SELECT t1.departure_time,
               COUNT(DISTINCT t2.departure_day) AS distinct_day_count
          FROM filtered_flights as t1
          JOIN filtered_flights as t2 
               ON t2.departure_time BETWEEN 
               t1.departure_time AND t1.departure_time + INTERVAL '%s days'
         GROUP BY t1.flight_id, t1.departure_time
      ),
      rolling_avg AS (
        SELECT t1.departure_time, ROUND(AVG(t1.flight_price) OVER w1, 2) as avg_three_day_price
          FROM filtered_flights as t1
        WINDOW w1 as (ORDER BY t1.departure_time
                     RANGE BETWEEN 
                     CURRENT ROW AND INTERVAL '%s days' FOLLOWING
                     )
      )
      
      SELECT r1.departure_time, r1.avg_three_day_price
        FROM rolling_avg AS r1
             JOIN day_counts AS d 
             ON r1.departure_time = d.departure_time
       WHERE d.distinct_day_count = %s and 
             r1.avg_three_day_price = (SELECT MIN(r2.avg_three_day_price) 
                                         FROM rolling_avg as r2)
       ORDER BY r1.departure_time;
    '''
    cur.execute(query, (destination, start, end, nday-1, nday-1, nday))
    rows = cur.fetchall()
    show_table( rows, cols = res_col )
    print(f"It is cheapest to travel to {destination} in the {nday}-day period starting on the departure_time")


show_cheapest_period('2025-03-03 00:00:00', '2025-03-10 23:59:59', 3, 'Italy')