-- CREATE USER CALLED HBTN_DEV IF EXISTS
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- grant select privileges to hbtn_dev on the db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost'; 