
CREATE TABLE movies IF NOT EXISTS(
    id INT NOT NULL PRIMARY KEY,
    title VARCHAR(30) NOT NULL,
    year_released INT
);


-- Create Student Table with foreign key references with Id as primary key
-- Create Student Table with foreign key references with Id as primary key


CREATE TABLE movie_returns(
    id INT NOT NULL PRIMARY KEY,
    theatre VARCHAR(30),
    movie_id INT,
    FOREIGN KEY (movie_id)
        REFERENCES movies (id),
    dollar_amount_made INT,
    num_tickets_sold INT
);

INSERT INTO `movies` VALUES
(1,'Annie Hall', 1977);
INSERT INTO `movies` VALUES
(2,'Fast Times at Ridgemont High', 1982);
INSERT INTO `movies` VALUES
(3,'The Warriors', 1979);

INSERT INTO `movie_returns` VALUES
(1,'19th Street', 3,500,50);

INSERT INTO `movie_returns` VALUES
(2,'19th Street', 2,699,64);

INSERT INTO `movie_returns` VALUES
(3,'34th Street', 3,800,70);

INSERT INTO `movie_returns` VALUES
(4,'42nd Street', 2,399,22);

SELECT theatre, num_tickets_sold, title FROM movie_returns JOIN movies ON movies.id=movie_returns.movie_id ORDER BY num_tickets_sold ASC;

SELECT theatre, num_tickets_sold, title FROM movie_returns JOIN movies ON movies.id=movie_returns.movie_id ORDER BY num_tickets_sold ASC;

SELECT title, SUM(dollar_amount_made) FROM movies JOIN movie_returns ON movies.id=movie_returns.movie_id GROUP BY movie_id ORDER BY year_released ASC;
