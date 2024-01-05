/* chapter 3, slide 52: List all departments along with the number of instructors in each department */

select dept_name,
        ( selct count(*)
          from instructor
          where department.dept_name = instructor.dept_name)
          as num_instructors
from department;