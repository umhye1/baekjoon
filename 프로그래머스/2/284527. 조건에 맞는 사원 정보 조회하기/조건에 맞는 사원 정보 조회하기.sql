# HR_DEPARTMENT, HR_EMPLOYEES, HR_GRADE 테이블에서 2022년도 한해 평가 점수가 가장 높은 사원 정보를 조회하려 합니다. 2022년도 평가 점수가 가장 높은 사원들의 점수, 사번, 성명, 직책, 이메일을 조회하는 SQL문을 작성해주세요.
# -> 사원별 총점. group by. sum 이용  -> group by!
# 2022년도의 평가 점수는 상,하반기 점수의 합을 의미하고, 평가 점수를 나타내는 컬럼의 이름은 SCORE로 해주세요.

select sum(g.SCORE) as SCORE, g.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL
from hr_grade g
join hr_employees e on g.emp_no = e.emp_no
where g.year = 2022
group by g.emp_no, e.emp_name, e.position, e.email
having sum(g.score) = (
    select max(total_score)
    from (select sum(score) as total_score
         from hr_grade
         where year = 2022
         group by emp_no
         ) as subq)
order by score desc;