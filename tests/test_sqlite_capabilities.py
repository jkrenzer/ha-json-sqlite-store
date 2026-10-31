import sqlite3
from pathlib import Path


def test_sqlite_wal_and_transaction_rollback(tmp_path: Path) -> None:
    db_path = tmp_path / "capability-test.sqlite3"
    conn = sqlite3.connect(db_path)

    try:
        journal_mode = conn.execute("PRAGMA journal_mode=WAL").fetchone()
        conn.execute("PRAGMA synchronous=FULL")
        conn.execute(
            "CREATE TABLE IF NOT EXISTS documents ("
            "document_id TEXT PRIMARY KEY, payload TEXT NOT NULL)"
        )

        conn.execute("BEGIN")
        conn.execute(
            "INSERT INTO documents (document_id, payload) VALUES (?, ?)",
            ("doc-1", '{"hello": "world"}'),
        )
        conn.rollback()

        remaining_rows = conn.execute("SELECT COUNT(*) FROM documents").fetchone()
    finally:
        conn.close()

    assert journal_mode == ("wal",)
    assert remaining_rows == (0,)
