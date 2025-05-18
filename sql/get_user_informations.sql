--- userfull to get the user infos in the user form page

SELECT 
    id,
    firstname TEXT, 
    lastname TEXT, 
    email TEXT NOT NULL UNIQUE 
FROM User_infos
