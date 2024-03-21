-- Prepares a MySQL server for the project (testing environment)

-- Create the database named 'hbnb_test_db' if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user 'hbnb_test'@'localhost' if it doesn't already exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';

-- Set the password for the user 'hbnb_test'@'localhost' to 'hbnb_test_pwd'
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';

-- Grant the 'hbnb_test'@'localhost' user all privileges on the hbnb_test_db database
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- Grant the 'hbnb_test'@'localhost' user the SELECT privilege on the performance_schema database
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';

-- Flush privileges to ensure immediate effect of changes
FLUSH PRIVILEGES;
