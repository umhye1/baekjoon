# -- 코드를 입력하세요
# APPOINTMENT 테이블에서 2022년 5월에 예약한 환자 수를 진료과코드 별로 조회하는 SQL문을 작성해주세요. 이때, 컬럼명은 '진료과 코드', '5월예약건수'로 지정해주시고 결과는 진료과별 예약한 환자 수를 기준으로 오름차순 정렬하고, 예약한 환자 수가 같다면 진료과 코드를 기준으로 오름차순 정렬해주세요.

select mcdp_cd as '진료과코드', count(apnt_no) as '5월예약건수'
from appointment
where year(apnt_ymd) = 2022 and month(apnt_ymd) = 5
group by mcdp_cd
order by count(apnt_no) asc, mcdp_cd asc;