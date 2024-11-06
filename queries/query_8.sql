SELECT t.teacher_name , s.subject_name , ROUND(AVG(m.mark), 2) as avg_mark
FROM marks m
JOIN subjects s on m.fk_subject_id = s.pk_id
JOIN teachers t on s.fk_teacher_id = t.pk_id
GROUP BY s.pk_id
ORDER BY t.teacher_name ;