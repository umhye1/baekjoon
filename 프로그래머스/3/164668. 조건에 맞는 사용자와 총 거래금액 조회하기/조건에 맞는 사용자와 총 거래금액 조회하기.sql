# USED_GOODS_BOARD와 USED_GOODS_USER 테이블에서 
# 완료된 중고 거래의 총금액이 70만 원 이상인 사람의 
# 회원 ID, 닉네임, 총거래금액을 조회
# 결과는 총거래금액을 기준으로 오름차순 정렬해주세요.

select u.USER_ID, u.NICKNAME, sum(b.price) as TOTAL_SALES
from USED_GOODS_USER u
join used_goods_board b on u.user_id = b.writer_id
where b.status = 'DONE'
group by u.user_id, u.nickname
having sum(b.price) >= 700000
order by TOTAL_SALES asc ;


# select u.USER_ID, u.NICKNAME, (
#     select sum(b.price) as total_price
#     from used_goods_board b
#     group by total_price
#     having total_price >= 70)
# from USED_GOODS_USER u, used_goods_board b
# where u.user_id in(
#     select b.writer_id
#     from USED_GOODS_BOARD b
#     where b.status = 'DONE'
# ) 
# order by TOTAL_S;

