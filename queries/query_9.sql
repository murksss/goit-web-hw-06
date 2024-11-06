SELECT s.student_name, sub.subject_name
FROM students s
JOIN marks m ON m.fk_student_id = s.pk_id
JOIN subjects sub ON m.fk_subject_id = sub.pk_id
WHERE s.pk_id = 2
GROUP BY sub.pk_id
ORDER BY sub.subject_name;