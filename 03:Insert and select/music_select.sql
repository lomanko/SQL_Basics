-- Albums released in 2018
SELECT name, release_year FROM albums
WHERE release_year = 2018;

-- Longest track
SELECT name, duration FROM songs
ORDER BY duration DESC
LIMIT 1;

-- Track with duration not less than 03:30
SELECT name, duration FROM songs
WHERE duration >= '03:30';

-- Collections released from 2018 to 2020
SELECT name, release_year FROM collections
WHERE release_year BETWEEN 2018 AND 2020;

-- Singers with one letter name
SELECT name FROM singers
WHERE name LIKE '_';

-- Tracks with 'My' or 'мой' in name
SELECT name, duration FROM songs 
WHERE name LIKE '%My%' OR name LIKE '%Мой%';

