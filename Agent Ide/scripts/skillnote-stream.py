#!/usr/bin/env bash
""":"
exec python3 "$0" "$@"
"""
# SkillNote Zero-Disk Streaming Client
# Maintained solely and independently by Chinmay Prakash Rout (ChinmayPrakashRout03)
# Repository: https://github.com/ChinmayPrakashRout03/skillsFORskillnote

import sys
import os
import json
import time
import argparse
import subprocess
import urllib.request
from pathlib import Path

GITHUB_RAW_BASE = "https://raw.githubusercontent.com/ChinmayPrakashRout03/skillsFORskillnote/main/Agent%20Ide"
INDEX_URL = f"{GITHUB_RAW_BASE}/resources/skills-index.json"
CACHE_DIR = Path.home() / ".skillnote"
INDEX_FILE = CACHE_DIR / "skills-index.json"

CATEGORIES = [
    "adapt", "assist", "audit", "automate", "beautify", "comprehend",
    "contextualize", "convert", "create", "curate", "design", "develop",
    "engineer", "execute", "guide", "humanize", "manage", "minimize",
    "navigate", "official", "optimize", "orchestrate", "prototype",
    "refine", "secure", "simplify", "simulate", "style", "systematize",
    "versatile", "visualize", "workflow"
]


def ensure_index():
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    if not INDEX_FILE.exists():
        # Check if local file exists in repo
        local_res = Path(__file__).resolve().parent.parent / "resources" / "skills-index.json"
        if local_res.exists():
            import shutil
            shutil.copy(local_res, INDEX_FILE)
            return

        print("▶ Syncing SkillNote lightweight cloud catalog index (~1MB)...", file=sys.stderr)
        req = urllib.request.Request(INDEX_URL, headers={"User-Agent": "SkillNote-Stream"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            with open(INDEX_FILE, "wb") as f:
                f.write(data)


def load_index():
    ensure_index()
    try:
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading catalog: {e}", file=sys.stderr)
        return []


def search_skills(query, limit=5, category=None):
    skills = load_index()
    words = [w.lower() for w in query.split()]
    scored = []
    for s in skills:
        if category and s["category"].lower() != category.lower():
            continue
        text = f"{s['name']} {s['category']} {s['title']} {s['description']} {s.get('tags', '')}".lower()
        score = sum(text.count(w) for w in words)
        if score > 0:
            scored.append((score, s))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [s for _, s in scored[:limit]]


def fetch_skill_content(rel_path):
    """Streams a skill markdown content on-demand from GitHub Raw into memory without saving to disk."""
    # Check if local repo exists
    local_path = Path(__file__).resolve().parent.parent / "skills" / rel_path
    if local_path.exists():
        return local_path.read_text(encoding="utf-8")

    # Fetch on demand from GitHub Raw
    encoded_path = urllib.parse.quote(rel_path)
    url = f"{GITHUB_RAW_BASE}/skills/{encoded_path}"
    req = urllib.request.Request(url, headers={"User-Agent": "SkillNote-Stream"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        return resp.read().decode("utf-8")


def classify_complexity(prompt):
    p = prompt.lower()
    if any(k in p for k in ["typo", "fix line", "quick fix", "null pointer", "undefined", "small bug", "format"]):
        return "micro", 3000, "Micro Mode: Surgical single-file patch with zero ceremony."
    if any(k in p for k in ["distributed", "system", "architecture", "microservice", "migration", "redesign", "security overhaul"]):
        return "complex", 60000, "Complex Mode: Phased milestones, dependency maps, and systematic validation."
    if any(k in p for k in ["algorithm", "novel", "experiment", "spike", "research", "explore", "benchmark", "prototype"]):
        return "experimental", 20000, "Experimental Mode: Hypothesis-driven testing with relaxed pattern constraints."
    return "standard", 20000, "Standard Mode: Architecture contract ➔ modular implementation ➔ test suite."


def verify_command(cmd):
    start = time.time()
    try:
        proc = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=120)
        dur = time.time() - start
        return {
            "command": cmd,
            "exit_code": proc.returncode,
            "status": "PASSED" if proc.returncode == 0 else "FAILED",
            "duration": f"{dur:.2f}s",
            "stdout": proc.stdout[-1000:] if proc.stdout else "",
            "stderr": proc.stderr[-1000:] if proc.stderr else ""
        }
    except Exception as e:
        return {
            "command": cmd,
            "exit_code": -1,
            "status": "ERROR",
            "duration": f"{time.time() - start:.2f}s",
            "error": str(e)
        }


def main():
    parser = argparse.ArgumentParser(description="SkillNote Zero-Disk Streaming Client")
    parser.add_argument("query", nargs="*", help="Task description or category")
    parser.add_argument("--search", "-s", help="Search skills in lightweight catalog")
    parser.add_argument("--fetch", "-f", help="Stream skill content on-demand into memory")
    parser.add_argument("--verify", "-v", help="Execute test command and verify evidence")
    parser.add_argument("--list", "-l", action="store_true", help="List 32 categories")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    if args.list:
        print("SkillNote 32 Capability Categories:")
        for c in sorted(CATEGORIES):
            print(f"  • {c}")
        return

    if args.search:
        results = search_skills(args.search)
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print(f"Top matching skills for '{args.search}':")
            for idx, r in enumerate(results, 1):
                print(f"[{idx}] {r['title']} ({r['category']}/{r['name']})")
                print(f"    Path: {r['path']}")
                print(f"    Desc: {r['description']}...\n")
        return

    if args.fetch:
        try:
            content = fetch_skill_content(args.fetch)
            print(content)
        except Exception as e:
            print(f"Error streaming skill '{args.fetch}': {e}", file=sys.stderr)
            sys.exit(1)
        return

    if args.verify:
        ev = verify_command(args.verify)
        if args.json:
            print(json.dumps(ev, indent=2))
        else:
            print(f"VERIFICATION RESULT: {ev['status']} (Exit Code: {ev['exit_code']}, Time: {ev['duration']})")
            if ev.get("stdout"):
                print("--- Output ---")
                print(ev["stdout"])
        return

    task = " ".join(args.query).strip()
    if not task:
        parser.print_help()
        return

    # Check if category
    if task.lower() in CATEGORIES:
        cat = task.lower()
        skills = search_skills(cat, limit=5, category=cat)
        print(f"SkillNote Category: {cat.upper()} (Zero-Disk Cloud Streaming)")
        print(f"Showing top {len(skills)} relevant skills in category:")
        for idx, s in enumerate(skills, 1):
            print(f"  [{idx}] {s['title']} ({s['path']})")
        return

    # Task adaptive routing
    mode, budget, desc = classify_complexity(task)
    skills = search_skills(task, limit=3)

    print("=" * 70)
    print("  SKILLNOTE ADAPTIVE COGNITIVE RUNTIME (Zero-Disk Mode)")
    print(f"  Task: \"{task}\"")
    print(f"  Active Mode: {mode.upper()} (Token Budget: ~{budget})")
    print(f"  Strategy:    {desc}")
    print("=" * 70)
    print("\nOn-Demand Retrieved Skills (Streamed in RAM, 0 files on disk):")
    for idx, s in enumerate(skills, 1):
        print(f"  [{idx}] {s['title']} ({s['category']}/{s['name']})")
        print(f"      Path: {s['path']}")
        print(f"      Desc: {s['description']}...\n")
    print("=" * 70)
    print("EVIDENCE RULE: Proof before claims. Record real test commands & exit codes.")
    print("=" * 70)


if __name__ == "__main__":
    main()
