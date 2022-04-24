--Proccess to load Dataset into PostgreSQL


-- 1. Open PostgreSQL in the terminal
-- 2. Create a table in the database with the same columns as CSV

 CREATE TABLE play_by_play(leagueid int, leaguename varchar, seasontype varchar, 
 gametimestamp timestamp, homenbateamid int, hometeamname varchar, awaynbateamid int,
 awayteamname varchar, nbateamid int, nbapersonid int, nbapersonname varchar, eventid int,
 period int, minutesecond time, points int, blockedshot int, rebdefensive int, fg3attempted int,
 assist int, ftmade int, fgmade int, fgattempted int, fg2attempted int, 
 ftattempted int, turnover int, fg2made int, reboffensive int, fg3made int, gameid int);

 --3 Copy local CSV file into the database table that you create
COPY play_by_play(leagueid int, leaguename varchar, seasontype varchar, 
 gametimestamp timestamp, homenbateamid int, hometeamname varchar, awaynbateamid int,
 awayteamname varchar, nbateamid int, nbapersonid int, nbapersonname varchar, eventid int,
 period int, minutesecond time, points int, blockedshot int, rebdefensive int, fg3attempted int,
 assist int, ftmade int, fgmade int, fgattempted int, fg2attempted int, 
 ftattempted int, turnover int, fg2made int, reboffensive int, fg3made int, gameid int)
FROM 'C:\path\to\csv'
DELIMITER ','
CSV HEADER;

