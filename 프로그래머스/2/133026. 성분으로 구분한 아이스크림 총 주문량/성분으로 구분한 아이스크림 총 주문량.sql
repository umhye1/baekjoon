# -- 코드를 입력하세요
# 상반기 동안 각 아이스크림 성분 타입과 성분 타입에 대한 아이스크림의 총주문량을 총주문량이 작은 순서대로 조회하는 SQL 문을 작성해주세요. 이때 총주문량을 나타내는 컬럼명은 TOTAL_ORDER로 지정해주세요.
select i.INGREDIENT_TYPE, sum(f.TOTAL_ORDER) as TOTAL_ORDER
from first_half f
join icecream_info i on i.flavor = f.flavor
group by i.INGREDIENT_TYPE
order by f.TOTAL_ORDER asc;
