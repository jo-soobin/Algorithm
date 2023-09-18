-- 코드를 입력하세요
SELECT A.name, A.datetime
from animal_ins as A
left join animal_outs as B
on a.animal_id = b.animal_id
where b.animal_id is null
order by a.datetime 
limit 3