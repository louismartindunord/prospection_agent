--- userfull to get the user infos in the user form page

SELECT 
    id,
    firstname, 
    lastname, 
    email,
    compagny_type,
    activity,
    activity_large_description
FROM User_infos
WHERE id = ?