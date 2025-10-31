-- 인라인 뷰(서브쿼리)를 사용한 조인 방식
SELECT r.FOOD_TYPE, r.REST_ID, r.REST_NAME, r.FAVORITES
from rest_info r
inner join(  # 그룹시 집계함수 한곳에만 쓰이면 랜덤하게 그룹됨.? 하튼 그러니까 서브쿼리로 빼와야함.
    # 먼저 그룹하고 -> select를 바깥 쿼리에서함
    select food_type, max(favorites) as max_favorites
    from rest_info
    group by food_type
) as max_fav on r.food_type = max_fav.food_type
            and r.favorites= max_fav.max_favorites
order by r.food_type desc;