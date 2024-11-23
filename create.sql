-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2024-11-23 21:58:55.758

-- tables
-- Table: Hotel
CREATE TABLE Hotel (
    hotel_id int  NOT NULL,
    hotel_name text  NOT NULL,
    location text  NOT NULL,
    pool boolean  NOT NULL,
    rating text  NOT NULL,
    cheapest_nightly_rate text  NOT NULL,
    CONSTRAINT Hotel_pk PRIMARY KEY (hotel_id)
);

-- Table: Room
CREATE TABLE Room (
    room_number int  NOT NULL,
    room_capacity int  NOT NULL,
    nightly_rate int  NOT NULL,
    available boolean  NOT NULL,
    hotel_id int  NOT NULL,
    CONSTRAINT Room_pk PRIMARY KEY (room_number,hotel_id)
);

-- foreign keys
-- Reference: Room_Hotel (table: Room)
ALTER TABLE Room ADD CONSTRAINT Room_Hotel
    FOREIGN KEY (hotel_id)
    REFERENCES Hotel (hotel_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

