-- 코드를 입력하세요
select icecream_info.flavor
from icecream_info, first_half
where icecream_info.flavor = first_half.flavor and icecream_info.ingredient_type ='fruit_based' and first_half.total_order>3000;

# SELECT
#     A.flavor
# FROM
#     icecream_info A  -- A는 icecream_info의 별칭
# JOIN
#     first_half B     -- B는 first_half의 별칭
#     ON A.flavor = B.flavor  -- 조인 조건
# WHERE
#     A.ingredient_type = 'fruit_based'  -- icecream_info의 조건
#     AND B.total_order > 3000;          -- first_half의 조건