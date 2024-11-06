SELECT t.teacher_name, sub.subject_name
FROM teachers t
JOIN subjects sub ON t.pk_id = sub.fk_teacher_id
ORDER BY t.teacher_name;