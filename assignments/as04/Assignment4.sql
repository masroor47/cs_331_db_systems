


/* chapter 3, slide 17: List all Comp Sci instructors */
SELECT name
FROM instructor
WHERE dept_name = 'Comp. Sci.';


/* chapter 3, slide 17: List all the good Comp Sci instructors */
SELECT name
FROM instructor
WHERE dept_name = 'Comp. Sci.' AND salary > 70000;


/* chapter 3, slide 19: Find the names of all instructors who have taught some course AND the course_id */
SELECT name, course_id
FROM instructor, teaches
WHERE instructor.ID = teaches.ID;


/* chapter 3, slide 19: Find the names of all instructors in the Art department who have taught some course AND the course_id */
SELECT name, course_id
FROM instructor , teaches
WHERE instructor.ID = teaches.ID  
          AND  instructor. dept_name = 'Art';


/* chapter 3, slide 25: Find the names of all instructors with salary between $90,000 AND $100,000*/
SELECT name
FROM instructor
WHERE salary between 90000 AND 100000;


/* chapter 3, slide 26: Find courses that ran in Fall 2017 or in Spring 2018*/
(SELECT course_id  FROM section WHERE semester = 'Fall' AND year = 2017)
UNION
(SELECT course_id  FROM section WHERE semester = 'Spring' AND year = 2018);

/* chapter 3, slide 31: Find the average salary of instructors in the Computer Science department */
SELECT avg(salary)
FROM instructor
WHERE dept_name = 'Comp. Sci.';


/* chapter 3, slide 52: List all departments along with the number of instructors in each department */
SELECT dept_name,
        ( SELECT count(*)
          FROM instructor
          WHERE department.dept_name = instructor.dept_name)
          AS num_instructors
FROM department;

/* chapter 3, slide 32: Find the average salary of instructors in each department */
SELECT dept_name, avg (salary) AS avg_salary
FROM instructor
GROUP BY dept_name;

/* chapter 3, slide 34: Find the names AND average salaries of all departments whose average salary is greater than 42000 */
SELECT dept_name, avg (salary) AS avg_salary
FROM instructor
GROUP BY dept_name
HAVING avg (salary) > 42000;


/* Homework query #1: Retrieve all courses that have the letters a, e, i in THAT order in their names */
SELECT course_id, title
FROM course
WHERE title LIKE '%a%e%i%';

/* Homework query #2: Retrieve all courses that have the letters a, e, i in ANY order in their names */
SELECT course_id, title
FROM course
WHERE title LIKE '%a%'
    AND title LIKE '%e%'
    AND title LIKE '%i%';

/* Homework query #3: Retrieve the names of all students who failed a course (grade of F) along with the name of the course that they failed. */
SELECT 
    student.name, course.title
FROM 
    student, takes, course
WHERE 
    student.id = takes.id
    AND takes.course_id = course.course_id 
    AND takes.grade = 'F';

/* Homework query #4: Retrieve the percentage of solid A grades compared to all courses, AND rename that column "Percent_A" */
SELECT 
    (num_solid_a / total_grades) * 100 AS Percent_A
FROM
    (SELECT 
        count(CASE WHEN grade = 'A' THEN 1 END) AS num_solid_a,
        count(grade) AS total_grades
    FROM 
        takes) AS subquery;

/* Homework query #5: Retrieve the names AND numbers of all courses that do not have prerequisites. */
SELECT
    course.title, course.course_id
FROM 
    course
WHERE course.course_id not in 
    (SELECT course_id
    FROM prereq);

/* Homework query #6: Retrieves the names of all students AND their advisors if they have one. */
SELECT
    s.name AS student_name,
    i.name AS advisor_name
FROM
    student s
LEFT JOIN
    advisor a ON s.id = a.s_ID
LEFT JOIN
    instructor i ON a.i_ID = i.ID