select b.category, sum(s.sales) as total_sales
from book_sales s
join book b on s.book_id = b.book_id
where s.sales_date between '2022-01-01' and '2022-01-31'
group by b.category
order by b.category asc;