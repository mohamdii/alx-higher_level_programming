-- REFERENCE Key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use this data base
USE hbtn_0d_usa;
-- create table with foreign key
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL,
name VARCHAR(256),
state_id INT NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (state_id) REFERENCES hbstates(id)
);