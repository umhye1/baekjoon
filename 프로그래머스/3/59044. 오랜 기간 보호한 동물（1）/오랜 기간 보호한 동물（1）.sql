-- 코드를 입력하세요
SELECT i.NAME,	i.DATETIME
from animal_ins i
left join animal_outs o on o.animal_id = i.animal_id
where o.datetime is null
order by i.datetime asc
limit 3;

