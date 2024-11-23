-- drop the trax database if it exists
DROP database if EXISTS project;

-- create it afresh
CREATE database project;
\c project

\i create.SQL

-- load the data

\copy Hotel_Provider(provider_id, provider_name) FROM data/hotel_provider.csv csv header;
\copy Hotel(hotel_id, hotel_name, location, pool, rating, cheapest_nightly_rate) FROM data/hotel.csv csv header;
\copy Room(room_number, hotel_id, room_capacity, nightly_rate, available) FROM data/room.csv csv header;
\copy Provision(hotel_id, provider_id) FROM data/provision.csv csv header;

