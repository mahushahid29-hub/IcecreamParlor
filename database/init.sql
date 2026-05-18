-- Ice Cream Parlor Database Initialization
CREATE TABLE IF NOT EXISTS orders (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    base     TEXT    NOT NULL,
    size     TEXT    NOT NULL,
    flavors  TEXT,
    total    REAL    NOT NULL
);
