import sqlite3

DB_NAME = "data-test.db"

schema = """
CREATE TABLE IF NOT EXISTS player
(
    id                    INTEGER PRIMARY KEY AUTOINCREMENT,
    name                  TEXT    NOT NULL,
    credits               INTEGER NOT NULL,
    avg_play_time         REAL    NOT NULL,
    quizzes_solved        INTEGER NOT NULL,
    quizzes_played        INTEGER NOT NULL,
    regions_unlocked      TEXT    NOT NULL,
    cosmetics_unlocked    TEXT    NOT NULL,
    cosmetics_purchased   TEXT    NOT NULL,
    completion_percentage REAL    NOT NULL
);

CREATE TABLE IF NOT EXISTS quizzes
(
    id                    INTEGER PRIMARY KEY AUTOINCREMENT,
    difficulty            TEXT    NOT NULL,
    completion_percentage REAL,
    player                INTEGER,
    FOREIGN KEY (player)
        REFERENCES player(id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS quizz_tasks
(
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    type      TEXT    NOT NULL,
    task_text TEXT,
    quizz     INTEGER,
    FOREIGN KEY (quizz)
        REFERENCES quizzes(id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS answers
(
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    answer_text TEXT    NOT NULL,
    is_correct  INTEGER NOT NULL,
    quizz_task  INTEGER,
    FOREIGN KEY (quizz_task)
        REFERENCES quizz_tasks(id)
        ON DELETE CASCADE
);

-- These SQLite system tables are automatically created.
-- Manually recreating sqlite_master and sqlite_sequence is not allowed in SQLite.
"""

def main():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.executescript(schema)
    conn.commit()
    conn.close()

    print(f"Database '{DB_NAME}' created with all tables.")

if __name__ == "__main__":
    main()
