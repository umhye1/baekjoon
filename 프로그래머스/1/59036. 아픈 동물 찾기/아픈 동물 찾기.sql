-- 코드를 입력하세요
# select animal_id, name
# from animal_ins
# where intake_condition in sick;
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'SICK';