CREATE TABLE IF NOT EXISTS company_info(
	code VARCHAR(20),
	company VARCHAR(40),
	last_update DATE,
	PRIMARY KEY (CODE)
);

CREATE TABLE IF NOT EXISTS daily_price(
	code VARCHAR(20),
	date DATE,
	OPEN BIGINT(20),
	high BIGINT(20),
	low BIGINT(20),
	close BIGINT(20),
	diff BIGINT(20),
	volume BIGINT(20),
	PRIMARY KEY (code, date)
);

SELECT *
FROM company_info