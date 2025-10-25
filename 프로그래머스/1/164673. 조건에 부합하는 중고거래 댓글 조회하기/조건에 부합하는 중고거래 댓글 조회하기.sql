-- 코드를 입력하세요
select b.title, b.board_id, r.reply_id, r.writer_id, r.contents, date_format(r.created_date,'%Y-%m-%d')
#게시글 제목, 게시글 ID, 댓글 ID, 댓글 작성자 ID, 댓글 내용, 댓글 작성일
from used_goods_board as b, used_goods_reply as r
where b.board_id = r.board_id and year(b.created_date) = 2022 and month(b.created_date) = 10
order by r.created_date asc, b.title asc;