-- drop the trax database if it exists
DROP database if EXISTS project;

-- create it afresh
CREATE database project;
\c project

CREATE TYPE Room_Type AS ENUM('customer', 'developer', 'manager');

\i create.SQL

-- load the data

\copy Hotel(hotel_id, location, pool, rating, cheapest_nightly_rate) FROM data/hotel.csv csv header;

