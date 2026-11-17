"""
SkillNote Adaptive Runtime — Skill Indexer (SQLite FTS5)
Maintained solely and independently by Chinmay Prakash Rout (ChinmayPrakashRout03)
GitHub: https://github.com/ChinmayPrakashRout03/skillsFORskillnote
"""

import sqlite3
import os
import re
from pathlib import Path
from typing import Dict, Any, List, Optional

DB_PATH = Path(__file__).resolve().parent.parent / ".skillnote" / "catalog.sqlite"


def get_connection(db_path: Path = DB_PATH) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    return conn


def init_db(conn: sqlite3.Connection):
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS skills (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                rel_path TEXT UNIQUE NOT NULL,
                abs_path TEXT NOT NULL,
                title TEXT,
                description TEXT,
                tags TEXT,
                word_count INTEGER DEFAULT 0,
                token_estimate INTEGER DEFAULT 0,
                is_primary INTEGER DEFAULT 1,
                last_modified REAL
            )
        """)
        conn.execute("""
            CREATE VIRTUAL TABLE IF NOT EXISTS skills_fts USING fts5(
                name,
                category,
                title,
                description,
                tags,
                content='skills',
                content_rowid='id',
                tokenize='porter unicode61'
            )
        """)
        conn.execute("""
            CREATE TRIGGER IF NOT EXISTS skills_ai AFTER INSERT ON skills BEGIN
                INSERT INTO skills_fts(rowid, name, category, title, description, tags)
                VALUES (new.id, new.name, new.category, new.title, new.description, new.tags);
            END;
        """)
        conn.execute("""
            CREATE TRIGGER IF NOT EXISTS skills_ad AFTER DELETE ON skills BEGIN
                INSERT INTO skills_fts(skills_fts, rowid, name, category, title, description, tags)
                VALUES('delete', old.id, old.name, old.category, old.title, old.description, old.tags);
            END;
        """)
        conn.execute("""
            CREATE TRIGGER IF NOT EXISTS skills_au AFTER UPDATE ON skills BEGIN
                INSERT INTO skills_fts(skills_fts, rowid, name, category, title, description, tags)
                VALUES('delete', old.id, old.name, old.category, old.title, old.description, old.tags);
                INSERT INTO skills_fts(rowid, name, category, title, description, tags)
                VALUES (new.id, new.name, new.category, new.title, new.description, new.tags);
            END;
        """)


def parse_markdown_metadata(file_path: Path) -> Dict[str, Any]:
    name = file_path.stem
    title = name.replace("-", " ").title()
    description = ""
    tags = []
    
    try:
        content = file_path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        content = ""

    words = len(content.split())
    tokens = int(words * 1.33)

    # Frontmatter extraction
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm = parts[1]
            body = parts[2]
            
            # extract name:
            m_name = re.search(r"^name:\s*['\"]?(.*?)['\"]?$", fm, re.MULTILINE)
            if m_name and m_name.group(1).strip():
                name = m_name.group(1).strip()
                
            # extract description:
            m_desc = re.search(r"^description:\s*(?:>|\|)?\s*\n?(.*?)(?=\n[a-zA-Z0-9_-]+:|$)", fm, re.DOTALL | re.MULTILINE)
            if m_desc:
                description = m_desc.group(1).strip().replace("\n", " ")
                # remove quotes
                description = re.sub(r"^['\"]|['\"]$", "", description)

            # extract tags / keywords
            m_tags = re.search(r"^(?:tags|keywords):\s*\[(.*?)\]", fm, re.MULTILINE)
            if m_tags:
                tags = [t.strip().strip("'\"") for t in m_tags.group(1).split(",") if t.strip()]
        else:
            body = content
    else:
        body = content

    # Find first markdown heading if title is default
    if not title or title == name.replace("-", " ").title():
        m_head = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
        if m_head:
            title = m_head.group(1).strip()

    # Fallback description from first non-empty paragraph
    if not description:
        for para in body.split("\n\n"):
            p = para.strip()
            if p and not p.startswith("#") and not p.startswith("---") and not p.startswith("```"):
                description = p[:250].replace("\n", " ")
                break

    return {
        "name": name,
        "title": title,
        "description": description[:350],
        "tags": ", ".join(tags),
        "word_count": words,
        "token_estimate": tokens
    }


def index_skills(library_dir: Path, db_path: Path = DB_PATH) -> int:
    conn = get_connection(db_path)
    init_db(conn)

    categories = [d for d in library_dir.iterdir() if d.is_dir() and not d.name.startswith(".")]
    indexed_count = 0

    with conn:
        for cat_dir in sorted(categories):
            cat_name = cat_dir.name
            for file_path in cat_dir.rglob("*.md"):
                if not file_path.is_file() or file_path.name.startswith("."):
                    continue

                rel_path = str(file_path.relative_to(library_dir))
                is_primary = 1 if file_path.parent == cat_dir else 0
                meta = parse_markdown_metadata(file_path)
                mtime = file_path.stat().st_mtime

                conn.execute("""
                    INSERT OR REPLACE INTO skills (
                        name, category, rel_path, abs_path, title, description,
                        tags, word_count, token_estimate, is_primary, last_modified
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    meta["name"],
                    cat_name,
                    rel_path,
                    str(file_path.resolve()),
                    meta["title"],
                    meta["description"],
                    meta["tags"],
                    meta["word_count"],
                    meta["token_estimate"],
                    is_primary,
                    mtime
                ))
                indexed_count += 1

    conn.close()
    return indexed_count


def get_stats(db_path: Path = DB_PATH) -> Dict[str, Any]:
    if not db_path.exists():
        return {"total_skills": 0, "categories": 0}
    conn = get_connection(db_path)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*), COUNT(DISTINCT category), SUM(is_primary) FROM skills")
    total, cats, primary = cur.fetchone()
    conn.close()
    return {
        "total_files": total,
        "categories": cats,
        "primary_skills": primary or 0,
        "db_path": str(db_path)
    }
