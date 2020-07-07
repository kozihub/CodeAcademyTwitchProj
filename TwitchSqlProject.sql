-- Check the unique games and channels to get a feel for the data
SELECT DISTINCT game FROM stream;

SELECT DISTINCT channel from stream;

-- Find how many streams each unique game is getting
SELECT DISTINCT game, COUNT(*) as num_stream FROM stream
GROUP BY 1
ORDER BY 2 DESC;

-- Find the top streaming countries for League of Legends
SELECT country, COUNT(*) as num_stream FROM stream
WHERE game = 'League of Legends'
GROUP BY 1
ORDER BY 2 DESC;

-- Find the most used applications for streaming  
SELECT player, COUNT(*) as num_stream from stream
GROUP BY 1
ORDER BY 2 DESC;

-- Create a new column 'genre' that lists the games into their respective genre
SELECT game,
  CASE
    WHEN game = 'League of Legends'
      THEN 'MOBA'
    WHEN game = 'Dota 2'
      THEN 'MOBA'
    WHEN game = 'Heroes of the Storm'
      THEN 'MOBA'
    WHEN game = 'Counter-Strike: Global Offensive'
      THEN 'FPS'
    WHEN game = 'DayZ'
      THEN 'Survival'
    WHEN game = 'Survival Evolved'
      THEN 'Survival'
    ELSE 'Other'
    END AS 'genre',
    COUNT(*) as num_stream
FROM stream
GROUP BY 1
ORDER BY 3 desc
LIMIT 10;

-- See how many users are streaming at the beggining of each hour
SELECT 
  strftime('%H', time) as hour_start_stream, COUNT(*) as num_stream
FROM stream
WHERE country = 'US'
GROUP BY 1;

-- Join the two tables
SELECT * FROM stream
JOIN chat 
	ON stream.device_id = chat.device_id;
