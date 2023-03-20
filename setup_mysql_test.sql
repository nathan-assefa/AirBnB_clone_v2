-- This script creates a new uset in a database

-- Creating a database if not exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creating a new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Granting all privileges on the database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Granting SELECT privileges on the database
GRANT SELECT ON performance_schema.* TO 'hbnb_testt'@'localhost';
