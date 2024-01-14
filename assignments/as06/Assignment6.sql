/* remove foreign key constraint from takes */
ALTER TABLE takes
DROP FOREIGN KEY takes_ibfk_3;

/* drop grade_points */
DROP TABLE IF EXISTS grade_points;
/* Assignment 6, [4] Create a table grade_points (grade, points) that maps letter grades to number grades.  */
CREATE TABLE grade_points(
    grade           VARCHAR(2) NOT NULL PRIMARY KEY,
    points          FLOAT,
    
    CONSTRAINT check_grade_in_range CHECK (points >= 0 and points <= 4)
);

/* Assignment 6, filling up the grade_point map */
INSERT INTO grade_points 
VALUES
('A', 4.0),
('A-', 3.7),
('B+', 3.3),
('B' , 3.0),
('B-', 2.7),
('C+', 2.3),
('C' , 2.0),
('C-', 1.7),
('D+', 1.3),
('D' , 1.0),
('D-', 0.7),
('F+', 0.3),
('F' , 0.0);


/* Check out grade_points*/
SELECT * FROM grade_points;

/* Assignment 6, [5] Add a foreign key from the grade column in the existing takes table to the new grade_points . */

ALTER TABLE takes
ADD FOREIGN KEY(grade) REFERENCES grade_points(grade);

/* Assignment 6, [6] */
CREATE OR REPLACE VIEW v_takes_points AS
SELECT takes.*, points
FROM takes
JOIN grade_points
ON takes.grade = grade_points.grade;

/* Assignment 6, checking out the v_takes_points view */
SELECT * FROM v_takes_points;

/* Assignment 6, [7] Compute the total number of grade points (credits * grade points) earned by student X 
You will need to join takes, course, and the new grade_points tables. 
If the student is in the system, but hasn't taken any courses, the student's total points is 0. 
Random Student's ID: 12345
*/

SELECT 
    COALESCE(ID, 12345) as random_students_id, 
    COALESCE(sum(course.credits * points), 0) as total_points
FROM
    takes
RIGHT JOIN
    course ON takes.course_id = course.course_id
RIGHT JOIN 
    grade_points ON takes.grade = grade_points.grade
WHERE ID = 12345;


/* Assignment 6 [8] Compute the GPA - i.e. total grade points / total credits - for the same student in the previous question.*/

SELECT
    random_students_id,
    ROUND(total_points / total_credits, 2) as GPA
FROM 
    (
        SELECT 
            COALESCE(takes.ID, 12345) AS random_students_id, 
            COALESCE(sum(course.credits * points), 0) AS total_points,
            COALESCE(sum(course.credits), 0) AS total_credits
        FROM
            student
        JOIN
            takes ON student.ID = takes.ID
        RIGHT JOIN
            course ON takes.course_id = course.course_id
        RIGHT JOIN 
            grade_points ON takes.grade = grade_points.grade
        WHERE student.ID = 12345
    ) AS pts;


/* Assignment 6 [9] Find the GPA of all students, i.e. not just for one student at a time. */
SELECT
    student_id,
    COALESCE(ROUND(total_points / total_credits, 2), 0.0) as GPA
FROM 
    (
        SELECT 
	        IFNULL (takes.id, student.id) as student_id, 
            COALESCE(sum(course.credits * points), 0) AS total_points,
            COALESCE(sum(course.credits), 0) AS total_credits
        FROM
            student
        LEFT JOIN
            takes ON student.ID = takes.ID
        LEFT JOIN
            course ON takes.course_id = course.course_id
        LEFT JOIN 
            grade_points ON takes.grade = grade_points.grade
        GROUP BY student.ID
        ORDER BY student_id
    ) AS pts;


/* Assignment 6 [10] Create a view v_student_gpa (id, gpa) that gives a dynamic version of the information in the previous question. */
CREATE OR REPLACE VIEW v_student_gpa AS 
    SELECT
        student_id,
        COALESCE(ROUND(total_points / total_credits, 2), 0.0) as GPA
    FROM 
        (
            SELECT 
                IFNULL (takes.id, student.id) as student_id, 
                COALESCE(sum(course.credits * points), 0) AS total_points,
                COALESCE(sum(course.credits), 0) AS total_credits
            FROM
                student
            LEFT JOIN
                takes ON student.ID = takes.ID
            LEFT JOIN
                course ON takes.course_id = course.course_id
            LEFT JOIN 
                grade_points ON takes.grade = grade_points.grade
            GROUP BY student.ID
            ORDER BY student_id
        ) AS pts;

/* Calling the view that shows students and their GPAs */
SELECT * FROM v_student_gpa;