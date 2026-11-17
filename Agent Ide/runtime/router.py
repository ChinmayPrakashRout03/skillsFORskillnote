"""
SkillNote Adaptive Runtime — Task Classifier & Smart Router
Maintained solely and independently by Chinmay Prakash Rout (ChinmayPrakashRout03)
GitHub: https://github.com/ChinmayPrakashRout03/skillsFORskillnote
"""

import sqlite3
import re
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

from .indexer import DB_PATH, get_connection

CATEGORIES = [
    "adapt", "assist", "audit", "automate", "beautify", "comprehend",
    "contextualize", "convert", "create", "curate", "design", "develop",
    "engineer", "execute", "guide", "humanize", "manage", "minimize",
    "navigate", "official", "optimize", "orchestrate", "prototype",
    "refine", "secure", "simplify", "simulate", "style", "systematize",
    "versatile", "visualize", "workflow"
]


def classify_task_mode(prompt: str) -> Dict[str, Any]:
    """
    Classifies task into one of 4 adaptive modes:
    1. micro       - 1-file fix, typo, null check, variable rename (<5k tokens)
    2. standard    - typical feature, refactor, API endpoint, unit tests (15-25k tokens)
    3. complex     - multi-system, architecture, full subsystem, payment/auth (50k+ tokens)
    4. experimental - novel algorithm, exploration, prototype alternatives
    """
    p_lower = prompt.lower().strip()
    words = p_lower.split()
    word_count = len(words)

    # 1. Experimental checks
    experimental_keywords = [
        "novel", "invent", "experiment", "prototype alternative",
        "explore alternative", "benchmark competing", "unconventional",
        "research approach", "try different", "speculative"
    ]
    for kw in experimental_keywords:
        if kw in p_lower:
            return {
                "mode": "experimental",
                "description": "Exploratory & hypothesis-driven. Relax rigid conventions, test alternatives, measure trade-offs.",
                "max_skills": 2,
                "token_budget": "20,000"
            }

    # 2. Micro checks (simple, isolated fix)
    micro_keywords = [
        "fix typo", "null check", "rename", "change color", "fix syntax",
        "small fix", "one line", "quick fix", "spelling", "docstring",
        "add log", "minor tweak"
    ]
    for kw in micro_keywords:
        if kw in p_lower:
            return {
                "mode": "micro",
                "description": "Minimal analysis, targeted fix, targeted tests. Zero process bloat.",
                "max_skills": 1,
                "token_budget": "3,000"
            }
    if word_count <= 5 and not any(k in p_lower for k in ["build", "architect", "pipeline", "system", "engine"]):
        return {
            "mode": "micro",
            "description": "Compact request. Execute with minimal overhead.",
            "max_skills": 1,
            "token_budget": "3,000"
        }

    # 3. Complex checks
    complex_keywords = [
        "subsystem", "distributed", "architecture", "microservice", "infrastructure",
        "payment", "migration", "end-to-end pipeline", "full stack",
        "multi-tenant", "zero trust", "high throughput", "consensus"
    ]
    for kw in complex_keywords:
        if kw in p_lower:
            return {
                "mode": "complex",
                "description": "Phased architecture, milestones, security review, and full test matrices.",
                "max_skills": 4,
                "token_budget": "60,000"
            }

    # 4. Standard default
    return {
        "mode": "standard",
        "description": "Balanced engineering: plan, implement, test, and verify.",
        "max_skills": 2,
        "token_budget": "20,000"
    }


def search_skills(query: str, limit: int = 5, db_path: Path = DB_PATH) -> List[Dict[str, Any]]:
    """Runs BM25 full-text search against the SQLite catalog."""
    if not db_path.exists():
        return []

    # Clean query for FTS5 (strip special punctuation, keep alphanumeric)
    tokens = re.findall(r"\b[a-zA-Z0-9_-]{2,}\b", query)
    if not tokens:
        return []

    # Exclude common stopwords
    stopwords = {"and", "the", "for", "with", "this", "that", "from", "into", "using"}
    clean_tokens = [t for t in tokens if t.lower() not in stopwords]
    if not clean_tokens:
        clean_tokens = tokens

    fts_query = " OR ".join(f'"{t}"' for t in clean_tokens[:8])

    conn = get_connection(db_path)
    cur = conn.cursor()
    
    try:
        cur.execute("""
            SELECT s.id, s.name, s.category, s.rel_path, s.abs_path,
                   s.title, s.description, s.token_estimate, s.is_primary, rank
            FROM skills_fts f
            JOIN skills s ON f.rowid = s.id
            WHERE skills_fts MATCH ?
            ORDER BY s.is_primary DESC, rank ASC
            LIMIT ?
        """, (fts_query, limit))
        rows = [dict(r) for r in cur.fetchall()]
    except Exception:
        rows = []
    finally:
        conn.close()

    return rows


def route_request(input_str: str, db_path: Path = DB_PATH) -> Dict[str, Any]:
    """
    Main routing function for /skillnote.
    Evaluates whether input is a Category Pipeline or a Task requiring adaptive routing.
    """
    cleaned = input_str.strip().lower()

    # Check for exact Category Pipeline match
    if cleaned in CATEGORIES:
        return {
            "type": "category_pipeline",
            "category": cleaned,
            "mode": "targeted_sequential",
            "description": f"Targeted sequential pipeline for category {cleaned.upper()}."
        }

    # Task classification
    classification = classify_task_mode(input_str)
    mode = classification["mode"]
    max_skills = classification["max_skills"]

    # Search relevant skills
    matched_skills = search_skills(input_str, limit=max_skills, db_path=db_path)

    # Format selected skills
    selected = []
    for s in matched_skills:
        selected.append({
            "name": s["name"],
            "category": s["category"],
            "title": s["title"],
            "description": s["description"],
            "rel_path": s["rel_path"],
            "abs_path": s["abs_path"],
            "tokens": s["token_estimate"]
        })

    return {
        "type": "adaptive_task",
        "prompt": input_str,
        "mode": mode,
        "mode_description": classification["description"],
        "token_budget": classification["token_budget"],
        "selected_skills_count": len(selected),
        "selected_skills": selected
    }
