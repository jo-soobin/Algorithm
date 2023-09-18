-- 코드를 입력하세요
SELECT USER_ID
    , NICKNAME
    , SUM(PRICE) TOTAL_SALES
FROM USED_GOODS_USER A
JOIN USED_GOODS_BOARD B
ON A.USER_ID = B.WRITER_ID
WHERE B.STATUS = 'DONE'
GROUP BY WRITER_ID
HAVING SUM(PRICE) >= 700000
ORDER BY TOTAL_SALES