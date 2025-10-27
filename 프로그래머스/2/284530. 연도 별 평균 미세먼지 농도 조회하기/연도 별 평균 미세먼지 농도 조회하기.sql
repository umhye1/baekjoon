-- 코드를 작성해주세요
select year(ym) as YEAR, round(avg(pm_val1),2) as PM10, round(avg(pm_val2),2) as 'PM2.5'
from air_pollution
where location2 like '%수원%'
group by year(ym) #수원 지역의 연도 별 평균 미세먼지 오염도와 평균 초미세먼지 오염도
order by year(ym) asc;

