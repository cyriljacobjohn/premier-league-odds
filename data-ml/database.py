import sqlite3

conn = sqlite3.connect('premier_league.db')

c = conn.cursor()

c.execute("PRAGMA foreign_keys = ON;")
c.execute("DROP TABLE IF EXISTS fixtures")

c.execute("""CREATE TABLE IF NOT EXISTS fixtures(
        fixture_id INTEGER PRIMARY KEY,
        match_id INTEGER NOT NULL,
        venue TEXT,
        raw_json TEXT NOT NULL,
        FOREIGN KEY (match_id) REFERENCES matches(match_id)
        )  """)



#commit command
conn.commit()

#close our connection
conn.close()

