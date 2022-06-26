select
	name,
	name n,
	name as n,
	sample_table.name,
	sample_table.name q,
	sample_table.name as q,
	'ww',
	'ww' w,
	'ww' as w,
	sample_table_a.*
from
	sample_table
join
	sample_table_a
on 
	sample_table.a = sample_table_a.a
inner join
	sample_table_b
on 
	sample_table.b = sample_table_b.b
right join
	sample_table_c
on 
	sample_table.c = sample_table_c.c
right outer join
	sample_table_d
on 
	sample_table.d = sample_table_d.d
left join
	sample_table_e
on 
	sample_table.e = sample_table_e.e
left outer join
	sample_table_f
on 
	sample_table.f = sample_table_f.f
outer join
	sample_table_g
on 
	sample_table.g = sample_table_g.g
full outer join
	sample_table_h
on 
	sample_table.h = sample_table_h.h
cross join
	sample_table_i
on 
	sample_table.i = sample_table_i.i
where
	sample_table.name in ('name', 'namae')
and
	sample_table.gender = 'mae'
and
	sample_table.age > 20
or
	sample_table.age >= 20
or
	sample_table.age = 20
or
	sample_table.age <= 20
or
	sample_table.age < 20