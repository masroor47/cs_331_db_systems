
/* Assignment 7 [2a]: Create a new table shape2d with columns: shape_id, shape_name, perimeter_formula, area_formula */
DROP TABLE IF EXISTS math_shape2d;
CREATE TABLE math_shape2d(
    shape_id            INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    shape_name          VARCHAR(25), 
    perimeter_formula   VARCHAR(25), 
    area_formula        VARCHAR(25)
);

/* Assignment 7 [2b]: Insert two rows into the shape3d table, at least one of which should involve π. */

INSERT INTO math_shape2d (shape_name, perimeter_formula, area_formula)
VALUES ('triangle', 's1+s2+s3', 'b*h*0.5');

INSERT INTO math_shape2d (shape_name, perimeter_formula, area_formula)
VALUES ('rectangle', '2*w+2*h', 'w*h');

/* Assignment 7 select from math_shape2d  */
SELECT * FROM math_shape2d;


/* Assignment 7 [3a]: Create a new table shape3d with columns: shape_id, shape_name, area_formula, volume_formula */
DROP TABLE IF EXISTS math_shape3d;
CREATE TABLE math_shape3d(
    shape_id            INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    shape_name          VARCHAR(25), 
    area_formula        VARCHAR(25), 
    volume_formula      VARCHAR(25)
);

/* Assignment 7 [3b]: Insert two rows into the shape3d table, at least one of which should involve π. */

INSERT INTO math_shape3d (shape_name, area_formula, volume_formula)
VALUES ('cube', '6 * s^2', 's^3');

INSERT INTO math_shape3d (shape_name, area_formula, volume_formula)
VALUES ('sphere', '4*pi*r^2', '(4/3)*pi*r^3');

/* Assignment 7 math_shape3d  */
SELECT * FROM math_shape3d;

DROP FUNCTION IF EXISTS area_circle;
/* Assignment 7 [4a]: Create a MySQL function area_circle(radius) that computes the area of a circle of given radius */
CREATE FUNCTION area_circle(radius INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    SET @area = 3.14 * radius * radius##
    RETURN @area##
END;

/* testing function area_circle */
SELECT area_circle(2) from dual;


DROP FUNCTION IF EXISTS volume_sphere;
/* Assignment 7 Task [4b]: Create a MySQL function volume_sphere(radius) that computes the volume of a sphere of given radius */
CREATE FUNCTION volume_sphere(radius INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    SET @volume = (4/3) * 3.14 * radius * radius * radius##
    RETURN @volume##
END;

/* Assignment 7 testing function volume_sphere */
SELECT volume_sphere(2) from dual;


DROP TABLE IF EXISTS math_circle;
/* Assignment 7 [5a] Create a table circle with columns circle_id, total_points, circle_points, pi_estimate */
CREATE TABLE math_circle(
    circle_id            INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    total_points         INT, 
    circle_points        INT, 
    pi_estimate          FLOAT
);
SELECT * FROM math_circle;

DROP TABLE IF EXISTS math_point;
/* Assignment 7 [5b] Create a table point with columns point_id, circle_id, x, y. */
CREATE TABLE math_point(
    point_id            INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    circle_id           INT, 
    x                   FLOAT, 
    y                   FLOAT
);
SELECT * FROM math_point;

DROP PROCEDURE IF EXISTS generate_points;
/* Assignment 7 [5c/d] Create a stored procedure random_points(n) that generates n random points (x, y) where both x and y are in the interval (-1, 1) */
CREATE PROCEDURE generate_points(num_points INT, circle_id INT)
BEGIN
SET @n = 0##
find_points: LOOP
IF @n > num_points THEN LEAVE find_points##
END IF##
SET @x=2*rand()-1##
SET @y=2*rand()-1##
INSERT INTO math_point(circle_id, x, y) VALUES(circle_id, @x, @y)##
SET @n = @n + 1##
END LOOP find_points##
END;

DROP FUNCTION IF EXISTS estimate_pi;
/* Assignment 7 [6] create a function estimate_pi() */
CREATE FUNCTION estimate_pi(c_id INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
SET @tot_points = (SELECT COUNT(*) FROM math_point WHERE circle_id=c_id)##
SET @circle_points = (SELECT COUNT(*) FROM math_point WHERE circle_id=c_id AND
power(x, 2)+power(y,2) <= power(1, 2))##
SET @pi = 4 * @circle_points / @tot_points##
RETURN @pi##
END;

DROP PROCEDURE IF EXISTS run_test;
/* Assignment 7 [7] create procedure run test */
CREATE PROCEDURE run_test(n INT)
BEGIN
INSERT INTO math_circle(total_points) VALUES(n)##
SELECT @id := LAST_INSERT_ID()##
CALL generate_points(n, @id)##
SET @circle_points = (SELECT COUNT(*) FROM math_point WHERE circle_id=@id AND
power(x,2)+power(y,2) <= power(1,2))##
SELECT estimate_pi(@id)##
UPDATE math_circle SET circle_points = @circle_points, pi_estimate = @pi WHERE
circle_id=@id##
END;

/* Assignment 7 [8] run test for 100 points */
CALL run_test(100);
/* Assignment 7 [8] run test for 1000 points */
CALL run_test(1000);
/* Assignment 7 [8] run test for 10'000 points */
CALL run_test(10000);

/* Assignment 7 [9] find estimate of pi for different n */
SELECT * FROM math_circle;