-- TOP COUNTRIES OF ORIGIN
SELECT DISTINCT erez_moza, COUNT(*) AS olims
FROM combined_table
GROUP BY erez_moza
ORDER BY COUNT(*) DESC
LIMIT 10;

-- SUBCONTINENTS OF ORIGIN
SELECT subcont, COUNT(*) as count
FROM combined_table
GROUP BY subcont
ORDER BY COUNT(*) DESC;

-- AGE GROUPS OF THE OLIMS
SELECT age_group, COUNT(*) as count
FROM combined_table
GROUP BY age_group
ORDER BY COUNT(*) DESC;

-- THE GENDER PROPORTIONS
SELECT gender, COUNT(*) as count
FROM combined_table
GROUP BY gender
ORDER BY COUNT(*) DESC;

-- OVERALL ALIYAH PER YEAR
SELECT year_aliya, COUNT(*) as count
FROM combined_table
GROUP BY year_aliya
ORDER BY COUNT(*) DESC;

-- THE MOST RESULTING MONTH PER EACH YEAR
WITH ResultMonth AS (
    SELECT year_aliya, 
           month_aliya, 
           COUNT(*) AS count,
           ROW_NUMBER() OVER (PARTITION BY year_aliya ORDER BY COUNT(*) DESC) AS rn
    FROM combined_table
    GROUP BY year_aliya, month_aliya
)
SELECT year_aliya, month_aliya, count
FROM ResultMonth
WHERE rn = 1;


-- IS THERE A CHANGE IN ALIYAH AFTER OCTOBER THE 7-TH AND FROM WHICH COUNTRIES
-- TOP-5 PER OCTOBER, NOVEMBER AND DECEMBER
WITH RankedCountries AS (
    SELECT 
        month_aliya,
        erez_moza,
        COUNT(*) AS country_count,
        ROW_NUMBER() OVER (PARTITION BY month_aliya ORDER BY COUNT(*) DESC) AS rank
    FROM combined_table
    WHERE year_aliya = '2023' AND month_aliya >= '6'
    GROUP BY month_aliya, erez_moza
)
SELECT 
    month_aliya,
    erez_moza,
    country_count
FROM RankedCountries
WHERE rank <= 5
ORDER BY month_aliya ASC;

-- THE WAR IN UKRAINE
-- TOP-5 COUNTRIES OF ORIGIN PER EACH MONTH BETWEEN 2022 AND 2023
WITH RankedCountries AS (
    SELECT 
        year_aliya,
        month_aliya,
        erez_moza,
        COUNT(*) AS country_count,
        ROW_NUMBER() OVER (PARTITION BY month_aliya ORDER BY COUNT (*) DESC) AS rank
    FROM combined_table
    WHERE year_aliya = '2023' or year_aliya = '2022' and month_aliya >= '2'
    GROUP BY year_aliya, month_aliya, erez_moza
)
SELECT 
    year_aliya, month_aliya, erez_moza, country_count
FROM RankedCountries
WHERE rank <= 5
ORDER BY year_aliya ASC, month_aliya ASC, country_count DESC
;

SELECT DISTINCT mikzoa
FROM combined_table
ORDER BY mikzoa ASC;

SELECT *
FROM combined_table;