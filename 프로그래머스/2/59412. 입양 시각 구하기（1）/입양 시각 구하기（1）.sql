-- 코드를 
# 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 
# 이때 결과는 시간대 순으로 정렬해야 합니다.

select hour(datetime)as HOUR, count(*) as COUNT
from animal_outs
where hour(datetime) >= 9 and  hour(datetime)<20 
group by hour(datetime)
order by hour(datetime);