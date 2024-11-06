SELECT sub.subject_name, g.group_name, s.student_name, m.mark
FROM marks m
JOIN students s on m.fk_student_id = s.pk_id
JOIN groups g on s.fk_group_id = g.pk_id
JOIN subjects sub on m.fk_subject_id = sub.pk_id
WHERE sub.pk_id = 2 and g.pk_id = 1
ORDER BY s.student_name;