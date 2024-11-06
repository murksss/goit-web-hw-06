SELECT s.student_name, t.teacher_name, sub.subject_name
FROM students s
JOIN marks m ON m.fk_student_id = s.pk_id
JOIN subjects sub ON m.fk_subject_id = sub.pk_id
JOIN teachers t ON sub.fk_teacher_id = t.pk_id
WHERE s.pk_id = 2 AND t.pk_id = 4
GROUP BY sub.pk_id
ORDER BY sub.subject_name;