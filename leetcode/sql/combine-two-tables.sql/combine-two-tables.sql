SELECT 
    p.firstName, 
    p.lastName, 
    c.city, 
    c.state 
FROM 
    Address c 
RIGHT JOIN 
    Person p 
ON 
    p.personId = c.personId;