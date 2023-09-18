-- 코드를 입력하세요
SELECT a.animal_id, a.name
from animal_ins A
JOIN animal_outs B
ON A.ANIMAL_ID = B.ANIMAL_ID
where a.animal_id = b.animal_id and a.datetime >= b.datetime
order by a.datetime asc