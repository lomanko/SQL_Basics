-- INSERT singer TABLE
INSERT INTO singers (name) 
VALUES 
	('Eminem'),
	('Lil Wayne'),
	('Beyonce'),
	('Drake'),
	('Coldplay'),
	('5'),
	('Ed Sheeran'),
	('Kanye West');

--INSERT genres TABLE
INSERT INTO genres (name)
VALUES
	('RAP'),
	('POP'),
	('Hip-Hop'),
	('Rock'),
	('R&B');

--INSERT genres_singers TABLE
INSERT INTO genres_singers(genre_id, singer_id)
VALUES
	(1, 1),
	(3, 2),
	(5, 3),
	(1, 4),
	(4, 5),
	(2, 6),
	(2, 7),
	(1, 8);

--INSERT albums TABLE
INSERT INTO albums (name, release_year)
VALUES
	('The Eminem Show', 2002), --eminem
	('Scorpion', 2018), --drake
	('Jordi', 2021), --maroon 5
	('Ye', 2018), --kanye west
	('Everyday Life', 2019), --coldplay
	('A Head Full of Dreams', 2015), --coldplay
	('Lemonade', 2016), --beyonce
	('4', 2011); --beyonce

--INSERT albums_singers TABLE
INSERT INTO albums_singers (album_id, singer_id)
VALUES 
	(1, 1),
	(2, 4),
	(3, 6),
	(4, 8),
	(5, 5),
	(6, 5),
	(7, 3),
	(8, 3);


--INSERT songs TABLE
INSERT INTO songs (name, duration, album_id)
VALUES 
	('Business', '04:11', 1),
	('Curtains Close', '01:01' , 1),
	('"Mob Ties"', '03:25', 2),
	('All My', '02:25', 4),
	('No Mistakes', '02:03', 4),
	('Formation', '03:26', 7),
	('All Night', '05:22', 7),
	('Forvard', '01:19', 7),
	('Memories', '03:09', 3),
	('Seasons', '02:48', 3),
	('Lost', '02:52', 3),
	('Sunrise', '02:31', 5),
	('Daddy', '04:58', 5),
	('Everyday Life', '04:18', 5),
	('Cry Cry Cry', '02:47', 5);

--INSERT collections TABLE
INSERT INTO collections (name, release_year)
VALUES
	('Coldplay collection', 2019),
	('Eminem collection', 2002),
	('Beyonce collection', 2016),
	('Maroon 5 collection', 2021),
	('Mix collection', 2019),
	('Kanye West collection', 2018),
	('R&B collection', 2022),
	('Rock collection', 2020);

--INSERT collections_songs TABLE
INSERT INTO collections_songs (collection_id, song_id)
VALUES
	(1, 12),
	(1, 13),
	(1, 14),
	(1, 15),
	(2, 1),
	(2, 2),
	(5, 12),
	(5, 1);
