-- 코드를 작성해주세요
select 
case when month(differentiation_date) >=1 and month(differentiation_date) <=3 
    then '1Q'
    when month(differentiation_date) >=4 and month(differentiation_date) <=6
    then '2Q'
    when month(differentiation_date) >=7 and month(differentiation_date) <=9
    then '3Q'
    when month(differentiation_date) >=10 and month(differentiation_date) <=12
    then '4Q'
    end as QUARTER,
count(*) as ECOLI_COUNT
from ECOLI_DATA
group by QUARTER
order by QUARTER asc;