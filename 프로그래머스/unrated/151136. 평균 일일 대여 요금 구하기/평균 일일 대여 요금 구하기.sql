-- 코드를 입력하세요
SELECT ROUND(avg(DAILY_FEE),0) AS AVERAGE_FEE
From CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE='SUV'