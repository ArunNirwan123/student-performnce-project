create database Nirwan;
SELECT s.student_id, s.student_name, c.course_name FROM students__id s inner JOIN 
courses_name c ON s.course_id = c.course_id;

SELECT c.course_name, COUNT(s.student_id) AS student_count
FROM students__id s inner JOIN courses_name c ON s.course_id = c.course_id
GROUP BY c.course_name;

SELECT c.course_name, AVG((m.python_marks + m.sql_marks + m.powerbi_marks + m.numpy_marks + m.pandas_marks)/5)
AS avg_course_marks FROM marks m inner JOIN students__id s ON m.student_id = s.student_id 
inner JOIN courses_name c ON s.course_id = c.course_id GROUP BY c.course_name;

SELECT student_id, (python_marks + sql_marks + powerbi_marks + numpy_marks + pandas_marks)/5 AS avg_marks FROM marks
ORDER BY avg_marks DESC LIMIT 5; SELECT * FROM courses_name LIMIT 3; SELECT * FROM avg_total LIMIT 3; SELECT * FROM payment_status LIMIT 3;
SELECT * FROM total_attendance LIMIT 3;

SELECT * FROM total_attendance LIMIT 3; 
SELECT s.student_id, s.student_name, (t.attended_classes / t.total_classes * 100) AS attendance_percent FROM total_attendance t
JOIN students__id s ON t.student_id = s.student_id WHERE (t.attended_classes / t.total_classes * 100) < 75;

SELECT SUM(amount) AS total_collection FROM payment_status;

SELECT payment_mode, SUM(amount) AS total FROM payment_status
GROUP BY payment_mode;

SELECT s.student_id, s.student_name, p.amount, p.payment_mode  FROM students__id s
inner JOIN payment_status p ON s.student_id = p.student_id;

SELECT s.student_id, s.student_name, (m.python_marks + m.sql_marks + m.powerbi_marks + m.numpy_marks + m.pandas_marks)
/5 AS avg_marks FROM marks m inner JOIN students__id s ON m.student_id = s.student_id ORDER BY avg_marks DESC LIMIT 1;

SELECT c.course_name, AVG((m.python_marks + m.sql_marks + m.powerbi_marks + m.numpy_marks + m.pandas_marks)/5) 
AS course_avg_performance FROM marks m inner JOIN students__id s ON m.student_id = s.student_id
inner JOIN courses_name c ON s.course_id = c.course_id GROUP BY c.course_name ORDER BY course_avg_performance DESC;
