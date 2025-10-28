-- 코드를 작성해주세요
select count(*) as FISH_COUNT
from FISH_INFO i
join FISH_NAME_INFO n on i.fish_type = n.fish_type
where n.fish_name in ('BASS','SNAPPER');