-- drop the trax database if it exists
DROP database if EXISTS project;

-- create it afresh
CREATE database project;
\c project

\i create.SQL

-- load the data

\copy Hotel(hotel_id, hotel_name, location, pool, rating, cheapest_nightly_rate) FROM data/hotel.csv csv header;
\copy Room(room_number, hotel_id, room_capacity, nightly_rate, available) FROM data/room.csv csv header;


-- trigger 
CREATE FUNCTION fn_update_cheapest_nightly_rate ()
RETURNS trigger
LANGUAGE plpgsql AS 
$$
DECLARE
    min_rate numeric;
    old_min_rate numeric;
BEGIN
    SELECT MIN(r.nightly_rate)
      INTO min_rate
      FROM Hotel as h 
           JOIN Room as r ON h.hotel_id = r.hotel_id;
    
    IF EXISTS(SELECT 1 
                FROM Hotel as h
               WHERE h.hotel = new.hotel_id)
    THEN 
        IF 
    
END
$$;



