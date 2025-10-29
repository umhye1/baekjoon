-- 코드를 작성해주세요
select c.ID, c.GENOTYPE, p.genotype PARENT_GENOTYPE
from ECOLI_DATA c
join ECOLI_DATA p on p.id = c.parent_id
where (c.genotype & p.genotype) = p.genotype
order by c.id;
