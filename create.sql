-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2024-10-22 23:29:39.139

-- tables
-- Table: Bugs
CREATE TABLE Bugs (
    bid int  NOT NULL,
    severity Severity_Type  NOT NULL,
    CONSTRAINT Bugs_pk PRIMARY KEY (bid)
);

-- Table: Comments
CREATE TABLE Comments (
    cid int  NOT NULL,
    date timestamp  NOT NULL,
    comment text  NOT NULL,
    iid int  NOT NULL,
    uid int  NOT NULL,
    CONSTRAINT Comments_pk PRIMARY KEY (cid)
);

-- Table: Features
CREATE TABLE Features (
    fid int  NOT NULL,
    votes int  NOT NULL,
    CONSTRAINT Features_pk PRIMARY KEY (fid)
);

-- Table: Issues
CREATE TABLE Issues (
    iid int  NOT NULL,
    initial_date timestamp  NOT NULL,
    product text  NOT NULL,
    status Status_Type  NOT NULL,
    priority int  NOT NULL,
    uid int  NOT NULL,
    message text  NOT NULL,
    CONSTRAINT Issues_pk PRIMARY KEY (iid)
);

-- Table: Users
CREATE TABLE Users (
    uid int  NOT NULL,
    name text  NOT NULL,
    role User_Type  NOT NULL,
    CONSTRAINT Users_pk PRIMARY KEY (uid)
);

-- foreign keys
-- Reference: Bugs_Issues (table: Bugs)
ALTER TABLE Bugs ADD CONSTRAINT Bugs_Issues
    FOREIGN KEY (bid)
    REFERENCES Issues (iid)  
    ON UPDATE RESTRICT
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Comments_Issues (table: Comments)
ALTER TABLE Comments ADD CONSTRAINT Comments_Issues
    FOREIGN KEY (iid)
    REFERENCES Issues (iid)  
    ON UPDATE RESTRICT
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Comments_Users (table: Comments)
ALTER TABLE Comments ADD CONSTRAINT Comments_Users
    FOREIGN KEY (uid)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Features_Issues (table: Features)
ALTER TABLE Features ADD CONSTRAINT Features_Issues
    FOREIGN KEY (fid)
    REFERENCES Issues (iid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Issues_Users (table: Issues)
ALTER TABLE Issues ADD CONSTRAINT Issues_Users
    FOREIGN KEY (uid)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

