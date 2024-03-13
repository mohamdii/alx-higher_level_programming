-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create user 2
CREATE USER IF NOT EXISTS user_0d_2 IDENTIFIED BY 'user_0d_2_pwd';
-- grant select
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2_pwd@localhost;
