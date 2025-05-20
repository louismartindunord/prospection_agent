--- userfull to get the user infos in the user form page

SELECT 
    id,
    firstname, 
    lastname, 
    email  
FROM User_infos
WHERE id = ?