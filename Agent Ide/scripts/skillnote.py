#!/usr/bin/env python3
"""
SkillNote Adaptive Runtime — Master CLI
Maintained solely and independently by Chinmay Prakash Rout (ChinmayPrakashRout03)
GitHub: https://github.com/ChinmayPrakashRout03/skillsFORskillnote

Principle: "Load less. Execute more. Verify everything. Restrict only what is necessary."
"""

import sys
import os
import argparse
import json
from pathlib import Path

# Add runtime directory to path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from runtime.indexer import index_skills, get_stats, DB_PATH
from runtime.router import route_request, search_skills, classify_task_mode
from runtime.verifier import execute_verification_check, format_evidence_markdown
from runtime.context_controller import build_adaptive_context


def cmd_index(args):
    lib_dir = Path(args.library) if args.library else BASE_DIR / "skills"
    if not lib_dir.exists():
        print(f"Error: Library directory not found at {lib_dir}")
        sys.exit(1)
    
    print(f"Indexing skills from: {lib_dir}")
    count = index_skills(lib_dir, DB_PATH)
    stats = get_stats(DB_PATH)
    print(f"✔ Successfully indexed {count} skills.")
    print(f"  Total Catalog: {stats['total_files']} files | {stats['categories']} categories | {stats['primary_skills']} primary skills")
    print(f"  SQLite Index: {DB_PATH}")


def cmd_search(args):
    results = search_skills(args.query, limit=args.limit, db_path=DB_PATH)
    if args.json:
        print(json.dumps(results, indent=2))
        return

    print("=" * 80)
    print(f"  SKILLNOTE FTS5 SEARCH: \"{args.query}\"")
    print(f"  Catalog: {DB_PATH}")
    print("=" * 80)
    if not results:
        print("No matching skills found in catalog.")
        return

    for idx, r in enumerate(results, 1):
        print(f"[{idx}] {r['title']} ({r['category']}/{r['name']})")
        print(f"    Path:   {r['rel_path']}")
        print(f"    Tokens: ~{r['token_estimate']} tokens | BM25 Rank: {r['rank']:.2f}")
        print(f"    Desc:   {r['description'][:120]}...\n")


def cmd_route(args):
    query = " ".join(args.prompt).strip()
    if not query:
        print("Error: Please provide a prompt or category to route.")
        sys.exit(1)

    result = route_request(query, DB_PATH)
    if args.json:
        print(json.dumps(result, indent=2))
        return

    print("=" * 80)
    print(f"  SKILLNOTE ADAPTIVE ROUTER")
    print(f"  Input: \"{query}\"")
    print("=" * 80)

    if result["type"] == "category_pipeline":
        print(f"▶ ROUTE: Targeted Category Pipeline ({result['category'].upper()})")
        print(f"  Mode: {result['mode']}")
        print(f"  Description: {result['description']}")
        print("\n  Run `python3 skillnote-runner.py " + result["category"] + "` to view full sequential pipeline.")
    else:
        print(f"▶ ROUTE: Adaptive Task Routing")
        print(f"  Classified Mode: {result['mode'].upper()}")
        print(f"  Token Budget:    {result['token_budget']} tokens")
        print(f"  Strategy:        {result['mode_description']}")
        print(f"  Selected Skills: {result['selected_skills_count']} loaded on-demand\n")

        for idx, s in enumerate(result["selected_skills"], 1):
            print(f"  [{idx}] {s['title']} ({s['category']}/{s['name']})")
            print(f"      Path:   {s['rel_path']}")
            print(f"      Tokens: ~{s['tokens']} tokens")
            print(f"      Desc:   {s['description'][:100]}...\n")


def cmd_verify(args):
    if not args.command:
        print("Error: Please provide a command to verify using --command '<cmd>'")
        sys.exit(1)

    proj_dir = args.project if args.project else "."
    print(f"Executing verification check: \"{args.command}\" in {proj_dir}...")
    evidence = execute_verification_check(
        command=args.command,
        project_dir=proj_dir,
        check_name=args.name or "Automated Check"
    )

    if args.json:
        print(json.dumps(evidence, indent=2))
    else:
        print(format_evidence_markdown(evidence))


def cmd_context(args):
    query = " ".join(args.prompt).strip()
    result = route_request(query, DB_PATH)
    ctx = build_adaptive_context(result)
    print(ctx)


def main():
    parser = argparse.ArgumentParser(
        description="SkillNote Adaptive Runtime (Smart Router, Context Controller, Verification Engine)"
    )
    subparsers = parser.add_subparsers(dest="subcommand", help="Adaptive Runtime subcommands")

    # index
    p_index = subparsers.add_parser("index", help="Index all skills into SQLite FTS5 catalog")
    p_index.add_argument("--library", "-l", help="Path to skills library directory")

    # search
    p_search = subparsers.add_parser("search", help="Search skills using SQLite FTS5 BM25")
    p_search.add_argument("query", help="Search keywords")
    p_search.add_argument("--limit", type=int, default=5, help="Number of results")
    p_search.add_argument("--json", action="store_true", help="Output JSON")

    # route
    p_route = subparsers.add_parser("route", help="Classify task complexity and route to selected skills")
    p_route.add_argument("prompt", nargs="+", help="User task or category")
    p_route.add_argument("--json", action="store_true", help="Output JSON")

    # verify
    p_verify = subparsers.add_parser("verify", help="Execute real command and record verifiable evidence")
    p_verify.add_argument("--command", "-c", required=True, help="Shell command to execute")
    p_verify.add_argument("--project", "-p", default=".", help="Project directory")
    p_verify.add_argument("--name", "-n", default="Verification Check", help="Name of check")
    p_verify.add_argument("--json", action="store_true", help="Output JSON")

    # context
    p_ctx = subparsers.add_parser("context", help="Generate minimal adaptive prompt payload")
    p_ctx.add_argument("prompt", nargs="+", help="Task prompt")

    args = parser.parse_args()

    if not args.subcommand:
        parser.print_help()
        return

    # Auto-index if database does not exist
    if not DB_PATH.exists() and args.subcommand != "index":
        print(f"Catalog database not found. Auto-indexing skills library...")
        lib_dir = BASE_DIR / "skills"
        if lib_dir.exists():
            index_skills(lib_dir, DB_PATH)

    if args.subcommand == "index":
        cmd_index(args)
    elif args.subcommand == "search":
        cmd_search(args)
    elif args.subcommand == "route":
        cmd_route(args)
    elif args.subcommand == "verify":
        cmd_verify(args)
    elif args.subcommand == "context":
        cmd_context(args)


if __name__ == "__main__":
    main()
