# 175. Combine Two Tables

## Problem Link

https://leetcode.com/problems/combine-two-tables/

## Problem Description

Write a solution to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.

```
CREATE PROCEDURE check_city()
BEGIN
    DECLARE k INT DEFAULT 1;
    DECLARE person_count INT;
    DECLARE personId_exists INT DEFAULT 0;

    SELECT COUNT(*) INTO person_count
    FROM Person;

    WHILE (k <= person_count) DO
        SELECT COUNT(*) INTO personId_exists
        FROM Address
        WHERE personId = k;

        IF (personId_exists = 0) THEN
            SELECT firstName, lastName, NULL AS city, NULL AS state
            FROM Person
            WHERE personId = k;
        ELSE
            SELECT firstName, lastName, c.city, c.state
            FROM Person p
            JOIN Address c ON p.personId = c.personId
            WHERE personId.id = k;
        END IF;

        SET k = k + 1;
    END WHILE;
END;
```

## Explanation

- Performs a LEFT JOIN between the Person table and the Address table
- LEFT JOIN ensures all records from the Person table are included in the result
- If there's no matching record in the Address table, null values are returned for city and state
- The join is performed based on the personId column from both tables
