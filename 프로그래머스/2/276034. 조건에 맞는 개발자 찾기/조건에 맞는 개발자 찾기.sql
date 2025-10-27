select ID, EMAIL, FIRST_NAME, LAST_NAME
from developers
where (skill_code &(select sum(code)
                   from skillcodes
                   where name in('Python','C#')))
order by id asc;