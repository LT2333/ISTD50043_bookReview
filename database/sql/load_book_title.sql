DROP TABLE IF EXISTS book_titles;

CREATE TABLE book_titles(
    asin CHAR(10) NOT NULL,
    title text NOT NULL

);

load data local infile 'bookinfo.csv' 
into table book_titles
fields terminated by ',' 
enclosed by '"' 
escaped by '"' 
lines terminated by '\n'
ignore 1 lines;



ALTER TABLE reviews
ADD COLUMN title text
AFTER asin;


UPDATE reviews t1
INNER JOIN book_titles t2 ON t1.asin = t2.asin
SET t1.title = t2.title;


select idx,asin,title from reviews limit 40;