SELECT
    I2.ITEM_ID,
    I2.ITEM_NAME,
    I2.RARITY
FROM ITEM_INFO I1  -- 1. 부모 아이템 정보 (RARE 아이템)
JOIN ITEM_TREE T ON I1.ITEM_ID = T.PARENT_ITEM_ID -- 2. ITEM_TREE를 통해 다음 업그레이드
JOIN ITEM_INFO I2 ON T.ITEM_ID = I2.ITEM_ID -- 3. 자식 아이템의 상세 정보 조회
WHERE I1.RARITY = 'RARE' -- 조건: 희귀도가 'RARE'인 부모 아이템
ORDER BY I2.ITEM_ID DESC; -- 아이템 ID를 기준으로 내림차순 정렬