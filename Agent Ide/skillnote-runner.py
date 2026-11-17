#!/usr/bin/env python3
"""
SkillNote Universal Agent IDE Runner
Maintained solely and independently by Chinmay Prakash Rout (ChinmayPrakashRout03)
GitHub: https://github.com/ChinmayPrakashRout03/skillsFORskillnote

This script serves as the universal dispatcher for the /skillnote command across:
- Claude Code
- OpenAI Codex
- Antigravity
- OpenCode
- Z Code (Zed AI)
"""

import sys
import os
import json
import argparse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SKILLS_DIR = BASE_DIR / "skills"

# Category descriptions and primary pipeline objectives
CATEGORY_METADATA = {
    "adapt": {
        "folder": "Adapt",
        "description": "Senior-dev minimalism, shortcut debt removal, and repo hygiene.",
        "skills_order": [
            "audit-repo-quality.md",
            "list-shortcut-debt.md",
            "review-change-quality.md",
            "lazy-senior-dev.md",
            "show-savings.md",
            "show-help.md"
        ]
    },
    "assist": {
        "folder": "Assist",
        "description": "Broad library assists, API integrations, and developer helpers."
    },
    "audit": {
        "folder": "Audit",
        "description": "Deep codebase vulnerability and security posture auditing.",
        "skills_order": ["audit-security.md"]
    },
    "automate": {
        "folder": "Automate",
        "description": "Autonomous pipelines, auto-merging, cron hooks, and triggers."
    },
    "beautify": {
        "folder": "Beautify",
        "description": "Tasteful frontend aesthetics, visual rhythm, and micro-interactions.",
        "skills_order": ["design-tasteful-frontend.md"]
    },
    "comprehend": {
        "folder": "Comprehend",
        "description": "Codebase indexing, knowledge graphs, architecture maps, and developer guides.",
        "skills_order": [
            "ask-codebase.md",
            "build-knowledge-graph.md",
            "explain-code.md",
            "explain-diff.md",
            "extract-domain-knowledge.md",
            "graph-knowledge-base.md",
            "open-knowledge-dashboard.md",
            "write-onboarding-guide.md"
        ]
    },
    "contextualize": {
        "folder": "Contextualize",
        "description": "Context degradation mitigation, mental state modeling, and prompt tuning."
    },
    "convert": {
        "folder": "Convert",
        "description": "Converting specs, books, and RFCs into executable agent skills.",
        "skills_order": ["convert-book-to-skill.md"]
    },
    "create": {
        "folder": "Create",
        "description": "Architecture decision records, bootstrap agents, and strategy synthesis."
    },
    "curate": {
        "folder": "Curate",
        "description": "MCP server creation, brand management, themes, and visual artifacts."
    },
    "design": {
        "folder": "Design",
        "description": "Frontend system design, layout architecture, and typography standards.",
        "skills_order": ["design-frontend.md"]
    },
    "develop": {
        "folder": "Develop",
        "description": "Interactive components, QA frameworks, and browser automation."
    },
    "engineer": {
        "folder": "Engineer",
        "description": "API design, observability, refactoring, quality constraints, and debugging.",
        "skills_order": [
            "break-down-tasks.md",
            "design-apis.md",
            "build-frontend-ui.md",
            "add-observability.md",
            "debugging.md",
            "adversarial-review.md",
            "deprecate-and-migrate.md"
        ]
    },
    "execute": {
        "folder": "Execute",
        "description": "Multi-step autonomous plan execution and milestone verification."
    },
    "guide": {
        "folder": "Guide",
        "description": "Project coding standards, defensive patterns, and Cursor rules.",
        "skills_order": [
            "coding-guidelines.md",
            "coding-guidelines-project.md",
            "coding-guidelines-cursor.mdc"
        ]
    },
    "humanize": {
        "folder": "Humanize",
        "description": "Removal of synthetic AI jargon and calibration of natural human writing.",
        "skills_order": [
            "humanize-writing.md",
            "humanize-writing-claude.md",
            "humanize-writing-single-file.md",
            "humanize-writing.skill"
        ]
    },
    "manage": {
        "folder": "Manage",
        "description": "Pull request validation, issue triage, and product evaluation."
    },
    "minimize": {
        "folder": "Minimize",
        "description": "Code reduction, token savings, and senior engineering restraint.",
        "skills_order": [
            "audit-repo-quality.md",
            "list-shortcut-debt.md",
            "review-change-quality.md",
            "lazy-senior-dev.md",
            "show-savings.md",
            "show-help.md"
        ]
    },
    "navigate": {
        "folder": "Navigate",
        "description": "Git safety guardrails, task decomposition, and architecture navigation."
    },
    "official": {
        "folder": "Official",
        "description": "Core Anthropic & foundational agent skills (MCP, Office, Art, Artifacts).",
        "skills_order": [
            "skill-creator.md",
            "mcp-builder.md",
            "frontend-design.md",
            "web-artifacts-builder.md",
            "edit-docx.md",
            "edit-pdf.md",
            "edit-pptx.md",
            "edit-xlsx.md",
            "algorithmic-art.md",
            "doc-coauthoring.md",
            "discernment-nudge.md",
            "academy-guide.md",
            "slack-gif-creator.md"
        ]
    },
    "optimize": {
        "folder": "Optimize",
        "description": "Token compression, lean code generation, and performance profiling."
    },
    "orchestrate": {
        "folder": "Orchestrate",
        "description": "Multi-agent coordination, execution plans, and phase gates."
    },
    "prototype": {
        "folder": "Prototype",
        "description": "Rapid MVP validation, technical design, and vertical slices.",
        "skills_order": [
            "research-app-idea.md",
            "write-mvp-prd.md",
            "write-mvp-tech-design.md",
            "select-workflow.md",
            "implement-project-slice.md",
            "add-bounded-feature.md",
            "verify-against-acceptance-criteria.md",
            "diagnose-and-fix-failure.md",
            "review-proposed-change.md",
            "prepare-handoff-context.md",
            "create-agent-instructions.md"
        ]
    },
    "refine": {
        "folder": "Refine",
        "description": "AI slop removal, comment cleanup, and human ergonomics.",
        "skills_order": [
            "clean-code-comments.md",
            "stop-ai-slop.md",
            "stop-ai-slop-pointer.md",
            "stop-ai-slop-cursor.mdc",
            "design-ui-without-slop.md",
            "design-for-real-people.md",
            "design-mobile-layout.md",
            "write-copy-without-slop.md"
        ]
    },
    "secure": {
        "folder": "Secure",
        "description": "Complete 5-stage defensive security, OWASP, pentesting, and remediation.",
        "skills_order": [
            "test-app-security.md",
            "test-owasp-top-10.md",
            "find-code-vulnerabilities.md",
            "pentest-web-app.md",
            "fix-vulnerabilities.md"
        ]
    },
    "simplify": {
        "folder": "Simplify",
        "description": "High-signal, scannable, ADHD-friendly documentation.",
        "skills_order": ["write-for-adhd.md"]
    },
    "simulate": {
        "folder": "Simulate",
        "description": "Realistic mock environments and simulation UIs.",
        "skills_order": ["build-faux-product-ui.md"]
    },
    "style": {
        "folder": "Style",
        "description": "Design systems, Tailwind/CSS styling, brand graphics, and slides.",
        "skills_order": [
            "build-design-system.md",
            "design-ui-ux.md",
            "style-ui.md",
            "manage-brand.md",
            "design-banners.md",
            "build-slides.md"
        ]
    },
    "systematize": {
        "folder": "Systematize",
        "description": "TDD, plan authoring, subagent dispatch, review triage, and git finish.",
        "skills_order": [
            "brainstorm.md",
            "write-plans.md",
            "test-first.md",
            "develop-with-subagents.md",
            "dispatch-parallel-agents.md",
            "execute-plans.md",
            "debug-systematically.md",
            "diagnose-session.md",
            "request-code-review.md",
            "receive-code-review.md",
            "verify-before-completion.md",
            "finish-branch.md",
            "use-git-worktrees.md",
            "use-superpowers.md",
            "write-skills.md"
        ]
    },
    "versatile": {
        "folder": "Versatile",
        "description": "Deep domain capabilities across languages, frameworks, and cloud infrastructure."
    },
    "visualize": {
        "folder": "Visualize",
        "description": "Mermaid/ASCII architecture diagrams, test value maps, and evidence reviews.",
        "skills_order": [
            "make-diagrams.md",
            "tune-diagram-accuracy.md",
            "simplify-codebase.md",
            "improve-test-value.md",
            "review-with-evidence.md"
        ]
    },
    "workflow": {
        "folder": "Workflow",
        "description": "Complete modern cloud/web workflows, database, API, CI/CD, and architecture.",
        "skills_order": [
            "analyzing-projects.md",
            "designing-architecture.md",
            "database-design.md",
            "convex-backend.md",
            "designing-apis.md",
            "security-patterns.md",
            "web-design-guidelines.md",
            "vercel-react-best-practices.md",
            "designing-tests.md",
            "optimizing-performance.md",
            "error-handling.md",
            "parallel-execution.md",
            "managing-git.md",
            "devops-infrastructure.md"
        ]
    }
}


def scan_categories():
    """Scans the filesystem and indexes all skills per category."""
    categories = {}
    if not SKILLS_DIR.exists():
        return categories

    for item in sorted(SKILLS_DIR.iterdir()):
        if item.is_dir():
            cat_name = item.name.lower()
            skill_files = sorted([
                f.name for f in item.iterdir()
                if f.is_file() and (f.suffix in [".md", ".mdc", ".skill"])
            ])
            subdirs = sorted([
                d.name for d in item.iterdir() if d.is_dir()
            ])
            
            meta = CATEGORY_METADATA.get(cat_name, {})
            skills_order = meta.get("skills_order", skill_files)
            # Ensure all files are in the order list
            ordered = [s for s in skills_order if s in skill_files]
            remaining = [s for s in skill_files if s not in ordered]
            final_order = ordered + remaining

            categories[cat_name] = {
                "name": cat_name,
                "folder": item.name,
                "path": str(item),
                "description": meta.get("description", f"Skills for {item.name}."),
                "count": len(skill_files),
                "skills": final_order,
                "subdirs_count": len(subdirs)
            }
    return categories


def print_list(categories):
    print("=" * 80)
    print("  SKILLNOTE AGENT IDE — 32 CAPABILITY CATEGORIES")
    print("  Maintained by: Chinmay Prakash Rout (ChinmayPrakashRout03)")
    print("  Repository: https://github.com/ChinmayPrakashRout03/skillsFORskillnote")
    print("=" * 80)
    print(f"{'Category':<16} {'Skills':<8} {'Folder':<16} {'Description'}")
    print("-" * 80)
    for cat_name, info in sorted(categories.items()):
        desc = info["description"]
        if len(desc) > 38:
            desc = desc[:35] + "..."
        print(f"{cat_name:<16} {info['count']:<8} {info['folder']:<16} {desc}")
    print("-" * 80)
    total_skills = sum(c["count"] for c in categories.values())
    print(f"Total categories: {len(categories)} | Total primary skill files: {total_skills}")
    print("=" * 80)


def print_targeted_pipeline(cat_name, info):
    print("=" * 80)
    print(f"  SKILLNOTE MODE 2: TARGETED CATEGORY PIPELINE")
    print(f"  Category: {cat_name.upper()} (Folder: {info['folder']})")
    print(f"  Description: {info['description']}")
    print(f"  Total Skills to Execute Sequentially: {info['count']}")
    print("=" * 80)
    print("\n▶ EXECUTION SEQUENCE (Execute ONE BY ONE in strict order):\n")
    for idx, skill in enumerate(info["skills"], 1):
        skill_path = Path(info["path"]) / skill
        print(f"  [{idx:02d}/{info['count']:02d}] {skill}")
        print(f"        Path: {skill_path}")
    print("\n" + "=" * 80)
    print("  INSTRUCTION FOR AGENT:")
    print("  1. Read and apply the instructions from each skill above in sequential order.")
    print("  2. Do not skip any skill.")
    print("  3. Report progress after each skill, detailing changes and checks made.")
    print("  4. Provide a consolidated summary and verification proof at completion.")
    print("=" * 80)


def print_global_pipeline(prompt, categories):
    print("=" * 80)
    print("  SKILLNOTE MODE 1: GLOBAL ORCHESTRATION")
    print(f"  Prompt: \"{prompt}\"")
    print("  Maintained by: Chinmay Prakash Rout (ChinmayPrakashRout03)")
    print("=" * 80)
    print("\n▶ ASSEMBLED MULTI-PHASE ENGINEERING LIFECYCLE:\n")
    phases = [
        ("Phase 1: Comprehend & Contextualize", ["Comprehend", "Contextualize", "Navigate"],
         "Scan codebase, extract domain models, establish dependency graphs, and prevent context drift."),
        ("Phase 2: Architecture & Specification", ["Design", "Prototype", "Visualize", "Style", "Beautify"],
         "Formulate technical specifications, component hierarchy, UI/UX tokens, and Mermaid diagrams."),
        ("Phase 3: Implementation & Synthesis", ["Develop", "Engineer", "Create", "Convert"],
         "Write clean, modular, typed production code following Guide standards."),
        ("Phase 4: Automation & Execution", ["Automate", "Execute", "Workflow", "Simulate"],
         "Build automated tests, run build scripts, verify edge cases, and ensure runtime correctness."),
        ("Phase 5: Security, Refinement & Optimization", ["Audit", "Secure", "Refine", "Optimize", "Minimize", "Simplify"],
         "Perform OWASP security scan, strip AI slop/boilerplate, compress tokens, and optimize latency."),
        ("Phase 6: Delivery & Systematization", ["Systematize", "Manage", "Humanize", "Curate", "Official", "Adapt"],
         "Verify acceptance criteria, squash clean git commits, humanize docs, and prepare PR.")
    ]
    for phase_name, assigned_cats, objective in phases:
        print(f"  ● {phase_name}")
        print(f"    Categories: {', '.join(assigned_cats)}")
        print(f"    Objective:  {objective}\n")
    print("=" * 80)
    print("  INSTRUCTION FOR AGENT:")
    print("  Execute all 6 phases systematically with rigorous verification before declaring completion.")
    print("=" * 80)


def main():
    parser = argparse.ArgumentParser(
        description="SkillNote Universal Runner for Agent IDEs (Claude Code, Codex, Antigravity, OpenCode, Z Code)"
    )
    parser.add_argument("target", nargs="*", help="Category name (e.g., adapt, secure) or full prompt")
    parser.add_argument("--list", "-l", action="store_true", help="List all 32 categories and skill counts")
    parser.add_argument("--json", action="store_true", help="Output information as structured JSON")
    args = parser.parse_args()

    categories = scan_categories()

    if args.list:
        if args.json:
            print(json.dumps(categories, indent=2))
        else:
            print_list(categories)
        return

    query = " ".join(args.target).strip()
    if not query:
        print_list(categories)
        print("\nUsage:")
        print("  python3 skillnote-runner.py adapt          # Run targeted pipeline for a category")
        print("  python3 skillnote-runner.py <prompt>       # Run global orchestration for any task")
        print("  python3 skillnote-runner.py --list         # List all 32 categories")
        return

    # Check if query matches a known category
    norm_query = query.lower()
    if norm_query in categories:
        info = categories[norm_query]
        if args.json:
            print(json.dumps({"mode": "targeted", "category": norm_query, **info}, indent=2))
        else:
            print_targeted_pipeline(norm_query, info)
    else:
        # Mode 1: Global Orchestration
        if args.json:
            print(json.dumps({
                "mode": "global",
                "prompt": query,
                "categories_count": len(categories)
            }, indent=2))
        else:
            print_global_pipeline(query, categories)


if __name__ == "__main__":
    main()
