SELECT sub.subject_name, ROUND(AVG(m.mark), 2) AS avg_mark
FROM marks m
JOIN subjects sub ON sub.pk_id = m.fk_subject_id
GROUP BY sub.pk_id
ORDER BY avg_mark DESC;
