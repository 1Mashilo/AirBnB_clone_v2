-- Prepares a MySQL server for the project by creating a database and user

-- Create the database named 'hbnb_dev_db' if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user 'hbnb_dev'@'localhost' if it doesn't already exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';

-- Set the password for the user 'hbnb_dev'@'localhost' to 'hbnb_dev_pwd'
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';

-- Grant the 'hbnb_dev'@'localhost' user the SELECT privilege on the performance_schema database
GRANT SELECT ON performance_schema . * TO 'hbnb_dev'@'localhost';

-- Grant the 'hbnb_dev'@'localhost' user all privileges on the hbnb_dev_db database
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';

-- Flush privileges to ensure immediate effect of changes
FLUSH PRIVILEGES;
