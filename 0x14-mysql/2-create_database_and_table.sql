-- CREATE database and table;
CREATE DATABASE IF NOT EXISTS tyrell_corp;
CREATE TABLE nexus6(id INT, name VARCHAR(256));
GRANT SELECT ON tyrell_ropt.nexus6 TO 'holberton_user'@'localhost';
INSERT INTO nexus6(id, name) VALUES (1, "Leon");
