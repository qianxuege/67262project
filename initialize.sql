-- drop the trax database if it exists
DROP database if EXISTS project;

-- create it afresh
CREATE database project;
\c project

\i create.SQL

-- load the data

\copy Hotel(hotel_id, hotel_name, location, pool, rating, cheapest_nightly_rate) FROM data/hotel.csv csv header;
\copy Room(room_number, hotel_id, room_capacity, nightly_rate, available) FROM data/room.csv csv header;

