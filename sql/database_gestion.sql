CREATE TABLE IF NOT EXISTS Prospect (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lastname TEXT, 
    firstname TEXT,
    email TEXT UNIQUE,
    phone_number TEXT,
    company_name TEXT, 
    prospect_status TEXT Default 'new'
);

CREATE TABLE IF NOT EXISTS Client (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prospect_id INTEGER UNIQUE,
    FOREIGN KEY (prospect_id) REFERENCES Prospect(id)
);

CREATE TABLE IF NOT EXISTS Campaign (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    start_date DATE,
    end_date DATE
);

CREATE TABLE IF NOT EXISTS Mail (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prospect_id INTEGER, 
    message_object TEXT, 
    message_text TEXT, 
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    campaign_id INTEGER,
    FOREIGN KEY (prospect_id) REFERENCES Prospect(id),
    FOREIGN KEY (campaign_id) REFERENCES Campaign(id)
);

CREATE TABLE IF NOT EXISTS User_infos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT, 
    lastname TEXT, 
    email TEXT NOT NULL UNIQUE 
    );

--Gestion des informations utilisateurs en base de données vectorielle
--CREATE VIRTUAL TABLE IF NOT EXISTS user_infos_document
--USING vss(content_embedding(1536));
--
--
--CREATE TABLE IF NOT EXISTS user_info_to_user_document (
--    id INTEGER PRIMARY KEY AUTOINCREMENT,
--    user_id INTEGER,
--    document_id INTEGER,
--    content TEXT,
--    FOREIGN KEY(document_id) REFERENCES user_infos_document(rowid),
--    FOREIGN KEY(user_id) REFERENCES User_infos(id)
--);

--Ajout d'informations concernant l'utilisateur afin de permettre au robot de fonctionner
--ALTER TABLE User_infos ADD COLUMN compagny_type;
--ALTER TABLE User_infos ADD COLUMN activity;
--ALTER TABLE User_infos ADD COLUMN activity_large_description;

-- Ajout de user_id foreign key sur l'ensemble des tables pour permettre d'ajouter des utilisateurs
-- Sqlite ne permet pas add column if not exist donc laisser commenter ces lignes
--ALTER TABLE Prospect
--ADD COLUMN  user_id INTEGER REFERENCES User_infos(id);
--ALTER TABLE Client
--ADD COLUMN  user_id INTEGER REFERENCES User_infos(id);
--ALTER TABLE Mail
--ADD COLUMN  user_id INTEGER REFERENCES User_infos(id);
--ALTER TABLE Campaign
--ADD COLUMN  user_id INTEGER REFERENCES User_infos(id);