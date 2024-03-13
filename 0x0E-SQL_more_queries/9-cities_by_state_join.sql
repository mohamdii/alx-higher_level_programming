-- using join
SELECT id, name FROM cities
    NATURAL JOIN states
ORDER BY id 
