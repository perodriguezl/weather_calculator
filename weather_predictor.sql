BEGIN TRANSACTION;
CREATE TABLE "planets" (
	`name`	TEXT UNIQUE,
	`speed`	INTEGER,
	`ratio`	INTEGER,
	PRIMARY KEY(name)
);
CREATE TABLE "day_weather" (
	`day`	INTEGER,
	`weather`	TEXT,
	PRIMARY KEY(day)
);
CREATE VIEW view_general_weather as
SELECT count(day), weather 
FROM day_weather GROUP BY weather;
COMMIT;
