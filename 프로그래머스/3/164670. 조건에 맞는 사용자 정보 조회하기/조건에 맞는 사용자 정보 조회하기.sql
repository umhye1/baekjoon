# USED_GOODS_BOARD와 USED_GOODS_USER 테이블에서 
# 중고 거래 게시물을 3건 이상 등록한 사용자의 
# 사용자 ID, 닉네임, 전체주소, 전화번호를 조회
# 이때, 전체 주소는 시, 도로명 주소, 상세 주소가 함께 출력, 
# 전화번호의 경우 xxx-xxxx-xxxx 같은 형태로 하이픈 문자열(-)을 삽입하여 출력
# 결과는 회원 ID를 기준으로 내림차순 정렬해주세요

select u.USER_ID,u.NICKNAME, concat(u.city, ' ', u.street_address1, ' ', u.street_address2) as 전체주소, CONCAT(SUBSTR(u.tlno, 1, 3), '-', SUBSTR(u.tlno, 4, 4), '-', SUBSTR(u.tlno, 8, 4)) as 전화번호
from USED_GOODS_USER u
join USED_GOODS_BOARD b on u.user_id = b.WRITER_ID	
group by u.user_id,u.nickname,전체주소, 전화번호
having count(b.board_id)>=3
order by u.user_id desc;