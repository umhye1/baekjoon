# CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블에서 
# 대여 시작일을 기준으로 
# 2022년 8월부터 2022년 10월까지 
# 총 대여 횟수가 5회 이상인 자동차들에 대해서 
# 해당 기간 동안의 월별 자동차 ID 별 총 대여 횟수(컬럼명: RECORDS) 리스트를 출력하는 SQL문을 작성
# 결과는 월을 기준으로 오름차순 정렬, 월이 같다면 자동차 ID를 기준으로 내림차순 정렬해주세요. 
# 특정 월의 총 대여 횟수가 0인 경우에는 결과에서 제외해주세요.

select month(start_date) as MONTH,CAR_ID, count(history_id) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY c1
where car_id in (
    select car_id
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where start_date between '2022-08-01' and '2022-10-31' 
    group by car_id
    having count(car_id) >= 5
) and start_date between '2022-08-01' and '2022-10-31' 
group by month(start_date),car_id
order by month(start_date) asc, car_id desc;



# SELECT month(start_date) as MONTH,CAR_ID, count(history_id) as RECORDS
# from CAR_RENTAL_COMPANY_RENTAL_HISTORY
# where start_date between '2022-08-01' and '2022-10-31' 
# group by month(start_date), car_id
# having count(car_id) >= 5 and count(car_id) = 0
# order by month(start_date) asc, car_id desc;
 