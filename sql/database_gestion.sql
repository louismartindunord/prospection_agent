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
