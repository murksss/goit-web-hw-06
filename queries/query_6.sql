SELECT s.student_name, g.group_name
FROM students s
JOIN groups g ON s.fk_group_id = g.pk_id
WHERE g.pk_id = 3
ORDER BY s.student_name;