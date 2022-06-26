SELECT
	name,
	name n,
	name AS n,
	sample_table.name,
	sample_table.name q,
	sample_table.name AS q,
	'ww',
	'ww' w,
	'ww' AS w,
	sample_table_a.*
FROM
	sample_table
JOIN
	sample_table_a
ON 
	sample_table.a = sample_table_a.a
INNER JOIN
	sample_table_b
ON 
	sample_table.b = sample_table_b.b
RIGHT JOIN
	sample_table_c
ON 
	sample_table.c = sample_table_c.c
RIGHT OUTER JOIN
	sample_table_d
ON 
	sample_table.d = sample_table_d.d
LEFT JOIN
	sample_table_e
ON 
	sample_table.e = sample_table_e.e
LEFT OUTER JOIN
	sample_table_f
ON 
	sample_table.f = sample_table_f.f
OUTER JOIN
	sample_table_g
ON 
	sample_table.g = sample_table_g.g
FULL OUTER JOIN
	sample_table_h
ON 
	sample_table.h = sample_table_h.h
CROSS JOIN
	sample_table_i
ON 
	sample_table.i = sample_table_i.i
WHERE
	sample_table.name IN ('name', 'namae')
AND
	sample_table.gender = 'mae'
AND
	sample_table.age > 20
OR
	sample_table.age >= 20
OR
	sample_table.age = 20
OR
	sample_table.age <= 20
OR
	sample_table.age < 20