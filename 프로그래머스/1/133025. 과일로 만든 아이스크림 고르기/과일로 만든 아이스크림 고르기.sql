-- 코드를 입력하세요
select icecream_info.flavor
from icecream_info, first_half
where icecream_info.flavor = first_half.flavor and icecream_info.ingredient_type ='fruit_based' and first_half.total_order>3000;