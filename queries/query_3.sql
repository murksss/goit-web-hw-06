SELECT g.group_name, sub.subject_name, ROUND(AVG(m.mark), 2) as avg_mark
FROM groups g
JOIN students s ON g.pk_id = s.fk_group_id
JOIN marks m  ON s.pk_id = m.fk_student_id
JOIN subjects sub ON m.fk_subject_id = sub.pk_id
WHERE sub.pk_id = 3
GROUP BY g.pk_id, sub.pk_id
ORDER BY avg_mark DESC;