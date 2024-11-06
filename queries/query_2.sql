SELECT s.student_name, ROUND(AVG(m.mark), 2) AS avg_mark
FROM students s
JOIN marks m ON s.pk_id = m.fk_student_id
WHERE m.fk_subject_id = 1
GROUP BY s.pk_id
ORDER BY avg_mark DESC
LIMIT 1;