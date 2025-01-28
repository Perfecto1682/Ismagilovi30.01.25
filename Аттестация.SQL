Задание №1
SELECT DISTINCT R.name AS region_name
FROM Regions R
JOIN Mushrooms M ON R.region_id = M.primary_region_id;

Задание №2
SELECT M.name AS mushroom_name, M.season, M.edible
FROM Mushrooms M
JOIN Categories C ON M.category_id = C.category_id
WHERE C.name = 'Трубчатые';

Задание №3
SELECT C.name AS category_name, COUNT(M.mushroom_id) AS mushroom_count
FROM Categories C
LEFT JOIN Mushrooms M ON C.category_id = M.category_id
GROUP BY C.category_id, C.name
ORDER BY mushroom_count DESC;

Задание №4
SELECT M.name AS mushroom_name, M.description
FROM Mushrooms M
JOIN Regions R ON M.primary_region_id = R.region_id
WHERE M.edible = TRUE
ORDER BY R.size DESC
LIMIT 5;

Задание №5
SELECT M.name AS mushroom_name
FROM Mushrooms M
JOIN Categories C ON M.category_id = C.category_id
JOIN Regions R ON M.primary_region_id = R.region_id
WHERE M.season = 'Весна'
  AND C.name = 'Пластинчатые'
  AND R.size <= 6000;
