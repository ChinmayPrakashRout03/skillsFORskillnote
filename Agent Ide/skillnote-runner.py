#!/usr/bin/env python3
"""
SkillNote Universal Agent IDE Runner & Adaptive Runtime
Maintained solely and independently by Chinmay Prakash Rout (ChinmayPrakashRout03)
GitHub: https://github.com/ChinmayPrakashRout03/skillsFORskillnote

Principle: "Load less. Execute more. Verify everything. Restrict only what is necessary."
"""

import sys
import os
import json
import argparse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

SKILLS_DIR = BASE_DIR / "skills"

# Import adaptive runtime components
try:
    from runtime.indexer import DB_PATH, get_stats, index_skills
    from runtime.router import route_request, search_skills, CATEGORIES
    from runtime.verifier import execute_verification_check, format_evidence_markdown
    from runtime.context_controller import build_adaptive_context
    HAS_ADAPTIVE_RUNTIME = True
except ImportError:
    HAS_ADAPTIVE_RUNTIME = False


def print_list(categories):
    print("=" * 80)
    print("  SKILLNOTE AGENT IDE — 32 CAPABILITY CATEGORIES")
    print("  Maintained by: Chinmay Prakash Rout (ChinmayPrakashRout03)")
    print("  Repository: https://github.com/ChinmayPrakashRout03/skillsFORskillnote")
    print("=" * 80)
    print(f"{'Category':<16} {'Skills':<8} {'Folder':<16} {'Description'}")
    print("-" * 80)
    for cat_name, info in sorted(categories.items()):
        desc = info.get("description", "")
        if len(desc) > 38:
            desc = desc[:35] + "..."
        print(f"{cat_name:<16} {info.get('count', 0):<8} {info.get('folder', cat_name):<16} {desc}")
    print("-" * 80)
    total_skills = sum(c.get("count", 0) for c in categories.values())
    print(f"Total categories: {len(categories)} | Total primary skill files: {total_skills}")
    if HAS_ADAPTIVE_RUNTIME and DB_PATH.exists():
        stats = get_stats(DB_PATH)
        print(f"Indexed SQLite FTS5 Catalog: {stats['total_files']} files ({DB_PATH.name})")
    print("=" * 80)


def scan_categories_fallback():
    categories = {}
    if not SKILLS_DIR.exists():
        return categories
    for item in sorted(SKILLS_DIR.iterdir()):
        if item.is_dir() and not item.name.startswith("."):
            cat_name = item.name.lower()
            files = [f.name for f in item.iterdir() if f.is_file() and f.suffix in [".md", ".mdc", ".skill"]]
            categories[cat_name] = {
                "name": cat_name,
                "folder": item.name,
                "path": str(item),
                "count": len(files),
                "skills": sorted(files),
                "description": f"Skills in {item.name}"
            }
    return categories


def main():
    parser = argparse.ArgumentParser(
        description="SkillNote Universal Runner & Adaptive Runtime (Claude Code, Codex, Antigravity, OpenCode, Z Code)"
    )
    parser.add_argument("target", nargs="*", help="Category name (e.g., adapt, secure) or full prompt")
    parser.add_argument("--all", "-a", action="store_true", help="Run/list all skills in large categories without relevance filtering")
    parser.add_argument("--list", "-l", action="store_true", help="List all 32 categories and catalog stats")
    parser.add_argument("--search", "-s", help="Full-text search catalog with BM25 ranking")
    parser.add_argument("--verify", "-v", help="Run shell command and record verifiable evidence")
    parser.add_argument("--json", action="store_true", help="Output as structured JSON")
    args = parser.parse_args()

    # Ensure database is indexed
    if HAS_ADAPTIVE_RUNTIME and not DB_PATH.exists() and SKILLS_DIR.exists():
        index_skills(SKILLS_DIR, DB_PATH)

    if args.list:
        categories = scan_categories_fallback()
        if args.json:
            print(json.dumps(categories, indent=2))
        else:
            print_list(categories)
        return

    if args.search:
        results = search_skills(args.search, limit=5, db_path=DB_PATH)
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print("=" * 80)
            print(f"  SKILLNOTE BM25 SEARCH: \"{args.search}\"")
            print("=" * 80)
            for idx, r in enumerate(results, 1):
                print(f"[{idx}] {r['title']} ({r['category']}/{r['name']})")
                print(f"    Path:   {r['rel_path']}")
                print(f"    Tokens: ~{r['token_estimate']} | Score: {r['rank']:.2f}")
                print(f"    Desc:   {r['description'][:110]}...\n")
        return

    if args.verify:
        evidence = execute_verification_check(args.verify)
        if args.json:
            print(json.dumps(evidence, indent=2))
        else:
            print(format_evidence_markdown(evidence))
        return

    query = " ".join(args.target).strip()
    if not query:
        categories = scan_categories_fallback()
        print_list(categories)
        print("\nUsage:")
        print("  python3 skillnote-runner.py adapt                  # Targeted sequential category pipeline")
        print("  python3 skillnote-runner.py \"fix null pointer\"     # Adaptive routing (Micro/Standard/Complex/Experimental)")
        print("  python3 skillnote-runner.py --search \"auth jwt\"     # Search catalog with BM25 ranking")
        print("  python3 skillnote-runner.py --verify \"pytest\"       # Execute test and record evidence")
        return

    # Adaptive routing
    if HAS_ADAPTIVE_RUNTIME:
        result = route_request(query, DB_PATH)
        if args.json:
            print(json.dumps(result, indent=2))
            return

        if result["type"] == "category_pipeline":
            cat_name = result["category"]
            cat_folder = SKILLS_DIR / cat_name.capitalize()
            if not cat_folder.exists():
                cat_folder = SKILLS_DIR / cat_name
            files = sorted([f.name for f in cat_folder.iterdir() if f.is_file() and f.suffix in [".md", ".mdc", ".skill"]])
            
            is_large = len(files) > 50
            display_files = files
            if is_large and not args.all:
                display_files = files[:5]

            print("=" * 80)
            if is_large and not args.all:
                print(f"  SKILLNOTE MODE 2: TARGETED CATEGORY (RELEVANCE-FILTERED)")
                print(f"  Category: {cat_name.upper()} ({len(files)} total skills in catalog)")
                print(f"  Showing top {len(display_files)} skills (pass --all to show all {len(files)})")
            else:
                print(f"  SKILLNOTE MODE 2: TARGETED CATEGORY PIPELINE")
                print(f"  Category: {cat_name.upper()} (Folder: {cat_folder.name})")
                print(f"  Total Skills to Execute Sequentially: {len(display_files)}")
            print("=" * 80)
            for idx, skill in enumerate(display_files, 1):
                print(f"  [{idx:02d}/{len(display_files):02d}] {skill}")
                print(f"        Path: {cat_folder / skill}")
            print("\n" + "=" * 80)
            print("  INSTRUCTION FOR AGENT:")
            print("  1. Read and apply the instructions from the skills above.")
            print("  2. Provide observable evidence (exit codes, test logs) for verification claims.")
            print("=" * 80)
        else:
            print("=" * 80)
            print("  SKILLNOTE ADAPTIVE RUNTIME")
            print(f"  Task: \"{query}\"")
            print(f"  Maintained by: Chinmay Prakash Rout (ChinmayPrakashRout03)")
            print("=" * 80)
            print(f"▶ CLASSIFIED MODE: {result['mode'].upper()}")
            print(f"  Token Budget:    {result['token_budget']} tokens")
            print(f"  Strategy:        {result['mode_description']}")
            print(f"  Selected Skills: {result['selected_skills_count']} loaded on-demand (0.5ms SQLite FTS5)\n")

            for idx, s in enumerate(result["selected_skills"], 1):
                print(f"  [{idx}] {s['title']} ({s['category']}/{s['name']})")
                print(f"      Path:   {s['rel_path']}")
                print(f"      Tokens: ~{s['tokens']} tokens")
                print(f"      Desc:   {s['description'][:100]}...\n")
            print("=" * 80)
            print("  EVIDENCE RULE: Proof before claims. If no test command executed, mark as 'NOT VERIFIED'.")
            print("=" * 80)
    else:
        print("Fallback runner mode (runtime module not available).")


if __name__ == "__main__":
    main()
