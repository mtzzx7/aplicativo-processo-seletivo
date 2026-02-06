import os
import sqlite3
from pathlib import Path

DB_PATH = Path(os.getenv("SELECTION_DB_PATH", "selection.db"))


def connect_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")
    return conn
