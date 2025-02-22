SELECT 
    p.firstName, 
    p.lastName, 
    c.city, 
    c.state 
FROM 
    Person p 
INNER JOIN 
    Address c 
ON 
    p.personId = c.personId;