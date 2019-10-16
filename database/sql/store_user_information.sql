CREATE DATABASE IF NOT EXISTS accounts_info;

USE accounts_info;

DROP TABLE IF EXISTS accounts;

CREATE TABLE accounts(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(30) NOT NULL UNIQUE,
    password VARCHAR(30) NOT NULL
);

-- INSERT INTO accounts(username,password)
-- VALUES
-- ('test1','lalalala'),
-- ('Ainul','123456'),
-- ('Jiankun','123456'),
-- ('Pengfei','123456'),
-- ('Yunyi','123456'),
-- ('Shanshan','123456'),
-- ('Nashita','123456'),
-- ('Lutong','123456')
-- ;




