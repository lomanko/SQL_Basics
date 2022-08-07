-- 1. Number of artists in each genre.

SELECT g.name, count(gs.singer_id) 
  FROM genres g
  JOIN genres_singers gs ON g.id = gs.genre_id 
 GROUP BY g.name
 ORDER BY count(gs.singer_id) DESC;


-- 2. Number of songs in albums published in 2019-2020.

-- by album
SELECT a.name, a.release_year, count(s.name) 
  FROM songs s 
  JOIN albums a ON s.album_id = a.id
 WHERE a.release_year  BETWEEN 2019 AND 2020
 GROUP BY a.name, a.release_year;

-- only total
SELECT count(s.name) 
  FROM songs s 
  JOIN albums a ON s.album_id = a.id
 WHERE a.release_year BETWEEN 2019 AND 2020;


-- 3. Average duration by album.

SELECT a.name, to_char(avg(s.duration),'hh24:mi:ss') 
  FROM songs s
  JOIN albums a ON s.album_id  = a.id
 GROUP BY a.name
 ORDER BY avg(s.duration) DESC;


-- 4. All artists with no albums published in 2020.

SELECT DISTINCT s.name 
  FROM singers s 
  LEFT JOIN albums_singers as2 ON s.id = as2.singer_id -- LEFT JOIN to include artists without albums
  LEFT JOIN albums a ON as2.album_id = a.id
 WHERE a.release_year != 2020 OR a.release_year IS NULL
 ORDER BY s.name;


-- 5. Names of collections with songs from an exact artist.

SELECT DISTINCT c.name 
  FROM collections c
  JOIN collections_songs cs ON c.id = cs.collection_id
  JOIN songs s ON cs.song_id = s.id 
  JOIN albums_singers as2 ON s.album_id = as2.album_id
  JOIN singers sing ON as2.singer_id  = sing.id
 WHERE sing.name = 'Coldplay';


-- 6. Albums by singers with more that 1 genre.

SELECT a.name AS album_name, count(gs.genre_id) AS genres_number  
  FROM albums a 
  JOIN albums_singers as2 ON a.id = as2.album_id 
  JOIN genres_singers gs ON as2.singer_id = gs.singer_id
 GROUP BY a.name
HAVING count(*) > 1;


-- 7. Tracks not included in collections

SELECT s.name 
  FROM songs s
  LEFT JOIN collections_songs cs ON s.id = cs.song_id
 WHERE cs.collection_id IS NULL
 ORDER BY s.name;


-- 8. Artist(s) with the shortest song.

SELECT DISTINCT sing.name 
  FROM songs s 
  JOIN albums_singers as2 ON s.album_id = as2.album_id 
  JOIN singers sing ON as2.singer_id = sing.id 
 WHERE s.duration = (SELECT min(duration) 
                       FROM songs)
 GROUP BY sing.name;


-- 9. Albums with MIN tracks.

SELECT a.name AS album_name, count(s.name) AS number_tracks
  FROM albums a 
  JOIN songs s ON a.id = s.album_id
 GROUP BY a.name
HAVING count(s.name) = (SELECT min(counted) 
                          FROM (SELECT count(s.name) AS counted 
                                  FROM albums a 
                                  JOIN songs s ON a.id = s.album_id
                                 GROUP BY a.name
                                 ORDER BY count(s.name)) AS counted_albums);
