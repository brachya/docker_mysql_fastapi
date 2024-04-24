/*
  Name: MySQL Sample Database classicmodels
  Link: http://www.mysqltutorial.org/mysql-sample-database.aspx
*/


CREATE USER 'brachya'@'%' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON *.* TO 'brachya'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
/* Create the database */
CREATE DATABASE  IF NOT EXISTS logs_db;

/* Switch to the logs_db database */
USE logs_db;

/* Drop existing tables  */
DROP TABLE IF EXISTS logs;

CREATE TABLE logs(
  log_id INT UNSIGNED AUTO_INCREMENT,
  log_msg VARCHAR(50),
  PRIMARY KEY(log_id)
);
