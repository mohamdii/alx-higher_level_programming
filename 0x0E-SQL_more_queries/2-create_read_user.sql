-- User 2
CREATE DATABASE hbtn_0d_2 IF NOT EXISTS; 
CREATE USER IF NOT EXISTS user_0d_2 IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
TO user_0d_2
ON hbtn_0d_2@localhost;
