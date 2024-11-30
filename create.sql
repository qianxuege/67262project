-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2024-11-30 16:56:48.022

-- tables
-- Table: Aircraft
CREATE TABLE Aircraft (
    model_type text  NOT NULL,
    date_made timestamp  NOT NULL,
    seating_capacity int  NOT NULL,
    wifi boolean  NOT NULL,
    CONSTRAINT Aircraft_pk PRIMARY KEY (model_type,date_made,seating_capacity,wifi)
);

-- Table: Flight
CREATE TABLE Flight (
    flight_id int  NOT NULL,
    destination text  NOT NULL,
    flight_price int  NOT NULL,
    departure_time timestamp  NOT NULL,
    arrival_time timestamp  NOT NULL,
    occupancy int  NOT NULL,
    model_type text  NOT NULL,
    date_made timestamp  NOT NULL,
    seating_capacity int  NOT NULL,
    wifi boolean  NOT NULL,
    CONSTRAINT Flight_pk PRIMARY KEY (flight_id)
);

-- Table: Guest_Traveler
CREATE TABLE Guest_Traveler (
    user_id int  NOT NULL,
    login_ip_address text  NOT NULL,
    login_timestamp timestamp  NOT NULL,
    CONSTRAINT Guest_Traveler_pk PRIMARY KEY (user_id)
);

-- Table: Hotel
CREATE TABLE Hotel (
    hotel_id int  NOT NULL,
    hotel_name text  NOT NULL,
    location text  NOT NULL,
    pool boolean  NOT NULL,
    rating text  NOT NULL,
    cheapest_nightly_rate text  NOT NULL,
    total_rooms int  NOT NULL,
    CONSTRAINT Hotel_pk PRIMARY KEY (hotel_id)
);

-- Table: Registered_Traveler
CREATE TABLE Registered_Traveler (
    user_id int  NOT NULL,
    name text  NOT NULL,
    email text  NOT NULL,
    CONSTRAINT Registered_Traveler_pk PRIMARY KEY (user_id)
);

-- Table: Room
CREATE TABLE Room (
    room_number int  NOT NULL,
    hotel_id int  NOT NULL,
    room_capacity int  NOT NULL,
    nightly_rate int  NOT NULL,
    room_available boolean  NOT NULL,
    CONSTRAINT Room_pk PRIMARY KEY (room_number,hotel_id)
);

-- Table: Selected_Flight
CREATE TABLE Selected_Flight (
    user_id int  NOT NULL,
    flight_id int  NOT NULL,
    CONSTRAINT Selected_Flight_pk PRIMARY KEY (user_id,flight_id)
);

-- Table: Selected_Hotel
CREATE TABLE Selected_Hotel (
    user_id int  NOT NULL,
    hotel_id int  NOT NULL,
    CONSTRAINT Selected_Hotel_pk PRIMARY KEY (user_id,hotel_id)
);

-- Table: Traveler
CREATE TABLE Traveler (
    user_id int  NOT NULL,
    CONSTRAINT Traveler_pk PRIMARY KEY (user_id)
);

-- foreign keys
-- Reference: Flight_Aircraft (table: Flight)
ALTER TABLE Flight ADD CONSTRAINT Flight_Aircraft
    FOREIGN KEY (model_type, date_made, seating_capacity, wifi)
    REFERENCES Aircraft (model_type, date_made, seating_capacity, wifi)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Guest_Traveler_Traveler (table: Guest_Traveler)
ALTER TABLE Guest_Traveler ADD CONSTRAINT Guest_Traveler_Traveler
    FOREIGN KEY (user_id)
    REFERENCES Traveler (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Registered_Traveler_Traveler (table: Registered_Traveler)
ALTER TABLE Registered_Traveler ADD CONSTRAINT Registered_Traveler_Traveler
    FOREIGN KEY (user_id)
    REFERENCES Traveler (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Room_Hotel (table: Room)
ALTER TABLE Room ADD CONSTRAINT Room_Hotel
    FOREIGN KEY (hotel_id)
    REFERENCES Hotel (hotel_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Selected_Flight_Flight (table: Selected_Flight)
ALTER TABLE Selected_Flight ADD CONSTRAINT Selected_Flight_Flight
    FOREIGN KEY (flight_id)
    REFERENCES Flight (flight_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Selected_Flight_Traveler (table: Selected_Flight)
ALTER TABLE Selected_Flight ADD CONSTRAINT Selected_Flight_Traveler
    FOREIGN KEY (user_id)
    REFERENCES Traveler (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Selected_Hotel_Hotel (table: Selected_Hotel)
ALTER TABLE Selected_Hotel ADD CONSTRAINT Selected_Hotel_Hotel
    FOREIGN KEY (hotel_id)
    REFERENCES Hotel (hotel_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Selected_Hotel_Traveler (table: Selected_Hotel)
ALTER TABLE Selected_Hotel ADD CONSTRAINT Selected_Hotel_Traveler
    FOREIGN KEY (user_id)
    REFERENCES Traveler (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

