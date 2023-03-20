-- This script prepares SQL server for
-- + the airbnb project

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY hbnb_dev_pwd;
GRANT ALL PRIVILEGES ON hbnb_dev_db TO hbnb_dev;
GRANT SELECT On performance_schema TO 'hbnb_dev'@'localhost';
