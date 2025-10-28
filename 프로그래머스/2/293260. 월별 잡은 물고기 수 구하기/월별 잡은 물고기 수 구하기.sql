# -- 코드를 작성해주세요
# select count(*) as FISH_COUNT, date_format(TIME,'%c') as MONTH
# from fish_info
# group by date_format(TIME,'%c')
# order by cast(date_format(TIME,'%c') as unsigned) asc;
select count(*) as FISH_COUNT, month(TIME) as MONTH
from fish_info
group by month(TIME)
order by month(TIME) asc;