SELECT * FROM (SELECT A.name, A.hour, A.timestamp, B.max_high FROM (SELECT name, high, timestamp, SUBSTRING(timestamp, 12, 2) AS hour  FROM "01" db) A
INNER JOIN (SELECT name, SUBSTRING(timestamp, 12, 2) AS hour, MAX(high) AS max_high FROM "01" GROUP BY name, SUBSTRING(timestamp, 12, 2)) B
ON A.name = B.name AND A.hour = B.hour AND A.high = B.max_high)
ORDER BY name, hour
