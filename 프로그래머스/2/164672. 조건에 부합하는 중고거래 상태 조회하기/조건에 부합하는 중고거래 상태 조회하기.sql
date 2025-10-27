-- 코드를 입력하세요
# 게시글 ID, 작성자 ID, 게시글 제목, 가격, 거래상태 조회
select BOARD_ID, WRITER_ID, TITLE, PRICE,
case when status = 'sale' then '판매중'
when status  = 'reserved' then '예약중'
when status = 'done' then '거래완료'
end as STATUS
from USED_GOODS_BOARD
where CREATED_DATE = '2022-10-05'
order by board_id desc;
