-- MySQL setup development 
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION SLAVE ON *.* TO 'holberton_user'@'%' IDENTIFIED BY 'password';
