-- drop the project database if it exists
DROP database if EXISTS project;

-- create it afresh
CREATE database project;
\c project

\i create.SQL

-- load the data
\copy Aircraft(model_type, date_made, seating_capacity, wifi) FROM data/aircraft.csv csv header;
-- \copy Flight(flight_id, destination, flight_price, departure_time, arrival_time, occupancy) FROM data/flight.csv csv header;
\copy Traveler(user_id) FROM data/traveler.csv csv header;
\copy Guest_Traveler(user_id, login_ip_address, login_timestamp) FROM data/guest_traveler.csv csv header;
-- \copy Hotel() FROM data/room.csv csv header;
\copy Hotel(hotel_id, hotel_name, location, pool, rating, cheapest_nightly_rate, total_rooms) FROM data/hotel.csv csv header;
\copy Room(room_number, hotel_id, room_capacity, nightly_rate, room_available) FROM data/room.csv csv header;

-- trigger 
-- DROP FUNCTION IF EXISTS fn_update_cheapest_nightly_rate() cascade;
CREATE FUNCTION fn_update_cheapest_nightly_rate()
RETURNS trigger
LANGUAGE plpgsql AS 
$$
DECLARE
    new_min_rate numeric;
    old_min_rate numeric;
BEGIN
    SELECT MIN(r.nightly_rate)
      INTO new_min_rate
      FROM Hotel as h 
           JOIN Room as r ON h.hotel_id = r.hotel_id;
    
    SELECT cheapest_nightly_rate FROM Hotel INTO old_min_rate;
    IF old_min_rate != new_min_rate THEN
        UPDATE Hotel
            SET cheapest_nightly_rate = new_min_rate
            WHERE hotel_id = new.hotel_id;
    END IF;

    return null;
    
    
END
$$;

-- DROP TRIGGER IF EXISTS tr_update_cheapest_nightly_rate ON Room;

CREATE TRIGGER tr_update_cheapest_nightly_rate
  -- TODO
    AFTER INSERT OR UPDATE ON Room
    FOR EACH ROW
    EXECUTE FUNCTION fn_update_cheapest_nightly_rate();





