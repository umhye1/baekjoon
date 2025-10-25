-- 코드를 작성해주세요
# Python 스킬을 가진 개발자의 ID, 이메일, 이름, 성을 조회하는 SQL 문을 작성
select id, email, first_name, last_name
from developer_infos
where skill_1 = 'Python' or skill_2 = 'Python' or skill_3 = 'Python'
order by id;