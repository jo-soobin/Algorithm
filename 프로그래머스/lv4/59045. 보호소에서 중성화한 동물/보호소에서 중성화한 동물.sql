-- 코드를 입력하세요
SELECT a.animal_id, a.animal_type, a.name
from animal_ins as a
join animal_outs as B on a.animal_id = b.animal_id 
where a.SEX_UPON_INTAKE != b.sex_upon_outcome
order by a.animal_id