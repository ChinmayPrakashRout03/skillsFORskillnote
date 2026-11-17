# skillsFORskillnote

> **Curated, standardized, and maintained solely and independently by [Chinmay Prakash Rout](https://github.com/ChinmayPrakashRout03)**  
> **Repository**: [https://github.com/ChinmayPrakashRout03/skillsFORskillnote](https://github.com/ChinmayPrakashRout03/skillsFORskillnote)

---

## ⚡ Quick Install (Zero Download Needed)

Any user on macOS or Linux can install SkillNote across all AI coding agents (**Antigravity**, **Claude Code**, **OpenCode**, **OpenAI Codex**, and **Zed AI**) with a single terminal command — **without manually cloning or downloading the repository**:

```bash
curl -fsSL https://raw.githubusercontent.com/ChinmayPrakashRout03/skillsFORskillnote/main/install.sh | bash
```

This automatically:
1. Installs the **SkillNote Adaptive Runtime** and pre-indexed SQLite FTS5 catalog.
2. Configures the `/skillnote` slash command across all active AI coding agents.
3. Provides a global `skillnote` CLI command in your terminal (`skillnote search`, `skillnote route`, `skillnote verify`).

---

Skills from 32 open-source repositories, reorganized by functional category and curated for local host/IDE use (v14: v13 plus 7 repos — aeon, context-engineering, awesome-copilot, anthropics, jwynia, qodex, claude-workflow-v2).

Upstream repositories and revisions:
- https://github.com/open-gsd/gsd-core — commit `d1ae72c4de1c2a890aef0a2cdfa60f19152eda36`
- https://github.com/multica-ai/andrej-karpathy-skills — commit `2c606141936f1eeef17fa3043a72095b4765b9c2`
- https://github.com/udaysharmadev/Not-Ai — commit `b35270e310b5f8ec626122926cdce1b2a4d0a78e` (not-ai v4.0.0)
- https://github.com/addyosmani/agent-skills — commit `39b723ceebf81474d0557c1fecd01eddab585563` (v0.6.16)
- https://github.com/obra/superpowers — commit `22f0b463e7a5e579904dd6211a520321035526f7` (v7.0.2)
- https://github.com/mattpocock/skills — commit `5863806dd4e15c63174bee4e7515a4256792ecfa`
- https://github.com/dietrichgebert/ponytail — commit `96608e078b2d5ea607c5c3b8b5a54d1c1fba6846` (v5.3.3)
- https://github.com/nextlevelbuilder/ui-ux-pro-max-skill — commit `d643997c82e94742dd3bee43210b0198e8bbba3d` (v2.15.0)
- https://github.com/Graphify-Labs/graphify — commit `52cb28218eea0c68d80a9f4b2ae102d2fa63e267` (checked: no skills, see below)
- https://github.com/juliusbrussee/caveman — commit `b4ee71d557d96e3cbc14f88fa6e953a1362865f5`
- https://github.com/Egonex-AI/Understand-Anything — commit `5cc4aad9b8b43596dfedaee00755a7223825fe9b`
- https://github.com/ComposioHQ/awesome-claude-skills — commit `be2a406907dbc61b73e6827ded415c96139d13a2`
- https://github.com/tt-a1i/archify — commit `e37848822238e3a61b12739185cdadd49843a620`
- https://github.com/pbakaus/impeccable — commit `1995764b4936f2bfbf4eb719cb37b384a45ceacb`
- https://github.com/Leonxlnx/taste-skill — commit `f6b76575f949707b4e3c37cd86cb44b0b98643e8` (tasteskill v2.5.1)
- https://github.com/paperclipai/paperclip — commit `890dcbdd66f177dcdd6fc724f7a87b590060589b`
- https://github.com/cloudflare/security-audit-skill — commit `c1c8a8c1471069fb0e188eeaff69b8e8db6564a8`
- https://github.com/ayghri/i-have-adhd — commit `1ecea1993b7fce257ffbd686c070948b5e07eda6`
- https://github.com/Nutlope/hallmark — commit `04977e15f3dfd6ee4b74c887dac3eb52665d6c92`
- https://github.com/sickn33/agentic-awesome-skills — commit `560b762c309d6b96315855d7968727d3bca7df20`
- https://github.com/virgiliojr94/book-to-skill — commit `e7bb659d3261491c8b28793dcb9102fa64a46c22`
- https://github.com/miqdadbadjuber/anti-slop — commit `35b54dc660aa7d11428ee62c5788ad36bc18ac3c`
- https://github.com/usestrix/strix — commit `4719329d1c3eb0db796714397551945c514a2301`
- https://github.com/benjitaylor/skills — commit `299140fafd08df55a9c234e610c3f64af3f45531` (stageshow v1.1.1)
- https://github.com/KhazP/vibe-coding-prompt-template — commit `d26fb0d8a9cdac94cf99f004087620487e4da33d` (v3.2.0, 11 skills)
- https://github.com/aeonfun/aeon — commit `7b20c9595955bfb3a0f7798aef35749e758b0405` (94 skills)
- https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering — commit `9ff0c99108b36d3b886defd825d8ac1f47dba374` (20 skills)
- https://github.com/github/awesome-copilot — commit `8ecd5b17f02fe5fbebf35eccd1867265eded811f` (481 skills)
- https://github.com/anthropics/skills — commit `1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064` (20 skills, 6 duplicates skipped)
- https://github.com/jwynia/agent-skills — commit `e02ec7e226a6e4f8419fd3b88a1d8e472d421b32` (119 skills)
- https://github.com/qodex-ai/ai-agent-skills — commit `6ea9f00885c5dc5e6d9435d443dbf7d9ce865e29` (80 new skills)
- https://github.com/CloudAI-X/claude-workflow-v2 — commit `3b5a89ec1c106dd387e372aec073f9401336382a` (14 skills)

**15899 skill files in total (3708 unique skills).**


## Directory Structure & Behaviour Mapping

Each repository's skills have been reorganized into a dedicated top-level folder named by its functional role:

| Folder | Role / Category | Upstream Source Repository |
| :--- | :--- | :--- |
| `Adapt/` | Adapt | `dietrichgebert/ponytail` (OpenClaw variant) |
| `Assist/` | Assist | `github/awesome-copilot` |
| `Audit/` | Audit | `cloudflare/security-audit-skill` |
| `Automate/` | Automate | `aeonfun/aeon` |
| `Beautify/` | Beautify | `Leonxlnx/taste-skill` |
| `Comprehend/` | Comprehend | `Egonex-AI/Understand-Anything` |
| `Contextualize/` | Contextualize | `muratcankoylan/Agent-Skills-for-Context-Engineering` |
| `Convert/` | Convert | `virgiliojr94/book-to-skill` |
| `Create/` | Create | `jwynia/agent-skills` |
| `Curate/` | Curate | `ComposioHQ/awesome-claude-skills` |
| `Design/` | Design | `pbakaus/impeccable` |
| `Develop/` | Develop | `qodex-ai/ai-agent-skills` |
| `Engineer/` | Engineer | `addyosmani/agent-skills` |
| `Execute/` | Execute | `open-gsd/gsd-core` (Pi variant) |
| `Guide/` | Guide | `multica-ai/andrej-karpathy-skills` |
| `Humanize/` | Humanize | `udaysharmadev/Not-Ai` |
| `Manage/` | Manage | `paperclipai/paperclip` |
| `Minimize/` | Minimize | `dietrichgebert/ponytail` (main variant) |
| `Navigate/` | Navigate | `mattpocock/skills` |
| `Official/` | Official | `anthropics/skills` |
| `Optimize/` | Optimize | `juliusbrussee/caveman` |
| `Orchestrate/` | Orchestrate | `open-gsd/gsd-core` (Claude variant) |
| `Prototype/` | Prototype | `KhazP/vibe-coding-prompt-template` |
| `Refine/` | Refine | `miqdadbadjuber/anti-slop` |
| `Secure/` | Secure | `usestrix/strix` |
| `Simplify/` | Simplify | `ayghri/i-have-adhd` |
| `Simulate/` | Simulate | `benjitaylor/skills` (stageshow) |
| `Style/` | Style | `nextlevelbuilder/ui-ux-pro-max-skill` |
| `Systematize/` | Systematize | `obra/superpowers` |
| `Versatile/` | Versatile | `sickn33/agentic-awesome-skills` |
| `Visualize/` | Visualize | `tt-a1i/archify` |
| `Workflow/` | Workflow | `CloudAI-X/claude-workflow-v2` |

## Removed in v11

v11 removes **1172 skills** that each need a separate API key / token / MCP
connection / external service account and cannot run on the host IDE/agent model
alone. The full
list of removed skills, with the reason for each, is in `REMOVED_SKILLS.md` in
this zip.

By category:

- mcp-service-connection: 912
- service-api-key: 188
- api-teaching: 40
- llm-provider-key: 21
- cli-auth: 11

By repo:

- awesome: 836 (all 832 Composio app-automation skills + 4 curated skills)
- agentic-awesome-skills: 311
- paperclip: 17
- strix: 4
- caveman: 1
- hallmark: 1 (its only skill — the `hallmark/` folder is gone)
- ui-ux-pro-max: 1
- understand-anything: 1

## Removed in v14

v14 removes **75 skills** (76 zip paths — the aeon skill has two variant paths) from the 7 new repos, under the same rule as v11: each needs a separate API key / token / MCP connection / external service account and cannot run on the host IDE/agent model alone. 209 skills were reviewed (200 keyword candidates + 9 found by a supplementary grep); 134 were kept despite a key/token/service mention, each with its reason recorded in `REMOVE_LIST_V14.json` (`kept_ambiguous`). The full list of removed skills, with the reason for each, is in `REMOVED_SKILLS.md` in this zip.

By category:

- service-api-key: 33
- mcp-service-connection: 31
- llm-provider-key: 6
- api-teaching: 3
- cli-auth: 2

By repo:

- aeon: {'removed': 25, 'kept': 32} (incl. the aeon skill itself and get-started)
- awesome-copilot: {'removed': 34, 'kept': 81}
- qodex: {'removed': 9, 'kept': 3}
- jwynia: {'removed': 6, 'kept': 8}
- anthropics: {'removed': 1, 'kept': 2} (claude-api)
- context-engineering: {'removed': 0, 'kept': 3}
- claude-workflow-v2: {'removed': 0, 'kept': 5}

## gsd-core — 144 files (72 unique skills x 2 variants)

- `Orchestrate/` (formerly `claude/`) — the 72 skills from `skills/` (Claude Code version, `/gsd-*` invocation).
- `Execute/` (formerly `pi/`) — the same 72 skills from `pi/package-skills/` (Pi-adapted version, `/skill:gsd-*` invocation).

## andrej-karpathy-skills — 3 files (1 skill, 3 formats)

This repo contains exactly **1 skill** — `plugin.json` declares only
`"skills": ["./skills/karpathy-guidelines"]`, and it is the only `SKILL.md`
in the repo. The same guidelines are also shipped as a per-project `CLAUDE.md`
and a Cursor rule, so all three formats are included, labelled:

- `Guide/coding-guidelines.md` — the skill itself (`skills/karpathy-guidelines/SKILL.md`).
  Behaviour: reduce common LLM coding mistakes — think before coding, simplicity
  first, surgical changes, goal-driven execution with verifiable success criteria.
- `Guide/coding-guidelines-project.md` — same guidelines as `CLAUDE.md`.
- `Guide/coding-guidelines-cursor.mdc` — same guidelines as the Cursor rule
  (`.cursor/rules/karpathy-guidelines.mdc`, extension kept so Cursor can use it).

## Not-Ai — 43 files (1 skill, full package)

This repo contains exactly **1 skill** — `not-ai` v4.0.0. It is an editorial skill:
edit prose into a clear, specific, source-grounded version that preserves the author's
meaning and voice (humanizing stiff writing, removing generic phrasing, matching a
supplied voice sample, diagnosing robotic prose, drafting from notes). It explicitly
is NOT a detector-bypass tool and does not claim to prove authorship.

- `Humanize/humanize-writing.md` — the skill itself (`plugins/not-ai/skills/not-ai/SKILL.md`).
- `Humanize/reference/` — the skill's 17 reference manuals (already behaviour-named,
  e.g. `punctuation-and-prosody.md`, `voice-persistence.md`, `fidelity.md`).
  The SKILL.md links to these, so they are included to keep the skill complete.
- `Humanize/tools/` — the skill's 22 supporting Python tools (`gate.py` + `not_ai_core/`).
- `Humanize/humanize-writing-claude.md` — the Claude copy (`.claude/skills/not-ai.md`,
  byte-identical to the skill file).
- `Humanize/humanize-writing-single-file.md` — the built single-file skill (`dist/SKILL.md`,
  references inlined).
- `Humanize/humanize-writing.skill` — the official packaged skill archive (`dist/not-ai.skill`,
  itself a zip of SKILL.md + 17 reference files + 22 tools).

## agent-skills — 33 files (25 skills)

Production-grade engineering skills for AI coding agents covering the full software
development lifecycle, from spec to ship. Each skill is a single `SKILL.md` in `skills/`.
Four skills ship extra files, kept next to their skill under `<behaviour>-files/`:

- `enforce-quality-constraints-files/` — `references/floor-guard.md`, `scripts/quality-gate.mjs`.
- `refine-ideas-files/` — `examples.md`, `frameworks.md`, `refinement-criteria.md`, `scripts/idea-refine.sh`.
- `optimize-performance-files/` — `references/optimization-patterns.md`.
- `harden-security-files/` — `references/hardening-patterns.md`.

The repo's `.claude/commands/` and `.gemini/commands/` files are thin slash-command
wrappers that invoke these skills, not skills themselves, so they are not included.

## superpowers — 80 files (15 skills)

A workflow plugin for AI coding agents (v7.0.2): brainstorming before creative work,
writing and executing plans, subagent-driven development, systematic debugging,
test-driven development, code review in both directions, and verification before
claiming work is complete. Each skill is a `SKILL.md` in `skills/`, and most ship
supporting files (prompts, references, templates, scripts) that the skill invokes —
those are kept next to their skill under `<behaviour>-files/`, preserving their
original relative paths, e.g.:

- `diagnose-session-files/` — 11 analyst prompts, 4 references, 4 report templates.
- `develop-with-subagents-files/` — implementer/reviewer prompts, 7 references, 4 scripts.
- `brainstorm-files/` — visual-companion docs and a small HTML helper server.
- `write-skills-files/` — 8 references on how to write and test skills.
- `use-superpowers-files/` — per-harness tool references (Claude Code, Codex, Gemini, …).

The repo's plugin manifests (`.claude-plugin/`, `.codex-plugin/`, `.gemini/`, …)
and `hooks/`/`scripts/`/`tests/` are harness plumbing, not skills, so they are not
included — only the `skills/` tree is.

## mattpocock/skills — 109 files (39 skills)

Matt Pocock's personal, curated skill set — the skills he uses every day, judged
against a strict bar (an observed failure in a real session + fits the philosophy;
see `SCOPE.md`). Skills live in four buckets, recorded as the `variant` in
`MANIFEST.csv`:

- `engineering/` (20) — the main workflow: triage, wayfinding, specs, tickets,
  implementation, TDD, code review, diagnosing bugs, domain modelling, retrospectives.
- `productivity/` (7) — grilling, handoffs, teaching, questionnaires, writing for agents.
- `in-progress/` (8) — drafts still being built (chief-of-staff, software-factory,
  the writing trio), included as-is and labelled `in-progress` in the manifest.
- `misc/` (4) — frozen and unmaintained per the repo's own `SCOPE.md`.

Most skills ship an `agents/openai.yaml` (an OpenAI-harness config for the skill)
and some ship reference docs and scripts — kept next to their skill under
`<behaviour>-files/`, preserving original relative paths.

The five category `README.md` files inside `skills/` (one per bucket plus
`deprecated/`) are category index docs, not skill files, so they are not included.

## ponytail — 12 files (6 skills x 2 variants)

"Lazy senior dev mode" (v5.3.3): force the simplest solution that works — YAGNI,
stdlib first, one line over fifty. The core skill makes the agent write the smallest
change that fully solves the task and reply in one readable line; the companions audit
a whole repo's quality, review a change, list deferred `shortcut:` debt, show measured
savings, and explain how to use ponytail.

- `Minimize/` (formerly `ponytail/`) — the 6 skills from `skills/` (main version).
- `Adapt/` (formerly `ponytail-openclaw/`) — the same 6 skills from `.openclaw/skills/` (OpenClaw-adapted
  version: same body, frontmatter adapted for OpenClaw).

The repo's `commands/` (`.toml` slash-command wrappers), `hooks/` (band/statusline
plumbing) and `assets/` are harness plumbing, not skills, so they are not included.

## ui-ux-pro-max-skill — 227 files (6 skills)

AI-powered design intelligence (v2.15.0): UI/UX design skills with searchable local
data — 80 UI styles, 192 color palettes, 74 font pairings, 120 UX guidelines, 25 chart
types across 22 tech stacks. The 6 skills are the canonical set in `.claude/skills/`:

- `design-ui-ux.md` — the flagship: UI/UX design intelligence for web, mobile, desktop.
- `style-ui.md` — shadcn/ui + Tailwind interfaces, themes, dark mode, canvas designs
  (98 files: the biggest skill here, including its canvas font files).
- `comprehensive-design.md` was removed in v11 (it needs a Gemini API key) — see "Removed in v11".
- `build-design-system.md` — token architecture (primitive→semantic→component),
  component specs, slide generation.
- `manage-brand.md` — brand voice, visual identity, messaging, asset management.
- `design-banners.md` — banners for social, ads, heroes, print (22 styles).
- `build-slides.md` — strategic HTML presentations with Chart.js and design tokens.

Supporting files (221) are kept next to their skill under `<behaviour>-files/`,
preserving original relative paths: `references/`, `scripts/`, `data/` (palettes, fonts,
icons, charts), `templates/`, and `canvas-fonts/` (the .ttf files the canvas skill uses).

The `cli/assets/skills/` copies are the installer's copies of the same 6 skills —
5 are byte-identical to the `.claude/` versions and the 6th (ui-styling) is a trimmed
subset of the full one — so they are not duplicated here. The `cli/`, `src/`, `stack/`,
`gallery/`, `docs/` and `scripts/` trees are the installer, build source, example stack
and docs, not skills, so they are not included — only the `.claude/skills/` tree is.

## graphify — 0 files (checked: this repo contains no skills)

Graphify-Labs/graphify is a Python knowledge-graph library (the `graphifyy` package
on PyPI) for building and querying knowledge graphs — it is a tool, not a skill
collection. The whole repo was searched and it contains **zero** `SKILL.md` files,
so nothing from it was added to this zip. It is listed here so the check is on record.

## caveman — 63 files (21 skills)

Caveman: terse, evidence-first coding-agent skills with a token-cost conscience.
The core voice skill answers first with zero fluff; around it sit lean-build,
investigate-first, surgical-patch, safe-refactor, verify-and-stop, context compression,
token-stats, and Caveman Cloud evidence/experiment skills. Two voice variants:
`caveman-wenyan.md` (Classical Chinese register) and `caveman-ultra.md` (maximum
compression). Each skill is a `SKILL.md` in `skills/`, with supporting files kept under
`<behaviour>-files/`. Shared files used by several skills — the activation rule, the
compiler, the engine MCP tools, the skill registry, the verbs gate, the per-harness
generated packs, and the native core doc — are kept in `shared-files/`.

The `plugins/caveman/skills/` copies are duplicates of the `skills/` set (5 byte-identical,
1 — caveman-stats — reworded in a single line), so they are not duplicated here.

## Understand-Anything — 67 files (8 skills)

Understand a codebase by turning it into an interactive knowledge graph: architecture,
components and relationships as an explorable dashboard, plus domain extraction,
LLM-wiki knowledge graphs, diff/PR explanations, onboarding
guides, and a chat skill that answers questions from the graph. The 8 skills live in
`understand-anything-plugin/skills/`; each ships scripts (graph builders, fingerprinting,
framework guides) kept under `<behaviour>-files/`. The plugin's `agents/`, `hooks/` and
`packages/core/` are the implementation code behind the skills, not skills themselves,
so they are not included.

## awesome-claude-skills — 299 files (28 skills)

A large curated collection of Claude skills (ComposioHQ). Two parts:

- **28 curated skills** in `Curate/` (formerly `awesome/`) — everyday skills (changelog generation, file
  organization, meeting insights, resume tailoring, MCP building, webapp testing, …),
  including 4 document skills in `Curate/document-skills/` (docx, pdf, pptx, xlsx) with
  their reference docs and scripts.
- **Composio app-automation skills (832) were removed in v11** — one skill
  per SaaS app, each automating that app's tasks via Rube MCP (Composio), which needs
  an MCP connection plus an OAuth connection to the app — they cannot run on the host
  model alone. See "Removed in v11" above.

The repo root `README.md`/`CONTRIBUTING.md`, the `connect-apps-plugin/` manifest files
and the `composio-skills/.claude-plugin/marketplace.json` are not skills, so they are
not included.

## archify — 230 files (5 skills)

Turn any idea, plan, or codebase into a beautiful interactive diagram: validated
architecture, workflow, sequence, data-flow, lifecycle/state, ERD, class, tree,
timeline and waterfall diagrams as explorable standalone HTML, plus one-page explainers.
The main skill (`make-diagrams.md`) is a full implementation — renderers, schemas,
explainer engine, examples and locales — kept complete under `make-diagrams-files/`.
Four smaller companion skills live in `.agents/skills/`: review issues/PRs with evidence,
tune diagram accuracy, simplify a codebase, and improve test value.

- `Visualize/archify-packaged.zip` — the repo's official packaged skill archive (203 files).

The repo's `viewer/`, `website/`, `examples/` (top-level), `benchmarks/`, `docs/` and
`tools/` are the app/docs around the skill, not skills, so they are not included.
The full clones of this repo (1.6 GB) and impeccable (907 MB) were avoided by fetching
only the skill trees.

## impeccable — 69 files (1 skill)

"The design vocabulary for your coding agent": design, redesign, critique, audit,
polish, simplify, harden, animate, or otherwise improve a frontend interface — websites,
landing pages, dashboards, product UI, components, native iOS/Android screens, and
design systems. The skill ships 45 reference guides (one per verb: audit, bolder,
colorize, craft, delight, layout, typeset, …), 4 subagent definitions, and a launcher
binary with live-browser tooling.

The repo generates the same skill into 22 per-harness install directories (`.claude/`,
`.cursor/`, `.agents/`, …) with only path strings substituted, so only one generated
copy is included — `plugin/skills/impeccable/` (the generic plugin copy) as
`design-frontend.md` + `design-frontend-files/`. The authored source files that the
generated copy does not contain — `SKILL.src.md`, the Hermes plugin, and the 4 subagent
definitions — are kept in `design-frontend-source-files/`.

## taste-skill — 1631 files (1 skill)

tasteskill v2.5.1, "the anti-slop frontend skill": build professional company
websites at the level of figma.com and x.ai — plain copy in a voice of its own, one
system, one section per screen, real photographs and real product UI, a hero entrance
and one or two dealt moments on every page, shader effects only where they belong, and
a checker and finish gate that enforce it in a real browser. Use whenever a page looks
generic, templated or "AI-made". The skill ships a huge asset library — 958 SVG
components, backgrounds, photos, scripts and checkers — kept complete under
`design-tasteful-frontend-files/` (40 MB). The repo-root `assets/` and `examples/`
are demo material for the repo, not part of the skill dir, so they are not included.

## paperclip — 197 files (60 unique skills)

Paperclip's own skills: the agent platform's internal dev skills (`.agents/skills/`,
30 — PR loops, release coordination, evals, verification skills, storybook, tracing),
its user-facing skills (`skills/`, 5 — the paperclip task skill, AgentMail,
PARA memory, complaint and suggestion boxes), the skills catalog (bundled + optional,
13 — issue triage, wireframes, QA acceptance, Ramp finance, design
critique, …), the LLM-wiki plugin skills (6), the assistant-plugin skills (3, kept
from `shared/` — the claude/openai copies are byte-identical), the onboarding
first-task skill and the content-calendar skill. The 83 `SKILL.md`
files in the repo hash down to 77 unique skills; `doc-maintenance` exists twice with
different content (dev skill vs catalog skill) and is kept as `maintain-docs.md` and
`maintain-docs-catalog.md`. Most names are already behaviour-descriptive, so they are
kept as-is; only the opaque ones were renamed (`release` → `release-paperclip.md`,
`complain` → `file-complaint.md`, `slack` → `work-in-slack.md`, `paperclip` →
`use-paperclip.md`, `ramp` → `track-ramp-finances.md`, `wireframe` → `make-wireframes.md`).
17 paperclip skills were removed in v11 (they need the Paperclip
platform API or a Slack/Ramp/Honeycomb account) — see "Removed in v11" above.

## security-audit-skill — 20 files (1 skill)

Cloudflare's security audit skill: security guidance and vulnerability review for
codebases, APIs, services, CLI tools, libraries and daemons — focused reviews,
vulnerability research, full audits and pen tests, with a findings report schema and
validator scripts. 15 reference guides (web/auth, cloud, supply chain, memory safety,
AI/LLM, hunting, …) are kept under `audit-security-files/`.

## i-have-adhd — 3 files (1 skill)

Shape output for a reader with ADHD: lead with the next action, number multi-step
work, restate state across turns, suppress tangents, give specific time estimates,
make wins visible. The skill ships two agent configs (`agents/openai.yaml`,
`agents/gemini.toml`) kept under `write-for-adhd-files/`. The `.cursor/skills/` copy
is the same `SKILL.md` without the agent configs, so it is not duplicated.

## hallmark — 0 files (0 skills)

The hallmark skill (`design-with-hallmark.md`) was **removed in v11**: its core
workflow calls the Together API with its own key (`TOGETHER_API_KEY`), so it cannot
run on the host IDE/agent model alone. The `hallmark/` folder is gone from this zip.
See "Removed in v11" above.

## agentic-awesome-skills — 9131 files (2646 unique skills)

A mega-collection of 2646 skills (the repo's own catalog count in `CATALOG.md` is 2957; 311 were removed in v11),
covering everything from agent orchestration and evaluation to API design, accessibility,
product management, data, security and design. The canonical set is `skills/` — every
skill there is unique by name. The 62 plugin bundles in `plugins/` repeat the same
skills: verified by hash, every plugin copy is either byte-identical to the `skills/`
copy or differs only in frontmatter metadata placement (`risk:`/`source:`/`date_added:`
moved under `metadata:`) and/or leading/trailing whitespace — all 24 same-name
collisions differ by whitespace only after stripping — so the plugin copies are not
duplicated here. Behaviour filenames are the skill dir names, which are already
behaviour-descriptive and unique. Supporting files (6485) are kept next to their skill
under `<behaviour>-files/`. Note `skills/` is not flat: some skills live in group
dirs (`design-it/*`, `libreoffice/*`, `security/*`, `sendblue/*`) and some dirs are
both a skill and a group (`agent-squad` + its 8 member skills, `app-builder` +
`templates`); each `SKILL.md`'s parent dir is one skill, and nested skills are kept
as their own skills, not folded into their parent's files.

## book-to-skill — 19 files (1 skill)

Convert books and documents (PDF, EPUB, DOCX, HTML, Markdown, plain text, RTF,
MOBI/AZW with Calibre) into structured agent skills — extracting frameworks, mental
models, principles, techniques and anti-patterns. The skill runs `scripts/extract.py`,
which imports the `book_to_skill` Python package (17 files: PDF/EPUB/DOCX/HTML/RTF/text
parsers, sanitizer, config, CLI), so both are kept under
`convert-book-to-skill-files/`. The repo's `docs/` and `evals/` are project docs and
evals, not skill files, so they are not included.

## anti-slop — 17 files (6 skills)

Anti Slop: rules for AI coding agents — a filter, not a style guide. The core skill
(`stop-ai-slop.md`) loads always; five companions cover UI/visual, copywriting,
people/accessibility (with a contrast checker), mobile layout and code-comment hygiene.
The always-on pointer doc (`stop-ai-slop-pointer.md`) and the Cursor rule
(`stop-ai-slop-cursor.mdc`) that load the matching skills are included as formats of the
core skill. The repo's `assets/` banners are branding, not skill files.

## strix — 5 files (5 skills)

Security testing with Strix (open-source CLI or the managed app.strix.ai cloud):
pentest a web app, find vulnerabilities in code (OWASP Top 10) with working
proof-of-concept exploits, fix them and re-verify. Each skill is a single `SKILL.md`,
no supporting files. 4 of the 9 Strix skills were removed in v11
(they need an LLM provider key, a Strix token, or a Postman key) — see "Removed in v11" above.

## stageshow — 372 files (1 skill)

Build faux product UI that looks like a real product — a still illustration or an
animated demo with a cursor: browser and app windows, dashboards, phones,
notifications, terminals, bento grids and cursor walkthroughs, framed, masked and
cropped the way a marketing page, feature card or docs hero needs them. React +
plain CSS, filmed locally with Node/Vite/Playwright. The skill ships the full kit
(155 files: windows, bars, rows, icons, brands), 15 reference guides, 12 filming
scripts, 155 gold example files, teaching material and a playground — kept complete
under `build-faux-product-ui-files/`. It needs no separate API key, token, MCP
connection or external account, so it passes the v11 API filter and is added in
full. The repo-root `README.md`/`AGENTS.md`/`CLAUDE.md` are repo docs, not part of
the skill, so they are not included.

## vibe-coding — 16 files (11 skills)

Eleven vibe-coding workflow skills (v3.2.0): plan, build, change, debug,
review, verify and hand off an app project — PRD, technical design, agent
instructions, research and workflow selection. Each skill exists in five
byte-identical copies in the repo (`.agents/skills/`, `.claude/skills/`,
`templates/.agents/skills/`, `templates/.claude/skills/`, `workflow/skills/`);
only the canonical `.agents/skills/` copy is included, once per skill, with
its `references/` files under `<behaviour>-files/references/`. The skills
need no separate API key, token, MCP connection or external account, so they
pass the v11 API filter and are added in full. The repo's `cli/` (installer
tooling), `docs/`, `examples/`, `scripts/`, `workflow/evals/`, `.github/`,
repo-root files and `templates/` scaffolding are not skill files and are not
included.

## aeon — 226 files (69 skills)

Aeon is an agent that runs on the user's own GitHub repo via Actions: a skill
is a Markdown file (`skills/<name>/SKILL.md`) and `aeon.yml` says which ones
run and when. The 92 skills in `skills/` cover crypto/web3 (onchain monitoring,
token trading and picks, Base, Uniswap hooks, canister and contract audits),
X/Twitter (fetching, writing and replying to tweets, mention radar, ship logs),
GitHub (PR review and triage, auto-merge, filing registry, fleet control),
content (articles, digests, changelogs, SEO audits) and finance (spend watch,
defi overview, token movers). Each skill is a `SKILL.md` in `skills/` with its
supporting files (references, scripts) kept next to it under
`<behaviour>-files/`. The `aeon` skill itself (set up and run an Aeon agent
instance) ships in two harness variants that differ only in one path
(`.claude/skills/aeon` vs the plugin root); the build treats them as two
variants, like GSD claude/pi (`Automate/run-aeon-agent.md` and
`aeon-plugin/run-aeon-agent.md`), but both were removed in v14 (see below),
so the `aeon-plugin/` folder is empty. get-started is the plugin's
onboarding skill. `skills/security/trusted-sources.txt`
is a shared file invoked by install-skill, pack-submit and search-skill and is
kept once under `Automate/shared-files/`. 25 skills were removed in v14 (see
"Removed in v14"), including the aeon skill itself and get-started — both
need a separate model key / MCP connection. Excluded: `docs/examples/skill-templates/`
(6 template skills with `[REPLACE:...]` placeholders), `scripts/tests/skill-scan-fixtures/`
(42 SKILL.md security-scanner test fixtures), and everything else (`apps/`,
`docs/`, `scripts/`, `harness-adapter/`, `plugin/` besides the two skill dirs,
`catalog/`, `memory/`, `soul/`, `bin/`).

## context-engineering — 65 files (20 skills)

A collection of Agent Skills for context engineering, harness engineering,
multi-agent architectures and production agent systems: context fundamentals,
compression, optimization and degradation, memory systems, multi-agent patterns,
harness engineering, evaluation, hosted agents, self-improvement loops and
project development. 18 skills in `skills/`, plus the root `SKILL.md` (the
collection's umbrella skill, `context-engineering-collection.md`) and
`template/SKILL.md` (a template for creating new skills, renamed from its
description to `add-new-skill.md`). No skill was removed in v14. Excluded:
`examples/` (4 demo skills), `researcher/` (research corpus/benchmarks),
`docs/`, `governance/`, `assets/` and the repo-root docs.

## awesome-copilot — 1485 files (447 skills)

GitHub's awesome-copilot collection: 481 skills (478 in `skills/` + 3 in
`.github/skills/` — agentic-workflows, code-review, create-canvas-extension),
covering coding workflows, Azure, Microsoft 365, .NET, Java, Python, MCP server
generation, testing, security review and more. Leaf dir names are unique, so
behaviour names are the leaf names. 15 skills are nested inside another skill
dir (the qdrant family: monitoring, performance-optimization, scaling and
search-quality sub-skills); each SKILL.md's parent dir is one skill and a file
belongs to its deepest containing skill dir, the same rule as
agentic-awesome-skills. 34 skills were removed in v14 (see "Removed in v14").
This is a blobless sparse clone — only `skills/` and `.github/skills/` are
checked out, and every `MANIFEST.csv` source path is inside them.

## anthropics — 236 files (13 skills)

Anthropic's official skills repo: 14 new skills added (332 files before the
v14 filter). docx/pdf/pptx/xlsx are renamed to `edit-docx.md`, `edit-pdf.md`,
`edit-pptx.md`, `edit-xlsx.md` from their descriptions; the rest keep their
dir names. claude-api was removed in v14 (it teaches the Claude API and needs
an Anthropic API key). Six skills are byte-identical duplicates of skills
already in the zip (brand-guidelines, canvas-design, internal-comms,
theme-factory, webapp-testing, template) and are skipped entirely — their
supporting files are already in the zip. Their 5 `LICENSE.txt` files
(byte-identical to each other, differing from the awesome copies only
in the copyright-holder line: "Copyright 2026 Anthropic, PBC." vs the
placeholder) are not carried over as separate files, but their exact text
is present in the zip: 7 of the new anthropics skills ship a byte-identical
`LICENSE.txt`.

## jwynia — 573 files (113 skills)

119 skills, deeply nested under `skills/` (`creative/fiction/...`, `general/...`,
`tech/...`): creative writing and fiction orchestration, general research and
education, and tech development workflows (architecture, workflow, security,
testing). Leaf dir names are unique, so behaviour names are the leaf names.
13 reference files live in a parallel tree (`skills/<path>/` without the
`tech/`/`general/` prefix) and are invoked by relative path from 6 skills
(requirements-analysis, system-design, github-agile, competency, research,
fact-check); they are kept under those skills' `<behaviour>-files/references/`.
6 skills were removed in v14 (see "Removed in v14"). Excluded: the repo
`skills/README.md`, `skills/.DS_Store`, and the `creative/fiction/orchestrators/README.md`
group doc (its SKILL.md reference is a stale path that does not resolve in the
source repo).

## qodex — 507 files (71 skills)

80 new skills in `skills/`: cloud, backend, frontend, data and AI-agent
specialists (AWS, Supabase, Shopify, serverless, RAG, agent frameworks and
more). The template skill at the repo root is a byte-identical duplicate of
the zip's `template-skill.md` and is skipped. 9 skills were removed in v14
(see "Removed in v14"). Four skills link to `../../docs/aws-mcp-setup.md`,
which does not exist in the repo (dead link); they were judged on their
SKILL.md content, not the dead link.

## claude-workflow-v2 — 17 files (14 skills)

14 development-workflow skills: analyzing projects, Convex backend, database
design, designing APIs and architecture, designing tests, devops infrastructure,
error handling, managing git, optimizing performance, parallel execution,
security patterns, Vercel + React best practices and web design guidelines.
Three ship a second file (convex-backend and vercel-react-best-practices:
`AGENTS.md`; designing-apis: `OPENAPI-TEMPLATE.md`). No skill was removed in
v14. `commands/`, `hooks/`, `agents/`, `templates/`, `examples/` and `packages/`
are harness plumbing and are not included — only the `skills/` tree is.

The original import renamed files by behaviour.
v11 removes 1172 skills that need a separate key or service (see "Removed in v11");
v14 removes 75 more from the 7 new repos (see "Removed in v14").
The filename is what the skill *does* — e.g. `gsd-plan-phase` → `plan.md`,
`gsd-execute-phase` → `execution.md`, `karpathy-guidelines` → `coding-guidelines.md`,
`not-ai` → `humanize-writing.md`, `test-driven-development` → `test-first.md`,
`brainstorming` → `brainstorm.md`, `subagent-driven-development` → `develop-with-subagents.md`,
`triage` → `triage-issues.md`, `wayfinder` → `map-huge-work.md`,
`ponytail` → `lazy-senior-dev.md`, `ponytail-audit` → `audit-repo-quality.md`,
`ui-ux-pro-max` → `design-ui-ux.md`, `ui-styling` → `style-ui.md`,
`caveman` → `talk-like-caveman.md`, `understand` → `build-knowledge-graph.md`,
`archify` → `make-diagrams.md`, `impeccable` → `design-frontend.md`,
`taste-skill` → `design-tasteful-frontend.md`,
`antislop` → `stop-ai-slop.md`, `security-audit` → `audit-security.md`.
`MANIFEST.csv` maps every behaviour filename back to its repo, original skill name,
source path, description and SHA-256 at import. Files with updated collection credits can have different local hashes and sizes.

## Index — gsd-core (Claude variant in `Orchestrate/`, same names in `Execute/`)

| Behaviour file | Original skill | What it does |
|---|---|---|
| `ai-design-contract.md` | `gsd-ai-integration-phase` | Generate an AI-SPEC.md design contract for phases that involve building AI systems. |
| `audit-fix-pipeline.md` | `gsd-audit-fix` | Autonomous audit-to-fix pipeline — find issues, classify, fix, test, commit |
| `audit-milestone.md` | `gsd-audit-milestone` | Audit milestone completion against original intent before archiving |
| `audit-uat.md` | `gsd-audit-uat` | Cross-phase audit of all outstanding UAT and verification items |
| `autonomous-execution.md` | `gsd-autonomous` | Run all remaining phases autonomously — discuss→plan→execute per phase |
| `capture-ideas.md` | `gsd-capture` | Capture ideas, tasks, notes, and seeds to their destination |
| `cleanup-archive.md` | `gsd-cleanup` | Archive accumulated phase directories from completed milestones |
| `code-review.md` | `gsd-code-review` | Review source files changed during a phase for bugs, security issues, and code quality problems |
| `complete-milestone.md` | `gsd-complete-milestone` | Archive completed milestone and prepare for next version |
| `configure-settings.md` | `gsd-config` | Configure GSD settings — workflow toggles, advanced knobs, integrations, and model profile |
| `debugging.md` | `gsd-debug` | Systematic debugging with persistent state across context resets |
| `discuss-phase.md` | `gsd-discuss-phase` | Gather phase context through adaptive questioning before planning. |
| `eval-review.md` | `gsd-eval-review` | Audit an executed AI phase's evaluation coverage and produce an EVAL-REVIEW.md remediation plan. |
| `execution.md` | `gsd-execute-phase` | SDD phase execution — execute all plans in a phase with dependency-aware wave parallelization |
| `explore-ideas.md` | `gsd-explore` | Socratic ideation and idea routing — think through ideas before committing to plans |
| `extract-learnings.md` | `gsd-extract-learnings` | Extract decisions, lessons, patterns, and surprises from completed phase artifacts |
| `fast-task.md` | `gsd-fast` | Execute a trivial task inline — no subagents, no planning overhead |
| `forensics-postmortem.md` | `gsd-forensics` | Post-mortem investigation for failed GSD workflows — diagnoses what went wrong. |
| `generate-tests.md` | `gsd-add-tests` | Generate tests for a completed phase based on UAT criteria and implementation |
| `health-check.md` | `gsd-health` | Diagnose planning directory health and optionally repair issues |
| `help.md` | `gsd-help` | Show available GSD commands and usage guide |
| `import-plans.md` | `gsd-import` | Ingest external plans with conflict detection against project decisions before writing anything. |
| `inbox-triage.md` | `gsd-inbox` | Triage and review open GitHub issues and PRs against project templates and contribution guidelines. |
| `ingest-docs.md` | `gsd-ingest-docs` | Bootstrap or merge a .planning/ setup from existing ADRs, PRDs, SPECs, and docs in a repo. |
| `knowledge-graph.md` | `gsd-graphify` | Build, query, and inspect the project knowledge graph in .planning/graphs/ |
| `manage-phase-roadmap.md` | `gsd-phase` | Multi-phase management — add, insert, remove, or edit phases in ROADMAP.md (roadmap phase CRUD) |
| `manage-phases.md` | `gsd-manager` | Interactive command center for managing multiple phases from one terminal |
| `manage-threads.md` | `gsd-thread` | Manage persistent context threads for cross-session work |
| `manage-workspaces.md` | `gsd-workspace` | Manage GSD workspaces — create, list, or remove isolated workspace environments |
| `manage-workstreams.md` | `gsd-workstreams` | Manage parallel workstreams — list, create, switch, status, progress, complete, and resume |
| `map-codebase.md` | `gsd-map-codebase` | Analyze codebase with parallel mapper agents to produce .planning/codebase/ documents |
| `memory-capture.md` | `gsd-mempalace-capture` | File a phase artifact into MemPalace; mirror decision facts into its temporal KG |
| `memory-recall.md` | `gsd-mempalace-recall` | Recall decisions, patterns, and surprises from MemPalace before planning |
| `milestone-summary.md` | `gsd-milestone-summary` | Generate a comprehensive project summary from milestone artifacts for team onboarding and review |
| `namespace-context.md` | `gsd-ns-context` | codebase intel | map graphify docs learnings mempalace |
| `namespace-ideate.md` | `gsd-ns-ideate` | exploration capture | explore sketch spike spec capture |
| `namespace-manage.md` | `gsd-ns-manage` | config workspace | workstreams thread update ship inbox |
| `namespace-project.md` | `gsd-ns-project` | project lifecycle | milestones audits summary |
| `namespace-review.md` | `gsd-ns-review` | quality gates | code review debug audit security eval ui |
| `namespace-workflow.md` | `gsd-ns-workflow` | workflow | discuss plan execute verify phase progress |
| `new-milestone.md` | `gsd-new-milestone` | Start a new milestone cycle — update PROJECT.md and route to requirements |
| `new-project.md` | `gsd-new-project` | Initialize a new project with deep context gathering and PROJECT.md |
| `next-action.md` | `gsd-next` | Smart entry — detect project state and route to the right next GSD action. |
| `onboard-codebase.md` | `gsd-onboard` | Guide existing codebase onboarding through mapping, doc ingest, and planning setup |
| `pause-work.md` | `gsd-pause-work` | Create context handoff when pausing work mid-phase |
| `peer-review.md` | `gsd-review` | Request cross-AI peer review of phase plans from external AI CLIs |
| `plan-mvp.md` | `gsd-mvp-phase` | Plan a phase as a vertical MVP slice — user story, SPIDR splitting, then plan-phase |
| `plan-review-convergence.md` | `gsd-plan-review-convergence` | Cross-AI plan convergence - replan until review concerns are resolved. |
| `plan.md` | `gsd-plan-phase` | Create detailed phase plan (PLAN.md) with verification loop |
| `pr-branch.md` | `gsd-pr-branch` | Create a clean PR branch by filtering out .planning/ commits — ready for code review |
| `profile-user.md` | `gsd-profile-user` | Generate developer behavioral profile and create Claude-discoverable artifacts |
| `progress-tracking.md` | `gsd-progress` | Check progress, advance workflow, or dispatch freeform intent — the unified GSD situational command |
| `project-stats.md` | `gsd-stats` | Display project statistics — phases, plans, requirements, git metrics, and timeline |
| `quick-batch.md` | `gsd-quick-batch` | Batch several `/gsd-quick`-shaped tasks together — planned, dispatched, and merged as one run |
| `quick-task.md` | `gsd-quick` | Execute a quick task with GSD guarantees (atomic commits, state tracking) but skip optional agents |
| `resume-work.md` | `gsd-resume-work` | Resume work from previous session with full context restoration |
| `review-backlog.md` | `gsd-review-backlog` | Review and promote backlog items to active milestone |
| `secure-phase.md` | `gsd-secure-phase` | Retroactively verify threat mitigations for a completed phase |
| `settings.md` | `gsd-settings` | Configure GSD workflow toggles and model profile |
| `ship.md` | `gsd-ship` | Create PR, run review, and prepare for merge after verification passes |
| `sketch-ui.md` | `gsd-sketch` | Sketch UI/design ideas with throwaway HTML mockups, or propose what to sketch next (frontier mode) |
| `specify-phase.md` | `gsd-spec-phase` | Clarify WHAT a phase delivers with ambiguity scoring; produces a SPEC.md before discuss-phase. |
| `spike-exploration.md` | `gsd-spike` | Spike an idea through experiential exploration, or propose what to spike next (frontier mode) |
| `surface-skills.md` | `gsd-surface` | Toggle which skills are surfaced — apply a profile, list, or disable a cluster without reinstall |
| `ui-design.md` | `gsd-ui-phase` | Generate UI design contract (UI-SPEC.md) for frontend phases |
| `ui-review.md` | `gsd-ui-review` | Retroactive 6-pillar visual audit of implemented frontend code |
| `ultraplan.md` | `gsd-ultraplan-phase` | [BETA] Offload plan phase to Claude Code's ultraplan cloud; review in browser and import back. |
| `undo-revert.md` | `gsd-undo` | Safe git revert. |
| `update-docs.md` | `gsd-docs-update` | Generate or update project documentation verified against the codebase |
| `update-gsd.md` | `gsd-update` | Update GSD to latest version with changelog display |
| `validate-phase.md` | `gsd-validate-phase` | Retroactively audit and fill Nyquist validation gaps for a completed phase |
| `verify-work.md` | `gsd-verify-work` | Validate built features through conversational UAT |

## Index — andrej-karpathy-skills

| Behaviour file | Original skill | Format | What it does |
|---|---|---|---|
| `coding-guidelines.md` | `karpathy-guidelines` | skill | Behavioural guidelines to reduce common LLM coding mistakes — think before coding, simplicity first, surgical changes, goal-driven execution. |
| `coding-guidelines-project.md` | `karpathy-guidelines` | claude-md | Same guidelines as a per-project CLAUDE.md. |
| `coding-guidelines-cursor.mdc` | `karpathy-guidelines` | cursor-rule | Same guidelines as a Cursor project rule. |

## Index — Not-Ai

| Behaviour file | Original skill | Format | What it does |
|---|---|---|---|
| `humanize-writing.md` | `not-ai` | skill | Edit prose into a clear, specific, source-grounded version preserving the author's meaning and voice. |
| `reference/*.md` (17 files) | `not-ai` | reference | The skill's reference manuals (punctuation/prosody, voice, fidelity, plain language, …). |
| `tools/*.py` (22 files) | `not-ai` | tool | The skill's supporting Python tools (review gate + core engines). |
| `humanize-writing-claude.md` | `not-ai` | claude | Same skill file, Claude copy (byte-identical). |
| `humanize-writing-single-file.md` | `not-ai` | single-file | Same skill as one built file with references inlined. |
| `humanize-writing.skill` | `not-ai` | packaged | Official packaged skill archive. |

## Index — agent-skills

| Behaviour file | Original skill | What it does |
|---|---|---|
| `add-observability.md` | `observability-and-instrumentation` | Instruments code so production behavior is visible and diagnosable. |
| `adversarial-review.md` | `doubt-driven-development` | Subjects every non-trivial decision to a fresh-context adversarial review before it stands. |
| `break-down-tasks.md` | `planning-and-task-breakdown` | Breaks work into ordered tasks. |
| `build-frontend-ui.md` | `frontend-ui-engineering` | Builds production-quality, accessible, responsive user-facing UIs. |
| `code-review.md` | `code-review-and-quality` | Conducts multi-axis code review. |
| `debugging.md` | `debugging-and-error-recovery` | Guides systematic root-cause debugging. |
| `deprecate-and-migrate.md` | `deprecation-and-migration` | Manages deprecation and migration. |
| `design-apis.md` | `api-and-interface-design` | Guides stable API and interface design. |
| `develop-from-docs.md` | `source-driven-development` | Grounds every implementation decision in official documentation. |
| `discover-skills.md` | `using-agent-skills` | Discovers and invokes agent skills. |
| `document-decisions.md` | `documentation-and-adrs` | Records decisions and documentation, and detects when documentation has drifted from the code it describes. |
| `enforce-quality-constraints.md` | `constraint-driven-development` | Establishes a project's quality bar as a written contract and stops agents quietly lowering it. |
| `git-workflow.md` | `git-workflow-and-versioning` | Structures git workflow practices. |
| `harden-security.md` | `security-and-hardening` | Hardens code against vulnerabilities. |
| `implement-incrementally.md` | `incremental-implementation` | Delivers changes incrementally in thin, verifiable slices. |
| `interview-user.md` | `interview-me` | Extracts what the user actually wants instead of what they think they should want. |
| `optimize-context.md` | `context-engineering` | Optimizes agent context setup. |
| `optimize-performance.md` | `performance-optimization` | Optimizes application performance across frontend, backend, queries, and databases. |
| `refine-ideas.md` | `idea-refine` | Refines raw ideas into sharp, actionable concepts through structured divergent and convergent thinking. |
| `setup-ci-cd.md` | `ci-cd-and-automation` | Automates CI/CD pipeline setup. |
| `ship-and-launch.md` | `shipping-and-launch` | Prepares production launches. |
| `simplify-code.md` | `code-simplification` | Simplifies code for clarity. |
| `test-first.md` | `test-driven-development` | Drives development with tests using the red-green-refactor loop. |
| `test-in-browser.md` | `browser-testing-with-devtools` | Tests in real browsers via Chrome DevTools MCP. |
| `write-specs-first.md` | `spec-driven-development` | Creates specs before coding. |

## Index — superpowers

| Behaviour file | Original skill | What it does |
|---|---|---|
| `brainstorm.md` | `brainstorming` | You MUST use this before any creative work - creating features, building components, adding functionality, modifying behavior, or planning anything new, in software or out of it (a talk, a business, a renovation). |
| `debug-systematically.md` | `systematic-debugging` | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| `develop-with-subagents.md` | `subagent-driven-development` | Use when executing implementation plans with independent tasks in the current session |
| `diagnose-session.md` | `diagnosing-superpowers` | Use when a superpowers session went wrong and your human partner wants to know why — repeated work, ignored plans, stumbles, poor results, a skill that didn't fire, "it took too long", "why is it so expensive", "what is it doing" — or wants to build a bug report for the superpowers maintainers, for the current session or a past one identified by id or path, on any harness. |
| `dispatch-parallel-agents.md` | `dispatching-parallel-agents` | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies |
| `execute-plans.md` | `executing-plans` | Use when executing an implementation plan in the current session as the implementer yourself — your human partner chose inline execution, or no subagent tool is available |
| `finish-branch.md` | `finishing-a-development-branch` | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work |
| `receive-code-review.md` | `receiving-code-review` | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation |
| `request-code-review.md` | `requesting-code-review` | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| `test-first.md` | `test-driven-development` | Use when implementing any feature or bugfix, before writing implementation code |
| `use-git-worktrees.md` | `using-git-worktrees` | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native tools or git worktree fallback |
| `use-superpowers.md` | `using-superpowers` | Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including clarifying questions |
| `verify-before-completion.md` | `verification-before-completion` | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always |
| `write-plans.md` | `writing-plans` | Use when you have a spec or requirements for a multi-step task, before touching code |
| `write-skills.md` | `writing-skills` | Use when creating new skills, editing existing skills, or verifying skills work before deployment |

## Index — mattpocock/skills

| Behaviour file | Bucket | Original skill | What it does |
|---|---|---|---|
| `map-huge-work.md` | `engineering` | `wayfinder` | Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on your issue tracker, and resolve them one at a time until the way to the destination is clear. |
| `hand-off-to-agent.md` | `in-progress` | `claude-handoff` | Hand the current conversation off to a fresh background agent that picks up the work immediately. |
| `make-questionnaire.md` | `productivity` | `to-questionnaire` | Turn a decision you can't fully answer into a questionnaire for someone else to fill in. |
| `scaffold-exercises.md` | `misc` | `scaffold-exercises` | Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. |
| `review-code.md` | `engineering` | `code-review` | Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes: Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match what the originating issue/spec asked for?). |
| `design-codebase.md` | `engineering` | `codebase-design` | Shared vocabulary for designing deep modules. |
| `research-topic.md` | `engineering` | `research` | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. |
| `setup-skills.md` | `engineering` | `setup-matt-pocock-skills` | Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain doc layout. |
| `test-first.md` | `engineering` | `tdd` | Test-driven development. |
| `setup-deep-modules.md` | `in-progress` | `setup-ts-deep-modules` | Wire dependency-cruiser into a TypeScript repo so each package is a deep module, with implementation hidden in subfolders and reachable only through its entry-point files. |
| `design-software-factory.md` | `in-progress` | `software-factory` | Shared language for designing a software factory: the tasks it runs and the services it plugs into. |
| `setup-pre-commit.md` | `misc` | `setup-pre-commit` | Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. |
| `teach-me.md` | `productivity` | `teach` | Teach the user a new skill or concept, within this workspace. |
| `re-pitch-message.md` | `productivity` | `wait-what` | Stop. |
| `shape-writing.md` | `in-progress` | `writing-shape` | Writing, exploit: shape raw material into an article, paragraph by paragraph. |
| `diagnose-bugs.md` | `engineering` | `diagnosing-bugs` | Diagnosis loop for hard bugs and performance regressions. |
| `mine-writing-fragments.md` | `in-progress` | `writing-fragments` | Writing, explore: mine raw fragments, no structure yet. |
| `migrate-to-shoehorn.md` | `misc` | `migrate-to-shoehorn` | Migrate test files from `as` type assertions to @total-typescript/shoehorn. |
| `block-dangerous-git.md` | `misc` | `git-guardrails-claude-code` | Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. |
| `implement-spec.md` | `engineering` | `implement-spec` | Implement the result of /to-spec and /to-tickets in code. |
| `implement-work.md` | `engineering` | `implement` | Implement a piece of work based on a spec or set of tickets. |
| `improve-architecture.md` | `engineering` | `improve-codebase-architecture` | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. |
| `route-to-skill.md` | `engineering` | `ask-matt` | Ask which skill or flow fits your situation. |
| `model-domain.md` | `engineering` | `domain-modeling` | Build and sharpen a project's domain model. |
| `coordinate-long-goal.md` | `in-progress` | `chief-of-staff` | Pursue a long-running goal in a single session by co-ordinating subagents. |
| `grill-plan-with-docs.md` | `engineering` | `grill-with-docs` | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. |
| `write-pr-body.md` | `engineering` | `pr` | Use when writing a PR body. |
| `write-spec-from-chat.md` | `engineering` | `to-spec` | Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed. |
| `break-into-tickets.md` | `engineering` | `to-tickets` | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker (edges as text in one file per ticket locally, or native blocking links on a real tracker). |
| `triage-issues.md` | `engineering` | `triage` | Move issues and external PRs through a state machine of triage roles, categorise, verify, grill if needed, and write agent-ready briefs. |
| `grill-workflow-specs.md` | `in-progress` | `loop-me` | Grill me about specs for the workflows I want to build, within this workspace. |
| `grill-my-plan.md` | `productivity` | `grill-me` | A relentless interview to sharpen a plan or design. |
| `grill-my-thinking.md` | `productivity` | `grilling` | Grill the user relentlessly about a plan, decision, or idea. |
| `write-handoff.md` | `productivity` | `handoff` | Compact the current conversation into a handoff document for another agent to pick up. |
| `write-for-agents.md` | `productivity` | `writing-for-agents` | Writing documents for agents. |
| `assemble-writing-beats.md` | `in-progress` | `writing-beats` | Writing, exploit; assemble raw material into a journey of beats, grounding each term before a beat leans on it. |
| `build-prototype.md` | `engineering` | `prototype` | Build a throwaway prototype to answer a design question. |
| `run-retrospective.md` | `engineering` | `retro` | Conduct a retrospective on a coding session. |
| `build-bash-wizard.md` | `engineering` | `wizard` | Generate an interactive bash wizard that walks a human through steps only they can perform. |

## Index — ponytail (main variant in `Minimize/`, same names in `Adapt/`)

| Behaviour file | Original skill | What it does |
|---|---|---|
| `audit-repo-quality.md` | `ponytail-audit` | Quality audit of a whole repo: bugs, security holes, what breaks under real load, risky code without tests, slow paths, and what to delete, merge or split. |
| `lazy-senior-dev.md` | `ponytail` | Lazy senior dev mode: the smallest change that fully solves the task, and a reply a busy human understands in one read. |
| `list-shortcut-debt.md` | `ponytail-debt` | List every `shortcut:` comment (and older `ponytail:` ones) as a debt ledger. |
| `review-change-quality.md` | `ponytail-review` | Quality review of a change: is the logic right, is it safe, does it hold under real load, is risky code tested, is it fast enough, and is every line needed. |
| `show-help.md` | `ponytail-help` | Quick reference for ponytail levels, skills and commands. |
| `show-savings.md` | `ponytail-gain` | Show ponytail's measured savings (code, cost, speed) from the benchmark. |

## Index — ui-ux-pro-max-skill

| Behaviour file | Original skill | What it does |
|---|---|---|
| `build-design-system.md` | `design-system` | Token architecture, component specifications, and slide generation. |
| `build-slides.md` | `slides` | Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting formulas, and contextual slide strategies. |
| `design-banners.md` | `banner-design` | Design banners for social media, ads, website heroes, creative assets, and print. |
| `design-ui-ux.md` | `ui-ux-pro-max` | UI/UX design intelligence for web, mobile, and desktop. |
| `manage-brand.md` | `brand` | Brand voice, visual identity, messaging frameworks, asset management, brand consistency. |
| `style-ui.md` | `ui-styling` | Create beautiful, accessible user interfaces with shadcn/ui components (built on Radix UI + Tailwind), Tailwind CSS utility-first styling, and canvas-based visual designs. |

## Index — caveman

| Behaviour file | Original skill | What it does |
|---|---|---|
| `build-lean.md` | `lean-build` | Build feature work with high overbuilding risk. |
| `caveman-ultra.md` | `ultracave` | Caveman at maximum compression: fragments, one word when one word is enough, each fact once. |
| `caveman-wenyan.md` | `megacave` | Caveman in Classical Chinese: 文言文 register, far fewer characters, technical terms verbatim. |
| `compress-context.md` | `caveman-compress` | Compress a memory file such as CLAUDE.md or a todo list into caveman format to save input tokens, keeping a readable backup. |
| `delegate-to-crew.md` | `cavecrew` | When to delegate to `cavecrew-investigator` (locate code), `cavecrew-builder` (1-2 file edit) or `cavecrew-reviewer` (diff review) instead of working inline or using `Explore`. |
| `discover-llm-workflows.md` | `caveman-discover` | Find and label every LLM workflow in the repository so Caveman Cloud groups spend by workflow instead of one bucket. |
| `evaluate-optimization.md` | `caveman-optimize` | Turn a Caveman optimization observation into an operator-chosen candidate with a paired baseline evaluation. |
| `explore-repo-readonly.md` | `caveman-explore` | Read-only repository explorer for cold-start orientation, broad cross-file localization, or when a direct search failed. |
| `investigate-first.md` | `investigate-first` | Diagnose ambiguous failures before editing. |
| `lower-token-cost.md` | `caveman-learn` | Act on a Caveman learn report - review the ranked token sinks, apply cost-lowering fixes with per-edit consent, and report what those fixes returned. |
| `manage-cloud-experiments.md` | `caveman-manage` | Inspect Caveman Cloud's experiment lifecycle and block unsafe execution. |
| `migrate-safely.md` | `migration` | Implement reversible compatibility-safe transitions. |
| `patch-surgically.md` | `surgical-patch` | Fix bugs and small behavior changes at the narrowest responsible layer. |
| `refactor-safely.md` | `safe-refactor` | Restructure code while preserving behavior. |
| `review-cloud-evidence.md` | `caveman-evidence-review` | Read-only review of Caveman Cloud evidence: cost, Cave Score, workflows, traces, latency, errors, routing, savings. |
| `review-code-terse.md` | `caveman-review` | Compressed code review - one line per finding with location, problem and fix. |
| `show-caveman-help.md` | `caveman-help` | Quick-reference card for the three caveman skills and their commands. |
| `show-token-stats.md` | `caveman-stats` | Show recorded output and cache-read token usage and mode attribution for the current Claude Code session, or locate the host's native usage report. |
| `talk-like-caveman.md` | `caveman` | Terse caveman voice: answer first, fluff gone, every technical fact kept. |
| `verify-and-stop.md` | `verify-and-stop` | Prove existing work meets acceptance conditions without expanding scope. |
| `write-commit-message.md` | `caveman-commit` | Write a Conventional Commits message compressed to intent only. |

## Index — Understand-Anything

| Behaviour file | Original skill | What it does |
|---|---|---|
| `ask-codebase.md` | `understand-chat` | Use when you need to ask questions about a codebase or understand code using a knowledge graph |
| `build-knowledge-graph.md` | `understand` | Analyze a codebase to produce an interactive knowledge graph for understanding architecture, components, and relationships |
| `explain-code.md` | `understand-explain` | Use when you need a deep-dive explanation of a specific file, function, or module in the codebase |
| `explain-diff.md` | `understand-diff` | Use when you need to analyze git diffs or pull requests to understand what changed, affected components, and risks |
| `extract-domain-knowledge.md` | `understand-domain` | Extract business domain knowledge from a codebase and generate an interactive domain flow graph. |
| `graph-knowledge-base.md` | `understand-knowledge` | Analyze a Karpathy-pattern LLM wiki knowledge base and generate an interactive knowledge graph with entity extraction, implicit relationships, and topic clustering. |
| `open-knowledge-dashboard.md` | `understand-dashboard` | Launch the interactive web dashboard to visualize a codebase's knowledge graph |
| `write-onboarding-guide.md` | `understand-onboard` | Use when you need to generate an onboarding guide for new team members joining a project |

## Index — awesome-claude-skills (curated)

| Behaviour file | Original skill | What it does |
|---|---|---|
| `analyze-meeting-insights.md` | `meeting-insights-analyzer` | Analyzes meeting transcripts and recordings to uncover behavioral patterns, communication insights, and actionable feedback. |
| `apply-anthropic-brand.md` | `brand-guidelines` | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. |
| `brainstorm-domain-names.md` | `domain-name-brainstormer` | Generates creative domain name ideas for your project and checks availability across multiple TLDs (.com, .io, .dev, .ai, etc.). |
| `build-html-artifacts.md` | `artifacts-builder` | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). |
| `build-mcp-servers.md` | `mcp-builder` | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. |
| `build-themes.md` | `theme-factory` | Toolkit for styling artifacts with a theme. |
| `create-skills.md` | `skill-creator` | Guide for creating effective skills. |
| `create-slack-gifs.md` | `slack-gif-creator` | Toolkit for creating animated GIFs optimized for Slack, with validators for size constraints and composable animation primitives. |
| `design-on-canvas.md` | `canvas-design` | Create beautiful visual art in .png and .pdf documents using design philosophy. |
| `download-videos.md` | `video-downloader` | Download YouTube videos with customizable quality and format options. |
| `enhance-images.md` | `image-enhancer` | Improves the quality of images, especially screenshots, by enhancing resolution, sharpness, and clarity. |
| `extract-competitor-ads.md` | `competitive-ads-extractor` | Extracts and analyzes competitors' ads from ad libraries (Facebook, LinkedIn, etc.) to understand what messaging, problems, and creative approaches are working. |
| `generate-changelog.md` | `changelog-generator` | Automatically creates user-facing changelogs from git commits by analyzing commit history, categorizing changes, and transforming technical commits into clear, customer-friendly release notes. |
| `optimize-for-twitter-algorithm.md` | `twitter-algorithm-optimizer` | Analyze and optimize tweets for maximum reach using Twitter's open-source algorithm insights. |
| `organize-files.md` | `file-organizer` | Intelligently organizes your files and folders across your computer by understanding context, finding duplicates, suggesting better structures, and automating cleanup tasks. |
| `organize-invoices.md` | `invoice-organizer` | Automatically organizes invoices and receipts for tax preparation by reading messy files, extracting key information, renaming them consistently, and sorting them into logical folders. |
| `pick-raffle-winner.md` | `raffle-winner-picker` | Picks random winners from lists, spreadsheets, or Google Sheets for giveaways, raffles, and contests. |
| `research-and-write-content.md` | `content-research-writer` | Assists in writing high-quality content by conducting research, adding citations, improving hooks, iterating on outlines, and providing real-time feedback on each section. |
| `research-leads.md` | `lead-research-assistant` | Identifies high-quality leads for your product or service by analyzing your business, searching for target companies, and providing actionable contact strategies. |
| `share-skills.md` | `skill-share` | A skill that creates new Claude skills and automatically shares them on Slack using Rube for seamless team collaboration and skill discovery. |
| `template-skill.md` | `template-skill` | Replace with description of the skill and when Claude should use it. |
| `test-webapps.md` | `webapp-testing` | Toolkit for interacting with and testing local web applications using Playwright. |
| `write-internal-comms.md` | `internal-comms` | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. |
| `write-tailored-resume.md` | `tailored-resume-generator` | Analyzes job descriptions and generates tailored resumes that highlight relevant experience, skills, and achievements to maximize interview chances |
| `document-skills/edit-docx.md` | `document-skills/docx` | Comprehensive document creation, editing, and analysis with support for tracked changes, comments, formatting preservation, and text extraction. |
| `document-skills/edit-pdf.md` | `document-skills/pdf` | Comprehensive PDF manipulation toolkit for extracting text and tables, creating new PDFs, merging/splitting documents, and handling forms. |
| `document-skills/edit-pptx.md` | `document-skills/pptx` | Presentation creation, editing, and analysis. |
| `document-skills/edit-xlsx.md` | `document-skills/xlsx` | Comprehensive spreadsheet creation, editing, and analysis with support for formulas, formatting, data analysis, and visualization. |

## Index — archify

| Behaviour file | Original skill | What it does |
|---|---|---|
| `improve-test-value.md` | `test-value` | Improve test value and feedback cost when auditing slow, flaky, redundant or brittle tests; choosing tests during implementation; or reviewing test changes before a commit or PR. |
| `make-diagrams.md` | `archify` | Create validated architecture, workflow, sequence, data-flow, lifecycle/state, ERD, class, tree, timeline, and waterfall diagrams as explorable standalone HTML with dark/light themes, motion and image/SVG/WebM export. |
| `review-with-evidence.md` | `archify-review` | Review Archify issues, PRs, or code through value, cost, and impact to support evidence-based maintenance decisions. |
| `simplify-codebase.md` | `simplify-codebase` | Simplification audit or authorized codebase simplification whose stated objective is to remove accidental complexity. |
| `tune-diagram-accuracy.md` | `archify-tuning` | Improve Archify diagram accuracy, visual quality and complete authoring speed with fewer repairs. |

## Index — impeccable

| Behaviour file | Original skill | What it does |
|---|---|---|
| `design-frontend.md` | `impeccable` | Use to design, redesign, critique, audit, polish or animate a frontend: websites, landing pages, dashboards, app UI, components, native iOS/Android screens, or a design system (DESIGN.md). |

## Index — taste-skill

| Behaviour file | Original skill | What it does |
|---|---|---|
| `design-tasteful-frontend.md` | `taste-skill` | >- |

## Index — paperclip

| Behaviour file | Original skill | Source | What it does |
|---|---|---|---|
| `add-product-e2e-eval.md` | `add-product-e2e-eval` | `.agents/skills/add-product-e2e-eval` | Add or extend a Paperclip full-stack runner E2E workflow, fixture, matcher, or report evidence path for local or Daytona execution. |
| `add-runner-eval.md` | `add-runner-eval` | `.agents/skills/add-runner-eval` | Add or extend a Paperclip Runner protocol evaluation definition, roster, assertion, or report fixture with provenance and narrow validation. |
| `agent-browser.md` | `agent-browser` | `packages/skills-catalog/catalog/optional/browser/agent-browser` | Drive a real browser to inspect or interact with a web page or app — navigate, take screenshots, read console and network, fill simple forms — for verification tasks, not unattended automation. |
| `agentmail.md` | `agentmail` | `skills/agentmail` | Use your assigned AgentMail inbox to read email tasks, explicitly send or reply, and check delivery. |
| `check-pr.md` | `check-pr` | `.agents/skills/check-pr` | Check a GitHub, GitLab, or Perforce PR/MR/CL for review comments, failing checks, and PR-body gaps. |
| `company-creator.md` | `company-creator` | `.agents/skills/company-creator` | Create agent company packages that conform to agentcompanies/v1. |
| `content-calendar.md` | `content-calendar` | `packages/teams-catalog/catalog/optional/content/content-machine/skills/content-calendar` | Plan a weekly editorial calendar by mapping company goals to publishable topics, owners, status, and verification notes. |
| `create-case.md` | `create-case` | `.agents/skills/create-case` | Create and kick off a Paperclip case from a user request, with workflow instructions and an initial agent. |
| `create-external-bot-integration.md` | `create-external-bot-integration` | `.agents/skills/create-external-bot-integration` | >- |
| `create-issue-interaction-ui.md` | `create-issue-interaction-ui` | `.agents/skills/create-issue-interaction-ui` | Add a new Paperclip issue-thread interaction kind end-to-end. |
| `create-paperclip-bundled-skill.md` | `create-paperclip-bundled-skill` | `.agents/skills/create-paperclip-bundled-skill` | Turn an idea, tweet, or task into a skill in the Paperclip skills catalog (packages/skills-catalog). |
| `create-runner-adapter.md` | `create-runner-adapter` | `.agents/skills/create-runner-adapter` | Add a new harness/provider integration to native Paperclip Runner, from requirements and protocol research through implementation, packaging, and real end-to-end acceptance. |
| `create-verification-skill.md` | `create-verification-skill` | `.agents/skills/create-verification-skill` | Generate a project-local verification skill that drives your app the way a user does — any language, framework, or platform. |
| `deal-with-security-advisory.md` | `deal-with-security-advisory` | `.agents/skills/deal-with-security-advisory` | Handle confidential GitHub Security Advisory response for Paperclip. |
| `delegate-work.md` | `delegate-work` | `integrations/assistant-plugins/shared/skills/delegate-work` | Delegate user-requested work to an existing Paperclip agent, with a durable task reference and clear execution expectations. |
| `design-critique.md` | `design-critique` | `packages/skills-catalog/catalog/optional/product/design-critique` | Give a structured product design critique — user job clarity, hierarchy, affordance, error states, accessibility, and consistency — focused on what to change, in what order, and why. |
| `design-guide.md` | `design-guide` | `.claude/skills/design-guide` | Paperclip UI design system guide for building consistent, reusable frontend components. |
| `diagnose-why-work-stopped.md` | `diagnose-why-work-stopped` | `.agents/skills/diagnose-why-work-stopped` | Compatibility entry point for failed, stalled, looping, or over-recovered Paperclip work. |
| `directions-lab.md` | `directions-lab` | `.agents/skills/directions-lab` | Scaffold a directions lab that shows shipped UI (Today) beside 2-3 design directions, with surface tabs, theme and animation toggles and the V1 MVP hover motion, registered in design-proposals Storybook. |
| `file-complaint.md` | `complain` | `skills/complain` | Autonomously yeet a brief, unstructured complaint about agent tooling or doing agent work. |
| `first-task.md` | `first-task` | `server/src/onboarding-assets/first-task/skills/first-task` | Guide the user's first Paperclip task when its description invokes /first-task. |
| `fix-failed-paperclip-run.md` | `fix-failed-paperclip-run` | `.agents/skills/fix-failed-paperclip-run` | Diagnose and fix failed, stuck, slow, or incorrectly blocked Paperclip tasks and runs. |
| `fix-slow-queries.md` | `fix-slow-queries` | `.agents/skills/fix-slow-queries` | >- |
| `follow-up-results.md` | `follow-up-results` | `integrations/assistant-plugins/shared/skills/follow-up-results` | Find progress or deliverables from earlier Paperclip work and add user-requested feedback with human attribution. |
| `github-pr-workflow.md` | `github-pr-workflow` | `packages/skills-catalog/catalog/bundled/software-development/github-pr-workflow` | Prepare a GitHub pull request from a feature branch — branch hygiene, commit shape, title/body, verification notes, screenshots for UI work, and replies to review comments. |
| `index-refresh.md` | `index-refresh` | `packages/plugins/plugin-llm-wiki/skills/index-refresh` | Use when an LLM Wiki operation issue requests an index refresh. |
| `issue-triage.md` | `issue-triage` | `packages/skills-catalog/catalog/bundled/paperclip-operations/issue-triage` | Triage Paperclip inbox issues that are stale, blocked, in-review, or assigned-but-not-progressing, and decide a single next action per issue (resume, reassign, unblock, escalate, or close). |
| `maintain-docs-catalog.md` | `doc-maintenance` | `packages/skills-catalog/catalog/bundled/docs/doc-maintenance` | Keep project docs aligned with recent code and feature changes — detect drift, update affected pages, and add release-relevant notes without rewriting unchanged sections. |
| `maintain-docs.md` | `doc-maintenance` | `.agents/skills/doc-maintenance` | Audit README and PRODUCT docs against recent git history for drift and make minimal PR-ready edits. |
| `maintain-storybook.md` | `maintain-storybook` | `.agents/skills/maintain-storybook` | Keep Paperclip stories and their downstream catalog aligned with the feature map and production UI. |
| `maintain-verification-skill.md` | `maintain-verification-skill` | `.agents/skills/maintain-verification-skill` | Keep a project's verification skill and product/agent access maps aligned with current source and real evidence. |
| `make-wireframes.md` | `wireframe` | `packages/skills-catalog/catalog/bundled/product/wireframe` | Produce low-fidelity black-and-white UI wireframes as SVGs or viewer pages. |
| `paperclip-capsules.md` | `paperclip-capsules` | `packages/skills-catalog/catalog/bundled/product/paperclip-capsules` | Generate, implement, or review Paperclip capsule visuals. |
| `paperclip-converting-plans-to-tasks.md` | `paperclip-converting-plans-to-tasks` | `skills/paperclip-converting-plans-to-tasks` | Decide whether Paperclip work needs delegation, and connect justified tasks with owners and real dependencies. |
| `paperclip-create-plugin.md` | `paperclip-create-plugin` | `.agents/skills/paperclip-create-plugin` | Create and develop external Paperclip plugins with the CLI-first workflow. |
| `paperclip-distill.md` | `paperclip-distill` | `packages/plugins/plugin-llm-wiki/skills/paperclip-distill` | Use when an operation issue is a Paperclip cursor-window, distill, or backfill. |
| `paperclip-evals.md` | `paperclip-evals` | `.agents/skills/paperclip-evals` | Choose, inspect, validate, and report Paperclip Runner or Product E2E evaluations while preserving evidence, provenance, cost, and failure classification. |
| `para-memory-files.md` | `para-memory-files` | `skills/para-memory-files` | Use a file-based PARA memory system to store, retrieve, and organize durable knowledge across sessions. |
| `pr-gardening.md` | `pr-gardening` | `.agents/skills/pr-gardening` | Discover the pull requests this Paperclip instance opened (never community contributions), report what each is for and how confident we are that it is merge-ready, and automatically drive the non-ready ones back to green with /prepare-paperclip-pr — without ever merging. |
| `pr-report.md` | `pr-report` | `.agents/skills/pr-report` | Produce a maintainer-grade PR or contribution report as HTML or Markdown. |
| `prcheckloop.md` | `prcheckloop` | `.agents/skills/prcheckloop` | Iterate on a GitHub PR until latest-head checks are green or a precise blocker is named. |
| `prepare-mcp-integration.md` | `prepare-mcp-integration` | `packages/skills-catalog/catalog/optional/software-development/prepare-mcp-integration` | Prepare MCP/vendor integrations through cited research, a content PR, exact-revision human approval, and one governed Paperclip connector PR per approved connection. |
| `prepare-paperclip-pr.md` | `prepare-paperclip-pr` | `.agents/skills/prepare-paperclip-pr` | Prepare a Paperclip branch for PR with commits, template body, and checks. |
| `qa-acceptance.md` | `qa-acceptance` | `packages/skills-catalog/catalog/bundled/quality/qa-acceptance` | Produce QA acceptance criteria and a manual validation plan for a feature change — golden path, edge cases, error states, performance limits, and explicit pass/fail evidence. |
| `release-announcement.md` | `release-announcement` | `packages/skills-catalog/catalog/optional/content/release-announcement` | Write a release announcement — changelog, blog post, in-app note, or social post — that leads with user impact, names the audience, and includes upgrade/migration steps without filler. |
| `release-changelog-discord-message.md` | `release-changelog-discord-message` | `.agents/skills/release-changelog-discord-message` | Write the Discord announcement for a stable Paperclip release from the release changelog. |
| `release-changelog.md` | `release-changelog` | `.agents/skills/release-changelog` | Generate the stable Paperclip release changelog at releases/vYYYY.MDD.P.md by reading commits, changesets, and merged PR context since the last stable tag. |
| `review-my-team.md` | `review-my-team` | `integrations/assistant-plugins/shared/skills/review-my-team` | Review a connected Paperclip team's agents, tasks, blockers and pending approvals when the user asks for a team summary or what needs attention. |
| `review-storybook.md` | `review-storybook` | `.agents/skills/review-storybook` | Review Paperclip stories for a feature or change using the Storybook catalog, production source, and existing browser tests. |
| `setup-code-maintenance-bot.md` | `setup-code-maintenance-bot` | `.agents/skills/setup-code-maintenance-bot` | Set up a Paperclip agent and routine that applies a selected code-maintenance skill to a repository and opens pull requests. |
| `simplified-english.md` | `simplified-english` | `packages/skills-catalog/catalog/optional/content/simplified-english` | Write user-facing comments, plans, and documents in ASD-STE100 Simplified Technical English — short, unambiguous sentences with approved words and one meaning each — so readers understand them the first time. |
| `suggestion-box.md` | `suggestion-box` | `skills/suggestion-box` | Quietly suggest a concrete improvement after observing material, generalizable friction in agent work. |
| `task-planning.md` | `task-planning` | `packages/skills-catalog/catalog/bundled/paperclip-operations/task-planning` | Write or revise a useful Paperclip plan with a clear outcome and verification. |
| `test-audit.md` | `test-audit` | `.agents/skills/test-audit` | Garden the test suite by finding and removing redundant, vacuous, or implementation-coupled tests while preserving useful regression coverage. |
| `track-ramp-finances.md` | `ramp` | `packages/skills-catalog/catalog/optional/finance/ramp` | Fetch and follow Ramp's published agent playbooks inside Paperclip, with mandatory approval gates for spend, incorporation, cards, account setup, and other financial actions. |
| `verify-paperclip.md` | `verify-paperclip` | `.agents/skills/verify-paperclip` | Verify Paperclip from a source checkout, published npm install, or existing staging or production stack. |
| `wiki-ingest.md` | `wiki-ingest` | `packages/plugins/plugin-llm-wiki/skills/wiki-ingest` | Use when an operation issue asks to ingest a captured `raw/` source into the LLM Wiki, or the user says "ingest <slug>". |
| `wiki-lint.md` | `wiki-lint` | `packages/plugins/plugin-llm-wiki/skills/wiki-lint` | Use when an LLM Wiki operation issue is a lint or health check. |
| `wiki-maintainer.md` | `wiki-maintainer` | `packages/plugins/plugin-llm-wiki/skills/wiki-maintainer` | Use the LLM Wiki plugin tools to maintain a cited local company wiki. |
| `wiki-query.md` | `wiki-query` | `packages/plugins/plugin-llm-wiki/skills/wiki-query` | Use when an LLM Wiki operation issue asks a question. |

## Index — security-audit-skill

| Behaviour file | Original skill | What it does |
|---|---|---|
| `audit-security.md` | `security-audit` | Security guidance and vulnerability review for codebases, APIs, services, CLI tools, libraries, and daemons. |

## Index — i-have-adhd

| Behaviour file | Original skill | What it does |
|---|---|---|
| `write-for-adhd.md` | `i-have-adhd` | Shape output for a reader with ADHD: lead with the next action, number multi-step work, restate state across turns, suppress tangents, give specific time estimates, make wins visible. |

## Index — agentic-awesome-skills (2646)

One row per skill; full descriptions are in `MANIFEST.csv`.

| Behaviour file | Original skill | What it does |
|---|---|---|
| `00-andruia-consultant.md` | `00-andruia-consultant` | Usar al iniciar o mejorar un proyecto de IA: diagnostica código y restricciones, propone skills existentes y redacta tareas y un plan de implementación en español. |
| `007.md` | `007` | Security audit, hardening, threat modeling (STRIDE/PASTA), Red/Blue Team, OWASP checks, code review, incident response, and infrastructure security for any project. |
| `10-andruia-skill-smith.md` | `10-andruia-skill-smith` | Usar para crear o mejorar una skill de Andru.ia: define entradas y resultados, redacta SKILL.md con ejemplos y límites, valida la estructura y prepara una PR. |
| `20-andruia-niche-intelligence.md` | `20-andruia-niche-intelligence` | Usar tras definir el sector de un proyecto: prepara un dossier en español con contexto, normas aplicables, patrones UX y riesgos, distinguiendo fuentes verificadas de hipótesis. |
| `2d-games.md` | `2d-games` | >- |
| `360-feedback-system.md` | `360-feedback-system` | 360 feedback register: reviewer, subject, review cycle, visibility, due date and score, as CSV, SQL, JSON Schema or Notion on request. |
| `3d-games.md` | `3d-games` | 3D game development principles. |
| `3d-ui.md` | `3d-ui` | Web and App implementation guide for 3D UI. |
| `3d-web-experience.md` | `3d-web-experience` | Use when building or debugging web 3D scenes, product configurators or portfolios with Three.js, React Three Fiber or Spline; review assets, loading, controls, fallbacks and performance. |
| `a4a.md` | `a4a` | Connect your AI agent to the A4A end-to-end encrypted agent-to-agent messaging network via local MCP tools or Python SDK. |
| `aas-compose-stack.md` | `aas-compose-stack` | Preserve the coding agent's explicit AAS skill selection as a validated stack and optional evidence. |
| `aas-discover.md` | `aas-discover` | Discover AAS skills for an explicit task and compare their complete instructions without installing them. |
| `aas-review-stack.md` | `aas-review-stack` | Review AAS stack manifests, preview plans and selection evidence in Workbench without applying changes. |
| `ab-test-setup.md` | `ab-test-setup` | Use when designing an A/B or split test: define the hypothesis, control and variants, estimate sample size, verify tracking, and predeclare metrics and stopping rules. |
| `ab-testing.md` | `ab-testing` | When the user wants to plan, design, or implement an A/B test or experiment, or build a growth experimentation program. |
| `acceptance-orchestrator.md` | `acceptance-orchestrator` | Use when a coding task should be driven end-to-end from issue intake through implementation, review, deployment, and acceptance verification with minimal human re-intervention. |
| `access-matrix.md` | `access-matrix` | Access matrix of role-by-module permissions, with per-role scope, confidentiality level and SME tier, as CSV, SQL, JSON Schema or Notion on request. |
| `access-review.md` | `access-review` | Conduct periodic access reviews and certifications. |
| `accessibility-compliance-accessibility-audit.md` | `accessibility-compliance-accessibility-audit` | Audit pages and user journeys against a declared WCAG scope. |
| `accesslint-audit.md` | `accesslint-audit` | Find and fix WCAG 2.2 accessibility issues. |
| `accesslint-diff.md` | `accesslint-diff` | Diff a live page's accessibility violations against a baseline — by default compares uncommitted changes (stash-based), or pass --branch [name] to diff against a branch. |
| `accesslint-scan.md` | `accesslint-scan` | Audit a live page for accessibility issues, locate each WCAG violation precisely, and return a selector-grounded fix worklist without editing. |
| `accint-commitments.md` | `accint-commitments` | Triage acc's open promises and close them with honest real-world verdicts via acc_act(runtime="outcome"). |
| `accint-frames.md` | `accint-frames` | Drain acc's deliberation queue — open/waiting brain_frames checkpointed by headless runs — via acc_act(runtime="continue"). |
| `accint-solve.md` | `accint-solve` | Route a goal through acc's scored-memory loop via acc_act(runtime="solve"); deliberate any returned brain_frame and submit via continue. |
| `accounting-audit-system-builder.md` | `accounting-audit-system-builder` | Routes an accounting or audit request to the right module skill, from software selection through monthly closing, asking only what is missing. |
| `accounting-software-selection.md` | `accounting-software-selection` | Scores shortlisted accounting packages against 57 evidence-backed fields, emitted as CSV, SQL, JSON Schema or Notion on request. |
| `active-directory-attacks.md` | `active-directory-attacks` | Assess Active Directory attack paths using scoped configuration review and controlled synthetic lab validation; identify prerequisites, evidence and mitigations. |
| `ad-campaign-analyzer.md` | `ad-campaign-analyzer` | Analyze cross-channel campaign data, quantify uncertainty, and propose evidence-labeled budget tests without overstating causality. |
| `ad-creative.md` | `ad-creative` | Create, iterate, and scale paid ad creative for Google Ads, Meta, LinkedIn, TikTok, and similar platforms. |
| `add-app-clip.md` | `add-app-clip` | Add an iOS App Clip target to an Expo app. |
| `address-github-comments.md` | `address-github-comments` | Use when you need to address review or issue comments on an open GitHub Pull Request using the gh CLI. |
| `adhx.md` | `adhx` | Fetch any X/Twitter post as clean LLM-friendly JSON. |
| `admin-access-register.md` | `admin-access-register` | Admin account register: system, main and backup admin, seats, plan, 2FA, shared logins and access-review dates, as CSV, SQL, JSON Schema or Notion on request. |
| `advanced-analytics-dashboard.md` | `advanced-analytics-dashboard` | Dashboard metric register: metric, source module, formula, period, value, target, trend, owner and last-updated, as CSV, SQL, JSON Schema or Notion on request. |
| `advanced-evaluation.md` | `advanced-evaluation` | Design LLM-as-judge rubrics, direct scores and pairwise comparisons. |
| `advogado-criminal.md` | `advogado-criminal` | Assistente de pesquisa informativa, sem credenciais profissionais, sobre em Maria da Penha, violencia domestica, feminicidio, direito penal brasileiro, medidas protetivas, inquerito policial e acao penal. |
| `advogado-especialista.md` | `advogado-especialista` | Apoio a pesquisa juridica brasileira, organizacao de fatos e minutas, com verificacao em fontes oficiais e revisao profissional para casos concretos. |
| `aegisops-ai.md` | `aegisops-ai` | Autonomous DevSecOps & FinOps Guardrails. |
| `agent-creator.md` | `agent-creator` | Create custom AI subagents with proper plugin structure, persona generation, and companion routing skills. |
| `agent-evaluation.md` | `agent-evaluation` | Evaluate agent behavior with versioned cases and explicit verifiers. |
| `agent-evaluation-reporting.md` | `agent-evaluation-reporting` | Use when summarizing agent evaluations where autonomous, assisted, failed, timed-out, or invalid outcomes must remain distinct and comparable. |
| `agent-framework-azure-ai-py.md` | `agent-framework-azure-ai-py` | Build persistent agents on Azure AI Foundry using the Microsoft Agent Framework Python SDK. |
| `agent-harness-fault-injection.md` | `agent-harness-fault-injection` | Use when an agent workflow needs deterministic recovery evidence for sandbox, MCP/tool, worker, checkpoint, memory, or orchestration failures. |
| `agent-manager-skill.md` | `agent-manager-skill` | Manage multiple local CLI agents via tmux sessions (start/stop/monitor/assign) in an explicitly authorized workspace. |
| `agent-memory.md` | `agent-memory` | A hybrid memory system that provides persistent, searchable knowledge management for AI agents. |
| `agent-memory-discipline.md` | `agent-memory-discipline` | Rules for when an agent should recall from long-term memory before acting and when it should save decisions, corrections and failures afterwards. |
| `agent-memory-mcp.md` | `agent-memory-mcp` | A hybrid memory system that provides persistent, searchable knowledge management for AI agents (Architecture, Patterns, Decisions). |
| `agent-memory-systems.md` | `agent-memory-systems` | Design tenant-scoped memory, retrieval and retention for agents. |
| `agent-observability.md` | `agent-observability` | Instrument AI agents with tracing, token metrics, latency, and cost visibility. |
| `agent-orchestration-improve-agent.md` | `agent-orchestration-improve-agent` | Systematic improvement of existing agents through performance analysis, prompt engineering, and continuous iteration. |
| `agent-orchestration-multi-agent-optimize.md` | `agent-orchestration-multi-agent-optimize` | Optimize multi-agent systems with coordinated profiling, workload distribution, and cost-aware orchestration. |
| `agent-orchestrator.md` | `agent-orchestrator` | Meta-skill que orquestra todos os agentes do ecossistema. |
| `agent-qa-authoring.md` | `agent-qa-authoring` | Create, edit, validate, and run Agent QA tests, suites, and hooks through MCP or CLI while preserving canonical IDs and schema contracts. |
| `agent-qa-debug-fix.md` | `agent-qa-debug-fix` | Debug, patch, and verify failed Agent QA runs from MCP evidence, artifacts, logs, and local code without hiding product or infrastructure defects. |
| `agent-qa-result-triage.md` | `agent-qa-result-triage` | Triage failed Agent QA runs with MCP evidence, artifacts, logs, fixed failure categories, confidence, and actionable next steps. |
| `agent-reels.md` | `agent-reels` | Find animation and video references on 1human, consult a human-agent shared library, and contribute public creations only with prior owner permission. |
| `agent-self-scheduling.md` | `agent-self-scheduling` | Schedule AI agent runs with cron, loops, or external clocks while avoiding unsafe tight autonomous timers. |
| `agent-squad.md` | `agent-squad` | Main agent orchestrator that coordinates a specialized squad of agents |
| `agent-tool-builder.md` | `agent-tool-builder` | Tools are how AI agents interact with the world. |
| `agentflow.md` | `agentflow` | Orchestrate autonomous AI development pipelines through your Kanban board (Asana, GitHub Projects, Linear). |
| `agentfolio.md` | `agentfolio` | Skill for discovering and researching autonomous AI agents, tools, and ecosystems using the AgentFolio directory. |
| `agentic-actions-auditor.md` | `agentic-actions-auditor` | Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. |
| `agentic-test-audit.md` | `agentic-test-audit` | Audit a pytest suite: surviving mutants and untested code, flaky, order-dependent and slow tests, and removal candidates checked on held-out mutants. |
| `agentic-verify.md` | `agentic-verify` | Check that a Python change is caught by tests: run every mutant of the changed lines and write tests until they catch them. |
| `agentphone.md` | `agentphone` | Build AI phone agents with AgentPhone API. |
| `agents-generator.md` | `agents-generator` | Generate project-specific AGENTS.md and companion rules by analyzing a codebase. |
| `agents-md.md` | `agents-md` | Create, revise, or audit AGENTS.md files from repository evidence, verified commands, and correctly scoped instructions without overwriting maintainer intent. |
| `agents-v2-py.md` | `agents-v2-py` | Build container-based Foundry Agents with Azure AI Projects SDK (HostedAgentDefinition). |
| `agenttrace-session-audit.md` | `agenttrace-session-audit` | Audit local AI coding-agent sessions with agenttrace for cost, tool failures, latency, anomalies, health, diffs, and CI gates. |
| `agy-delegate.md` | `agy-delegate` | Delegate coding tasks to the Google Antigravity CLI (`agy`) only when |
| `agy-powerline.md` | `agy-powerline` | Install, check and restyle the agy-powerline statusline for Antigravity CLI (agy): quotas, model, context window and git on agy's status bar. |
| `ai-agent-development.md` | `ai-agent-development` | AI agent development workflow for building autonomous agents, multi-agent systems, and agent orchestration with CrewAI, LangGraph, and custom agents. |
| `ai-agent-evaluation-benchmarking.md` | `ai-agent-evaluation-benchmarking` | Autonomous AI agent benchmark evaluation register: task completion rates, planning accuracy, tool invocation precision, and cost benchmarks. |
| `ai-agent-security.md` | `ai-agent-security` | Secure AI agents against prompt injection, tool abuse, and data exfiltration |
| `ai-agent-tool-routing.md` | `ai-agent-tool-routing` | Use when designing or reviewing an AI agent tool registry or MCP router: document parameter schemas, caller authorization, execution limits, replay-safe retries and verification evidence. |
| `ai-agents-architect.md` | `ai-agents-architect` | Expert in designing and building autonomous AI agents. |
| `ai-analyzer.md` | `ai-analyzer` | AI驱动的综合健康分析系统，整合多维度健康数据、识别异常模式、整理风险因素、提供一般性健康信息。支持智能问答和AI健康报告生成。 |
| `ai-audiobook-narration.md` | `ai-audiobook-narration` | Install and use the official AI Audiobook Generator package, pinned by digest, for paid hosted work on the Beatra service. |
| `ai-blog-intro-writer.md` | `ai-blog-intro-writer` | AI Blog Intro Writer. |
| `ai-code-generation-guardrails.md` | `ai-code-generation-guardrails` | Use when reviewing AI-generated code before merge or execution: plan AST/security checks, isolated behavior tests and evidence, with language-specific coverage limits. |
| `ai-coding-agent-guardrails.md` | `ai-coding-agent-guardrails` | Secure AI coding agents (Claude Code, Cursor, Codex, Copilot) with permission |
| `ai-competitor-title-rewriter.md` | `ai-competitor-title-rewriter` | AI Competitor Title Rewriter. |
| `ai-content-detector.md` | `ai-content-detector` | AI Content Detector. |
| `ai-content-improver.md` | `ai-content-improver` | AI Content Improver. |
| `ai-content-outline-generator.md` | `ai-content-outline-generator` | AI Content Outline Generator. |
| `ai-dev-jobs-mcp.md` | `ai-dev-jobs-mcp` | Search indexed AI and ML jobs, inspect listings and employers, match roles, and view salary and market stats via AI Dev Jobs MCP |
| `ai-engineer.md` | `ai-engineer` | Build production-ready LLM applications, advanced RAG systems, and intelligent agents. |
| `ai-engineering-toolkit.md` | `ai-engineering-toolkit` | Overview of six AI engineering workflows: prompt evaluation (8-dimension scoring), context budget planning, RAG pipeline design, agent security audit (65-point checklist), eval harness building, and product sense coaching. |
| `ai-faq-creator.md` | `ai-faq-creator` | AI FAQ Creator. |
| `ai-headshot-studio.md` | `ai-headshot-studio` | Install and use the official AI Headshot Generator package, pinned by digest, for paid hosted work on the Beatra service. |
| `ai-image-generation-studio.md` | `ai-image-generation-studio` | Install and use the official AI Image Generator package, pinned by digest, for paid hosted work on the Beatra service. |
| `ai-image-realism.md` | `ai-image-realism` | Install and use the official AI Image Realism package, pinned by digest, for paid hosted work on the Beatra service. |
| `ai-inference-service-mesh.md` | `ai-inference-service-mesh` | Use verified service mesh patterns for AI inference traffic management, mTLS, |
| `ai-keyword-explainer.md` | `ai-keyword-explainer` | AI Keyword Explainer. |
| `ai-logo-maker.md` | `ai-logo-maker` | Install and use the official AI Logo Maker package, pinned by digest, for paid hosted work on the Beatra service. |
| `ai-loop.md` | `ai-loop` | Runs a bounded spec-build-review development loop with explicit scope, stop conditions, and human approval gates for risky or ambiguous work. |
| `ai-md.md` | `ai-md` | Convert human-written CLAUDE.md into AI-native structured-label format. |
| `ai-meta-tag-writer.md` | `ai-meta-tag-writer` | AI Meta Tag Writer. |
| `ai-ml.md` | `ai-ml` | AI and machine learning workflow covering LLM application development, RAG implementation, agent architecture, ML pipelines, and AI-powered features. |
| `ai-multilingual-dubbing.md` | `ai-multilingual-dubbing` | Install and use the official Multilingual Voiceover package, pinned by digest, for paid hosted work on the Beatra service. |
| `ai-native-cli.md` | `ai-native-cli` | Design spec with 98 rules for building CLI tools that AI agents can safely use. |
| `ai-native-ui.md` | `ai-native-ui` | Web and App implementation guide for AI Native UI. |
| `ai-photo-restyler.md` | `ai-photo-restyler` | Install and use the official Photo to Anime package, pinned by digest, for paid hosted work on the Beatra service. |
| `ai-pipeline-orchestration.md` | `ai-pipeline-orchestration` | Orchestrate AI/ML pipelines for data ingestion, model training, batch |
| `ai-podcast-voiceover.md` | `ai-podcast-voiceover` | Install and use the official AI Podcast Voiceover package, pinned by digest, for paid hosted work on the Beatra service. |
| `ai-product.md` | `ai-product` | Design and evaluate LLM product features, retrieval, validated outputs, latency, and cost controls. |
| `ai-prompt-regression-testing.md` | `ai-prompt-regression-testing` | Use when comparing prompt changes against a fixed evaluation set: record actual model settings, required checks, missing results, judge limitations and case-level regression evidence. |
| `ai-red-teaming.md` | `ai-red-teaming` | Run structured AI red team exercises for jailbreak resistance, data exfiltration |
| `ai-schema-generator.md` | `ai-schema-generator` | AI Schema Generator. |
| `ai-schema-markup-generator.md` | `ai-schema-markup-generator` | Schema Markup Generator. |
| `ai-security-hardening.md` | `ai-security-hardening` | Harden AI/LLM deployments against prompt injection, data exfiltration, |
| `ai-seo.md` | `ai-seo` | Optimize content for AI search and LLM citations across AI Overviews, ChatGPT, Perplexity, Claude, Gemini, and similar systems. |
| `ai-snippet-generator.md` | `ai-snippet-generator` | AI Snippet Generator. |
| `ai-sre-incident-response.md` | `ai-sre-incident-response` | Build AI-focused SRE incident response practices for LLM outages, degraded |
| `ai-storyboard-generator.md` | `ai-storyboard-generator` | Install and use the official AI Storyboard Generator package, pinned by digest, for paid hosted work on the Beatra service. |
| `ai-wrapper-product.md` | `ai-wrapper-product` | Expert in building products that wrap AI APIs (OpenAI, Anthropic, |
| `aident-loadout.md` | `aident-loadout` | Run multi-step work across apps the user connected in Aident Loadout: live action schemas, connection checks, cost preflight, and approval before side effects. |
| `airflow-dag-patterns.md` | `airflow-dag-patterns` | Build production Apache Airflow DAGs with best practices for operators, sensors, testing, and deployment. |
| `akf-trust-metadata.md` | `akf-trust-metadata` | The AI native file format. |
| `alerting-oncall.md` | `alerting-oncall` | Set up alerting rules, configure on-call rotations, and manage incident |
| `alex.md` | `alex` | Turns requirements into a precise, dependency-aware implementation plan. |
| `algolia-search.md` | `algolia-search` | Expert patterns for Algolia search implementation, indexing |
| `algorithmic-art.md` | `algorithmic-art` | Algorithmic philosophies are computational aesthetic movements that are then expressed through code. |
| `alternatives-pages.md` | `alternatives-pages` | Create \"[Competitor] alternative\" and comparison pages for developer tools. |
| `altorank.md` | `altorank` | Run AltoRank through its hosted MCP server: readiness audits, Search Console, keyword research, and SEO drafts into a review queue. |
| `alumni-re-hire-tracker.md` | `alumni-re-hire-tracker` | Alumni and re-hire register: former role, last working day, re-hire eligibility, current employer and re-engagement date, as CSV, SQL, JSON Schema or Notion on request. |
| `amazon-alexa.md` | `amazon-alexa` | Integracao completa com Amazon Alexa para criar skills de voz inteligentes, transformar Alexa em assistente com Claude como cerebro (projeto Auri) e integrar com AWS ecosystem (Lambda, DynamoDB, Polly, Transcribe, Lex, Smart Home). |
| `analytics.md` | `analytics` | When the user wants to set up, improve, or audit analytics tracking and measurement. |
| `analytics-tracking.md` | `analytics-tracking` | Design, audit, and improve analytics tracking systems that produce reliable, decision-ready data. |
| `analyze-project.md` | `analyze-project` | Forensic root cause analyzer for Antigravity sessions. |
| `anchor-text-analyzer.md` | `anchor-text-analyzer` | Anchor Text Analyzer. |
| `andrej-karpathy.md` | `andrej-karpathy` | Behavioral guidelines to reduce common LLM coding mistakes. |
| `android-cli.md` | `android-cli` | Orchestrates Android development tasks including project creation, deployment, SDK management, and environment diagnostics using the `android` command-line tool. |
| `android-dev.md` | `android-dev` | Production-grade Android app development guide covering native (Kotlin/Java), cross-platform (Flutter, RN, KMM), and hybrid architectures. |
| `android-jetpack-compose-expert.md` | `android-jetpack-compose-expert` | Expert guidance for building modern Android UIs with Jetpack Compose, covering state management, navigation, performance, and Material Design 3. |
| `android-ui-journey-testing.md` | `android-ui-journey-testing` | XML-specified Android UI journey testing, interactive step execution, assertion verification, and JSON outcome reporting. |
| `android_ui_verification.md` | `android_ui_verification` | Automated end-to-end UI testing and verification on an Android Emulator using ADB. |
| `angular.md` | `angular` | Modern Angular (v20+) expert with deep knowledge of Signals, Standalone Components, Zoneless applications, SSR/Hydration, and reactive patterns. |
| `angular-best-practices.md` | `angular-best-practices` | Angular performance optimization and best practices guide. |
| `angular-migration.md` | `angular-migration` | Master AngularJS to Angular migration, including hybrid apps, component conversion, dependency injection changes, and routing migration. |
| `angular-state-management.md` | `angular-state-management` | Master modern Angular state management with Signals, NgRx, and RxJS. |
| `angular-ui-patterns.md` | `angular-ui-patterns` | Modern Angular UI patterns for loading states, error handling, and data display. |
| `animate.md` | `animate` | Build purposeful web animations with appropriate tools, easing, duration, interruption, exits, and reduced-motion support. |
| `animate-expo.md` | `animate-expo` | Build React Native and Expo motion with gestures, Reanimated, haptics, accessible fallbacks, and device verification. |
| `animation-performance.md` | `animation-performance` | Diagnose dropped animation frames and choose properties, rendering paths, and profiling checks for smooth web motion. |
| `animation-vocabulary.md` | `animation-vocabulary` | Name a described animation effect using a reverse-lookup motion glossary. |
| `animejs-animation.md` | `animejs-animation` | Advanced JavaScript animation library skill for creating complex, high-performance web animations. |
| `announcement-board.md` | `announcement-board` | Announcement board: author, category, department, priority, audience, publish and expiry dates, status and acknowledgements, as CSV, SQL, JSON Schema or Notion on request. |
| `anti-deception.md` | `anti-deception` | Use before responding to pressure for agreement, manufactured urgency, authority appeals, or requests to certify unsupported claims; separate evidence from persuasion and state uncertainty. |
| `anti-reversing-techniques.md` | `anti-reversing-techniques` | Analyze anti-debugging, obfuscation, and anti-tamper techniques during authorized binary analysis and reverse engineering. |
| `anti-sleep.md` | `anti-sleep` | Keep a Mac awake with caffeinate during long builds, downloads, or supervised automation runs. |
| `anti-slop-design.md` | `anti-slop-design` | Autonomous Principal Design Technologist. |
| `anti-sycophancy.md` | `anti-sycophancy` | Eliminate sycophantic agreement patterns in AI responses. |
| `anti-ui-slop.md` | `anti-ui-slop` | Stop coding agents from shipping generic UI. |
| `antigravity-agent-manager.md` | `antigravity-agent-manager` | Configure and orchestrate parallel agents using the standalone Antigravity 2.0 Agent Manager and Antigravity IDE. |
| `antigravity-design-expert.md` | `antigravity-design-expert` | Core UI/UX engineering skill for building highly interactive, spatial, weightless, and glassmorphism-based web interfaces using GSAP and 3D CSS. |
| `antigravity-maintainer-batch-release.md` | `antigravity-maintainer-batch-release` | Run protected AAS maintainer sweeps, PR merge batches, resumable review, immutable distribution, Core checks, and scripted releases. |
| `antigravity-skill-orchestrator.md` | `antigravity-skill-orchestrator` | A meta-skill that understands task requirements, dynamically selects appropriate skills, tracks successful skill combinations using agent-memory-mcp, and prevents skill overuse for simple tasks. |
| `antigravity-workflows.md` | `antigravity-workflows` | Use when asked to ship a SaaS MVP, audit application security, build an AI agent, run browser QA, or design a domain model with multiple skills and verified checkpoints. |
| `aomi-transact.md` | `aomi-transact` | Use Aomi's standalone CLI or hosted Agent/Pipeline MCP to read chain state and prepare user-authorized transactions. |
| `api-analyzer.md` | `api-analyzer` | Validates whether an API request is correct based on provided inputs (method, URL, headers, body, auth, query params). |
| `api-and-interface-design.md` | `api-and-interface-design` | Guides stable API and interface design. |
| `api-contract-testing.md` | `api-contract-testing` | Design and review API contract tests across providers and consumers. |
| `api-design-principles.md` | `api-design-principles` | Master REST and GraphQL API design principles to build intuitive, scalable, and maintainable APIs that delight developers and stand the test of time. |
| `api-designer.md` | `api-designer` | Generates complete, production-ready REST API endpoint specifications for any system or domain the user describes. |
| `api-documentation.md` | `api-documentation` | API documentation workflow for generating OpenAPI specs, creating developer guides, and maintaining comprehensive API documentation. |
| `api-documentation-generator.md` | `api-documentation-generator` | Generate comprehensive, developer-friendly API documentation from code, including endpoints, parameters, examples, and best practices |
| `api-documenter.md` | `api-documenter` | Master API documentation with OpenAPI 3.1, AI-powered tools, and modern developer experience practices. |
| `api-endpoint-builder.md` | `api-endpoint-builder` | Builds reviewable REST API endpoint scaffolds with validation, error handling, authentication, and documentation. |
| `api-fuzzing-bug-bounty.md` | `api-fuzzing-bug-bounty` | Provide comprehensive techniques for testing REST, SOAP, and GraphQL APIs during bug bounty hunting and penetration testing engagements. |
| `api-integration.md` | `api-integration` | Designs event-driven architectures, webhook systems, API chaining flows, ETL pipelines, and integration patterns between services. |
| `api-integration-architect.md` | `api-integration-architect` | Design, implement, debug, and optimize API integrations with expert-level |
| `api-onboarding.md` | `api-onboarding` | Reduce time-to-first-API-call (TTFAC) by optimizing every step of the developer onboarding journey. |
| `api-patterns.md` | `api-patterns` | API design principles and decision-making. |
| `api-rate-limit-handler.md` | `api-rate-limit-handler` | Implement bounded, idempotency-aware API throttling, backoff, and retry handling for 429 and transient 5xx responses. |
| `api-sdk-generator.md` | `api-sdk-generator` | Generates client SDK code, API wrapper libraries, request/response models, and language-specific usage patterns for any REST API. |
| `api-security.md` | `api-security` | Authorized security assessment of REST, GraphQL, WebSocket, and SOAP APIs: discovery, authentication and authorization flaws (BOLA/IDOR, JWT/OAuth), rate-limit testing, and a structured multi-phase methodology. |
| `api-security-best-practices.md` | `api-security-best-practices` | Implement secure API design patterns including authentication, authorization, input validation, rate limiting, and protection against common API vulnerabilities |
| `api-security-testing.md` | `api-security-testing` | API security testing workflow for REST and GraphQL APIs covering authentication, authorization, rate limiting, input validation, and security best practices. |
| `api-testing-observability-api-mock.md` | `api-testing-observability-api-mock` | You are an API mocking expert specializing in realistic mock services for development, testing, and demos. |
| `apify-generate-output-schema.md` | `apify-generate-output-schema` | Generate output schemas (dataset_schema.json, output_schema.json, key_value_store_schema.json) |
| `apk-redteam-pipeline.md` | `apk-redteam-pipeline` | End-to-end Android APK red-team pipeline |
| `apk-reverse.md` | `apk-reverse` | Android APK reverse engineering: unpacking, Java decompilation, smali modification, repacking and signing, Frida dynamic hooking, and native .so analysis with jadx, apktool, adb, and related tools. |
| `app-builder.md` | `app-builder` | Main application building orchestrator. |
| `app-store-changelog.md` | `app-store-changelog` | Generate user-facing App Store release notes from git history since the last tag. |
| `app-store-optimization.md` | `app-store-optimization` | Complete App Store Optimization (ASO) toolkit for researching, optimizing, and tracking mobile app performance on Apple App Store and Google Play Store |
| `appdeploy.md` | `appdeploy` | Deploy web apps with backend APIs, database, and file storage. |
| `apple-container.md` | `apple-container` | Build, run, and manage OCI/Linux containers as lightweight per-container VMs on Apple-silicon macOS using Apple's open-source container CLI, no Docker daemon required. |
| `apple-design.md` | `apple-design` | Apply Apple-inspired interface and motion principles to gestures, typography, depth, feedback, and accessibility on the web. |
| `apple-notes-search.md` | `apple-notes-search` | Semantic + keyword search and connection-discovery across the user's own Apple Notes via the apple-notes MCP server. |
| `application-performance-performance-optimization.md` | `application-performance-performance-optimization` | Optimize end-to-end application performance with profiling, observability, and backend/frontend tuning. |
| `applicationinsights-web-ts.md` | `applicationinsights-web-ts` | Instrument browser/web apps with the Application Insights JavaScript SDK (@microsoft/applicationinsights-web). |
| `architect-review.md` | `architect-review` | Master software architect specializing in modern architecture |
| `architecture.md` | `architecture` | Architectural decision-making framework. |
| `architecture-decision-records.md` | `architecture-decision-records` | Comprehensive patterns for creating, maintaining, and managing Architecture Decision Records (ADRs) that capture the context and rationale behind significant technical decisions. |
| `architecture-patterns.md` | `architecture-patterns` | Master proven backend architecture patterns including Clean Architecture, Hexagonal Architecture, and Domain-Driven Design to build maintainable, testable, and scalable systems. |
| `architecture-review.md` | `architecture-review` | Review repository architecture using Ontoly Software Graph and MCP capabilities. |
| `arcmira-find-quotes.md` | `arcmira-find-quotes` | Search indexed YouTube and podcast transcripts for quotes, speakers and clip boundaries with timestamped source links using Arcmira. |
| `argocd-gitops.md` | `argocd-gitops` | Implement GitOps with ArgoCD for declarative Kubernetes deployments. |
| `aria.md` | `aria` | Designs the data model, API contracts, and structural foundation of the system. |
| `arm-cortex-expert.md` | `arm-cortex-expert` | Senior embedded software engineer specializing in firmware and driver development for ARM Cortex-M microcontrollers (Teensy, STM32, nRF52, SAMD). |
| `arm-templates.md` | `arm-templates` | Deploy Azure resources with ARM templates and Bicep. |
| `arrowspace.md` | `arrowspace` | Spectral vector search using graph Laplacian eigenstructure. |
| `article-illustrations.md` | `article-illustrations` | Generate hand-drawn 16:9 article illustrations with the Grav character IP, sparse annotations, and absurd but clear visual metaphors. |
| `artifact-yylo.md` | `artifact-yylo` | Capture and retrieve durable YYLO Ledger artifact Records with intentional |
| `ask-copilot.md` | `ask-copilot` | Use GitHub Copilot CLI in non-interactive mode to ask questions, review code, or generate snippets without manual interaction. |
| `ask-human-expert.md` | `ask-human-expert` | Ask real executives and domain experts a question through Instant Expert for a written answer or short call: practitioner knowledge, customer discovery. |
| `ask-matt.md` | `ask-matt` | Ask which skill or flow fits your situation. |
| `ask-questions-if-underspecified.md` | `ask-questions-if-underspecified` | Clarify requirements before implementing. |
| `ask-sonner.md` | `ask-sonner` | Set up and troubleshoot Sonner React toasts, including promises, loading states, updates, styling, theming, and placement. |
| `assay.md` | `assay` | Run assay on a web page you just wrote or changed. |
| `asset-inventory.md` | `asset-inventory` | Maintain IT asset inventory and configuration management database. |
| `asset-it-management.md` | `asset-it-management` | Asset and IT register: serial, model, condition, assignee, location, purchase value, warranty expiry and return date, as CSV, SQL, JSON Schema or Notion on request. |
| `astro.md` | `astro` | Build content-focused websites with Astro — zero JS by default, islands architecture, multi-framework components, and Markdown/MDX support. |
| `astropy.md` | `astropy` | Astropy is the core Python package for astronomy, providing essential functionality for astronomical research and data analysis. |
| `async-python-patterns.md` | `async-python-patterns` | Comprehensive guidance for implementing asynchronous Python applications using asyncio, concurrent programming patterns, and async/await for building high-performance, non-blocking systems. |
| `atlas-contract.md` | `atlas-contract` | Goal-integrity skill. |
| `atlas-ledger.md` | `atlas-ledger` | Companion to atlas-contract. |
| `attack-chain.md` | `attack-chain` | Authorized multi-stage attack-path planning and orchestration spanning reconnaissance, initial access, privilege escalation, lateral movement, and reporting. |
| `attack-tree-construction.md` | `attack-tree-construction` | Build comprehensive attack trees to visualize threat paths. |
| `attendance.md` | `attendance` | Daily attendance register: check-in and check-out, hours worked, work mode, late minutes, leave and regularisation flags, as CSV, SQL, JSON Schema or Notion on request. |
| `audio-transcriber.md` | `audio-transcriber` | Transform audio recordings into professional Markdown documentation with intelligent summaries using LLM integration |
| `audit-agent-run-evidence.md` | `audit-agent-run-evidence` | Use when an agent, harness, gateway, MCP workflow, or multi-step automation claims completion and the available traces, checkpoints, approvals, tool calls, or deployment records must be judged without trusting self-reported success. |
| `audit-context-building.md` | `audit-context-building` | Enables ultra-granular, line-by-line code analysis to build deep architectural context before vulnerability or bug finding. |
| `audit-log.md` | `audit-log` | Audit trail register: timestamp, user, module, record, action, field changed, old and new value, and the reason for the change. |
| `audit-logging.md` | `audit-logging` | Implement centralized audit logging and SIEM integration. |
| `audit-preparation.md` | `audit-preparation` | Audit preparation register: required document, period covered, request and receipt dates, preparer and reviewer, auditor queries and adjustments. |
| `audit-skills.md` | `audit-skills` | Expert security auditor for AI Skills and Bundles. |
| `auri-core.md` | `auri-core` | Auri: assistente de voz inteligente (Alexa + modelo Claude configurado e verificado). |
| `aurora-ui.md` | `aurora-ui` | Web and App implementation guide for Aurora UI. |
| `auth-implementation-patterns.md` | `auth-implementation-patterns` | Implement or review authentication and authorization with explicit token, session and resource-access boundaries. |
| `auto-research.md` | `auto-research` | Research uncertain questions with an explicit, user-approved web search or ChatGPT consultation, then present options and wait for implementation approval. |
| `automated-triage.md` | `automated-triage` | Triage Monte Carlo alerts interactively or build an automated workflow. |
| `autonomous-agent-patterns.md` | `autonomous-agent-patterns` | Design patterns for building autonomous coding agents, inspired by [Cline](https://github.com/cline/cline) and [OpenAI Codex](https://github.com/openai/codex). |
| `autonomous-agents.md` | `autonomous-agents` | Autonomous agents are AI systems that can independently decompose |
| `autorekt.md` | `autorekt` | Read live market data with the autorekt CLI before answering questions about prices, market moves, liquidity, positioning, options or prediction-market odds |
| `avalonia-layout-zafiro.md` | `avalonia-layout-zafiro` | Guidelines for modern Avalonia UI layout using Zafiro.Avalonia, emphasizing shared styles, generic components, and avoiding XAML redundancy. |
| `avalonia-viewmodels-zafiro.md` | `avalonia-viewmodels-zafiro` | Optimal ViewModel and Wizard creation patterns for Avalonia using Zafiro and ReactiveUI. |
| `avalonia-zafiro-development.md` | `avalonia-zafiro-development` | Mandatory skills, conventions, and behavioral rules for Avalonia UI development using the Zafiro toolkit. |
| `avoid-ai-writing.md` | `avoid-ai-writing` | Audit and rewrite prose for repetitive, vague, or formulaic wording while preserving meaning, evidence, and the writer's voice. |
| `awareness-stage-mapper.md` | `awareness-stage-mapper` | Map audience awareness stages to messaging strategy when planning a campaign, offer, or persuasion sequence. |
| `aws-agentic-ai.md` | `aws-agentic-ai` | AWS Bedrock AgentCore comprehensive expert for deploying and managing AI agents at scale. |
| `aws-cdk-development.md` | `aws-cdk-development` | AWS Cloud Development Kit (CDK) expert for building cloud infrastructure with TypeScript/Python. |
| `aws-cloudtrail.md` | `aws-cloudtrail` | Configure AWS CloudTrail for audit logging. |
| `aws-compliance-checker.md` | `aws-compliance-checker` | Automated compliance checking against CIS, PCI-DSS, HIPAA, and SOC 2 benchmarks |
| `aws-cost-cleanup.md` | `aws-cost-cleanup` | Automated cleanup of unused AWS resources to reduce costs |
| `aws-cost-operations.md` | `aws-cost-operations` | AWS cost optimization, monitoring, and operational excellence expert. |
| `aws-cost-optimization.md` | `aws-cost-optimization` | Reduce AWS spend with rightsizing, autoscaling, commitment planning, |
| `aws-cost-optimizer.md` | `aws-cost-optimizer` | Comprehensive AWS cost analysis and optimization recommendations using AWS CLI and Cost Explorer |
| `aws-ec2.md` | `aws-ec2` | Manage EC2 instances, AMIs, and auto-scaling groups. |
| `aws-lambda.md` | `aws-lambda` | Build and deploy serverless functions on AWS Lambda. |
| `aws-penetration-testing.md` | `aws-penetration-testing` | Provide comprehensive techniques for penetration testing AWS cloud environments. |
| `aws-rds.md` | `aws-rds` | Provision and manage RDS databases. |
| `aws-s3.md` | `aws-s3` | Configure S3 buckets, policies, and lifecycle rules. |
| `aws-secrets-rotation.md` | `aws-secrets-rotation` | Automate AWS secrets rotation for RDS, API keys, and credentials |
| `aws-security-audit.md` | `aws-security-audit` | Comprehensive AWS security posture assessment using AWS CLI and security best practices |
| `aws-serverless.md` | `aws-serverless` | Specialized skill for building production-ready serverless |
| `aws-serverless-eda.md` | `aws-serverless-eda` | AWS serverless and event-driven architecture expert based on Well-Architected Framework. |
| `aws-skills.md` | `aws-skills` | Plan and review AWS architecture and infrastructure changes using the upstream AWS skill collection. |
| `aws-sst-development.md` | `aws-sst-development` | SST v4 (Ion) expert for managing AWS resources as code with the Pulumi-backed framework. |
| `aws-vpc.md` | `aws-vpc` | Design and implement VPCs and networking. |
| `awt-e2e-testing.md` | `awt-e2e-testing` | AI-powered E2E web testing — eyes and hands for AI coding tools. |
| `ax-extract-workflow.md` | `ax-extract-workflow` | Reconstruct workflow behind a past coding-agent artifact using local ax sessions/commits/skills/tool traces. |
| `axiom.md` | `axiom` | First-principles assumption auditor. |
| `azd-deployment.md` | `azd-deployment` | Prepare and verify authorized Azure Container Apps deployments with azd. |
| `azure-ai-agents-persistent-dotnet.md` | `azure-ai-agents-persistent-dotnet` | Azure AI Agents Persistent SDK for .NET. |
| `azure-ai-agents-persistent-java.md` | `azure-ai-agents-persistent-java` | Azure AI Agents Persistent SDK for Java. |
| `azure-ai-contentunderstanding-py.md` | `azure-ai-contentunderstanding-py` | Azure AI Content Understanding SDK for Python. |
| `azure-ai-ml-py.md` | `azure-ai-ml-py` | Azure Machine Learning SDK v2 for Python. |
| `azure-ai-projects-dotnet.md` | `azure-ai-projects-dotnet` | Azure AI Projects SDK for .NET. |
| `azure-ai-projects-java.md` | `azure-ai-projects-java` | Azure AI Projects SDK for Java. |
| `azure-ai-projects-py.md` | `azure-ai-projects-py` | Build AI applications on Microsoft Foundry using the azure-ai-projects SDK. |
| `azure-ai-projects-ts.md` | `azure-ai-projects-ts` | High-level SDK for Azure AI Foundry projects with agents, connections, deployments, and evaluations. |
| `azure-aks.md` | `azure-aks` | Deploy and manage Azure Kubernetes Service clusters. |
| `azure-appconfiguration-java.md` | `azure-appconfiguration-java` | Azure App Configuration SDK for Java. |
| `azure-appconfiguration-py.md` | `azure-appconfiguration-py` | Azure App Configuration SDK for Python. |
| `azure-appconfiguration-ts.md` | `azure-appconfiguration-ts` | Centralized configuration management with feature flags and dynamic refresh. |
| `azure-communication-callautomation-java.md` | `azure-communication-callautomation-java` | Build server-side call automation workflows including IVR systems, call routing, recording, and AI-powered interactions. |
| `azure-communication-callingserver-java.md` | `azure-communication-callingserver-java` | ⚠️ DEPRECATED: This SDK has been renamed to Call Automation. |
| `azure-communication-sms-java.md` | `azure-communication-sms-java` | Send SMS messages with Azure Communication Services SMS Java SDK. |
| `azure-containerregistry-py.md` | `azure-containerregistry-py` | Azure Container Registry SDK for Python. |
| `azure-cosmos-py.md` | `azure-cosmos-py` | Azure Cosmos DB SDK for Python (NoSQL API). |
| `azure-cosmos-rust.md` | `azure-cosmos-rust` | Azure Cosmos DB SDK for Rust (NoSQL API). |
| `azure-data-tables-java.md` | `azure-data-tables-java` | Build table storage applications using the Azure Tables SDK for Java. |
| `azure-data-tables-py.md` | `azure-data-tables-py` | Azure Tables SDK for Python (Storage and Cosmos DB). |
| `azure-devops.md` | `azure-devops` | Set up Azure Pipelines for CI/CD, configure build and release pipelines, |
| `azure-eventgrid-py.md` | `azure-eventgrid-py` | Azure Event Grid SDK for Python. |
| `azure-eventhub-dotnet.md` | `azure-eventhub-dotnet` | Azure Event Hubs SDK for .NET. |
| `azure-eventhub-java.md` | `azure-eventhub-java` | Build real-time streaming applications with Azure Event Hubs SDK for Java. |
| `azure-eventhub-py.md` | `azure-eventhub-py` | Azure Event Hubs SDK for Python streaming. |
| `azure-eventhub-rust.md` | `azure-eventhub-rust` | Azure Event Hubs SDK for Rust. |
| `azure-eventhub-ts.md` | `azure-eventhub-ts` | High-throughput event streaming and real-time data ingestion. |
| `azure-functions.md` | `azure-functions` | Expert patterns for Azure Functions development including isolated |
| `azure-functions-devsec.md` | `azure-functions-devsec` | Build serverless applications on Azure Functions. |
| `azure-identity-dotnet.md` | `azure-identity-dotnet` | Azure Identity SDK for .NET. |
| `azure-identity-java.md` | `azure-identity-java` | Authenticate Java applications with Azure services using Microsoft Entra ID (Azure AD). |
| `azure-identity-py.md` | `azure-identity-py` | Azure Identity SDK for Python authentication. |
| `azure-identity-rust.md` | `azure-identity-rust` | Azure Identity SDK for Rust authentication. |
| `azure-identity-ts.md` | `azure-identity-ts` | Authenticate to Azure services with various credential types. |
| `azure-keyvault.md` | `azure-keyvault` | Manage secrets and certificates in Azure Key Vault. |
| `azure-keyvault-certificates-rust.md` | `azure-keyvault-certificates-rust` | Azure Key Vault Certificates SDK for Rust. |
| `azure-keyvault-keys-rust.md` | `azure-keyvault-keys-rust` | Azure Key Vault Keys SDK for Rust. |
| `azure-keyvault-keys-ts.md` | `azure-keyvault-keys-ts` | Manage cryptographic keys using Azure Key Vault Keys SDK for JavaScript (@azure/keyvault-keys). |
| `azure-keyvault-py.md` | `azure-keyvault-py` | Azure Key Vault SDK for Python. |
| `azure-keyvault-secrets-rust.md` | `azure-keyvault-secrets-rust` | Azure Key Vault Secrets SDK for Rust. |
| `azure-keyvault-secrets-ts.md` | `azure-keyvault-secrets-ts` | Manage secrets using Azure Key Vault Secrets SDK for JavaScript (@azure/keyvault-secrets). |
| `azure-maps-search-dotnet.md` | `azure-maps-search-dotnet` | Azure Maps SDK for .NET. |
| `azure-messaging-webpubsubservice-py.md` | `azure-messaging-webpubsubservice-py` | Azure Web PubSub Service SDK for Python. |
| `azure-mgmt-apicenter-dotnet.md` | `azure-mgmt-apicenter-dotnet` | Azure API Center SDK for .NET. |
| `azure-mgmt-apicenter-py.md` | `azure-mgmt-apicenter-py` | Azure API Center Management SDK for Python. |
| `azure-mgmt-apimanagement-dotnet.md` | `azure-mgmt-apimanagement-dotnet` | Azure Resource Manager SDK for API Management in .NET. |
| `azure-mgmt-apimanagement-py.md` | `azure-mgmt-apimanagement-py` | Azure API Management SDK for Python. |
| `azure-mgmt-applicationinsights-dotnet.md` | `azure-mgmt-applicationinsights-dotnet` | Azure Application Insights SDK for .NET. |
| `azure-mgmt-arizeaiobservabilityeval-dotnet.md` | `azure-mgmt-arizeaiobservabilityeval-dotnet` | Azure Resource Manager SDK for Arize AI Observability and Evaluation (.NET). |
| `azure-mgmt-botservice-dotnet.md` | `azure-mgmt-botservice-dotnet` | Azure Resource Manager SDK for Bot Service in .NET. |
| `azure-mgmt-botservice-py.md` | `azure-mgmt-botservice-py` | Azure Bot Service Management SDK for Python. |
| `azure-mgmt-fabric-dotnet.md` | `azure-mgmt-fabric-dotnet` | Azure Resource Manager SDK for Fabric in .NET. |
| `azure-mgmt-fabric-py.md` | `azure-mgmt-fabric-py` | Azure Fabric Management SDK for Python. |
| `azure-mgmt-mongodbatlas-dotnet.md` | `azure-mgmt-mongodbatlas-dotnet` | Manage MongoDB Atlas Organizations as Azure ARM resources with unified billing through Azure Marketplace. |
| `azure-mgmt-weightsandbiases-dotnet.md` | `azure-mgmt-weightsandbiases-dotnet` | Azure Weights & Biases SDK for .NET. |
| `azure-monitor-audit.md` | `azure-monitor-audit` | Configure Azure Monitor and Activity Log for auditing. |
| `azure-monitor-ingestion-java.md` | `azure-monitor-ingestion-java` | Azure Monitor Ingestion SDK for Java. |
| `azure-monitor-ingestion-py.md` | `azure-monitor-ingestion-py` | Azure Monitor Ingestion SDK for Python. |
| `azure-monitor-opentelemetry-exporter-java.md` | `azure-monitor-opentelemetry-exporter-java` | Azure Monitor OpenTelemetry Exporter for Java. |
| `azure-monitor-opentelemetry-exporter-py.md` | `azure-monitor-opentelemetry-exporter-py` | Azure Monitor OpenTelemetry Exporter for Python. |
| `azure-monitor-opentelemetry-py.md` | `azure-monitor-opentelemetry-py` | Azure Monitor OpenTelemetry Distro for Python. |
| `azure-monitor-opentelemetry-ts.md` | `azure-monitor-opentelemetry-ts` | Auto-instrument Node.js applications with distributed tracing, metrics, and logs. |
| `azure-monitor-query-java.md` | `azure-monitor-query-java` | Azure Monitor Query SDK for Java. |
| `azure-monitor-query-py.md` | `azure-monitor-query-py` | Azure Monitor Query SDK for Python. |
| `azure-networking.md` | `azure-networking` | Configure Azure VNets, NSGs, and Azure Firewall. |
| `azure-postgres-ts.md` | `azure-postgres-ts` | Connect to Azure Database for PostgreSQL Flexible Server from Node.js/TypeScript using the pg (node-postgres) package. |
| `azure-resource-manager-cosmosdb-dotnet.md` | `azure-resource-manager-cosmosdb-dotnet` | Azure Resource Manager SDK for Cosmos DB in .NET. |
| `azure-resource-manager-durabletask-dotnet.md` | `azure-resource-manager-durabletask-dotnet` | Azure Resource Manager SDK for Durable Task Scheduler in .NET. |
| `azure-resource-manager-mysql-dotnet.md` | `azure-resource-manager-mysql-dotnet` | Azure MySQL Flexible Server SDK for .NET. |
| `azure-resource-manager-playwright-dotnet.md` | `azure-resource-manager-playwright-dotnet` | Azure Resource Manager SDK for Microsoft Playwright Testing in .NET. |
| `azure-resource-manager-postgresql-dotnet.md` | `azure-resource-manager-postgresql-dotnet` | Azure PostgreSQL Flexible Server SDK for .NET. |
| `azure-resource-manager-redis-dotnet.md` | `azure-resource-manager-redis-dotnet` | Azure Resource Manager SDK for Redis in .NET. |
| `azure-resource-manager-sql-dotnet.md` | `azure-resource-manager-sql-dotnet` | Azure Resource Manager SDK for Azure SQL in .NET. |
| `azure-search-documents-py.md` | `azure-search-documents-py` | Azure AI Search SDK for Python. |
| `azure-security-keyvault-keys-dotnet.md` | `azure-security-keyvault-keys-dotnet` | Azure Key Vault Keys SDK for .NET. |
| `azure-security-keyvault-secrets-java.md` | `azure-security-keyvault-secrets-java` | Azure Key Vault Secrets Java SDK for secret management. |
| `azure-servicebus-dotnet.md` | `azure-servicebus-dotnet` | Azure Service Bus SDK for .NET. |
| `azure-servicebus-py.md` | `azure-servicebus-py` | Azure Service Bus SDK for Python messaging. |
| `azure-servicebus-rust.md` | `azure-servicebus-rust` | Azure Service Bus library for Rust. |
| `azure-servicebus-ts.md` | `azure-servicebus-ts` | Enterprise messaging with queues, topics, and subscriptions. |
| `azure-sql.md` | `azure-sql` | Provision Azure SQL Database and Cosmos DB. |
| `azure-storage-blob-java.md` | `azure-storage-blob-java` | Build blob storage applications using the Azure Storage Blob SDK for Java. |
| `azure-storage-blob-py.md` | `azure-storage-blob-py` | Azure Blob Storage SDK for Python. |
| `azure-storage-blob-rust.md` | `azure-storage-blob-rust` | Azure Blob Storage SDK for Rust. |
| `azure-storage-file-datalake-py.md` | `azure-storage-file-datalake-py` | Azure Data Lake Storage Gen2 SDK for Python. |
| `azure-storage-file-share-py.md` | `azure-storage-file-share-py` | Azure Storage File Share SDK for Python. |
| `azure-storage-file-share-ts.md` | `azure-storage-file-share-ts` | Azure File Share JavaScript/TypeScript SDK (@azure/storage-file-share) for SMB file share operations. |
| `azure-storage-queue-py.md` | `azure-storage-queue-py` | Azure Queue Storage SDK for Python. |
| `azure-storage-queue-rust.md` | `azure-storage-queue-rust` | Azure Queue Storage library for Rust. |
| `azure-storage-queue-ts.md` | `azure-storage-queue-ts` | Azure Queue Storage JavaScript/TypeScript SDK (@azure/storage-queue) for message queue operations. |
| `azure-vms.md` | `azure-vms` | Manage Azure Virtual Machines and scale sets. |
| `azure-web-pubsub-ts.md` | `azure-web-pubsub-ts` | Real-time messaging with WebSocket connections and pub/sub patterns. |
| `babysit-pr.md` | `babysit-pr` | 'Babysit a pull request through its bot review rounds: verify, fix, reply, |
| `backend-architect.md` | `backend-architect` | Expert backend architect specializing in scalable API design, microservices architecture, and distributed systems. |
| `backend-dev-guidelines.md` | `backend-dev-guidelines` | You are a senior backend engineer operating production-grade services under strict architectural and reliability constraints. |
| `backend-development-feature-development.md` | `backend-development-feature-development` | Orchestrate end-to-end backend feature development from requirements to deployment. |
| `backend-security-coder.md` | `backend-security-coder` | Expert in secure backend coding practices specializing in input validation, authentication, and API security. |
| `backlink-idea-generator.md` | `backlink-idea-generator` | Backlink Idea Generator. |
| `backlink-tracking-template-generator.md` | `backlink-tracking-template-generator` | Backlink Tracking Template Generator. |
| `backtesting-frameworks.md` | `backtesting-frameworks` | Build robust, production-grade backtesting systems that avoid common pitfalls and produce reliable strategy performance estimates. |
| `backup-recovery.md` | `backup-recovery` | Implement backup and recovery strategies. |
| `base.md` | `base` | Database management, forms, reports, and data operations with LibreOffice Base. |
| `baseline-ui.md` | `baseline-ui` | Quickly deslop UI code by fixing spacing, hierarchy, typography, and small layout issues. |
| `bash.md` | `bash` | Language-specific super-code guidelines for bash. |
| `bash-defensive-patterns.md` | `bash-defensive-patterns` | Master defensive Bash programming techniques for production-grade scripts. |
| `bash-linux.md` | `bash-linux` | Bash/Linux terminal patterns. |
| `bash-pro.md` | `bash-pro` | 'Master of defensive Bash scripting for production automation, CI/CD |
| `bash-scripting.md` | `bash-scripting` | Bash scripting workflow for creating production-ready shell scripts with defensive patterns, error handling, and testing. |
| `bats-testing-patterns.md` | `bats-testing-patterns` | Master Bash Automated Testing System (Bats) for comprehensive shell script testing. |
| `bazel-build-optimization.md` | `bazel-build-optimization` | Optimize Bazel builds for large-scale monorepos. |
| `bb-methodology.md` | `bb-methodology` | Use at the START of any bug bounty hunting session, when switching targets, |
| `bdi-mental-states.md` | `bdi-mental-states` | This skill should be used when the user asks to "model agent mental states", "implement BDI architecture", "create belief-desire-intention models", "transform RDF to beliefs", "build cognitive agent", or mentions BDI ontology, mental state modeling, rational agency, or neuro-symbolic AI integration. |
| `bdistill-behavioral-xray.md` | `bdistill-behavioral-xray` | X-ray any AI model's behavioral patterns — refusal boundaries, hallucination tendencies, reasoning style, formatting defaults. |
| `bdistill-knowledge-extraction.md` | `bdistill-knowledge-extraction` | Extract structured domain knowledge from AI models in-session or from local open-source models via Ollama. |
| `beatra.md` | `beatra` | Install and use the official AI Media Generator package, pinned by digest, for paid hosted work on the Beatra service. |
| `beatra-ai-video-studio.md` | `beatra-ai-video-studio` | Install and use the official Beatra AI Video Studio package, pinned by digest, for paid text-to-video, image-to-video, and video edit or extend jobs on the hosted Beatra service. |
| `beautiful-prose.md` | `beautiful-prose` | A hard-edged writing style contract for timeless, forceful English prose without modern AI tics. |
| `before-you-build.md` | `before-you-build` | Review product risk before coding by checking demand, alternatives, channels, switching costs, and failure signals. |
| `behavioral-modes.md` | `behavioral-modes` | AI operational modes (brainstorm, implement, debug, review, teach, ship, orchestrate). |
| `bento-ui.md` | `bento-ui` | Web and App implementation guide for Bento UI. |
| `better-accessibility.md` | `better-accessibility` | Reviews and fixes keyboard and focus behavior, ARIA, accessible names, forms, screen-reader announcements, motion and zoom against WCAG 2.2. |
| `better-colors.md` | `better-colors` | Builds and checks color systems by generating palettes, naming semantic tokens, converting between formats and measuring contrast. |
| `better-interface.md` | `better-interface` | Reviews a screen, flow or whole interface across accessibility, layout, writing, typography, color and UI polish, and returns one ranked report. |
| `better-layout.md` | `better-layout` | Sets grouping, alignment, reading order, responsive structure and room for translated text, so a layout holds up when it is resized, translated or mirrored. |
| `better-typography.md` | `better-typography` | Sets and reviews how text renders, from the type scale and spacing to font features, wrapping, truncation and punctuation. |
| `better-ui.md` | `better-ui` | Polishes surfaces, icons and motion with exact values for border radius, optical alignment, shadows, icon states and animation. |
| `better-writing.md` | `better-writing` | Writes and reviews interface copy, from labels and errors to empty states and confirmations, so it matches the product's voice and tells people what to do next. |
| `bevy-ecs-expert.md` | `bevy-ecs-expert` | Master Bevy's Entity Component System (ECS) in Rust, covering Systems, Queries, Resources, and parallel scheduling. |
| `bilig-workpaper.md` | `bilig-workpaper` | Use formula-backed WorkPaper JSON and MCP tools for agent spreadsheet tasks without driving Excel or a browser UI. |
| `bill-gates.md` | `bill-gates` | Simulacao educativa de analise estrategica inspirada em temas publicos de Bill Gates; nao representa a pessoa real ou suas opinioes atuais. |
| `billing-automation.md` | `billing-automation` | Master automated billing systems including recurring billing, invoice generation, dunning management, proration, and tax calculation. |
| `binary-analysis-patterns.md` | `binary-analysis-patterns` | Comprehensive patterns and techniques for analyzing compiled binaries, understanding assembly code, and reconstructing program logic. |
| `binary-diff.md` | `binary-diff` | Cross-version binary symbol migration: diff updated binaries, recover function names without PDBs, and propagate annotations after software updates using BinDiff-style tooling. |
| `biopython.md` | `biopython` | Biopython is a comprehensive set of freely available Python tools for biological computation. |
| `block-storage.md` | `block-storage` | Manage block storage volumes and LVM. |
| `blockchain-developer.md` | `blockchain-developer` | Build production-ready Web3 applications, smart contracts, and decentralized systems. |
| `blockrun.md` | `blockrun` | BlockRun works with Claude Code and Google Antigravity. |
| `blockvectra-docs.md` | `blockvectra-docs` | Answer BlockVectra RPC, indexed-data, and Robinhood Chain integration questions from cited documentation. |
| `blog-title-generator.md` | `blog-title-generator` | Blog Title Generator. |
| `blog-writing-guide.md` | `blog-writing-guide` | This skill enforces Sentry's blog writing standards across every post — whether you're helping an engineer write their first blog post or a marketer draft a product announcement. |
| `blue-green-deploy.md` | `blue-green-deploy` | Configure zero-downtime deployment strategies including blue-green, canary, |
| `bluebook-writing.md` | `bluebook-writing` | Write design-reading books and articles in plain language with a two-layer skeleton: a zero-terminology everyday story first, then the professional layer with formal names, mechanisms, boundaries, and costs. |
| `blueprint.md` | `blueprint` | Turn a one-line objective into a step-by-step construction plan any coding agent can execute cold. |
| `board-governance.md` | `board-governance` | Board and governance register: meeting date, agenda, decision, resolution number, vote result, action owner and due date. |
| `boost-asio-pro.md` | `boost-asio-pro` | Use when writing asynchronous C++ networking code with Boost.Asio or standalone Asio — TCP/UDP servers and clients, SSL/TLS, timers, strands, composed async ops. |
| `bounce-rate-estimator.md` | `bounce-rate-estimator` | Bounce Rate Estimator. |
| `brain-to-docs.md` | `brain-to-docs` | Interview the user to turn project vision and decisions into README and ADR documentation. |
| `brainstorming.md` | `brainstorming` | Use before creative or constructive work (features, architecture, behavior). |
| `brand-growth-system-builder.md` | `brand-growth-system-builder` | Route requests across 13 brand and growth modules. |
| `brand-guidelines.md` | `brand-guidelines` | Write copy following Sentry brand guidelines. |
| `brand-guidelines-anthropic.md` | `brand-guidelines-anthropic` | To access Anthropic's official brand identity and style resources, use this skill. |
| `brand-guidelines-community.md` | `brand-guidelines-community` | To access Anthropic's official brand identity and style resources, use this skill. |
| `brand-kit-print-collateral.md` | `brand-kit-print-collateral` | Print collateral spec: item, finished/trim size and artwork size including bleed, bleed, colour mode, stock and GSM, finish, safe margin, print method, quantity and unit cost. |
| `brand-perception-psychologist.md` | `brand-perception-psychologist` | Audit visual, verbal, and behavioral brand signals and propose alignment changes when market perception differs from the intended position. |
| `brave-man.md` | `brave-man` | Runs a structured clarifying interview for new project requests before building. |
| `break.md` | `break` | Renders a component you choose under every scenario that can reach it on a temporary page and stress tests it. |
| `break-ai-fix-loops.md` | `break-ai-fix-loops` | Stop ineffective AI coding repair loops with stable failure fingerprints, a three-attempt budget, real-path proof, negative controls, and tested rollback. |
| `break-ui.md` | `break-ui` | Stress-test a component with realistic worst-case data through a development-only fixture toggle and report verified failures. |
| `brendangregg-use-tsa.md` | `brendangregg-use-tsa` | Methodical performance troubleshooting and root-cause analysis with Brendan Gregg's USE and TSA methods, plus evidence-backed RCA and postmortem reports. |
| `broken-authentication.md` | `broken-authentication` | Identify and exploit authentication and session management vulnerabilities in web applications. |
| `broken-link-finder.md` | `broken-link-finder` | Broken Link Finder. |
| `brooks-audit.md` | `brooks-audit` | Architecture audit that maps module dependencies, checks layering integrity, and flags structural decay across a codebase, drawing on twelve classic engineering books. |
| `brooks-debt.md` | `brooks-debt` | Tech debt assessment that identifies, classifies, and prioritizes maintainability problems — helping teams build a refactoring roadmap — drawing on twelve classic engineering books. |
| `brooks-harness.md` | `brooks-harness` | Maintenance orchestrator for the brooks-lint plugin itself. |
| `brooks-lint.md` | `brooks-lint` | AI code reviewer grounded in classic software engineering books for catching design smells, coupling issues, and architectural risks. |
| `brooks-review.md` | `brooks-review` | PR code review that surfaces decay risks, design smells, and maintainability issues with concrete Symptom → Source → Consequence → Remedy findings, drawing on twelve classic engineering books. |
| `brooks-sweep.md` | `brooks-sweep` | Full-sweep mode: runs a unified analysis across all quality dimensions — code decay, architecture, tech debt, and test quality — then applies fixes directly to the codebase. |
| `brooks-test.md` | `brooks-test` | Review test-suite quality using established testing literature; identify brittleness, mock abuse, unclear fixtures, weak assertions, slow feedback, and maintenance risks. |
| `browser-act.md` | `browser-act` | Use BrowserAct for authenticated browser automation, JS-rendered extraction, screenshots, parallel sessions, verification handling, and human handoff. |
| `browser-automation.md` | `browser-automation` | Build reliable browser checks using observed UI state, semantic locators, bounded waits, isolated test data and explicit outcome verification. |
| `browser-bridge.md` | `browser-bridge` | Inspect, control, and automate tasks in your real Microsoft Edge or Google Chrome browser via Chrome DevTools Protocol (CDP) with bilingual UI, native tab grouping, and self-healing daemon. |
| `browser-extension-builder.md` | `browser-extension-builder` | Expert in building browser extensions that solve real problems - |
| `browser-extension-launch.md` | `browser-extension-launch` | Builds, tests, packages, and prepares Chrome extensions for store launch from a plain-language idea; use for new extensions, fixes, releases, and submission recovery. |
| `browser-extension-reverse.md` | `browser-extension-reverse` | Authorized reverse engineering of Chrome/Firefox extensions: manifest analysis, background workers, content scripts, and extension-based credential or data-exposure research. |
| `browser-testing-with-devtools.md` | `browser-testing-with-devtools` | Test browser apps with Chrome DevTools MCP by inspecting live DOM, console logs, network traffic, screenshots, accessibility, and performance traces. |
| `brutalism.md` | `brutalism` | Web and App implementation guide for Brutalism. |
| `brutalist-typography.md` | `brutalist-typography` | Web and App implementation guide for Brutalist Typography. |
| `buddy-program-manager.md` | `buddy-program-manager` | Buddy programme register: new hire, assigned buddy, department, start and end dates, check-ins planned and done, and feedback score. |
| `budget-cash-flow.md` | `budget-cash-flow` | Budget against actual by department, category and period, with budget and actual amounts, variance, percentage used and linked expenses. |
| `bug-bounty.md` | `bug-bounty` | Complete bug bounty workflow |
| `bug-hunt-swarm.md` | `bug-hunt-swarm` | Parallel read-only multi-agent root-cause investigation for bugs, regressions, crashes, flaky behavior, or unexplained failures. |
| `bug-hunter.md` | `bug-hunter` | Systematically finds and fixes bugs using proven debugging techniques. |
| `bugcrowd-reporting.md` | `bugcrowd-reporting` | Bugcrowd-specific reporting tactics complementing report-writing |
| `bugs-are-annoying.md` | `bugs-are-annoying` | Adversarial code auditor that hunts down bugs, logic errors, and security flaws. |
| `build.md` | `build` | Use when developing a major feature: research the project, create a phased implementation plan, track progress and verify phase outcomes before declaring completion. |
| `build-design.md` | `build-design` | Builds UI from a Figma file or a design image so it matches the design, using the project's existing tokens and components. |
| `build-ui.md` | `build-ui` | Step-by-step workflow for UI work: read the project, follow the plan for the job (new screen, dashboard, polish, simplify, review), then render, fix and check again. |
| `building-native-ui.md` | `building-native-ui` | Complete guide for building beautiful apps with Expo Router. |
| `bulletmind.md` | `bulletmind` | Convert input into clean, structured, hierarchical bullet points for summarization, note-taking, and structured thinking. |
| `bullmq-specialist.md` | `bullmq-specialist` | BullMQ expert for Redis-backed job queues, background processing, |
| `bumblebee.md` | `bumblebee` | Run Bumblebee supply-chain inventory and exposure scans on macOS/Linux to detect compromised packages, extensions, and MCP host configs. |
| `bun-development.md` | `bun-development` | Fast, modern JavaScript/TypeScript development with the Bun runtime, inspired by [oven-sh/bun](https://github.com/oven-sh/bun). |
| `burp-suite-testing.md` | `burp-suite-testing` | Execute comprehensive web application security testing using Burp Suite's integrated toolset, including HTTP traffic interception and modification, request analysis and replay, automated vulnerability scanning, and manual testing workflows. |
| `burpsuite-project-parser.md` | `burpsuite-project-parser` | Searches and explores Burp Suite project files (.burp) from the command line. |
| `busabase.md` | `busabase` | Use when managing Busabase workspace records, knowledge, apps, or skills through permission-aware ChangeRequests with auditable history. |
| `business-analyst.md` | `business-analyst` | Master modern business analysis with AI-powered analytics, real-time dashboards, and data-driven insights. |
| `business-continuity.md` | `business-continuity` | Develop business continuity plans and impact analysis. |
| `business-email-template.md` | `business-email-template` | Business email template register: trigger, sender and recipient type, subject pattern, body structure, personalisation tokens and send checks. |
| `business-website-setup.md` | `business-website-setup` | Website page register: URL, title, meta description, search intent, NAP block, schema type, canonical, indexability and Core Web Vitals target. |
| `busybox-on-windows.md` | `busybox-on-windows` | How to use a Win32 build of BusyBox to run many of the standard UNIX command line tools on Windows. |
| `buywhere-product-catalog.md` | `buywhere-product-catalog` | Use BuyWhere's MCP and API surfaces to add product search, price comparison, and deal discovery to AI shopping agents. |
| `c.md` | `c` | Language-specific super-code guidelines for c. |
| `c-pro.md` | `c-pro` | Review and implement C systems code with explicit memory ownership, pointer bounds, error handling, and measured performance. |
| `c4-architecture-c4-architecture.md` | `c4-architecture-c4-architecture` | Generate comprehensive C4 architecture documentation for an existing repository/codebase using a bottom-up analysis approach. |
| `c4-code.md` | `c4-code` | Expert C4 Code-level documentation specialist. |
| `c4-component.md` | `c4-component` | Expert C4 Component-level documentation specialist. |
| `c4-container.md` | `c4-container` | Expert C4 Container-level documentation specialist. |
| `c4-context.md` | `c4-context` | Expert C4 Context-level documentation specialist. |
| `calc.md` | `calc` | Spreadsheet creation, format conversion (ODS/XLSX/CSV), formulas, data automation with LibreOffice Calc. |
| `calibrate-first.md` | `calibrate-first` | Measure a dataset's detection floor before reading any trading-signal result, pre-register every test, and report too-small-to-see as UNDECIDABLE, not 'no effect'. |
| `candidate-talent-pool.md` | `candidate-talent-pool` | Candidate and prospect pool: contact details, experience, skills, consent status and date, referral source and last contact. |
| `canonical-tag-checker.md` | `canonical-tag-checker` | Canonical Tag Checker. |
| `canonical-url-builder.md` | `canonical-url-builder` | Canonical URL Builder. |
| `canvas-design.md` | `canvas-design` | These are instructions for creating design philosophies - aesthetic movements that are then EXPRESSED VISUALLY. |
| `capacity-workload-planner.md` | `capacity-workload-planner` | Weekly capacity and workload register: available and allocated hours, utilisation percentage, over-allocation check and leave days. |
| `card-based-design.md` | `card-based-design` | Web and App implementation guide for Card-Based Design. |
| `career-ops.md` | `career-ops` | 'Open-source AI job search agent for AI coding CLIs: evaluate offers, |
| `carrier-relationship-management.md` | `carrier-relationship-management` | Codified expertise for managing carrier portfolios, negotiating freight rates, tracking carrier performance, allocating freight, and maintaining strategic carrier relationships. |
| `case-review.md` | `case-review` | Quality-gate review of a reverse-engineering or assessment case package: scope readiness, Evidence-to-Finding-to-Path traceability, work-item coverage, timeline consistency, and artifact hashes. |
| `cc-skill-backend-patterns.md` | `cc-skill-backend-patterns` | Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, Express, and Next.js API routes. |
| `cc-skill-clickhouse-io.md` | `cc-skill-clickhouse-io` | ClickHouse database patterns, query optimization, analytics, and data engineering best practices for high-performance analytical workloads. |
| `cc-skill-coding-standards.md` | `cc-skill-coding-standards` | Universal coding standards, best practices, and patterns for TypeScript, JavaScript, React, and Node.js development. |
| `cc-skill-continuous-learning.md` | `cc-skill-continuous-learning` | Turn a completed debugging session or repeated user correction into a small, evidence-backed procedure. |
| `cc-skill-frontend-patterns.md` | `cc-skill-frontend-patterns` | Frontend development patterns for React, Next.js, state management, performance optimization, and UI best practices. |
| `cc-skill-project-guidelines-example.md` | `cc-skill-project-guidelines-example` | Project Guidelines Skill (Example) |
| `cc-skill-security-review.md` | `cc-skill-security-review` | This skill guides review of security practices and potential vulnerabilities; no checklist ensures all code is secure. |
| `cc-skill-strategic-compact.md` | `cc-skill-strategic-compact` | Prepare a verified checkpoint before condensing an agent conversation at a phase boundary. |
| `cdk-patterns.md` | `cdk-patterns` | Common AWS CDK patterns and constructs for building cloud infrastructure with TypeScript, Python, or Java. |
| `change-management.md` | `change-management` | Implement change management processes. |
| `changelog-automation.md` | `changelog-automation` | Automate changelog generation from commits, PRs, and releases following Keep a Changelog format. |
| `changelog-entry.md` | `changelog-entry` | Generate a properly formatted CHANGELOG.md entry in Keep a Changelog format from a commit range or PR. |
| `changelog-updates.md` | `changelog-updates` | Create release notes and product updates that developers actually read and care about. |
| `chat-widget.md` | `chat-widget` | Build a real-time support chat system with a floating widget for users and an admin dashboard for support staff. |
| `chatexport-need-miner.md` | `chatexport-need-miner` | Mines offline Telegram Desktop chat exports (result.json) for unmet market needs and product opportunities using chunked streaming and verbatim quote grounding. |
| `chord-onchain-trading.md` | `chord-onchain-trading` | Read DEX market data and prepare best-route swap quotes and unsigned swap transactions on eight EVM chains with the Chord API. |
| `chrome-extension-developer.md` | `chrome-extension-developer` | Expert in building Chrome Extensions using Manifest V3. |
| `churn-prevention.md` | `churn-prevention` | Reduce voluntary and involuntary churn with cancel flows, save offers, dunning, win-back tactics, and retention strategy. |
| `ci-cd-and-automation.md` | `ci-cd-and-automation` | Automates CI/CD pipeline setup. |
| `cicd-automation-workflow-automate.md` | `cicd-automation-workflow-automate` | You are a workflow automation expert specializing in creating efficient CI/CD pipelines, GitHub Actions workflows, and automated development processes. |
| `circleci.md` | `circleci` | Configure CircleCI workflows and orbs for continuous integration and |
| `cirq.md` | `cirq` | Cirq is Google Quantum AI's open-source framework for designing, simulating, and running quantum circuits on quantum computers and simulators. |
| `cis-benchmarks.md` | `cis-benchmarks` | Audit and remediate CIS benchmark violations. |
| `citation-management.md` | `citation-management` | Manage citations systematically throughout the research and writing process. |
| `ckw-design.md` | `ckw-design` | Frontend design entry point: direction, design system, visual philosophy. |
| `claimable-postgres.md` | `claimable-postgres` | Provision instant temporary Postgres databases via Claimable Postgres by Neon (neon.new) with no login, signup, or credit card. |
| `clarity-gate.md` | `clarity-gate` | Pre-ingestion verification for epistemic quality in RAG systems. |
| `clarvia-aeo-check.md` | `clarvia-aeo-check` | Score any MCP server, API, or CLI for agent-readiness using Clarvia AEO (Agent Experience Optimization). |
| `claude-ally-health.md` | `claude-ally-health` | A health assistant skill for medical information analysis, symptom tracking, and wellness guidance. |
| `claude-api.md` | `claude-api` | Build apps with the Claude API or Anthropic SDK. |
| `claude-code-expert.md` | `claude-code-expert` | Especialista profundo em Claude Code - CLI da Anthropic. |
| `claude-code-guide.md` | `claude-code-guide` | To provide a comprehensive reference for configuring and using Claude Code (the agentic coding tool) to its full potential. |
| `claude-d3js-skill.md` | `claude-d3js-skill` | This skill provides guidance for creating sophisticated, interactive data visualisations using d3.js. |
| `claude-delegate.md` | `claude-delegate` | Delegate coding tasks to a separate Claude Code CLI process or Claude |
| `claude-in-chrome-troubleshooting.md` | `claude-in-chrome-troubleshooting` | Diagnose and fix Claude in Chrome MCP extension connectivity issues. |
| `claude-monitor.md` | `claude-monitor` | Monitor de performance do Claude Code e sistema local. |
| `claude-scientific-skills.md` | `claude-scientific-skills` | Scientific research and analysis skills |
| `claude-settings-audit.md` | `claude-settings-audit` | Analyze a repository to generate recommended Claude Code settings.json permissions. |
| `claude-speed-reader.md` | `claude-speed-reader` | -Speed read Claude's responses at 600+ WPM using RSVP with Spritz-style ORP highlighting |
| `claude-win11-speckit-update-skill.md` | `claude-win11-speckit-update-skill` | Review updates to GitHub SpecKit on Windows 11 with PowerShell, preserving local templates and customizations |
| `claymorphism.md` | `claymorphism` | Web and App implementation guide for Claymorphism. |
| `clean-code.md` | `clean-code` | This skill embodies the principles of \"Clean Code\" by Robert C. |
| `clean-code-guard.md` | `clean-code-guard` | Review generated or changed production code with Clean Code, SOLID, DRY, KISS, YAGNI, and LLM-specific failure-mode checks. |
| `clerk-auth.md` | `clerk-auth` | Expert patterns for Clerk auth implementation, middleware, |
| `client-secret-exposure-audit.md` | `client-secret-exposure-audit` | Audit a deployed web app for secrets exposed to the browser: hardcoded API keys/tokens in JS, secrets in HTML meta/attributes/comments, publicly reachable source/config/deploy files, and header/CORS misconfig. |
| `clients-accounts.md` | `clients-accounts` | Client and account register: contacts, billing address, tax ID and basis, payment terms, invoice totals, amounts paid and outstanding balance. |
| `cline-pilot.md` | `cline-pilot` | >- |
| `cloro-mcp.md` | `cloro-mcp` | Get Google results with the AI Overview, and ChatGPT, Google AI Mode, Bing AI Mode and Gemini answers with their cited sources, through cloro's hosted MCP server. |
| `closed-loop-delivery.md` | `closed-loop-delivery` | Use when a coding task must be completed against explicit acceptance criteria with minimal user re-intervention across implementation, review feedback, deployment, and runtime verification. |
| `cloud-architect.md` | `cloud-architect` | Expert cloud architect specializing in AWS/Azure/GCP multi-cloud infrastructure design, advanced IaC (Terraform/OpenTofu/CDK), FinOps cost optimization, and modern architectural patterns. |
| `cloud-devops.md` | `cloud-devops` | Cloud infrastructure and DevOps workflow covering AWS, Azure, GCP, Kubernetes, Terraform, CI/CD, monitoring, and cloud-native development. |
| `cloud-k8s.md` | `cloud-k8s` | Authorized cloud, container, and Kubernetes security assessment: metadata SSRF, IAM misconfiguration, container escape paths, and cluster RBAC review. |
| `cloud-penetration-testing.md` | `cloud-penetration-testing` | Conduct comprehensive security assessments of cloud infrastructure across Microsoft Azure, Amazon Web Services (AWS), and Google Cloud Platform (GCP). |
| `cloudflare-security-audit.md` | `cloudflare-security-audit` | Audit authorized codebases for exploitable vulnerabilities using scoped reconnaissance, adversarial review, validation, and structured reporting. |
| `cloudflare-workers-expert.md` | `cloudflare-workers-expert` | Expert in Cloudflare Workers and the Edge Computing ecosystem. |
| `cloudformation.md` | `cloudformation` | Deploy AWS resources with CloudFormation templates. |
| `cloudformation-best-practices.md` | `cloudformation-best-practices` | CloudFormation template optimization, nested stacks, drift detection, and production-ready patterns. |
| `cmux.md` | `cmux` | Control cmux workspaces, panes, surfaces, and agent sessions safely from macOS terminal workflows. |
| `co-marketing.md` | `co-marketing` | When the user wants to find co-marketing partners, plan joint campaigns, or brainstorm partnership opportunities. |
| `cockney.md` | `cockney` | Cheeky Cockney coding mode: terse replies, the smallest correct change, plain English for anything risky. |
| `code-audit.md` | `code-audit` | Authorized source-code security review and SAST workflows: Semgrep and CodeQL pattern hunting, dangerous API identification, and fix verification. |
| `code-documentation-code-explain.md` | `code-documentation-code-explain` | You are a code education expert specializing in explaining complex code through clear narratives, visual diagrams, and step-by-step breakdowns. |
| `code-documentation-doc-generate.md` | `code-documentation-doc-generate` | Compatibility alias of documentation-generation-doc-generate. |
| `code-of-conduct.md` | `code-of-conduct` | Build a human-reviewed conduct register after context-first intake. |
| `code-polish.md` | `code-polish` | Rewrites unprofessional code comments into clear ones and performs non-semantic cleanup. |
| `code-refactoring-context-restore.md` | `code-refactoring-context-restore` | Resume interrupted project work from a handoff and current checkout evidence; reconcile completed work, pending changes and existing user constraints. |
| `code-refactoring-refactor-clean.md` | `code-refactoring-refactor-clean` | You are a code refactoring expert specializing in clean code principles, SOLID design patterns, and modern software engineering best practices. |
| `code-refactoring-tech-debt.md` | `code-refactoring-tech-debt` | Identify technical debt from actual code and change history, estimate its impact, and prioritize bounded improvements with explicit assumptions. |
| `code-review-ai-ai-review.md` | `code-review-ai-ai-review` | Review pull requests with source inspection, available static analysis and evidence-backed AI assistance; report actionable bugs, security risks and unverified coverage. |
| `code-review-and-quality.md` | `code-review-and-quality` | Conducts multi-axis code review. |
| `code-review-checklist.md` | `code-review-checklist` | Comprehensive checklist for conducting thorough code reviews covering functionality, security, performance, and maintainability |
| `code-review-excellence.md` | `code-review-excellence` | Review a defined code diff for correctness, security, performance and maintainability; report evidence-backed findings with severity and actionable feedback. |
| `code-review-sensei.md` | `code-review-sensei` | Expert code reviewer that catches bugs, security issues, performance |
| `code-reviewer.md` | `code-reviewer` | Elite code review expert specializing in modern AI-powered code |
| `code-showcase-core-components.md` | `code-showcase-core-components` | Apply the ChrisWiles code-showcase component and token conventions when the target project actually uses that API; examples require local adaptation. |
| `code-showcase-react-ui-patterns.md` | `code-showcase-react-ui-patterns` | Modern React UI patterns for loading states, error handling, and data fetching. |
| `code-showcase-systematic-debugging.md` | `code-showcase-systematic-debugging` | Four-phase debugging methodology with root cause analysis. |
| `code-showcase-testing-patterns.md` | `code-showcase-testing-patterns` | Jest testing patterns, factory functions, mocking strategies, and TDD workflow. |
| `code-simplification.md` | `code-simplification` | Simplifies code for clarity. |
| `code-simplifier.md` | `code-simplifier` | Simplifies and refines code for clarity, consistency, and maintainability while preserving all functionality. |
| `codebase-audit-pre-push.md` | `codebase-audit-pre-push` | Deep audit before GitHub push: removes junk files, dead code, security holes, and optimization issues. |
| `codebase-cleanup-deps-audit.md` | `codebase-cleanup-deps-audit` | You are a dependency security expert specializing in vulnerability scanning, license compliance, and supply chain security. |
| `codebase-cleanup-refactor-clean.md` | `codebase-cleanup-refactor-clean` | You are a code refactoring expert specializing in clean code principles, SOLID design patterns, and modern software engineering best practices. |
| `codebase-cleanup-tech-debt.md` | `codebase-cleanup-tech-debt` | Identify technical debt from actual code and change history, estimate its impact, and prioritize bounded improvements with explicit assumptions. |
| `codebase-design.md` | `codebase-design` | Shared vocabulary for designing deep modules. |
| `codebase-onboarding.md` | `codebase-onboarding` | Onboard a developer to a repository using Ontoly graph summaries. |
| `codebase-to-wordpress-converter.md` | `codebase-to-wordpress-converter` | Expert skill for converting any codebase (React/HTML/Next.js) into a pixel-perfect, SEO-optimized, and dynamic WordPress theme. |
| `codex-delegate.md` | `codex-delegate` | Delegate coding tasks to the OpenAI Codex CLI only when the user explicitly |
| `codex-fable5.md` | `codex-fable5` | Apply Fable-inspired discipline to Codex work: inspect first, track goals and findings, ground conclusions in evidence, verify before completion, and adapt Claude/Fable prompt guidance without identity or provider claims. |
| `codex-profiles.md` | `codex-profiles` | Use codex-profiles to run Codex CLI or Codex Desktop with isolated CODEX_HOME profiles for separate accounts, projects, and local state. |
| `codex-review.md` | `codex-review` | Professional code review with auto CHANGELOG generation, integrated with Codex AI. |
| `codex-subagent.md` | `codex-subagent` | Launch Codex CLI as an isolated subagent for bounded coding, review, or verification tasks. |
| `cohesivity.md` | `cohesivity` | Provision headless backend services for AI agents through Cohesivity: hosting, databases, storage, LLMs, and third-party APIs over one HTTP API. |
| `cold-email.md` | `cold-email` | Write B2B cold emails and follow-up sequences that earn replies. |
| `color-blocking.md` | `color-blocking` | Web and App implementation guide for Color Blocking. |
| `comfyui-gateway.md` | `comfyui-gateway` | REST API gateway for ComfyUI servers. |
| `command-center-ui.md` | `command-center-ui` | Web and App implementation guide for Command Center UI. |
| `commandcode-delegate.md` | `commandcode-delegate` | Delegate coding tasks to the Command Code CLI (`cmd`) only when the user |
| `commit.md` | `commit` | Prepare or create commits using Sentry-style message conventions when the repository requests them; inspect staged scope and honor its protected branch workflow. |
| `community-building.md` | `community-building` | When the user wants to build, grow, or improve a developer community on Discord, Slack, or forums. |
| `company-email-accounts.md` | `company-email-accounts` | Mailbox and licence register: employee, account type, aliases, groups, tool, licence cost, 2FA and password policy state, and access-review dates. |
| `competency-matrix.md` | `competency-matrix` | Competency matrix of expected proficiency by job title and grade, with assessment method and linked skill area. |
| `competitive-landscape.md` | `competitive-landscape` | Comprehensive frameworks for analyzing competition, identifying differentiation opportunities, and developing winning market positioning strategies. |
| `competitor-ad-intelligence.md` | `competitor-ad-intelligence` | Research public competitor ads, analyze creative patterns and landing pages, and produce an evidence-labeled strategic teardown. |
| `competitor-alternatives.md` | `competitor-alternatives` | You are an expert in creating competitor comparison and alternative pages. |
| `competitor-backlink-idea-generator.md` | `competitor-backlink-idea-generator` | Competitor Backlink Idea Generator. |
| `competitor-gap-analyzer.md` | `competitor-gap-analyzer` | Competitor Gap Analyzer. |
| `competitor-keyword-overlap-checker.md` | `competitor-keyword-overlap-checker` | Competitor Keyword Overlap Checker. |
| `competitor-profiling.md` | `competitor-profiling` | When the user wants to research, profile, or analyze competitors from their URLs. |
| `competitor-summary-report-creator.md` | `competitor-summary-report-creator` | Competitor Summary Report Creator. |
| `competitor-tracking.md` | `competitor-tracking` | Systematic competitor analysis for developer tools. |
| `compile-knowledge.md` | `compile-knowledge` | Compile durable, non-obvious findings into an interlinked markdown knowledge store — atomic files, [[wiki-links]], a maintained index — so an agent gets smarter across sessions instead of relearning the same facts. |
| `complexity-cuts.md` | `complexity-cuts` | Lower Big-O on existing code via a one-transformation-at-a-time playbook with verify-revert-stop. |
| `composition-patterns.md` | `composition-patterns` | Use when working with composition-patterns tasks or workflows |
| `comprehensive-review-full-review.md` | `comprehensive-review-full-review` | Use when working with comprehensive review full review |
| `comprehensive-review-pr-enhance.md` | `comprehensive-review-pr-enhance` | Generate structured PR descriptions from diffs, add review checklists, risk assessments, and test coverage summaries. |
| `computer-use-agents.md` | `computer-use-agents` | Build AI agents that interact with computers like humans do - |
| `computer-vision-expert.md` | `computer-vision-expert` | Computer vision pipeline design and evaluation. |
| `concise-planning.md` | `concise-planning` | Use when a user asks for a plan for a coding task, to generate a clear, actionable, and atomic checklist. |
| `conductor-implement.md` | `conductor-implement` | Execute tasks from a track's implementation plan following TDD workflow |
| `conductor-manage.md` | `conductor-manage` | Manage track lifecycle: archive, restore, delete, rename, and cleanup |
| `conductor-new-track.md` | `conductor-new-track` | Create a new track with specification and phased implementation plan |
| `conductor-revert.md` | `conductor-revert` | Git-aware undo by logical work unit (track, phase, or task) |
| `conductor-setup.md` | `conductor-setup` | Configure a Rails project to work with Conductor (parallel coding agents) |
| `conductor-status.md` | `conductor-status` | Display project status, active tracks, and next actions |
| `conductor-validator.md` | `conductor-validator` | 'Validates Conductor project artifacts for completeness, |
| `connection-auth-rules.md` | `connection-auth-rules` | Build a Connection Auth Rules for a Monte Carlo connection type. |
| `constant-time-analysis.md` | `constant-time-analysis` | Analyze cryptographic code to detect operations that leak secret data through execution timing variations. |
| `constraint-driven-development.md` | `constraint-driven-development` | 'Write the project quality bar as enforced CONSTRAINTS.md so agents stop |
| `container-hardening.md` | `container-hardening` | Secure Docker images and container runtime configurations. |
| `container-scanning.md` | `container-scanning` | Scan container images for vulnerabilities using Trivy, Grype, and cloud-native |
| `container-security-hardening.md` | `container-security-hardening` | Harden Docker/container images and runtime deployments with secure base images, non-root users, CVE scanning, SBOM/signing, seccomp/AppArmor, and Kubernetes pod security controls. |
| `content-creator.md` | `content-creator` | Draft and review audience-specific content using supplied brand examples, local text diagnostics, and adaptable channel templates. |
| `content-freshness-checker.md` | `content-freshness-checker` | Content Freshness Checker. |
| `content-gap-finder.md` | `content-gap-finder` | Content Gap Finder. |
| `content-length-comparator.md` | `content-length-comparator` | Content Length Comparator. |
| `content-marketer.md` | `content-marketer` | Elite content marketing strategist specializing in AI-powered content creation, omnichannel distribution, SEO optimization, and data-driven performance marketing. |
| `content-strategy.md` | `content-strategy` | Plan a content strategy, topic clusters, editorial roadmap, and content mix for traffic, authority, and lead generation. |
| `context-agent.md` | `context-agent` | Agente de contexto para continuidade entre sessoes. |
| `context-compression.md` | `context-compression` | When agent sessions generate millions of tokens of conversation history, compression becomes mandatory. |
| `context-degradation.md` | `context-degradation` | Language models exhibit predictable degradation patterns as context length increases. |
| `context-driven-development.md` | `context-driven-development` | Guide for implementing and maintaining context as a managed artifact alongside code, enabling consistent AI interactions and team alignment through structured project documentation. |
| `context-engineering.md` | `context-engineering` | Optimizes agent context setup. |
| `context-fundamentals.md` | `context-fundamentals` | Context is the complete state available to a language model at inference time. |
| `context-guardian.md` | `context-guardian` | Guardiao de contexto que preserva dados criticos antes da compactacao automatica. |
| `context-kit.md` | `context-kit` | Evaluate, adapt, and safely install Context Kit personal context artifacts for Claude Code or adjacent agent workflows. |
| `context-management-context-restore.md` | `context-management-context-restore` | Resume interrupted project work from a handoff and current checkout evidence; reconcile completed work, pending changes and existing user constraints. |
| `context-management-context-save.md` | `context-management-context-save` | Use when working with context management context save |
| `context-manager.md` | `context-manager` | Elite AI context engineering specialist mastering dynamic context management, vector databases, knowledge graphs, and intelligent memory systems. |
| `context-optimization.md` | `context-optimization` | Context optimization extends the effective capacity of limited context windows through strategic compression, masking, caching, and partitioning. |
| `context-window-management.md` | `context-window-management` | Strategies for managing LLM context windows including |
| `context7-auto-research.md` | `context7-auto-research` | Automatically fetch latest library/framework documentation for Claude Code via Context7 API. |
| `contract-document-renewal.md` | `contract-document-renewal` | Contract register: counterparty, owner, start and end dates, auto-renewal flag, renewal notice deadline, value and tax basis. |
| `conversation-memory.md` | `conversation-memory` | Persistent memory systems for LLM conversations including |
| `convex.md` | `convex` | Convex reactive backend expert: schema design, TypeScript functions, real-time subscriptions, auth, file storage, scheduling, and deployment. |
| `copilot-sdk.md` | `copilot-sdk` | Build applications that programmatically interact with GitHub Copilot. |
| `copy-editing.md` | `copy-editing` | You are an expert copy editor specializing in marketing and conversion copy. |
| `copywriting.md` | `copywriting` | Write rigorous, conversion-focused marketing copy for landing pages and emails. |
| `copywriting-psychologist.md` | `copywriting-psychologist` | Write or revise conversion copy using audience awareness, motivations, and credible proof when ads, landing pages, or sales messages feel generic. |
| `core-components.md` | `core-components` | Adapt an existing project component library and design tokens to a UI change; inspect real exports, preserve native behavior, and verify accessibility. |
| `cost-optimization.md` | `cost-optimization` | Strategies and patterns for optimizing cloud costs across AWS, Azure, and GCP. |
| `coupler-marketing-analytics.md` | `coupler-marketing-analytics` | Analyze cross-channel marketing performance from live Coupler.io data through its hosted MCP server: channel and campaign comparison, ROI, anomalies and budget insights. |
| `course-upskilling-requests.md` | `course-upskilling-requests` | Training request register: course, provider, cost, duration, budget line, the three approval steps, service bond and completion evidence. |
| `court.md` | `court` | Put an idea on trial: a prosecutor and a defense Claude argue, 12 juror sub-agents vote independently, and a judge reads the verdict and the changes that would flip it. |
| `cowork-to-code-bridge.md` | `cowork-to-code-bridge` | Use an already-installed, independently verified cowork-to-code bridge to run narrowly approved actions on the user's own macOS, Linux, or WSL2 machine through a local file queue. |
| `cpp.md` | `cpp` | Language-specific super-code guidelines for cpp. |
| `cpp-pro.md` | `cpp-pro` | Write idiomatic C++ code with modern features, RAII, smart pointers, and STL algorithms. |
| `cqrs-implementation.md` | `cqrs-implementation` | Implement Command Query Responsibility Segregation for scalable architectures. |
| `create-branch.md` | `create-branch` | Create a git branch following Sentry naming conventions. |
| `create-issue-gate.md` | `create-issue-gate` | Use when starting a new implementation task and an issue must be created with strict acceptance criteria gating before execution. |
| `create-pr.md` | `create-pr` | Alias for pr-writer. |
| `cred-omega.md` | `cred-omega` | CISO operacional enterprise para gestao total de credenciais e segredos. |
| `credit-cycle-analysis.md` | `credit-cycle-analysis` | Debtor and creditor credit-cycle analysis: weighted collection or payment days, ageing buckets, credit limit utilisation and gap against benchmark. |
| `crewai.md` | `crewai` | Design role-based agents, tasks, crews, and flows with CrewAI. |
| `cro.md` | `cro` | When the user wants to optimize, improve, or increase conversions on any marketing page or form — including homepage, landing pages, pricing pages, feature pages, lead capture forms, or contact forms. |
| `cron-doctor.md` | `cron-doctor` | Diagnose and validate cron expressions before they ship. |
| `cross-chain-relayer-audit.md` | `cross-chain-relayer-audit` | Cross-chain relayer bridge audit register: message hash verifications, replay protection nonces, validator quorum, and withdrawal proofs. |
| `cross-platform-contract-propagation-audit.md` | `cross-platform-contract-propagation-audit` | Use when auditing whether a field, enum, flag, or API contract propagates consistently across storage, services, clients, analytics, and tests. |
| `crossframe.md` | `crossframe` | Use when the user explicitly invokes CrossFrame or 跨尺度结构诊断 for Chinese-canonical structural diagnosis of complex relationships, organizations, institutions, public disputes, or long-term evolution. |
| `crossframe-casebook.md` | `crossframe-casebook` | Use when CrossFrame Suite routes explicit Chinese casebook work: turning materials into reusable cases, anonymized entries, mechanisms, and retrieval indexes. |
| `crossframe-critical.md` | `crossframe-critical` | Use only when the user explicitly names crossframe-critical for a Chinese structural critique dossier, article plan, or long-form critical essay. |
| `crossframe-debate.md` | `crossframe-debate` | Use when CrossFrame Suite routes explicit Chinese proposition testing, debate analysis, hidden-premise review, rebuttal design, or withdrawal condition checks. |
| `crossframe-dialogue.md` | `crossframe-dialogue` | Use when CrossFrame Suite routes explicit Chinese reader replies, editor responses, consultation-style short answers, or boundary-aware structural advice. |
| `crossframe-essay.md` | `crossframe-essay` | Use when explicit CrossFrame work needs a Chinese critical insight essay, commentary, concept essay, public piece, or structure-to-article draft after diagnosis. |
| `crossframe-notebook.md` | `crossframe-notebook` | Use when CrossFrame Suite routes explicit Chinese notes for books, theories, articles, excerpts, bidirectional reading, absorption, or conflict mapping. |
| `crossframe-org.md` | `crossframe-org` | Use when CrossFrame Suite routes explicit Chinese analysis of teams, projects, organizations, responsibility chains, feedback write-back, repair, or retrospectives. |
| `crossframe-public.md` | `crossframe-public` | Use when CrossFrame Suite routes explicit Chinese analysis of public issues, platform governance, policy, institutional responsibility, appeals, or compliance evidence. |
| `crossframe-review.md` | `crossframe-review` | Use when explicit CrossFrame output needs review for reasoning fidelity, evidence boundaries, source anchors, concept drift, article collapse, or repair steps. |
| `crossframe-suite.md` | `crossframe-suite` | Use when the user explicitly invokes CrossFrame Suite for Chinese structural diagnosis workflows across relationships, organizations, public issues, philosophy, research, or essay output. |
| `crossframe-teach.md` | `crossframe-teach` | Use when CrossFrame Suite routes explicit Chinese teaching of CrossFrame concepts, misreading boundaries, plain-language examples, signals, or exercises. |
| `crypto-bd-agent.md` | `crypto-bd-agent` | Reference patterns (upstream reports, not independently verified here) for building AI agents that autonomously discover, evaluate, and acquire token listings for cryptocurrency exchanges. |
| `csharp.md` | `csharp` | Language-specific super-code guidelines for csharp. |
| `csharp-pro.md` | `csharp-pro` | Write modern C# code with advanced features like records, pattern matching, and async/await. |
| `csv-manual-export.md` | `csv-manual-export` | CSV Manual Export: a UTF-8 CSV template from a confirmed field list, empty by default, with no invented columns or values. |
| `ctr-predictor.md` | `ctr-predictor` | CTR Predictor. |
| `culture-retention.md` | `culture-retention` | Employee survey and retention register: engagement, growth, happiness, work-life balance and manager-relationship scores, key concern and retention risk. |
| `cursor-delegate.md` | `cursor-delegate` | Delegate coding tasks to the Cursor Agent CLI (`cursor-agent`) only when |
| `customer-psychographic-profiler.md` | `customer-psychographic-profiler` | Build an evidence-grounded customer profile of motivations, fears, identity, and trust barriers before positioning, copywriting, or funnel design. |
| `customer-research.md` | `customer-research` | When the user wants to conduct, analyze, or synthesize customer research. |
| `customer-support.md` | `customer-support` | Elite AI-powered customer support specialist mastering conversational AI, automated ticketing, sentiment analysis, and omnichannel support experiences. |
| `customs-trade-compliance.md` | `customs-trade-compliance` | Codified expertise for customs documentation, tariff classification, duty optimisation, restricted party screening, and regulatory compliance across multiple jurisdictions. |
| `cv-generator.md` | `cv-generator` | Generate professional, ATS-optimized CVs for FlowCV, Canva, Google Docs, or Word. |
| `cyber-audit.md` | `cyber-audit` | Run read-only exposure checks for security advisories and write a structured local audit report. |
| `cyber-y2k.md` | `cyber-y2k` | Web and App implementation guide for Cyber Y2K. |
| `cyberpunk-ui.md` | `cyberpunk-ui` | Web and App implementation guide for Cyberpunk UI. |
| `daily.md` | `daily` | Documentation and capabilities reference for Daily |
| `daily-gift.md` | `daily-gift` | Relationship-aware daily gift engine with five-stage creative pipeline — editorial judgment, synthesis, concept generation, visual strategy, and rendering in H5, image, or video |
| `daily-news-report.md` | `daily-news-report` | Scrapes content based on a preset URL list, filters high-quality technical information, and generates daily Markdown reports. |
| `dali-short-address-commissioner.md` | `dali-short-address-commissioner` | Commissions DALI and DALI-2 (IEC 62386) lighting buses: short-address assignment (0-63), 24-bit binary search collision resolution, groups, and DT8 color control. |
| `dark-mode.md` | `dark-mode` | Web and App implementation guide for Dark Mode Design. |
| `darkmoon-pentest.md` | `darkmoon-pentest` | Start, follow and triage authorized autonomous AI pentest runs on a self-hosted Darkmoon Pro instance through its MCP server. |
| `dart.md` | `dart` | Language-specific super-code guidelines for dart. |
| `dashboard-design.md` | `dashboard-design` | Web and App implementation guide for Dashboard Design. |
| `dast-scanning.md` | `dast-scanning` | Perform dynamic application security testing with OWASP ZAP, Burp Suite, |
| `data-dense-design.md` | `data-dense-design` | Web and App implementation guide for Data-Dense Design. |
| `data-engineer.md` | `data-engineer` | Build scalable data pipelines, modern data warehouses, and real-time streaming architectures. |
| `data-engineering-data-driven-feature.md` | `data-engineering-data-driven-feature` | Build features guided by data insights, A/B testing, and continuous measurement using specialized agents for analysis, implementation, and experimentation. |
| `data-engineering-data-pipeline.md` | `data-engineering-data-pipeline` | You are a data pipeline architecture expert specializing in scalable, reliable, and cost-effective data pipelines for batch and streaming data processing. |
| `data-export-engine.md` | `data-export-engine` | Data export log: source module, purpose, format, requester and approver, delivery dates, personal-data flag and status. |
| `data-privacy-controls.md` | `data-privacy-controls` | Data privacy control register: data category, lawful basis, retention period, access roles, encryption and consent requirement per module. |
| `data-quality-frameworks.md` | `data-quality-frameworks` | Implement data quality validation with Great Expectations, dbt tests, and data contracts. |
| `data-scientist.md` | `data-scientist` | Expert data scientist for advanced analytics, machine learning, and statistical modeling. |
| `data-storytelling.md` | `data-storytelling` | Transform raw data into compelling narratives that drive decisions and inspire action. |
| `data-structure-protocol.md` | `data-structure-protocol` | Give agents persistent structural memory of a codebase — navigate dependencies, track public APIs, and understand why connections exist without re-reading the whole repo. |
| `database.md` | `database` | Database development and operations workflow covering SQL, NoSQL, database design, migrations, optimization, and data engineering. |
| `database-admin.md` | `database-admin` | Expert database administrator specializing in modern cloud databases, automation, and reliability engineering. |
| `database-architect.md` | `database-architect` | Expert database architect specializing in data layer design from scratch, technology selection, schema modeling, and scalable database architectures. |
| `database-backups.md` | `database-backups` | Implement database backup strategies. |
| `database-cloud-optimization-cost-optimize.md` | `database-cloud-optimization-cost-optimize` | You are a cloud cost optimization expert specializing in reducing infrastructure expenses while maintaining performance and reliability. |
| `database-design.md` | `database-design` | Database design principles and decision-making. |
| `database-migration.md` | `database-migration` | Master database schema and data migrations across ORMs (Sequelize, TypeORM, Prisma), including rollback strategies and zero-downtime deployments. |
| `database-migrations-migration-observability.md` | `database-migrations-migration-observability` | Migration monitoring, CDC, and observability infrastructure |
| `database-migrations-sql-migrations.md` | `database-migrations-sql-migrations` | SQL database migrations with zero-downtime strategies for PostgreSQL, MySQL, and SQL Server. |
| `database-optimizer.md` | `database-optimizer` | Expert database optimizer specializing in modern performance tuning, query optimization, and scalable architectures. |
| `database-security.md` | `database-security` | Authorized database security assessment across PostgreSQL, MySQL, MSSQL, MongoDB, and Redis: exposure, authorization gaps, UDF/command execution paths, and misconfiguration review. |
| `datacircle.md` | `datacircle` | Every plan of every GTM API on datacircle.dev, as one file you download and query. |
| `datawebot.md` | `datawebot` | Find products for sale across online shops, list returned sellers' prices with direct links, and run Amazon and Shopify extraction Jobs through the hosted datawebot MCP server. |
| `day-book.md` | `day-book` | Daily cash, bank and digital day book: opening and closing balances per book, in/out movements, debit/credit presentation and reconciliation status. |
| `dbos-golang.md` | `dbos-golang` | Guide for building reliable, fault-tolerant Go applications with DBOS durable workflows. |
| `dbos-python.md` | `dbos-python` | Guide for building reliable, fault-tolerant Python applications with DBOS durable workflows. |
| `dbos-typescript.md` | `dbos-typescript` | Guide for building reliable, fault-tolerant TypeScript applications with DBOS durable workflows. |
| `dbt-transformation-patterns.md` | `dbt-transformation-patterns` | Production-ready patterns for dbt (data build tool) including model organization, testing strategies, documentation, and incremental processing. |
| `ddd-context-mapping.md` | `ddd-context-mapping` | Map relationships between bounded contexts and define integration contracts using DDD context mapping patterns. |
| `ddd-strategic-design.md` | `ddd-strategic-design` | Design DDD strategic artifacts including subdomains, bounded contexts, and ubiquitous language for complex business domains. |
| `ddd-tactical-patterns.md` | `ddd-tactical-patterns` | Apply DDD tactical patterns in code using entities, value objects, aggregates, repositories, and domain events with explicit invariants. |
| `de-ai-writer.md` | `de-ai-writer` | Chinese AI-smell removal engine: 35 Chinese AI-tell patterns (赋能/闭环), AI-smell scoring, de-AI rewriting, style clone. |
| `debate-review.md` | `debate-review` | Two-model debate review of a GitHub PR, GitLab MR, Azure DevOps PR, or |
| `debug-buttercup.md` | `debug-buttercup` | All pods run in namespace crs. |
| `debugger.md` | `debugger` | Investigate a reproducible error or failing test, test root-cause hypotheses, implement a scoped fix when authorized, and report actual verification evidence. |
| `debugging-and-error-recovery.md` | `debugging-and-error-recovery` | Guides systematic root-cause debugging. |
| `debugging-code.md` | `debugging-code` | Interactively debug source code — set breakpoints, step through execution line by line, inspect live variable state, evaluate expressions against the running program, and navigate the call stack to trace root causes. |
| `debugging-strategies.md` | `debugging-strategies` | Transform debugging from frustrating guesswork into systematic problem-solving with proven strategies, powerful tools, and methodical approaches. |
| `debugging-toolkit.md` | `debugging-toolkit` | Use when working with debugging toolkit smart debug (Alias for debugging-toolkit-smart-debug) |
| `debugging-toolkit-smart-debug.md` | `debugging-toolkit-smart-debug` | Diagnose failures from reproduction steps, traces, logs and code; test hypotheses and verify a scoped fix without inventing production evidence. |
| `decision-navigator.md` | `decision-navigator` | Guide stuck or overwhelmed users through targeted branching questions until they reach concrete next steps. |
| `deep-research-framework.md` | `deep-research-framework` | Framework for deep research reports: define the question and tier sources first, cross-verify, then write conclusion-first reports with explicit uncertainty statements. |
| `deepapi.md` | `deepapi` | Use DeepAPI for supported scraping, research, and email workflows with explicit credentials and approval. |
| `defi-protocol-templates.md` | `defi-protocol-templates` | Implement DeFi protocols with educational templates for staking, AMMs, governance, and lending systems. |
| `defi-yield-strategy-allocator.md` | `defi-yield-strategy-allocator` | Multi-vault automated yield strategy allocation register: APY benchmarks, impermanent loss risk tiers, and rebalancing triggers. |
| `define-my-content-pillars.md` | `define-my-content-pillars` | Find the three to five subjects someone can post about repeatedly, from what they have published and know first-hand. |
| `defuddle.md` | `defuddle` | Extract clean markdown content from web pages using Defuddle CLI, removing clutter and navigation to save tokens. |
| `dei-dashboard.md` | `dei-dashboard` | Diversity, equity and inclusion dashboard: metric by department and period, value against target, group size and minimum-threshold flag. |
| `deja-history.md` | `deja-history` | Search this machine's past AI coding sessions across Claude Code, Codex, Cursor, Gemini CLI and thirty-nine other agents before editing, debugging, or denying something exists. |
| `delegate-setup.md` | `delegate-setup` | Configure approved delegation lanes across installed implementer CLIs, |
| `delegating-to-agents.md` | `delegating-to-agents` | Delegate bounded work to other AI agents while preserving context, ownership, and progress checks. |
| `dep.md` | `dep` | Handles containerization, CI/CD pipelines, and deployment setup. |
| `dependency-analysis.md` | `dependency-analysis` | Analyze internal and package dependencies using Ontoly graph traversal. |
| `dependency-management-deps-audit.md` | `dependency-management-deps-audit` | You are a dependency security expert specializing in vulnerability scanning, license compliance, and supply chain security. |
| `dependency-upgrade.md` | `dependency-upgrade` | Master major dependency version upgrades, compatibility analysis, staged upgrade strategies, and comprehensive testing approaches. |
| `deploy-to-vercel.md` | `deploy-to-vercel` | Deploy applications and websites to Vercel. |
| `deployment-engineer.md` | `deployment-engineer` | Expert deployment engineer specializing in modern CI/CD pipelines, GitOps workflows, and advanced deployment automation. |
| `deployment-pipeline-design.md` | `deployment-pipeline-design` | Architecture patterns for multi-stage CI/CD pipelines with approval gates and deployment strategies. |
| `deployment-procedures.md` | `deployment-procedures` | Production deployment principles and decision-making. |
| `deployment-validation-config-validate.md` | `deployment-validation-config-validate` | Validate application configurations with schemas, configuration tests, and checks for security and environment consistency. |
| `deprecation-and-migration.md` | `deprecation-and-migration` | Manages deprecation and migration. |
| `design-it.md` | `design-it` | Routes frontend design tasks to 48 specific UI styles. |
| `design-md.md` | `design-md` | Analyze Stitch projects and synthesize a semantic design system into DESIGN.md files |
| `design-orchestration.md` | `design-orchestration` | Orchestrates design workflows by routing work through brainstorming, multi-agent review, and execution readiness in the correct order. |
| `design-philosophy.md` | `design-philosophy` | Visual philosophy and art-direction for frontend. |
| `design-spatial.md` | `design-spatial` | Design — spatial composition |
| `design-spells.md` | `design-spells` | Curated micro-interactions and design details that add "magic" and personality to websites and apps. |
| `design-system.md` | `design-system` | Mechanical implementation invariants for frontend design: token architecture, typography hierarchy, loading order, FOUT prevention, chrome stability, motion timing, color semantics. |
| `design-taste-frontend.md` | `design-taste-frontend` | Use when building high-agency frontend interfaces with strict design taste, calibrated color, responsive layout, and motion rules. |
| `design-theme-guide.md` | `design-theme-guide` | Design-token register: colour, typography, spacing and radius tokens with light and dark values, contrast ratio and WCAG level. |
| `design-thinking.md` | `design-thinking` | Direction and intent for frontend design. |
| `design-token-contrast.md` | `design-token-contrast` | Checks WCAG 2.2 contrast between the color tokens of a project (light and dark theme) and suggests the closest passing color that keeps the hue. |
| `design-ux.md` | `design-ux` | UX / usability audit — heuristic evaluation of INTERACTIVE UIs (not just visual polish). |
| `deterministic-design.md` | `deterministic-design` | Measure rendered UI layout with reproducible spatial metrics and a separately assessed usability review; distinguish measurements from subjective judgments and user tests. |
| `dev-to-hashnode.md` | `dev-to-hashnode` | When the user wants to publish on Dev.to, Hashnode, or other developer blogging platforms. |
| `devcontainer-setup.md` | `devcontainer-setup` | Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. |
| `developer-advocacy.md` | `developer-advocacy` | When the user wants to do developer advocacy activities including conference talks, live coding, podcasts, and building in public. |
| `developer-audience-context.md` | `developer-audience-context` | When the user wants to establish or update their developer audience context. |
| `developer-churn.md` | `developer-churn` | When the user wants to understand, reduce, or recover from developer churn. |
| `developer-listening.md` | `developer-listening` | Monitor what developers say about your brand, competitors, and the problems they're solving. |
| `developer-newsletter.md` | `developer-newsletter` | When the user wants to create, write, or improve a newsletter for developer audiences. |
| `developer-onboarding.md` | `developer-onboarding` | Get developers to \"Hello World\" fast with optimized quickstarts, tutorials, and sample apps. |
| `developer-sandbox.md` | `developer-sandbox` | Design and build interactive playgrounds that let developers experience your product without commitment. |
| `developer-seo.md` | `developer-seo` | SEO strategy for technical queries and developer audiences. |
| `developer-signup-flow.md` | `developer-signup-flow` | Design frictionless signup experiences for developers including GitHub OAuth, API key generation, and onboarding personalization. |
| `development.md` | `development` | Comprehensive web, mobile, and backend development workflow bundling frontend, backend, full-stack, and mobile development skills for end-to-end application delivery. |
| `devops-pipeline-builder.md` | `devops-pipeline-builder` | Design and implement CI/CD pipelines, Docker configurations, deployment |
| `devops-troubleshooter.md` | `devops-troubleshooter` | Expert DevOps troubleshooter specializing in rapid incident response, advanced debugging, and modern observability. |
| `devrel-content.md` | `devrel-content` | When the user wants to create technical content for developers including blog posts, tutorials, and documentation. |
| `diagnose-android-overheating.md` | `diagnose-android-overheating` | Use when diagnosing Android overheating, idle heat, thermal throttling, charging or radio heat, or abnormal battery drain with read-only ADB evidence and approval gates. |
| `diagnosing-bugs.md` | `diagnosing-bugs` | Diagnosis loop for hard bugs and performance regressions. |
| `diagram-generator.md` | `diagram-generator` | Generate, refine, validate, and render diagrams from natural language, notes, code, schemas, or existing diagram sources: flowcharts, swimlanes, attack-path graphs, data-flow diagrams, architecture, and state machines. |
| `diary.md` | `diary` | Unified Diary System: A context-preserving automated logger for multi-project development. |
| `differential-review.md` | `differential-review` | Security-focused code review for PRs, commits, and diffs. |
| `digital-forensics.md` | `digital-forensics` | Authorized digital forensics: memory dumps, disk timelines, PCAP investigation, artifact triage, and incident-response evidence preservation. |
| `disaster-recovery.md` | `disaster-recovery` | Implement disaster recovery strategies and runbooks. |
| `disciplinary-pip-tracker.md` | `disciplinary-pip-tracker` | Disciplinary and performance-improvement case register: case type, linked review or issue, improvement goals, review dates, outcome and confidentiality. |
| `discord-bot-architect.md` | `discord-bot-architect` | Specialized skill for building production-ready Discord bots. |
| `dispatch.md` | `dispatch` | Delegate tasks to OpenAI Codex CLI and Google Antigravity CLI from Claude Code with topic-aware sessions |
| `dispatching-parallel-agents.md` | `dispatching-parallel-agents` | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies |
| `distribute-skill-to-all-agents.md` | `distribute-skill-to-all-agents` | Distribute a skill across configured agent skill folders while respecting local symlink layouts. |
| `distributed-debugging-debug-trace.md` | `distributed-debugging-debug-trace` | You are a debugging expert specializing in setting up comprehensive debugging environments, distributed tracing, and diagnostic tools. |
| `distributed-tracing.md` | `distributed-tracing` | Implement distributed tracing with Jaeger and Tempo for request flow visibility across microservices. |
| `ditto.md` | `ditto` | Use when a user asks to mine or update a private, evidence-backed work profile from local Claude Code, Codex, Copilot CLI, or OpenCode sessions. |
| `django-access-review.md` | `django-access-review` | Use when reviewing Django or DRF access control: trace authorization flows, IDOR risks, object permissions, query scoping and tenant isolation before proposing a verified fix. |
| `django-perf-review.md` | `django-perf-review` | Django performance code review. |
| `django-pro.md` | `django-pro` | Master Django 5.x with async views, DRF, Celery, and Django Channels. |
| `doc-coauthoring.md` | `doc-coauthoring` | This skill provides a structured workflow for guiding users through collaborative document creation. |
| `doc2math.md` | `doc2math` | Convert narrative technical documents into grounded Mathematical Problem Specifications with variables, constraints, objectives, and uncertainty. |
| `docker-compose.md` | `docker-compose` | Define and run multi-container Docker applications using Docker Compose. |
| `docker-expert.md` | `docker-expert` | You are an advanced Docker containerization expert with comprehensive, practical knowledge of container optimization, security hardening, multi-stage builds, orchestration patterns, and production deployment strategies based on current industry best practices. |
| `docker-management.md` | `docker-management` | Build, optimize, and troubleshoot Docker containers and images. |
| `docs-architect.md` | `docs-architect` | Creates comprehensive technical documentation from existing codebases. |
| `docs-as-marketing.md` | `docs-as-marketing` | Transform documentation into a powerful marketing channel that attracts, converts, and retains developers. |
| `docs-generator.md` | `docs-generator` | Generate technical deliverables from completed analysis: reverse-engineering reports, penetration-test reports, CTF write-ups, and signature-analysis documentation with evidence-backed structure. |
| `docs-guard.md` | `docs-guard` | Review generated or changed documentation before it ships, including READMEs, API references, docstrings, changelogs, tutorials, and documentation sites. |
| `document-management-system.md` | `document-management-system` | Document register: type, owner, upload and signed dates, version, storage link, confidentiality and signature-required flag. |
| `documentation.md` | `documentation` | Documentation generation workflow covering API docs, architecture docs, README files, code comments, and technical writing. |
| `documentation-and-adrs.md` | `documentation-and-adrs` | Records decisions and documentation. |
| `documentation-generation-doc-generate.md` | `documentation-generation-doc-generate` | Generate API, architecture or user documentation from current code and tests; validate examples and label gaps without inventing behavior or deploying a site. |
| `documentation-templates.md` | `documentation-templates` | Documentation templates and structure guidelines. |
| `domain-authority-simulator.md` | `domain-authority-simulator` | Domain Authority Simulator. |
| `domain-comparison-report-tool.md` | `domain-comparison-report-tool` | Domain Comparison Report Tool. |
| `domain-driven-design.md` | `domain-driven-design` | Plan and route Domain-Driven Design work from strategic modeling to tactical implementation and evented architecture patterns. |
| `domain-modeling.md` | `domain-modeling` | Build and sharpen a project's domain model. |
| `doom-pay.md` | `doom-pay` | Add self-custodial DOOM and wDOOM checkout links with DoomPay, then verify payment receipts on Doomsday Network Layer-1 or Base Mainnet. |
| `doomsday-escrow.md` | `doomsday-escrow` | Verify cryptographic Proof-of-Escrow collateral (L1 UTXO outpoint proofs and Base Mainnet wDOOM settlement receipts) on GitHub bounties before spending autonomous agent compute. |
| `dos-verify-done-claims.md` | `dos-verify-done-claims` | Before accepting an agent's 'done / shipped / fixed' claim, verify it against ground truth (git ancestry + the commit's own diff) using the DOS kernel's `dos verify` and `dos commit-audit` — never the agent's own narration. |
| `dotnet-architect.md` | `dotnet-architect` | Expert .NET backend architect specializing in C#, ASP.NET Core, Entity Framework, Dapper, and enterprise application patterns. |
| `dotnet-backend.md` | `dotnet-backend` | Build ASP.NET Core 8+ backend services with EF Core, auth, background jobs, and production API patterns. |
| `dotnet-backend-patterns.md` | `dotnet-backend-patterns` | Master C#/.NET patterns for building production-grade APIs, MCP servers, and enterprise backends with modern best practices (2024/2025). |
| `dotnet-reverse.md` | `dotnet-reverse` | .NET/C# binary reverse engineering: managed PE analysis, dnSpyEx debugging, de4dot deobfuscation (ConfuserEx/SmartAssembly/Babel), IL patching, NativeAOT targets, and analysis of red-team Sharp* tooling. |
| `doubt-driven-development.md` | `doubt-driven-development` | Subjects every non-trivial decision to a fresh-context adversarial review before it stands. |
| `draft-my-comments.md` | `draft-my-comments` | Write a LinkedIn comment that adds something the post did not have, not agreement. |
| `draw.md` | `draw` | Vector graphics and diagram creation, format conversion (ODG/SVG/PDF) with LibreOffice Draw. |
| `drizzle-migration-conflict.md` | `drizzle-migration-conflict` | Diagnose, repair, and prevent Drizzle Kit migration conflicts involving generated SQL, snapshots, journals, merge queues, and team workflows. |
| `drizzle-orm-expert.md` | `drizzle-orm-expert` | Expert in Drizzle ORM for TypeScript — schema design, relational queries, migrations, and serverless database integration. |
| `dsh-deepread.md` | `dsh-deepread` | Use for evidence-first reading of articles, books, PDFs, web pages, or document sets, with knowledge maps and Feynman checks. |
| `dsl-vm-reverse.md` | `dsl-vm-reverse` | Reverse JavaScript-based custom DSL/VM interpreters and risk-control engines: identify IIFE/switch-based opcode dispatch, extract opcode tables, and capture runtime semantics. |
| `duotone-design.md` | `duotone-design` | Web and App implementation guide for Duotone Design. |
| `duplicate-content-checker.md` | `duplicate-content-checker` | Duplicate Content Checker. |
| `dwarf-expert.md` | `dwarf-expert` | Provides expertise for analyzing DWARF debug files and understanding the DWARF debug format/standard (v3-v5). |
| `dx-optimizer.md` | `dx-optimizer` | Developer Experience specialist. |
| `e2e-testing.md` | `e2e-testing` | End-to-end testing workflow with Playwright for browser automation, visual regression, cross-browser testing, and CI/CD integration. |
| `e2e-testing-patterns.md` | `e2e-testing-patterns` | Build reliable, fast, and maintainable end-to-end test suites that provide confidence to ship code quickly and catch regressions before users do. |
| `earllm-build.md` | `earllm-build` | Build, maintain, and extend the EarLLM One Android project — a Kotlin/Compose app that connects Bluetooth earbuds to an LLM via voice pipeline. |
| `eas-app-stores.md` | `eas-app-stores` | Curated upstream guidance for Eas App Stores; use when the workflow matches the user goal. |
| `eas-observe.md` | `eas-observe` | Curated upstream guidance for Eas Observe; use when the workflow matches the user goal. |
| `eas-update-insights.md` | `eas-update-insights` | Check the health of published EAS Updates: crash rates, install/launch counts, unique users, payload size, and the split between embedded and OTA users per channel. |
| `eas-workflows.md` | `eas-workflows` | Use when writing or reviewing Expo EAS workflow YAML: inspect current schema and job syntax, validate configuration, and separate draft edits from launching builds or submissions. |
| `ebpf-observability.md` | `ebpf-observability` | Use eBPF for deep kernel-level observability — trace syscalls, network |
| `ecl-harness-engineer.md` | `ecl-harness-engineer` | Create or audit ECL Agent Harness infrastructure: AGENTS.md, change tracking, repository guidance, lint checks, CI gates, and agent handoff docs. |
| `ecommerce-listing-image-set.md` | `ecommerce-listing-image-set` | Install and use the official Ecommerce Product Images package, pinned by digest, for paid hosted work on the Beatra service. |
| `editorial-design.md` | `editorial-design` | Web and App implementation guide for Editorial Design. |
| `edr-bypass-re.md` | `edr-bypass-re` | Review EDR telemetry and known defense-evasion classes using offline evidence and controlled defensive coverage assessments. |
| `effective-agent-skills.md` | `effective-agent-skills` | Author and review high-quality agent skills with triggers, progressive disclosure, and safety notes. |
| `efficient-web-research.md` | `efficient-web-research` | Protocol for token-efficient web research. |
| `electron-development.md` | `electron-development` | Master Electron desktop app development with secure IPC, contextIsolation, preload scripts, multi-process architecture, electron-builder packaging, code signing, and auto-update. |
| `electron-drive-skill.md` | `electron-drive-skill` | Launch the project's Electron app on a scratch profile and drive it: click, type, screenshot, run renderer or main-process code, read logs. |
| `elixir.md` | `elixir` | Language-specific super-code guidelines for elixir. |
| `elixir-pro.md` | `elixir-pro` | Write idiomatic Elixir code with OTP patterns, supervision trees, and Phoenix LiveView. |
| `elk-stack.md` | `elk-stack` | Deploy and manage the ELK Stack (Elasticsearch, Logstash, Kibana) for |
| `elon-musk.md` | `elon-musk` | Simulacao ficticia e explicitamente rotulada de estilo comunicacional associado a Elon Musk, com analise de primeiros principios e verificacao separada de fatos. |
| `email-issue-fixer.md` | `email-issue-fixer` | Fix small email mistakes without touching the writer's voice, and strip tracking parameters from links on request. |
| `email-marketing-bible.md` | `email-marketing-bible` | Data-backed email marketing for AI agents: automation flows, deliverability triage, copy de-slopping, AI email design, ESP control via MCP with send gates and compliance. |
| `email-security.md` | `email-security` | Authorized email security review: phishing analysis, SPF/DKIM/DMARC header authentication, BEC pattern investigation, and mailbox token abuse research. |
| `email-sequence.md` | `email-sequence` | You are an expert in email marketing and automation. |
| `email-systems.md` | `email-systems` | Design transactional and marketing email delivery, queues, templates, authentication, suppression and monitoring. |
| `embedding-strategies.md` | `embedding-strategies` | Guide to selecting and optimizing embedding models for vector search applications. |
| `emblemai-crypto-wallet.md` | `emblemai-crypto-wallet` | Crypto wallet management across 7 blockchains via EmblemAI Agent Hustle API. |
| `emergency-card.md` | `emergency-card` | 生成紧急情况下快速访问的医疗信息摘要卡片。当用户需要旅行、就诊准备、紧急情况或询问"紧急信息"、"医疗卡片"、"急救信息"时使用此技能。提取关键信息（过敏、用药、急症、植入物），支持多格式输出（JSON、文本、二维码），用于急救或快速就医。 |
| `emil-design-eng.md` | `emil-design-eng` | Design and review polished UI with Emil Kowalski’s guidance on animation, interaction feedback, component craft, and accessibility. |
| `emil-ui-prototype.md` | `emil-ui-prototype` | Build distinct UI variants behind a development-only picker and integrate the variant the user selects. |
| `emotional-arc-designer.md` | `emotional-arc-designer` | Map the emotional progression of a narrative, page, or campaign when content needs a coherent path from attention to action. |
| `employee-suggestion-hub.md` | `employee-suggestion-hub` | Suggestion register: submitter or anonymous flag, category, votes, reviewer, decision and response status. |
| `employment-contract-templates.md` | `employment-contract-templates` | Templates and patterns for creating draft employment documentation for jurisdiction-specific legal review including contracts, offer letters, and HR policies. |
| `energy-procurement.md` | `energy-procurement` | Codified expertise for electricity and gas procurement, tariff optimisation, demand charge management, renewable PPA evaluation, and multi-facility energy cost management. |
| `engine-selection.md` | `engine-selection` | >- |
| `enhance-prompt.md` | `enhance-prompt` | Transforms vague UI ideas into polished, Stitch-optimized prompts. |
| `enterprise-vpn-attack.md` | `enterprise-vpn-attack` | External SSL VPN / remote-access appliance attack matrix |
| `entropy-box.md` | `entropy-box` | Entropy Box knowledge-compiler for embodied-AI: turns bounded requirements into grounded workflows via Solution Consult, Search, Lookup, and Evidence. |
| `environment-setup-guide.md` | `environment-setup-guide` | Guide developers through setting up development environments with proper tools, dependencies, and configurations |
| `eol-resistor-calculator.md` | `eol-resistor-calculator` | Calculates and validates end-of-line (EOL, SEOL, DEOL, TEOL) resistor loops for intrusion alarm panels (Honeywell, DSC, Paradox, Bosch) with wire gauge drop and state tables. |
| `error-debugging-error-analysis.md` | `error-debugging-error-analysis` | You are an expert error analysis specialist with deep expertise in debugging distributed systems, analyzing production incidents, and implementing comprehensive observability solutions. |
| `error-debugging-error-trace.md` | `error-debugging-error-trace` | You are an error tracking and observability expert specializing in implementing comprehensive error monitoring solutions. |
| `error-debugging-multi-agent-review.md` | `error-debugging-multi-agent-review` | Review a defined code diff from relevant correctness, authorization and performance perspectives; delegate only when authorized and reproduce findings centrally. |
| `error-detective.md` | `error-detective` | Search logs and codebases for error patterns, stack traces, and anomalies. |
| `error-diagnostics-error-analysis.md` | `error-diagnostics-error-analysis` | You are an expert error analysis specialist with deep expertise in debugging distributed systems, analyzing production incidents, and implementing comprehensive observability solutions. |
| `error-diagnostics-error-trace.md` | `error-diagnostics-error-trace` | You are an error tracking and observability expert specializing in implementing comprehensive error monitoring solutions. |
| `error-diagnostics-smart-debug.md` | `error-diagnostics-smart-debug` | Diagnose failures from reproduction steps, traces, logs and code; test hypotheses and verify a scoped fix without inventing production evidence. |
| `error-handling-patterns.md` | `error-handling-patterns` | Build resilient applications with robust error handling strategies that gracefully handle failures and provide excellent debugging experiences. |
| `esl-price-sync.md` | `esl-price-sync` | Synchronizes retail prices between ERP/POS systems and Electronic Shelf Labels (SES-imagotag, ZKONG, Pricer, Hanshow, SOLUM) with delta watermarking, idempotency, and battery modeling. |
| `esop-equity-tracker.md` | `esop-equity-tracker` | ESOP and equity grant register: grant date, shares granted, strike price, vesting start, schedule and cliff, plus vested and exercised shares. |
| `ethical-hacking-methodology.md` | `ethical-hacking-methodology` | Master the complete penetration testing lifecycle from reconnaissance through reporting. |
| `evaluation.md` | `evaluation` | Build evaluation frameworks for agent systems. |
| `event-sourcing-architect.md` | `event-sourcing-architect` | Expert in event sourcing, CQRS, and event-driven architecture patterns. |
| `event-staffing-compliance.md` | `event-staffing-compliance` | Assess worker-classification and compliance risk for temporary event staffing in the US and Canada — W-2 vs 1099, misclassification penalties, joint-employer liability, COI, and wage/hour rules. |
| `event-staffing-ordering.md` | `event-staffing-ordering` | Order W-2 compliant temporary event staff for conventions, trade shows, festivals, concerts, sporting events, and brand activations across 300+ US and Canadian markets via TempGuru. |
| `event-store-design.md` | `event-store-design` | Design and implement event stores for event-sourced systems. |
| `events-activities.md` | `events-activities` | Event register: type, date and time, venue, organizer, audience, budget against actual cost, RSVP and attendance counts and feedback score. |
| `evidence-hygiene.md` | `evidence-hygiene` | Evidence-capture and PoC-redaction discipline for bug-bounty submissions |
| `evolution.md` | `evolution` | This skill provides a reviewable workflow for maintaining makepad-skills during development. |
| `exa-search.md` | `exa-search` | Semantic search, similar content discovery, and structured research using Exa API. |
| `examprep-ai.md` | `examprep-ai` | Exam preparation assistant that converts syllabi, past papers, or notes into a ranked High Score Roadmap. |
| `executing-plans.md` | `executing-plans` | Use when you have a written implementation plan to execute in a separate session with review checkpoints |
| `expense-accounting.md` | `expense-accounting` | Expense accounting register: expense number and date, payee with PAN and VAT, bill reference, document type, amount with VAT, ledger account, approver and status. |
| `expense-management.md` | `expense-management` | Expense claim register: claim id, employee and department, amount and tax, approver and level, category, cost centre, budget line, receipt flag and status. |
| `explain-interface.md` | `explain-interface` | Explains how a website, a visual effect or an animation was built, from a live URL or a screenshot. |
| `explain-like-socrates.md` | `explain-like-socrates` | Explains concepts using Socratic-style dialogue. |
| `expo-animation.md` | `expo-animation` | Curated upstream guidance for Expo Animation; use when the workflow matches the user goal. |
| `expo-brownfield.md` | `expo-brownfield` | Integrate Expo and React Native into an existing native iOS or Android app. |
| `expo-cicd-workflows.md` | `expo-cicd-workflows` | Helps understand and write EAS workflow YAML files for Expo projects. |
| `expo-deployment.md` | `expo-deployment` | Deploy Expo apps with EAS: build and submit iOS and Android releases, configure build and submit profiles, manage versions and store metadata, and deploy web bundles or API routes. |
| `expo-dev-client.md` | `expo-dev-client` | Build Expo app for development |
| `expo-examples.md` | `expo-examples` | Expo's official example projects — the expo/examples repo of ~70 `with-*` integrations (Stripe, Clerk, Supabase, OpenAI, maps, Reanimated, SQLite, Skia, NativeWind, and more). |
| `expo-module.md` | `expo-module` | Guide for creating and writing Expo native modules and views using the Expo Modules API (Swift, Kotlin, TypeScript). |
| `expo-observe.md` | `expo-observe` | Set up and query EAS Observe for Expo apps, including root integration, interactive markers, route metrics, CLI summaries, traces, logs, and performance diagnosis. |
| `expo-tailwind-setup.md` | `expo-tailwind-setup` | Set up Tailwind CSS v4 in Expo with react-native-css and NativeWind v5 for universal styling |
| `expo-ui.md` | `expo-ui` | Build native UI with the @expo/ui package: real SwiftUI on iOS and Jetpack Compose on Android rendered from React in an Expo or React Native app. |
| `expo-ui-jetpack-compose.md` | `expo-ui-jetpack-compose` | Build Android-native Expo SDK 55 UI with Jetpack Compose views/modifiers, Host sizing and platform-specific integration. |
| `expo-ui-swift-ui.md` | `expo-ui-swift-ui` | Build iOS-native Expo SDK 55 UI with SwiftUI views/modifiers, Host/RNHostView embedding and native rebuild prerequisites. |
| `faber-language.md` | `faber-language` | Write, check and run Faber programs, an experimental statically typed language for coding agents and human authors. |
| `fable-safe-prompt.md` | `fable-safe-prompt` | Rewrite allowed prompts to reduce false-positive safety triggers without bypassing policy or changing intent. |
| `fact-check-x-complete.md` | `fact-check-x-complete` | Compare claims from one or more AI answers, verify their citations against public primary sources, and produce an evidence-linked fact-check report without installing a bundled browser runtime. |
| `fact-check-x-unified.md` | `fact-check-x-unified` | Fact-Check-X 流程编排能力，依次组织各方答案汇总、各方答案聚合（未核验）、权威核验后的最终答案和各方答案测评，生成可打开、可审计、可迁移的阶段产物与完整报告包。 |
| `faf-context.md` | `faf-context` | Get your project to 100% ✪ AI-readiness, fast — the AI auto-detects your stack and only asks for what it can't know (your goal and the human "why"). |
| `faf-expert.md` | `faf-expert` | Advanced .faf (Foundational AI-context Format) specialist. |
| `faf-go.md` | `faf-go` | Guided interview to Gold Code (100% AI-Readiness). |
| `faf-wizard.md` | `faf-wizard` | Done-for-you .faf generator. |
| `fal-audio.md` | `fal-audio` | Text-to-speech and speech-to-text using fal.ai audio models |
| `fal-generate.md` | `fal-generate` | Generate images and videos using fal.ai AI models |
| `fal-image-edit.md` | `fal-image-edit` | AI-powered image editing with style transfer and object removal |
| `fal-platform.md` | `fal-platform` | Platform APIs for model management, pricing, and usage tracking |
| `fal-upscale.md` | `fal-upscale` | Upscale and enhance image and video resolution using AI |
| `fal-workflow.md` | `fal-workflow` | Generate workflow JSON files for chaining AI models |
| `falsify.md` | `falsify` | The scientific thinking protocol for AI agents. |
| `family-health-analyzer.md` | `family-health-analyzer` | 整理家族病史和已知健康记录，识别需要医生或遗传咨询师评估的线索，不计算未经验证的个体发病概率 |
| `famulor-skill.md` | `famulor-skill` | Operate Famulor assistants, communication history, campaigns, knowledge, automations, telephony, and workspace administration through its hosted MCP server. |
| `faq-generator.md` | `faq-generator` | FAQ Generator. |
| `fastapi-pro.md` | `fastapi-pro` | Build high-performance async APIs with FastAPI, SQLAlchemy 2.0, and Pydantic V2. |
| `fastapi-router-py.md` | `fastapi-router-py` | Create FastAPI routers following established patterns with proper authentication, response models, and HTTP status codes. |
| `fastapi-templates.md` | `fastapi-templates` | Create production-ready FastAPI projects with async patterns, dependency injection, and comprehensive error handling. |
| `favicon.md` | `favicon` | Generate favicons from a source image |
| `fda-food-safety-auditor.md` | `fda-food-safety-auditor` | Expert AI auditor for FDA Food Safety (FSMA), HACCP, and PCQI compliance. |
| `fda-medtech-compliance-auditor.md` | `fda-medtech-compliance-auditor` | Expert AI auditor for Medical Device (SaMD) compliance, IEC 62304, and 21 CFR Part 820. |
| `feature-tracking.md` | `feature-tracking` | Maintain durable feature-level memory across AI coding sessions with lightweight Markdown tracks for status, source-of-truth docs, decisions, risks, and changes. |
| `featured-snippet-optimizer.md` | `featured-snippet-optimizer` | Featured Snippet Optimizer. |
| `featured-tool-schema-generator.md` | `featured-tool-schema-generator` | Featured Tool Schema Generator. |
| `fedora-hyprland-installer.md` | `fedora-hyprland-installer` | Install, configure, verify, repair, update, and uninstall Hyprland on Fedora Linux with GPU-aware detection (NVIDIA/AMD/Intel). |
| `fedramp-compliance.md` | `fedramp-compliance` | Implement FedRAMP requirements for federal cloud services. |
| `ffuf-claude-skill.md` | `ffuf-claude-skill` | Web fuzzing with ffuf |
| `ffuf-web-fuzzing.md` | `ffuf-web-fuzzing` | Expert guidance for ffuf web fuzzing during penetration testing, including authenticated fuzzing with raw requests, auto-calibration, and result analysis |
| `figma-designer.md` | `figma-designer` | Create structured Figma screens and libraries with ELAYA spacing, radius, semantic color variables, text styles, auto layout, and component states. |
| `file-organizer.md` | `file-organizer` | Organize files and folders by inspecting their contents, proposing a structure, and reviewing duplicates before authorized changes. |
| `file-path-traversal.md` | `file-path-traversal` | Identify and exploit file path traversal (directory traversal) vulnerabilities that allow attackers to read arbitrary files on the server, potentially including sensitive configuration files, credentials, and source code. |
| `file-uploads.md` | `file-uploads` | Expert at handling file uploads and cloud storage. |
| `filesystem-context.md` | `filesystem-context` | Use for file-based context management, dynamic context discovery, and reducing context window bloat. |
| `film-crew.md` | `film-crew` | Turn a one-line AI video idea into a shot list and per-shot, model-ready prompts via a film crew (director, DP, gaffer, editor, script supervisor). |
| `find-animation-opportunities.md` | `find-animation-opportunities` | Propose purposeful motion opportunities from a read-only codebase review, with evidence and explicit exclusions. |
| `find-bugs.md` | `find-bugs` | Find bugs, security vulnerabilities, and code quality issues in local branch changes. |
| `find-matching-tenders.md` | `find-matching-tenders` | Find open AU/NZ government tenders matching what a company does, ranked by fit with why and gap analysis. |
| `finishing-a-development-branch.md` | `finishing-a-development-branch` | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup |
| `firebase.md` | `firebase` | Firebase gives you a complete backend in minutes - auth, database, |
| `firewall-config.md` | `firewall-config` | Configure iptables, nftables, and cloud firewalls. |
| `firmware-analyst.md` | `firmware-analyst` | Expert firmware analyst specializing in embedded systems, IoT security, and hardware reverse engineering. |
| `firmware-pentest.md` | `firmware-pentest` | Firmware penetration testing following the OWASP FSTM nine-stage flow: extraction, EMBA automation, Firmadyne/QEMU emulation, AFL++ fuzzing, and hands-on exploitation in authorized labs. |
| `fitness-analyzer.md` | `fitness-analyzer` | 分析运动数据、识别运动模式、评估健身进展，并提供个性化训练建议。支持与慢性病数据的关联分析。 |
| `five-axis-code-review.md` | `five-axis-code-review` | Five-axis code review checklist (correctness, security, readability, performance, test coverage) producing actionable comments instead of style nitpicks. |
| `fix-review.md` | `fix-review` | Verify fix commits address audit findings without new bugs |
| `fixing-accessibility.md` | `fixing-accessibility` | Audit and fix HTML accessibility issues including ARIA labels, keyboard navigation, focus management, color contrast, and form errors. |
| `fixing-metadata.md` | `fixing-metadata` | Audit and fix HTML metadata including page titles, meta descriptions, canonical URLs, Open Graph tags, Twitter cards, favicons, JSON-LD structured data, and robots directives. |
| `fixing-motion-performance.md` | `fixing-motion-performance` | Audit and fix animation performance issues including layout thrashing, compositor properties, scroll-linked motion, and blur effects. |
| `flat-design.md` | `flat-design` | Web and App implementation guide for the Flat Design style. |
| `flat-design-2.md` | `flat-design-2` | Web and App implementation guide for Flat Design 2.0 (Semi-Flat). |
| `floating-ui.md` | `floating-ui` | Web and App implementation guide for Floating UI. |
| `flowhunt-skill.md` | `flowhunt-skill` | Automation discovery audit skill. |
| `flutter-expert.md` | `flutter-expert` | Master Flutter development with Dart 3, advanced widgets, and multi-platform deployment. |
| `folder-specific-claude-and-agents-md.md` | `folder-specific-claude-and-agents-md` | Create folder-scoped CLAUDE.md and AGENTS.md guidance for future agents working in that area. |
| `food-database-query.md` | `food-database-query` | Food Database Query |
| `footval-follow-matches-and-tables.md` | `footval-follow-matches-and-tables` | Football scores, fixtures, match centres and league tables through FootVal: live and past results, a team's next or last matches, events, statistics, line-ups and standings. |
| `footval-scout-and-rank-players.md` | `footval-scout-and-rank-players` | Scout and rank footballers with FootVal: shortlists by league, position, age, foot and value; undervalued, overvalued, rising and young players; club, league and national squads. |
| `footval-stats-and-transfer-news.md` | `footval-stats-and-transfer-news` | Football season leaderboards and transfer news from FootVal: top scorers, assists, minutes and appearances per competition, plus confirmed transfers and rumours with reliability. |
| `footval-value-and-compare-players.md` | `footval-value-and-compare-players` | Explain what a footballer is worth with FootVal: its own transfer value next to the market value, the factors behind the gap, and comparisons of two to four players. |
| `form-cro.md` | `form-cro` | Optimize any form that is NOT signup or account registration — including lead capture, contact, demo request, application, survey, quote, and checkout forms. |
| `formik-patterns.md` | `formik-patterns` | Formik form handling with validation patterns. |
| `fp-async.md` | `fp-async` | Practical async patterns using TaskEither - clean pipelines instead of try/catch hell, with real API examples |
| `fp-backend.md` | `fp-backend` | Functional programming patterns for Node.js/Deno backend development using fp-ts, ReaderTaskEither, and functional dependency injection |
| `fp-data-transforms.md` | `fp-data-transforms` | Everyday data transformations using functional patterns - arrays, objects, grouping, aggregation, and null-safe access |
| `fp-either-ref.md` | `fp-either-ref` | Quick reference for Either type. |
| `fp-errors.md` | `fp-errors` | Stop throwing everywhere - handle errors as values using Either and TaskEither for cleaner, more predictable code |
| `fp-option-ref.md` | `fp-option-ref` | Quick reference for Option type. |
| `fp-pipe-ref.md` | `fp-pipe-ref` | Quick reference for pipe and flow. |
| `fp-pragmatic.md` | `fp-pragmatic` | A practical, jargon-free guide to functional programming - the 80/20 approach that gets results without the academic overhead |
| `fp-react.md` | `fp-react` | Practical patterns for using fp-ts with React - hooks, state, forms, data fetching. |
| `fp-refactor.md` | `fp-refactor` | Comprehensive guide for refactoring imperative TypeScript code to fp-ts functional patterns |
| `fp-taskeither-ref.md` | `fp-taskeither-ref` | Quick reference for TaskEither. |
| `fp-ts-errors.md` | `fp-ts-errors` | Handle errors as values using fp-ts Either and TaskEither for cleaner, more predictable TypeScript code. |
| `fp-ts-pragmatic.md` | `fp-ts-pragmatic` | A practical, jargon-free guide to fp-ts functional programming - the 80/20 approach that gets results without the academic overhead. |
| `fp-ts-react.md` | `fp-ts-react` | Practical patterns for using fp-ts with React - hooks, state, forms, data fetching. |
| `fp-types-ref.md` | `fp-types-ref` | Quick reference for fp-ts types. |
| `framework-migration-code-migrate.md` | `framework-migration-code-migrate` | You are a code migration expert specializing in transitioning codebases between frameworks, languages, versions, and platforms. |
| `framework-migration-deps-upgrade.md` | `framework-migration-deps-upgrade` | You are a dependency management expert specializing in safe, incremental upgrades of project dependencies. |
| `framework-migration-legacy-modernize.md` | `framework-migration-legacy-modernize` | Orchestrate a comprehensive legacy system modernization using the strangler fig pattern, enabling gradual replacement of outdated components while maintaining continuous business operations through ex |
| `free-design-resources.md` | `free-design-resources` | Design resource register: resource and provider, licence type, commercial-use and attribution rules, export format, lock-in risk, free tier limit and accessibility notes. |
| `free-tier-strategy.md` | `free-tier-strategy` | Design free tiers that convert to paid without creating resentment or abuse. |
| `free-tool-strategy.md` | `free-tool-strategy` | You are an expert in engineering-as-marketing strategy. |
| `frontend-api-integration-patterns.md` | `frontend-api-integration-patterns` | Production-ready patterns for integrating frontend applications with backend APIs, including race condition handling, request cancellation, retry strategies, error normalization, and UI state management. |
| `frontend-architecture.md` | `frontend-architecture` | A portable, framework-agnostic architecture style for any React or React Native frontend. |
| `frontend-data-contracts.md` | `frontend-data-contracts` | A portable, framework-agnostic discipline for type safety at the network edge of any React or React Native app. |
| `frontend-design.md` | `frontend-design` | Design and implement a distinctive frontend within the product’s existing brand, accessibility, performance and framework constraints. |
| `frontend-dev-guidelines.md` | `frontend-dev-guidelines` | You are a senior frontend engineer operating under strict architectural and performance standards. |
| `frontend-developer.md` | `frontend-developer` | Build React components, implement responsive layouts, and handle client-side state management. |
| `frontend-lighthouse.md` | `frontend-lighthouse` | Add a portable Lighthouse CI gate for production frontend builds with Core Web Vitals budgets, category floors, median runs, and CI artifacts. |
| `frontend-mobile-development-component-scaffold.md` | `frontend-mobile-development-component-scaffold` | Scaffold React and React Native components with TypeScript, accessibility, tests, styles, and documentation. |
| `frontend-mobile-security-xss-scan.md` | `frontend-mobile-security-xss-scan` | Inspect frontend code for XSS injection points, unsafe DOM manipulation, and missing sanitization. |
| `frontend-observability.md` | `frontend-observability` | A portable, framework-agnostic field-side observability pattern for React or React Native integrations. |
| `frontend-optimistic-mutations.md` | `frontend-optimistic-mutations` | A portable, framework-agnostic discipline for the write path of any React or React Native app using a query/cache layer. |
| `frontend-security-coder.md` | `frontend-security-coder` | Expert in secure frontend coding practices specializing in XSS prevention, output sanitization, and client-side security patterns. |
| `frontend-seo.md` | `frontend-seo` | A portable, framework-agnostic SEO system for any React or React Native-for-web frontend. |
| `frontend-slides.md` | `frontend-slides` | Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. |
| `frontend-slides-frontend-slides.md` | `frontend-slides-frontend-slides` | Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. |
| `frontend-ui-dark-ts.md` | `frontend-ui-dark-ts` | A modern dark-themed React UI system using Tailwind CSS and Framer Motion. |
| `frontend-ui-engineering.md` | `frontend-ui-engineering` | Builds production-quality UIs. |
| `frutiger-aero.md` | `frutiger-aero` | Web and App implementation guide for Frutiger Aero. |
| `fsi-compliance-checker.md` | `fsi-compliance-checker` | Maps code, architecture, and infrastructure changes to specific control IDs in PCI-DSS v4.0.1 and MAS TRM (Singapore financial regulator), producing an audit-traceable findings report with per-control remediation. |
| `full-output-enforcement.md` | `full-output-enforcement` | Use when a task requires exhaustive unabridged output, complete files, or strict prevention of placeholders and skipped code. |
| `full-stack-orchestration-full-stack-feature.md` | `full-stack-orchestration-full-stack-feature` | Use when working with full stack orchestration full stack feature |
| `game-art.md` | `game-art` | Game art principles. |
| `game-audio.md` | `game-audio` | Game audio principles. |
| `game-design.md` | `game-design` | Game design principles. |
| `game-development.md` | `game-development` | >- |
| `gamification-engine.md` | `gamification-engine` | Gamification points register: player and department, points balance and points earned this month, level, badges, source module and last-updated date. |
| `gbp-local-seo-intent.md` | `gbp-local-seo-intent` | Google Business Profile register: element, primary and supporting keywords, search intent, landing page, post dates, review rating and reply status, visibility and status. |
| `gcp-audit-logs.md` | `gcp-audit-logs` | Configure GCP Cloud Audit Logs for compliance. |
| `gcp-cloud-functions.md` | `gcp-cloud-functions` | Deploy serverless functions on Google Cloud Functions. |
| `gcp-cloud-run.md` | `gcp-cloud-run` | Specialized skill for building production-ready serverless |
| `gcp-cloud-sql.md` | `gcp-cloud-sql` | Provision Cloud SQL databases. |
| `gcp-compute.md` | `gcp-compute` | Manage Compute Engine instances and instance templates. |
| `gcp-gke.md` | `gcp-gke` | Deploy and manage Google Kubernetes Engine clusters. |
| `gcp-networking.md` | `gcp-networking` | Configure VPCs, firewall rules, and Cloud NAT. |
| `gdb-cli.md` | `gdb-cli` | GDB debugging assistant for AI agents - analyze core dumps, debug live processes, investigate crashes and deadlocks with source code correlation |
| `gdpr-compliance.md` | `gdpr-compliance` | Implement GDPR data protection requirements. |
| `gdpr-data-handling.md` | `gdpr-data-handling` | Practical implementation guide for GDPR-oriented data-processing design, consent management, and privacy controls. |
| `gemini-api-dev.md` | `gemini-api-dev` | Use this skill when building applications with Gemini API hosted models, including Gemini and Gemma 4, working with multimodal content (text, images, audio, video), implementing function calling, using structured outputs, or needing current model specifications. |
| `gemini-interactions-api.md` | `gemini-interactions-api` | Build with the Gemini Interactions API for text, chat, multimodal generation, streaming, managed or background agents, function calling, structured output, and generateContent migrations. |
| `geminiignore-finops.md` | `geminiignore-finops` | Configure and optimize .geminiignore files for AI context window efficiency and token cost reduction (FinOps). |
| `geo-audit.md` | `geo-audit` | Full website GEO+SEO audit with parallel subagent delegation. |
| `geo-brand-mentions.md` | `geo-brand-mentions` | Brand mention and authority scanner for AI visibility. |
| `geo-citability.md` | `geo-citability` | AI citability scoring and optimization. |
| `geo-compare.md` | `geo-compare` | Monthly delta tracking and progress reporting for GEO clients. |
| `geo-content.md` | `geo-content` | Content quality and E-E-A-T assessment for AI citability — evaluate experience, |
| `geo-crawlers.md` | `geo-crawlers` | AI crawler access analysis. |
| `geo-fundamentals.md` | `geo-fundamentals` | Generative Engine Optimization for AI search engines (ChatGPT, Claude, Perplexity). |
| `geo-keyword-expansion-tool.md` | `geo-keyword-expansion-tool` | Geo Keyword Expansion Tool. |
| `geo-llmstxt.md` | `geo-llmstxt` | Analyzes and generates llms.txt files -- a proposed convention for helping |
| `geo-platform-optimizer.md` | `geo-platform-optimizer` | Platform-specific AI search optimization — audit and optimize for Google |
| `geo-proposal.md` | `geo-proposal` | Auto-generate a professional, client-ready GEO service proposal from |
| `geo-prospect.md` | `geo-prospect` | CRM-lite for managing GEO agency prospects and clients. |
| `geo-report.md` | `geo-report` | Generate a professional, client-facing GEO report combining all audit |
| `geo-report-pdf.md` | `geo-report-pdf` | Generate a professional PDF report from a GEO audit using pandoc + Chrome |
| `geo-schema.md` | `geo-schema` | Schema.org structured data audit and generation optimized for AI discoverability |
| `geo-technical.md` | `geo-technical` | Technical SEO audit with GEO-specific checks — crawlability, indexability, |
| `geoffrey-hinton.md` | `geoffrey-hinton` | Agente que simula Geoffrey Hinton — Godfather of Deep Learning, Prêmio Turing 2018, coautor do trabalho de 1986 que popularizou backpropagation e das Deep Belief Networks. |
| `get-seen-in-replies.md` | `get-seen-in-replies` | Write a reply to someone else's tweet that is worth reading on its own. |
| `gh-attach.md` | `gh-attach` | Upload and download GitHub user-attachments (screenshots, PDFs, zips, videos) from the terminal; use when asked to attach or embed a file in a PR, issue, or comment, or download an attachment URL. |
| `gh-review-requests.md` | `gh-review-requests` | Fetch unread GitHub notifications for open PRs where review is requested from a specified team or opened by a team member. |
| `gha-security-review.md` | `gha-security-review` | Review GitHub Actions workflows for exploitable vulnerabilities with concrete attack paths and harmless proof-of-concept sketches. |
| `ghidra-reverse.md` | `ghidra-reverse` | Free/open reverse engineering with Ghidra (headless or GUI): decompilation, cross-references, scripting, and optional Ghidra MCP workflows when IDA is unavailable. |
| `git-advanced-workflows.md` | `git-advanced-workflows` | Master advanced Git techniques to maintain clean history, collaborate effectively, and recover from any situation with confidence. |
| `git-commit-message.md` | `git-commit-message` | Generates conventional-commit messages from staged changes: type prefix + English imperative subject (≤50 chars) + optional body explaining why. |
| `git-hooks-automation.md` | `git-hooks-automation` | Master Git hooks setup with Husky, lint-staged, pre-commit framework, and commitlint. |
| `git-pr-review.md` | `git-pr-review` | Generate a concise and structured PR description from commit history with minimal token usage |
| `git-pr-workflows-git-workflow.md` | `git-pr-workflows-git-workflow` | Orchestrate review, tests, commits, branch pushes, and pull-request creation with parallel agents. |
| `git-pr-workflows-onboard.md` | `git-pr-workflows-onboard` | You are an **expert onboarding specialist and knowledge transfer architect** with deep experience in remote-first organizations, technical team integration, and accelerated learning methodologies. |
| `git-pr-workflows-pr-enhance.md` | `git-pr-workflows-pr-enhance` | Improve pull request descriptions, reviewability, change scope, and supporting validation evidence. |
| `git-pushing.md` | `git-pushing` | Safely stage, commit, and push intended git changes with conventional commit messages. |
| `git-workflow.md` | `git-workflow` | Implement Git branching strategies, PR workflows, and release management |
| `git-workflow-and-versioning.md` | `git-workflow-and-versioning` | Structures git workflow practices. |
| `github.md` | `github` | Use the `gh` CLI for issues, pull requests, Actions runs, and GitHub API queries. |
| `github-actions.md` | `github-actions` | Build, test, and deploy applications using GitHub Actions workflows. |
| `github-actions-advanced.md` | `github-actions-advanced` | Design, debug, and harden GitHub Actions CI/CD workflows, including reusable workflows, matrix builds, self-hosted runners, OIDC authentication, caching, environments, secrets, and release automation. |
| `github-actions-debugger.md` | `github-actions-debugger` | Specialized skill for diagnosing, analyzing, and fixing failing GitHub Actions workflows by parsing run logs and pipeline definitions. |
| `github-actions-templates.md` | `github-actions-templates` | Production-ready GitHub Actions workflow patterns for testing, building, and deploying applications. |
| `github-issue-creator.md` | `github-issue-creator` | Turn error logs, screenshots, voice notes, and rough bug reports into crisp, developer-ready GitHub issues with repro steps, impact, and evidence. |
| `github-workflow-automation.md` | `github-workflow-automation` | Patterns for automating GitHub workflows with AI assistance, inspired by [Gemini CLI](https://github.com/google-gemini/gemini-cli) and modern DevOps practices. |
| `gitlab-ci.md` | `gitlab-ci` | Configure GitLab CI/CD pipelines and runners for automated building, |
| `gitlab-ci-patterns.md` | `gitlab-ci-patterns` | Comprehensive GitLab CI/CD pipeline patterns for automated testing, building, and deployment. |
| `gitops-workflow.md` | `gitops-workflow` | Complete guide to implementing GitOps workflows with ArgoCD and Flux for automated Kubernetes deployments. |
| `glassmorphism.md` | `glassmorphism` | Web and App implementation guide for Glassmorphism. |
| `global-chat-agent-discovery.md` | `global-chat-agent-discovery` | Discover and compare MCP servers and AI agents using Global Chat's cross-protocol directory and MCP server. |
| `gmail-automation.md` | `gmail-automation` | Lightweight Gmail integration with standalone OAuth authentication. |
| `gmb-optimization-helper.md` | `gmb-optimization-helper` | GMB Optimization Helper. |
| `go.md` | `go` | Language-specific super-code guidelines for go. |
| `go-concurrency-patterns.md` | `go-concurrency-patterns` | Master Go concurrency with goroutines, channels, sync primitives, and context. |
| `go-in-depth.md` | `go-in-depth` | Go in depth harness — fan-out web searches, fetch sources, adversarially verify claims, synthesize a cited report. |
| `go-playwright.md` | `go-playwright` | Expert capability for robust, stealthy, and efficient browser automation using Playwright Go. |
| `go-rod-master.md` | `go-rod-master` | Comprehensive guide for browser automation and web scraping with go-rod (Chrome DevTools Protocol) including stealth anti-bot-detection patterns. |
| `go-rust-reverse.md` | `go-rust-reverse` | Reverse engineer stripped Go and Rust binaries: runtime recognition, pclntab/module metadata recovery, panic-string analysis, and idiomatic decompilation strategies. |
| `goal-analyzer.md` | `goal-analyzer` | 分析健康目标数据、识别目标模式、评估目标进度,并提供个性化目标管理建议。支持与营养、运动、睡眠等健康数据的关联分析。 |
| `goal-instruction-writer.md` | `goal-instruction-writer` | Preview, draft, refine, or audit durable agent Goals with acceptance evidence, drift controls, proportional verification, and bounded waiting. |
| `goal-loop.md` | `goal-loop` | Draft and explain persistent goal-loop prompts for long-running agent work with clear stop conditions. |
| `godot-4-migration.md` | `godot-4-migration` | Specialized guide for migrating Godot 3.x projects to Godot 4 (GDScript 2.0), covering syntax changes, Tweens, and exports. |
| `godot-gdscript-patterns.md` | `godot-gdscript-patterns` | Master Godot 4 GDScript patterns including signals, scenes, state machines, and optimization. |
| `golang-pro.md` | `golang-pro` | Master Go 1.21+ with modern patterns, advanced concurrency, performance optimization, and production-ready microservices. |
| `google-calendar-automation.md` | `google-calendar-automation` | Plan and perform authorized Google Calendar workflows through an existing authenticated integration; inspect events, draft changes and verify results. |
| `google-docs-automation.md` | `google-docs-automation` | Read and edit Google Docs through an available authenticated connector or reviewed API integration, with scoped changes and read-back verification. |
| `google-drive-automation.md` | `google-drive-automation` | Lightweight Google Drive integration with standalone OAuth authentication. |
| `google-no-code.md` | `google-no-code` | Design Google Forms and wire Apps Script triggers (onFormSubmit) for email alerts, spreadsheet logging, and dynamic questions — no code editor required. |
| `google-sheets-automation.md` | `google-sheets-automation` | Read and edit Google Sheets through an available authenticated connector or reviewed API integration, with scoped changes and read-back verification. |
| `google-slides-automation.md` | `google-slides-automation` | Read and edit Google Slides through an available authenticated connector or reviewed API integration, with scoped changes and read-back verification. |
| `gpt-taste.md` | `gpt-taste` | Use when generating elite GSAP-heavy frontend pages with strict AIDA structure, wide hero typography, and gapless bento grids. |
| `gpu-kubernetes-operations.md` | `gpu-kubernetes-operations` | Operate GPU-backed Kubernetes clusters for AI inference and training |
| `gpu-server-management.md` | `gpu-server-management` | Set up and manage NVIDIA GPU servers for AI workloads |
| `graceful-shutdown.md` | `graceful-shutdown` | Implement graceful shutdown for servers and workers: drain connections, finish in-flight work, release resources, and exit cleanly on SIGTERM/SIGINT. |
| `gradient-design.md` | `gradient-design` | Web and App implementation guide for Gradient Design. |
| `grafana-dashboards.md` | `grafana-dashboards` | Create and manage production-ready Grafana dashboards for comprehensive system observability. |
| `graphql.md` | `graphql` | GraphQL gives clients exactly the data they need - no more, no |
| `graphql-architect.md` | `graphql-architect` | Master modern GraphQL with federation, performance optimization, and enterprise security. |
| `graphql-schema.md` | `graphql-schema` | GraphQL queries, mutations, and code generation patterns. |
| `grill-me.md` | `grill-me` | A relentless interview to sharpen a plan or design. |
| `grill-with-docs.md` | `grill-with-docs` | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. |
| `grilling.md` | `grilling` | Interview the user relentlessly about a plan or design. |
| `grok-build.md` | `grok-build` | Delegate well-specified implementation tasks to xAI's Grok Build CLI running headlessly while the orchestrating agent plans, writes task specs, reviews every diff, and owns the result. |
| `growth-engine.md` | `growth-engine` | Motor de crescimento para produtos digitais -- growth hacking, SEO, ASO, viral loops, email marketing, CRM, referral programs e aquisicao organica. |
| `grpc-golang.md` | `grpc-golang` | Build production-ready gRPC services in Go with mTLS, streaming, and observability. |
| `guest-posting-opportunity-finder.md` | `guest-posting-opportunity-finder` | Guest Posting Opportunity Finder. |
| `handoff.md` | `handoff` | Compact the current conversation into a handoff document for another agent to pick up. |
| `hardware-security.md` | `hardware-security` | Authorized hardware and embedded interface security research: UART/JTAG discovery, debug-pad triage, secure-boot overview, and offline firmware analysis. |
| `harvey-specter.md` | `harvey-specter` | Prepare negotiations, difficult conversations, and leadership replies with evidence, clear boundaries, relationship-aware tone, and Harvey Specter-inspired composure. |
| `hasdata-cli.md` | `hasdata-cli` | Command-line access to search, scraping, and structured web data. |
| `haskell-pro.md` | `haskell-pro` | Design and review Haskell types, pure domain logic, parsing, exception-safe concurrency, Cabal/Stack builds and measured performance. |
| `heading-analyzer.md` | `heading-analyzer` | Heading Analyzer. |
| `headline-analyzer.md` | `headline-analyzer` | Headline Analyzer. |
| `headline-psychologist.md` | `headline-psychologist` | Draft and compare audience-aware headlines when copy needs clearer relevance and curiosity without clickbait or unsupported promises. |
| `health-trend-analyzer.md` | `health-trend-analyzer` | 分析一段时间内健康数据的趋势和模式。关联药物、症状、生命体征、化验结果和其他健康指标的变化。识别令人担忧的趋势、改善情况，并提供数据驱动的洞察。当用户询问健康趋势、模式、随时间的变化或"我的健康状况有什么变化？"时使用。支持多维度分析（体重/BMI、症状、药物依从性、化验结果、情绪睡眠），相关性分析，变化检测，以及交互式HTML可视化报告（ECharts图表）。 |
| `health-wellness.md` | `health-wellness` | Wellbeing check-in register: anonymous flag, department, check-in date, wellbeing score, stress and energy levels, support and resource flags, confidentiality and status. |
| `healthcare-job-search.md` | `healthcare-job-search` | Find open US healthcare jobs (nursing, CNA, allied health, therapy, imaging, pharmacy, physicians) and the hourly pay employers post, via CareJobs.Now's free MCP server or JSON endpoints. |
| `helium-mcp.md` | `helium-mcp` | Connect to Helium's MCP server for news research, media bias analysis, balanced perspectives, stock/options data, and semantic meme search across 3.2M+ articles and 5,000+ sources |
| `helm-chart-scaffolding.md` | `helm-chart-scaffolding` | Comprehensive guidance for creating, organizing, and managing Helm charts for packaging and deploying Kubernetes applications. |
| `helm-charts.md` | `helm-charts` | Create, manage, and deploy Helm charts for Kubernetes package management. |
| `hf-cli.md` | `hf-cli` | Curated upstream guidance for Hf Cli; use when the workflow matches the user goal. |
| `hf-cloud-aws-context-discovery.md` | `hf-cloud-aws-context-discovery` | Discover the effective local AWS profile, region, account, and caller identity before any AWS task without exposing credentials. |
| `hf-mcp.md` | `hf-mcp` | Use Hugging Face Hub via MCP server tools. |
| `hf-mem.md` | `hf-mem` | Hugging Face CLI to estimate the required memory to load Safetensors or GGUF model weights for inference from the Hugging Face Hub |
| `hierarchical-agent-memory.md` | `hierarchical-agent-memory` | Scoped CLAUDE.md memory system that reduces context token spend. |
| `hig-components-content.md` | `hig-components-content` | Apple Human Interface Guidelines for content display components. |
| `hig-components-controls.md` | `hig-components-controls` | Choose and review Apple selection and input controls: toggles, segmented controls, sliders, pickers, steppers, text fields, labels and keyboard behavior. |
| `hig-components-dialogs.md` | `hig-components-dialogs` | Apple HIG guidance for presentation components including alerts, action sheets, popovers, sheets, and digit entry views. |
| `hig-components-layout.md` | `hig-components-layout` | Apple Human Interface Guidelines for layout and navigation components. |
| `hig-components-menus.md` | `hig-components-menus` | Design Apple-platform menus, buttons, toolbars and disclosure controls using the appropriate platform conventions, command hierarchy and accessible interactions. |
| `hig-components-search.md` | `hig-components-search` | Apple HIG guidance for navigation-related components including search fields, page controls, and path controls. |
| `hig-components-status.md` | `hig-components-status` | Apple HIG guidance for status and progress UI components including progress indicators, status bars, and activity rings. |
| `hig-components-system.md` | `hig-components-system` | Apple HIG guidance for system experience components: widgets, live activities, notifications, complications, home screen quick actions, top shelf, watch faces, app clips, and app shortcuts. |
| `hig-foundations.md` | `hig-foundations` | Apple Human Interface Guidelines design foundations. |
| `hig-inputs.md` | `hig-inputs` | Design Apple-platform input interactions for touch, keyboard, pointer, Pencil, controllers, spatial gestures and supported device sensors, with accessible alternatives. |
| `hig-patterns.md` | `hig-patterns` | Apple Human Interface Guidelines interaction and UX patterns. |
| `hig-platforms.md` | `hig-platforms` | Apple Human Interface Guidelines for platform-specific design. |
| `hig-project-context.md` | `hig-project-context` | Create or update a shared Apple design context document that other HIG skills use to tailor guidance. |
| `hig-technologies.md` | `hig-technologies` | Review Apple-platform technology UX against HIG patterns for payments, health data, identity, Siri, AR, cloud sync, and shared experiences. |
| `high-contrast.md` | `high-contrast` | Web and App implementation guide for High Contrast Design. |
| `high-end-visual-design.md` | `high-end-visual-design` | Use when designing expensive agency-grade interfaces with premium fonts, spatial rhythm, soft depth, and fluid microinteractions. |
| `hipaa-compliance.md` | `hipaa-compliance` | Implement HIPAA security and privacy rules. |
| `holographic-ui.md` | `holographic-ui` | Web and App implementation guide for Holographic UI. |
| `hono.md` | `hono` | Build ultra-fast web APIs and full-stack apps with Hono — runs on Cloudflare Workers, Deno, Bun, Node.js, and any WinterCG-compatible runtime. |
| `hosted-agents.md` | `hosted-agents` | Build background agents in sandboxed environments. |
| `hosted-agents-v2-py.md` | `hosted-agents-v2-py` | Build hosted agents using Azure AI Projects SDK with HostedAgentDefinition. |
| `hr-pro.md` | `hr-pro` | Professional, ethical HR partner for hiring, onboarding/offboarding, PTO and leave, performance, compliant policies, and employee relations. |
| `hreflang-tag-generator.md` | `hreflang-tag-generator` | Hreflang Tag Generator. |
| `html-injection-testing.md` | `html-injection-testing` | Identify and exploit HTML injection vulnerabilities that allow attackers to inject malicious HTML content into web applications. |
| `http-status-code-tester.md` | `http-status-code-tester` | HTTP Status Code Tester. |
| `hubspot-integration.md` | `hubspot-integration` | Expert patterns for HubSpot CRM integration including OAuth |
| `hugging-face-cli.md` | `hugging-face-cli` | Hugging Face Hub CLI (`hf`) for downloading, uploading, and managing models, datasets, spaces, buckets, repos, papers, jobs, and more on the Hugging Face Hub. |
| `hugging-face-community-evals.md` | `hugging-face-community-evals` | Run evaluations for Hugging Face Hub models using inspect-ai and lighteval on local hardware. |
| `hugging-face-dataset-viewer.md` | `hugging-face-dataset-viewer` | Hugging Face Dataset Viewer |
| `hugging-face-datasets.md` | `hugging-face-datasets` | Create and manage datasets on Hugging Face Hub. |
| `hugging-face-evaluation.md` | `hugging-face-evaluation` | Add and manage evaluation results in Hugging Face model cards. |
| `hugging-face-gradio.md` | `hugging-face-gradio` | Build Gradio web UIs and demos in Python. |
| `hugging-face-jobs.md` | `hugging-face-jobs` | Run workloads on Hugging Face Jobs with managed CPUs, GPUs, TPUs, secrets, and Hub persistence. |
| `hugging-face-model-trainer.md` | `hugging-face-model-trainer` | Train or fine-tune language and vision models using TRL (Transformer Reinforcement Learning) or Unsloth with Hugging Face Jobs infrastructure. |
| `hugging-face-paper-publisher.md` | `hugging-face-paper-publisher` | Publish and manage research papers on Hugging Face Hub. |
| `hugging-face-papers.md` | `hugging-face-papers` | Look up and read Hugging Face paper pages in markdown, and use the papers API for structured metadata such as authors, linked models/datasets/spaces, Github repo and project page. |
| `hugging-face-tool-builder.md` | `hugging-face-tool-builder` | Your purpose is now is to create reusable command line scripts and utilities for using the Hugging Face API, allowing chaining, piping and intermediate processing where helpful. |
| `hugging-face-trackio.md` | `hugging-face-trackio` | Track and visualize ML training experiments with Trackio. |
| `hugging-face-vision-trainer.md` | `hugging-face-vision-trainer` | Train object detection, image classification, and SAM or SAM2 segmentation models locally or on Hugging Face Jobs, with bounded dataset pilots and explicit artifact persistence. |
| `huggingface-best.md` | `huggingface-best` | Use when the user asks about finding the best, top, or recommended model for a task, wants to know what AI model to use, or wants to compare models by benchmark scores. |
| `huggingface-community-evals.md` | `huggingface-community-evals` | Curated upstream guidance for Huggingface Community Evals; use when the workflow matches the user goal. |
| `huggingface-datasets.md` | `huggingface-datasets` | Use this skill for Hugging Face Dataset Viewer API workflows that fetch |
| `huggingface-local-models.md` | `huggingface-local-models` | Use to select models to run locally with llama.cpp and GGUF on CPU, Mac Metal, CUDA, or ROCm. |
| `huggingface-lora-space-builder.md` | `huggingface-lora-space-builder` | Build and publish a Gradio demo on Hugging Face Spaces for a user-provided LoRA. |
| `huggingface-spaces.md` | `huggingface-spaces` | Build, deploy, and maintain applications on Hugging Face Spaces — Gradio / Docker / Static SDKs, ZeroGPU and dedicated hardware, model loading, debugging, buckets, inference providers, community grants. |
| `huggingface-tool-builder.md` | `huggingface-tool-builder` | Use this skill when the user wants to build tool/scripts or achieve a task where using data from the Hugging Face API would help. |
| `huggingface-zerogpu.md` | `huggingface-zerogpu` | AI demos and GPU compute with Gradio Spaces and Hugging Face Spaces ZeroGPU. |
| `hugo-to-markdown.md` | `hugo-to-markdown` | Convert Hugo documentation sites and Hugo-managed content into standard Markdown. |
| `humanize-chinese.md` | `humanize-chinese` | Detect and rewrite AI-like Chinese text with a practical workflow for scoring, humanization, academic AIGC reduction, and style conversion. |
| `hunt-api-misconfig.md` | `hunt-api-misconfig` | Hunt API security misconfiguration |
| `hunt-aspnet.md` | `hunt-aspnet` | Hunt ASP.NET-specific surface |
| `hunt-ato.md` | `hunt-ato` | Hunt account takeover taxonomy |
| `hunt-auth-bypass.md` | `hunt-auth-bypass` | Hunting skill for auth bypass vulnerabilities. |
| `hunt-brute-force.md` | `hunt-brute-force` | Hunt Missing/Weak Rate Limiting |
| `hunt-business-logic.md` | `hunt-business-logic` | Hunting skill for business logic vulnerabilities. |
| `hunt-cache-poison.md` | `hunt-cache-poison` | Hunting skill for cache poison vulnerabilities. |
| `hunt-captcha-bypass.md` | `hunt-captcha-bypass` | Hunt CAPTCHA Bypass |
| `hunt-cicd.md` | `hunt-cicd` | Hunt CI/CD pipeline vulnerabilities |
| `hunt-clickjacking.md` | `hunt-clickjacking` | Hunt Clickjacking |
| `hunt-cloud-misconfig.md` | `hunt-cloud-misconfig` | Hunt cloud / infrastructure misconfigurations. |
| `hunt-cors.md` | `hunt-cors` | Hunt CORS Misconfiguration |
| `hunt-csrf.md` | `hunt-csrf` | Hunting skill for csrf vulnerabilities. |
| `hunt-deserialization.md` | `hunt-deserialization` | Hunt Insecure Deserialization |
| `hunt-dispatch.md` | `hunt-dispatch` | Skill-set loader for /hunt orchestrator. |
| `hunt-dom.md` | `hunt-dom` | Hunt client-side DOM vulnerabilities |
| `hunt-exceptional-conditions.md` | `hunt-exceptional-conditions` | Hunt mishandling of exceptional conditions |
| `hunt-file-upload.md` | `hunt-file-upload` | Hunt file upload bugs |
| `hunt-fintech-graphql.md` | `hunt-fintech-graphql` | Hunt fintech-specific GraphQL vulnerabilities |
| `hunt-forgot-password.md` | `hunt-forgot-password` | Hunt Forgot Password / Account Recovery Authentication Flaws |
| `hunt-graphql.md` | `hunt-graphql` | Hunting skill for graphql vulnerabilities. |
| `hunt-grpc.md` | `hunt-grpc` | Hunt gRPC vulnerabilities |
| `hunt-host-header.md` | `hunt-host-header` | Hunt Host Header Injection |
| `hunt-html-injection.md` | `hunt-html-injection` | Hunt HTML Injection |
| `hunt-http-smuggling.md` | `hunt-http-smuggling` | Hunt HTTP request smuggling (CL.TE, TE.CL, H2.CL, H2.TE). |
| `hunt-idor.md` | `hunt-idor` | Hunting skill for idor vulnerabilities. |
| `hunt-jwt-crypto.md` | `hunt-jwt-crypto` | Hunt JWT cryptographic failures |
| `hunt-k8s.md` | `hunt-k8s` | Hunt Kubernetes & Docker |
| `hunt-laravel.md` | `hunt-laravel` | Hunt Laravel specific vulnerabilities |
| `hunt-ldap.md` | `hunt-ldap` | Hunt LDAP Injection and XPath Injection |
| `hunt-lfi.md` | `hunt-lfi` | Hunt Local File Inclusion (LFI), Remote File Inclusion (RFI), and Path |
| `hunt-llm-ai.md` | `hunt-llm-ai` | Hunt LLM/AI feature bugs |
| `hunt-mfa-bypass.md` | `hunt-mfa-bypass` | Hunt MFA / 2FA bypass |
| `hunt-misc.md` | `hunt-misc` | Hunting skill for misc vulnerabilities. |
| `hunt-nextjs.md` | `hunt-nextjs` | Hunt Next.js specific vulnerabilities |
| `hunt-nodejs.md` | `hunt-nodejs` | Hunt Node.js specific vulnerabilities |
| `hunt-nosqli.md` | `hunt-nosqli` | Hunt NoSQL Injection |
| `hunt-ntlm-info.md` | `hunt-ntlm-info` | Hunt NTLM/Negotiate information disclosure on internet-reachable IIS/SharePoint/Exchange. |
| `hunt-oauth.md` | `hunt-oauth` | Hunting skill for oauth vulnerabilities. |
| `hunt-open-redirect.md` | `hunt-open-redirect` | Hunt Open Redirect |
| `hunt-race-condition.md` | `hunt-race-condition` | Hunting skill for race condition vulnerabilities. |
| `hunt-rag-vector.md` | `hunt-rag-vector` | Hunt vector-store / embedding-layer weaknesses in RAG pipelines (OWASP |
| `hunt-rce.md` | `hunt-rce` | Hunting skill for rce vulnerabilities. |
| `hunt-saml.md` | `hunt-saml` | Hunt SAML / SSO attacks. |
| `hunt-session.md` | `hunt-session` | Hunt Session Management vulnerabilities |
| `hunt-shadow-api.md` | `hunt-shadow-api` | Hunt shadow / zombie / undocumented API surface (OWASP API9 Improper |
| `hunt-sharepoint.md` | `hunt-sharepoint` | Hunt Microsoft SharePoint Server (2013/2016/2019/Subscription Edition) |
| `hunt-source-leak.md` | `hunt-source-leak` | Hunt source code and build artifact leakage |
| `hunt-spa-api.md` | `hunt-spa-api` | Discover a single-page-app's hidden backend API from its public JS bundle, |
| `hunt-springboot.md` | `hunt-springboot` | Hunt Spring Boot specific vulnerabilities |
| `hunt-sqli.md` | `hunt-sqli` | Hunting skill for sqli vulnerabilities. |
| `hunt-ssrf.md` | `hunt-ssrf` | Hunting skill for ssrf vulnerabilities. |
| `hunt-ssti.md` | `hunt-ssti` | Hunt server-side template injection (SSTI) across Jinja2 (Flask/Django), |
| `hunt-subdomain.md` | `hunt-subdomain` | Hunting skill for subdomain takeover vulnerabilities. |
| `hunt-tls-network.md` | `hunt-tls-network` | Hunt TLS/SSL and DNS misconfigurations |
| `hunt-websocket.md` | `hunt-websocket` | Hunt WebSocket vulnerabilities |
| `hunt-xss.md` | `hunt-xss` | Hunting skill for xss vulnerabilities. |
| `hunt-xxe.md` | `hunt-xxe` | Hunting skill for xxe vulnerabilities. |
| `hybrid-cloud-architect.md` | `hybrid-cloud-architect` | Expert hybrid cloud architect specializing in complex multi-cloud solutions across AWS/Azure/GCP and private clouds (OpenStack/VMware). |
| `hybrid-cloud-networking.md` | `hybrid-cloud-networking` | Configure secure, high-performance connectivity between on-premises and cloud environments using VPN, Direct Connect, and ExpressRoute. |
| `hybrid-search-implementation.md` | `hybrid-search-implementation` | Combine vector and keyword search for improved retrieval. |
| `hyperframes.md` | `hyperframes` | Create and review editable HTML-to-video projects with the HyperFrames timeline, composition and rendering contract. |
| `hyperframes-cli.md` | `hyperframes-cli` | Scaffold, inspect, preview and render HyperFrames projects; use local or explicitly authorized hosted workflows. |
| `hyperframes-registry.md` | `hyperframes-registry` | Find and integrate editable HyperFrames blocks and components for video scenes, transitions and effects. |
| `i-have-adhd.md` | `i-have-adhd` | 'Shape output for ADHD readers: next action first, numbered steps, restated |
| `i18n-localization.md` | `i18n-localization` | Internationalization and localization patterns. |
| `iconsax-library.md` | `iconsax-library` | Extensive icon library and AI-driven icon generation skill for premium UI/UX design. |
| `ida-reverse.md` | `ida-reverse` | Reverse engineer binaries with IDA Pro: decompilation, disassembly, data-flow tracking, cross-references, and IDA MCP automation for deep static analysis of PE/ELF/Mach-O targets. |
| `idea-autopsy.md` | `idea-autopsy` | Autopsy a business idea before you build it: kill-list check, five hard filters, a free-AI one-prompt test, live ad-market verification, and a verdict with a named kill-pattern. |
| `idea-darwin.md` | `idea-darwin` | Darwinian idea evolution engine — toss rough ideas onto an evolution island, let them compete, crossbreed, and mutate through structured rounds to surface your strongest concepts. |
| `idea-evaluator.md` | `idea-evaluator` | Evaluates an idea by hosting a multi-turn debate between a Pro and Con agent, delivering a final verdict on whether it's worth pursuing. |
| `idea-evaluator-con.md` | `idea-evaluator-con` | The Con Agent persona for idea evaluation. |
| `idea-evaluator-pro.md` | `idea-evaluator-pro` | The Pro Agent persona for idea evaluation. |
| `idea-os.md` | `idea-os` | Five-phase pipeline (triage → clarify → research → PRD → plan) that turns a raw idea into four linked files: clarifying questions, deep research, a PRD with non-goals and metrics, and a phased execution plan with mermaid user journey and kill criteria. |
| `idea-refine.md` | `idea-refine` | Refines raw ideas into sharp, actionable concepts through structured divergent and convergent thinking. |
| `idea-to-blueprint.md` | `idea-to-blueprint` | Turn a raw product, app, bot or feature idea into one evidence-backed build blueprint (researched stack, epics, Given/When/Then criteria, tests) that coding agents build one epic per session. |
| `identity-federation.md` | `identity-federation` | Authorized assessment of federated identity systems: SAML, OIDC, OAuth2 flows, SSO misconfiguration, and token-confusion issues. |
| `identity-mirror.md` | `identity-mirror` | Map an audience's current and aspirational identity into credible messaging when copy needs stronger personal relevance. |
| `idor-testing.md` | `idor-testing` | Provide systematic methodologies for identifying and exploiting Insecure Direct Object Reference (IDOR) vulnerabilities in web applications. |
| `ilya-sutskever.md` | `ilya-sutskever` | Agente que simula Ilya Sutskever — co-fundador da OpenAI, ex-Chief Scientist, fundador da SSI. |
| `image-alt-tag-generator.md` | `image-alt-tag-generator` | Image Alt Tag Generator. |
| `image-generator.md` | `image-generator` | Generate and edit images using Gemini's Nano Banana Pro model (gemini-3-pro-image-preview). |
| `image-studio.md` | `image-studio` | Studio de geracao de imagens inteligente — roteamento automatico entre ai-studio-image (fotos humanizadas/influencer) e stability-ai (arte/ ilustracao/edicao). |
| `imagera-media.md` | `imagera-media` | Generate or edit images, video clips, voiceovers and music through the hosted Imagera MCP server, quoting the credit cost and getting approval before each paid call. |
| `implement.md` | `implement` | Implement a piece of work based on a PRD or set of issues. |
| `impress.md` | `impress` | Presentation creation, format conversion (ODP/PPTX/PDF), slide automation with LibreOffice Impress. |
| `impression-to-click-ratio-calculator.md` | `impression-to-click-ratio-calculator` | Impression-to-Click Ratio Calculator. |
| `improve-animations.md` | `improve-animations` | Audit existing motion and write prioritized implementation plans with exact evidence, scope, and verification steps. |
| `improve-codebase-architecture.md` | `improve-codebase-architecture` | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. |
| `incident-management.md` | `incident-management` | Implement incident management processes and escalation procedures. |
| `incident-responder.md` | `incident-responder` | Expert SRE incident responder specializing in rapid problem resolution, modern observability, and comprehensive incident management. |
| `incident-response.md` | `incident-response` | Handle security incidents with IR playbooks and procedures. |
| `incident-response-incident-response.md` | `incident-response-incident-response` | Use when working with incident response incident response |
| `incident-response-smart-fix.md` | `incident-response-smart-fix` | Investigate production issues, reproduce root causes, implement scoped fixes, and verify recovery using tests and observability. |
| `incident-runbook-templates.md` | `incident-runbook-templates` | Adaptable templates for incident response runbooks covering detection, triage, mitigation, resolution, and communication. |
| `incremental-implementation.md` | `incremental-implementation` | Delivers changes incrementally. |
| `indexing-issue-auditor.md` | `indexing-issue-auditor` | High-level technical SEO and site architecture auditor. |
| `industrial-brutalist-ui.md` | `industrial-brutalist-ui` | Use when creating raw industrial or tactical telemetry UIs with rigid grids, stark typography, CRT effects, and high-density data. |
| `infinite-gratitude.md` | `infinite-gratitude` | Plan and synthesize multi-perspective research; use parallel agents only when authorized and verify findings against sources. |
| `infinity.md` | `infinity` | Enforces a strict input boundary protocol (detect, classify, filter, verify) to ensure untrusted data never reaches business logic raw. |
| `ingest-youtube.md` | `ingest-youtube` | Pull a YouTube video transcript into a queryable markdown vault with yt-dlp subtitle discovery, VTT cleanup, metadata frontmatter, and capture-seed stubs. |
| `inngest.md` | `inngest` | Inngest expert for serverless-first background jobs, event-driven |
| `instagram.md` | `instagram` | Integracao completa com Instagram via Graph API. |
| `instructree.md` | `instructree` | Map, explain, and lint repository-scoped coding-agent instructions before changing code. |
| `interactive-portfolio.md` | `interactive-portfolio` | Expert in building portfolios that actually land jobs and clients - |
| `interface-review.md` | `interface-review` | Reviews a branch, pull request or uncommitted change for the interface problems it introduced or regressed, across accessibility, layout, writing, typography, color and UI. |
| `intern-program.md` | `intern-program` | Internship register: intern and department, supervisor and mentor, institution, start and end dates, stipend, learning goals, mid-term and final scores, conversion flags. |
| `internal-comms.md` | `internal-comms` | Write internal communications such as status reports, leadership updates, 3P updates, newsletters, FAQs, incident reports, and project updates using repeatable internal formats. |
| `internal-comms-anthropic.md` | `internal-comms-anthropic` | Compatibility alias for internal-comms: draft status updates, newsletters and FAQs from approved sources. |
| `internal-comms-community.md` | `internal-comms-community` | Compatibility alias for internal-comms: draft status updates, newsletters and FAQs from approved sources. |
| `internal-communication.md` | `internal-communication` | Internal communication log: title, type, date, department, host and attendees, agenda, action items, follow-up date, meeting link and delivery status. |
| `internal-link-suggestion-tool.md` | `internal-link-suggestion-tool` | Internal Link Suggestion Tool. |
| `internal-linking-planner.md` | `internal-linking-planner` | Internal Linking Planner. |
| `interview-coach.md` | `interview-coach` | Full job search coaching system — JD decoding, resume, storybank, mock interviews, transcript analysis, comp negotiation. |
| `interview-me.md` | `interview-me` | Draw out what the user actually wants with one-question-at-a-time interviews |
| `interview-style-doc-building.md` | `interview-style-doc-building` | Build structured strategy documents by asking one question at a time and patching the file. |
| `invariant-guard.md` | `invariant-guard` | Correctness-first: forces writing the function contract, loop invariant, termination argument, and edge cases BEFORE code. |
| `inventory-demand-planning.md` | `inventory-demand-planning` | Codified expertise for demand forecasting, safety stock optimisation, replenishment planning, and promotional lift estimation at multi-location retailers. |
| `inventory-stock-reconciliation.md` | `inventory-stock-reconciliation` | Stock reconciliation register: count date, item, warehouse, book vs physical quantity, variance quantity and value, variance reason, damage and expiry, adjustment and approval. |
| `invoices-billing.md` | `invoices-billing` | Invoice and billing register: invoice number, client, project, issue and due dates, subtotal, discount, tax and withholding, total, payments, balance and aging. |
| `invokely-statistics.md` | `invokely-statistics` | Use Invokely MCP to find official statistics, retrieve values and series, compare or rank places, and report each figure with its period, unit, and source citation. |
| `ios-debugger-agent.md` | `ios-debugger-agent` | Debug the current iOS project on a booted simulator with XcodeBuildMCP. |
| `ios-developer.md` | `ios-developer` | Develop native iOS applications with Swift/SwiftUI. |
| `ios-flows.md` | `ios-flows` | Plan an iPhone app flow from how real apps handle it: onboarding, sign-up, paywalls, permissions, cancellation, account deletion and settings. |
| `ios-redteam-pipeline.md` | `ios-redteam-pipeline` | End-to-end iOS red-team pipeline |
| `ios-review.md` | `ios-review` | Review an iPhone app screen or flow and list what to fix, most important first: navigation, layout, touch targets, accessibility, states and App Store issues. |
| `ios-screens.md` | `ios-screens` | Build iPhone app screens that feel native: navigation, sheets, Dynamic Type, dark mode, permissions and paywalls, checked on small and large iPhones. |
| `iso27001-compliance.md` | `iso27001-compliance` | Implement ISO 27001 Information Security Management System. |
| `isometric-design.md` | `isometric-design` | Web and App implementation guide for Isometric Design. |
| `issue-grievance-tracker.md` | `issue-grievance-tracker` | Grievance register: issue type, raised by or anonymous, person or team concerned, department, date raised, policy reference, severity, assignee, action taken and status. |
| `issues.md` | `issues` | Interact with GitHub issues - create, list, and view issues. |
| `istio-traffic-management.md` | `istio-traffic-management` | Comprehensive guide to Istio traffic management for production service mesh deployments. |
| `it-manager-hospital.md` | `it-manager-hospital` | World-class Hospital IT Management Advisor specializing in clinical safety, digital maturity (HIMSS/ONA/JCI), and HIS/PEP ecosystems. |
| `it-manager-pro.md` | `it-manager-pro` | Elite IT Management Advisor specializing in data-driven strategy, executive communication, and human-centric leadership for the 2026 digital era. |
| `iterate-pr.md` | `iterate-pr` | Iterate on a PR until CI passes. |
| `itil-expert.md` | `itil-expert` | Expert advisor for ITIL 4 and ITIL 5 (2026 digital product paradigm), specialized in AI-native governance, sustainability, and value co-creation. |
| `java.md` | `java` | Language-specific super-code guidelines for java. |
| `java-pro.md` | `java-pro` | Master Java 21+ with modern features like virtual threads, pattern matching, and Spring Boot 3.x. |
| `javascript-mastery.md` | `javascript-mastery` | 33+ essential JavaScript concepts every developer should know, inspired by [33-js-concepts](https://github.com/leonardomso/33-js-concepts). |
| `javascript-pro.md` | `javascript-pro` | Master modern JavaScript with ES6+, async patterns, and Node.js APIs. |
| `javascript-testing-patterns.md` | `javascript-testing-patterns` | Comprehensive guide for implementing robust testing strategies in JavaScript/TypeScript applications using modern testing frameworks and best practices. |
| `javascript-typescript-typescript-scaffold.md` | `javascript-typescript-typescript-scaffold` | Scaffold TypeScript projects with build tooling, type checking, testing, and configuration. |
| `jenkins.md` | `jenkins` | Create and manage Jenkins CI/CD pipelines, configure agents, manage plugins, |
| `jest-skill.md` | `jest-skill` | Generates Jest unit and integration tests in JavaScript or TypeScript. |
| `jet-browser.md` | `jet-browser` | Verify or integrate Jet Browser when a project needs isolated WPE WebKit sessions, native input, screenshots, ordered JSONL automation, or reproducible runtime checks. |
| `jev-memory.md` | `jev-memory` | Set up an explicitly requested Claude Code memory mod using Treg and Jev, with informed consent for prompt transmission, recurring charges and local preference storage. |
| `jev-social.md` | `jev-social` | Run read-only, browser-grounded Instagram, TikTok, or LinkedIn research through Jev routing and socai CLI, returning source-linked evidence and reports. |
| `jobs-to-be-done-analyst.md` | `jobs-to-be-done-analyst` | Uncover the functional, emotional and social jobs a customer hires a product to do: progress state, hiring trigger, alternatives, success criteria, JTBD map. |
| `jq.md` | `jq` | Expert jq usage for JSON querying, filtering, transformation, and pipeline integration. |
| `js-reverse.md` | `js-reverse` | Front-end JavaScript reverse engineering: locate signature chains, analyze encrypted request parameters, sample runtime behavior, and reproduce logic locally in Node for evidence-based output. |
| `json-canvas.md` | `json-canvas` | Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, and connections. |
| `json-schema-manual.md` | `json-schema-manual` | JSON Schema Manual: draft 2020-12 validation schema from a confirmed field list, with required and enum values only where confirmed. |
| `julia-pro.md` | `julia-pro` | Master Julia 1.10+ with modern features, performance optimization, multiple dispatch, and production-ready practices. |
| `junit-5-skill.md` | `junit-5-skill` | Generates production-grade JUnit 5 unit and integration tests in Java. |
| `junta-leiloeiros.md` | `junta-leiloeiros` | Consulta e coleta assistida de registros públicos de leiloeiros nas 27 rotas estaduais; cobertura e atualidade exigem validação. |
| `k6-load-testing.md` | `k6-load-testing` | Comprehensive k6 load testing skill for API, browser, and scalability testing. |
| `k8s-manifest-generator.md` | `k8s-manifest-generator` | Step-by-step guidance for creating production-ready Kubernetes manifests including Deployments, Services, ConfigMaps, Secrets, and PersistentVolumeClaims. |
| `k8s-security-policies.md` | `k8s-security-policies` | Guide for NetworkPolicy, RBAC, and Pod Security Admission/Standards (PodSecurityPolicy was removed in Kubernetes1.25) in Kubernetes. |
| `kaizen.md` | `kaizen` | Guide for continuous improvement, error proofing, and standardization. |
| `keenable-search-mcp.md` | `keenable-search-mcp` | Search the public web with site and date filters, and read pages with an extraction prompt, through Keenable's keyless MCP server. |
| `keepmacawake.md` | `keepmacawake` | Keep a MacBook with Apple silicon awake with the lid closed during a long agent task, with the keepmacawake command of the Keep Mac Awake app. |
| `kernel-prompt.md` | `kernel-prompt` | Use when composing or improving an LLM prompt or agent instruction. |
| `keyword-clustering-tool.md` | `keyword-clustering-tool` | Keyword Clustering Tool. |
| `keyword-comparison-tool.md` | `keyword-comparison-tool` | Keyword Comparison Tool. |
| `keyword-density-checker.md` | `keyword-density-checker` | Keyword Density Checker. |
| `keyword-difficulty-estimator.md` | `keyword-difficulty-estimator` | Keyword Difficulty Estimator. |
| `keyword-expansion-tool.md` | `keyword-expansion-tool` | Keyword Expansion Tool. |
| `keyword-extractor.md` | `keyword-extractor` | Extracts up to 50 highly relevant SEO keywords from text. |
| `keyword-gap-finder.md` | `keyword-gap-finder` | Keyword Gap Finder. |
| `keyword-intent-identifier.md` | `keyword-intent-identifier` | Keyword Intent Identifier. |
| `keyword-placement-highlighter.md` | `keyword-placement-highlighter` | Keyword Placement Highlighter. |
| `keyword-roi-calculator.md` | `keyword-roi-calculator` | Keyword ROI Calculator. |
| `keyword-share-estimator.md` | `keyword-share-estimator` | Keyword Share Estimator. |
| `keyword-suggestion-tool.md` | `keyword-suggestion-tool` | Keyword Suggestion Tool. |
| `kimi-delegate.md` | `kimi-delegate` | Delegate coding tasks to the Kimi Code CLI (`kimi`) only when the user |
| `knowledge-base.md` | `knowledge-base` | Knowledge base register: article title, category, department, owner, tags, summary, linked SOP, audience, last and next review dates and status. |
| `kotler-macro-analyzer.md` | `kotler-macro-analyzer` | Professional PESTEL/SWOT analysis agent based on Kotler's methodology for strategic market audits. |
| `kotlin.md` | `kotlin` | Language-specific super-code guidelines for kotlin. |
| `kotlin-coroutines-expert.md` | `kotlin-coroutines-expert` | Expert patterns for Kotlin Coroutines and Flow, covering structured concurrency, error handling, and testing. |
| `kpi-dashboard-design.md` | `kpi-dashboard-design` | Comprehensive patterns for designing effective Key Performance Indicator (KPI) dashboards that drive business decisions. |
| `kpi-tracker.md` | `kpi-tracker` | KPI register: metric by level, department, job title and employee, linked OKR, unit and direction, target against actual, achievement and weight percentages, period and owner. |
| `kubernetes-architect.md` | `kubernetes-architect` | Expert Kubernetes architect specializing in cloud-native infrastructure, advanced GitOps workflows (ArgoCD/Flux), and enterprise container orchestration. |
| `kubernetes-deployment.md` | `kubernetes-deployment` | Kubernetes deployment workflow for container orchestration, Helm charts, service mesh, and production-ready K8s configurations. |
| `kubernetes-hardening.md` | `kubernetes-hardening` | Implement Kubernetes security contexts, Pod Security Standards, and network |
| `kubernetes-ops.md` | `kubernetes-ops` | Deploy, scale, and manage Kubernetes workloads. |
| `kubestellar-console.md` | `kubestellar-console` | Multi-cluster Kubernetes dashboard with AI-powered operations via MCP server and 10+ built-in agent skills |
| `kustomize.md` | `kustomize` | Customize Kubernetes manifests without templating using Kustomize. |
| `lambda-lang.md` | `lambda-lang` | Native agent-to-agent language for compact multi-agent messaging. |
| `landing-page.md` | `landing-page` | Build landing, home and pricing pages that look like a real product instead of AI output: honest copy, one design system, checked on phone and desktop. |
| `landing-page-design.md` | `landing-page-design` | Plan and build conversion-focused landing pages with intake, proof-based copy, explicit page structure, and the ELAYA visual system. |
| `landing-page-generator.md` | `landing-page-generator` | Generates high-converting Next.js/React landing pages with Tailwind CSS. |
| `langchain-architecture.md` | `langchain-architecture` | Master the LangChain framework for building sophisticated LLM applications with agents, chains, memory, and tool integration. |
| `langfuse.md` | `langfuse` | Expert in Langfuse - the open-source LLM observability platform. |
| `langgraph.md` | `langgraph` | Expert in LangGraph - the production-grade framework for building |
| `lanshu-create-ai-presenter-video.md` | `lanshu-create-ai-presenter-video` | Turn a topic or script into a publish-ready explainer video, led by an AI presenter or performed in one of twelve styled explainer looks. |
| `laravel-development-workflow.md` | `laravel-development-workflow` | Build and fix existing Laravel applications through root-cause diagnosis, repository-native implementation, regression coverage, and risk-based verification. |
| `laravel-expert.md` | `laravel-expert` | Senior Laravel Engineer role for production-grade, maintainable, and idiomatic Laravel solutions. |
| `laravel-security-audit.md` | `laravel-security-audit` | Security auditor for Laravel applications. |
| `last30days.md` | `last30days` | Research a topic from the last 30 days on Reddit + X + Web, summarize evidence, and write copy-paste-ready prompts for the user's target tool. |
| `latex-paper-conversion.md` | `latex-paper-conversion` | This skill should be used when the user asks to convert an academic paper in LaTeX from one format (e.g., Springer, IPOL) to another format (e.g., MDPI, IEEE, Nature). |
| `launch-check.md` | `launch-check` | Bounded pre-launch audit of a live URL for AI-built apps: exposed secret keys, open Supabase/Firebase tables, security headers, phone layout, search and speed. |
| `launch-strategy.md` | `launch-strategy` | You are an expert in SaaS product launches and feature announcements. |
| `layered-design.md` | `layered-design` | Web and App implementation guide for Layered Design. |
| `lead-magnets.md` | `lead-magnets` | Plan and optimize lead magnets for email capture and lead generation. |
| `learn.md` | `learn` | Help a user learn a topic through adaptive tutoring, lesson planning, practice, retrieval checks, explanations, study guides, or exercises. |
| `learning-career-development.md` | `learning-career-development` | Training register: course, provider, delivery method, department, employee, duration, progress percentage, score, mandatory flag, certificate earned and skills gained. |
| `leave-management.md` | `leave-management` | Leave register: request, leave type, employee and department, manager and approver, start and end dates, days requested, leave balances, handover notes and status. |
| `ledger-tasks-yylo.md` | `ledger-tasks-yylo` | 'Use YYLO Ledger task management: create, list, search, get, mark, update, |
| `legacy-modernizer.md` | `legacy-modernizer` | Refactor legacy codebases, migrate outdated frameworks, and implement gradual modernization. |
| `legal-advisor.md` | `legal-advisor` | Draft privacy policies, terms of service, disclaimers, and legal notices. |
| `legal-compliance-vault.md` | `legal-compliance-vault` | Legal and compliance document vault: document type, framework, owner and department, effective and expiry dates, renewal flag, storage link, confidentiality and status. |
| `leiloeiro-avaliacao.md` | `leiloeiro-avaliacao` | Organize evidence and indicative valuation scenarios for auction properties, with explicit market, method and professional-review limits. |
| `leiloeiro-edital.md` | `leiloeiro-edital` | Analise e auditoria de editais de leilao judicial e extrajudicial. |
| `leiloeiro-ia.md` | `leiloeiro-ia` | Especialista em leiloes judiciais e extrajudiciais de imoveis. |
| `leiloeiro-juridico.md` | `leiloeiro-juridico` | Analise juridica de leiloes: nulidades, bem de familia, alienacao fiduciaria, CPC arts 829-903, Lei 9514/97, onus reais, embargos e jurisprudencia. |
| `leiloeiro-mercado.md` | `leiloeiro-mercado` | Analise de mercado imobiliario para leiloes. |
| `leiloeiro-risco.md` | `leiloeiro-risco` | Analise de risco em leiloes de imoveis. |
| `lemmaly.md` | `lemmaly` | Algorithm-first discipline: state Big-O, data structure, and algorithm family BEFORE writing loops, queries, or recursion. |
| `lesson-generator.md` | `lesson-generator` | Build compact, standalone multi-lesson course artifacts with lesson navigation, objectives, flashcards, quizzes, and source links. |
| `lex.md` | `lex` | Structured research aid for cross-jurisdictional legal context (US, EU, CA) and contract scaffolding. |
| `lightning-architecture-review.md` | `lightning-architecture-review` | Review Bitcoin Lightning Network protocol designs, compare channel factory approaches, and analyze Layer 2 scaling tradeoffs. |
| `lightning-channel-factories.md` | `lightning-channel-factories` | Technical reference on Lightning Network channel factories, multi-party channels, LSP architectures, and Bitcoin Layer 2 scaling without soft forks. |
| `lightning-factory-explainer.md` | `lightning-factory-explainer` | Explain Bitcoin Lightning channel factories and the SuperScalar protocol — scalable Lightning onboarding using shared UTXOs, Decker-Wattenhofer trees, timeout-signature trees, MuSig2, and Taproot. |
| `lightweight-charts-react-components.md` | `lightweight-charts-react-components` | Build and debug React financial charts with realtime candles, viewport-preserving history, indicator panes, markers, and chart API refs using lightweight-charts-react-components. |
| `linear-claude-skill.md` | `linear-claude-skill` | Manage Linear issues, projects, and teams |
| `link-relevance-evaluator.md` | `link-relevance-evaluator` | Link Relevance Evaluator. |
| `link-source-categorizer.md` | `link-source-categorizer` | Link Source Categorizer. |
| `link-toxicity-checker.md` | `link-toxicity-checker` | Link Toxicity Checker. |
| `linkedin-cli.md` | `linkedin-cli` | Use when automating LinkedIn via CLI: fetch profiles, search people/companies, send messages, manage connections, create posts, and Sales Navigator. |
| `linkedin-content-generator.md` | `linkedin-content-generator` | AI-powered LinkedIn content suite: generate posts, carousels, newsletters, and 30-day calendars with niche-specific SEO rules and a feedback-based personal memory system. |
| `linkedin-post-writer.md` | `linkedin-post-writer` | Draft LinkedIn posts from 16 illustrative hook formulas mapped to engagement goals (comments, reposts, likes, saves), with optional formatting conventions and an AI-tell scrub pass before publishing. |
| `linkedin-profile-optimizer.md` | `linkedin-profile-optimizer` | High-intent expert for LinkedIn profile checks and SEO optimization. |
| `linkerd-patterns.md` | `linkerd-patterns` | Production patterns for Linkerd service mesh - the lightweight, security-first service mesh for Kubernetes. |
| `linktree-link-hub.md` | `linktree-link-hub` | Link-in-bio register: label, destination URL, link type, priority order, audience, click tracking, UTM source, schedule, click count and status. |
| `lint-and-validate.md` | `lint-and-validate` | Run configured lint and type checks, distinguish failures from checks that did not run, and report concrete validation results. |
| `lintlang-audit.md` | `lintlang-audit` | Audit named agent instructions, tool definitions, and supported Python prompts with local LintLang checks; return finding codes and locations without changing files. |
| `linux-administration.md` | `linux-administration` | System administration for Linux servers. |
| `linux-hardening.md` | `linux-hardening` | Apply CIS benchmarks and secure Linux servers. |
| `linux-privilege-escalation.md` | `linux-privilege-escalation` | Execute systematic privilege escalation assessments on Linux systems to identify and exploit misconfigurations, vulnerable services, and security weaknesses that allow elevation from low-privilege user access to root-level control. |
| `linux-shell-scripting.md` | `linux-shell-scripting` | Provide production-ready shell script templates for common Linux system administration tasks including backups, monitoring, user management, log analysis, and automation. |
| `linux-troubleshooting.md` | `linux-troubleshooting` | Linux system troubleshooting workflow for diagnosing and resolving system issues, performance problems, and service failures. |
| `liuguang-banlan-ui.md` | `liuguang-banlan-ui` | Builds two parameterized UI modes—流光溢彩白 (iridescent white) and 五彩斑斓黑 (colorful black)—with OKLCH, WebGL/CSS fallback, vision gating, screenshot QA, and total/per-color intensity reports. |
| `llm-app-patterns.md` | `llm-app-patterns` | Architecture and integration sketches for LLM applications, with explicit retrieval, tool, privacy and verification boundaries. |
| `llm-app-security.md` | `llm-app-security` | Secure LLM-powered applications with input validation, output controls, |
| `llm-application-dev-ai-assistant.md` | `llm-application-dev-ai-assistant` | Design and implement conversational AI assistants with context management, integration boundaries, and validation. |
| `llm-application-dev-langchain-agent.md` | `llm-application-dev-langchain-agent` | You are an expert LangChain agent developer specializing in production-grade AI systems using LangChain 0.1+ and LangGraph. |
| `llm-application-dev-prompt-optimize.md` | `llm-application-dev-prompt-optimize` | Improve LLM prompts using task-specific evaluation, structured instructions, and regression checks. |
| `llm-caching.md` | `llm-caching` | Implement multi-layer LLM caching with exact match, semantic similarity, |
| `llm-cost-optimization.md` | `llm-cost-optimization` | Reduce LLM API and infrastructure costs through model selection, prompt |
| `llm-council.md` | `llm-council` | Run Fireworks-hosted open-weight model councils that compare responses and synthesize a final answer. |
| `llm-evaluation.md` | `llm-evaluation` | Master comprehensive evaluation strategies for LLM applications, from automated metrics to human evaluation and A/B testing. |
| `llm-ops.md` | `llm-ops` | LLM Operations -- RAG, embeddings, vector databases, fine-tuning, prompt engineering avancado, custos de LLM, evals de qualidade e arquiteturas de IA para producao. |
| `llm-prompt-optimizer.md` | `llm-prompt-optimizer` | Use when improving prompts for any LLM. |
| `llm-security.md` | `llm-security` | Authorized security assessment of LLM applications and AI agents: prompt injection, tool abuse, RAG exposure, memory poisoning, system-prompt extraction, and agent-compliance engineering per OWASP LLM/ASI Top 10. |
| `llm-structured-output.md` | `llm-structured-output` | Get reliable JSON, enums, and typed objects from LLMs using response_format, tool_use, and schema-constrained decoding across OpenAI, Anthropic, and Google APIs. |
| `llmops-platform-engineering.md` | `llmops-platform-engineering` | Build production LLMOps platforms with CI/CD, model promotion workflows, |
| `load-balancing.md` | `load-balancing` | Configure load balancers and traffic distribution. |
| `local-citation-finder.md` | `local-citation-finder` | Local Citation Finder. |
| `local-keyword-generator.md` | `local-keyword-generator` | Local Keyword Generator. |
| `local-legal-seo-audit.md` | `local-legal-seo-audit` | Audit and improve local SEO for law firms, attorneys, forensic experts and legal/professional services sites with local presence, focusing on GBP, directories, E-E-A-T and practice/location pages. |
| `local-llm-expert.md` | `local-llm-expert` | Master local LLM inference, model selection, VRAM optimization, and local deployment using Ollama, llama.cpp, vLLM, and LM Studio. |
| `local-schema-builder.md` | `local-schema-builder` | Local Schema Builder. |
| `local-seo-audit-checklist.md` | `local-seo-audit-checklist` | Local SEO Audit Checklist. |
| `location-based-content-idea-generator.md` | `location-based-content-idea-generator` | Local Content Idea Generator. |
| `logic-diff.md` | `logic-diff` | Compare two code versions for semantic equivalence via semi-formal tracing of both versions side-by-side. |
| `logic-explain.md` | `logic-explain` | Explain what a specific piece of code actually does for a given input by producing a step-by-step execution trace (interprocedural, with name resolution and type transitions). |
| `logic-fix-all.md` | `logic-fix-all` | Autonomous repository-wide audit-and-fix pipeline: health → review → locate/explain → fix → diff-verify → iterate until clean. |
| `logic-lens.md` | `logic-lens` | AI-powered Claude Code skill that performs deep code review using formal logic and reasoning frameworks to detect bugs, anti-patterns, and security risks beyond what linters catch. |
| `logic-locate.md` | `logic-locate` | Locate the root cause of a CONFIRMED failure via backward-then-forward semi-formal tracing. |
| `logic-review.md` | `logic-review` | Find logic bugs in a single file or function via semi-formal execution tracing (Premises → Trace → Divergence → Trigger → Remedy). |
| `logistics-exception-management.md` | `logistics-exception-management` | Triage freight delays, damage, shortages, loss and carrier disputes; prepare evidence, recovery options and communications with jurisdiction-specific review. |
| `lognorm.md` | `lognorm` | Work a site's SEO and AI-visibility (GEO) backlog through the hosted LogNorm MCP server: audits, fixes, content, AI-answer tracking. |
| `logo-image-design.md` | `logo-image-design` | Brand asset register: asset type, format, dimensions and aspect ratio, colour mode, background variant, clear space, approved and prohibited uses, rights owner and licence. |
| `logo-to-stickers.md` | `logo-to-stickers` | Turn a brand mark or existing IP into consistent, playful paper stickers with small visual stories and separate transparent images. |
| `loki-logging.md` | `loki-logging` | Configure Grafana Loki for log aggregation and analysis. |
| `loki-mode.md` | `loki-mode` | Historical 2.35.x multi-agent workflow for turning a scoped PRD into reviewed implementation; includes experimental runner and benchmark artifacts. |
| `long-tail-keyword-generator.md` | `long-tail-keyword-generator` | Long-Tail Keyword Generator. |
| `longbridge.md` | `longbridge` | Guide to using a separately installed Longbridge integration — real-time quotes, charts, fundamentals, portfolio analysis, options, and more for HK/US/A-share/SG markets. |
| `longbridge-content.md` | `longbridge-content` | Latest news articles, regulatory filings, community discussion topics for listed stocks, and SEC EDGAR filing analysis (10-K/10-Q/8-K/proxy/Form 4) via Longbridge. |
| `longbridge-derivatives.md` | `longbridge-derivatives` | Curated upstream guidance for Longbridge Derivatives; use when the workflow matches the user goal. |
| `longbridge-fundamentals.md` | `longbridge-fundamentals` | Financial statements, business segments, dividends, valuation multiples (PE/PB/PS), industry comparison, operating data, corporate actions, company and executive profiles, cross-stock comparison, and valuation ranking via Longbridge. |
| `longbridge-market-data.md` | `longbridge-market-data` | Real-time quotes, K-line charts, order book, trade ticks, intraday capital flow, market sentiment temperature, trading session schedule, security lists, exchange rates, and IPO calendar for HK/US/A-share/SG via Longbridge. |
| `longbridge-quant.md` | `longbridge-quant` | Curated upstream guidance for Longbridge Quant; use when the workflow matches the user goal. |
| `longbridge-research.md` | `longbridge-research` | Curated upstream guidance for Longbridge Research; use when the workflow matches the user goal. |
| `lookdev.md` | `lookdev` | Human-in-the-loop web studio to tune AI-generated output by eye. |
| `lookdev-auto.md` | `lookdev-auto` | Automated visual tuning: a vision or video model rates rendered variants in a loop. |
| `looot.md` | `looot` | Search, price and run 2,500+ data API endpoints (work emails, company search, SERP, web pages) from one prepaid balance via the looot MCP server. |
| `loop-library.md` | `loop-library` | Find, compare, adapt, and design bounded AI-agent feedback loops with explicit checks, stop rules, guardrails, and handoffs. |
| `loopy.md` | `loopy` | Discover, find, compare, audit, repair, adapt, craft, run, debrief, and prepare repeatable AI-agent loops for publication. |
| `lore.md` | `lore` | Markdown project memory for AI agents. |
| `loss-aversion-designer.md` | `loss-aversion-designer` | Compare gain and loss framing and describe credible costs of inaction when an offer needs urgency without fearmongering. |
| `lovable-cleanup.md` | `lovable-cleanup` | Audits and strips Lovable scaffolding from Vite + React projects — removes lovable-tagger, swaps placeholder assets, prunes unused Radix deps, cleans generated docs, and neutralizes stale favicon/CDN caching so the codebase ships as yours. |
| `luna.md` | `luna` | Reviews code for objective correctness, security, and reliability. |
| `m365-agents-dotnet.md` | `m365-agents-dotnet` | Microsoft 365 Agents SDK for .NET. |
| `m365-entra-attack.md` | `m365-entra-attack` | Microsoft 365 / Entra ID red-team attack chain |
| `mac-api-connection-diagnostics.md` | `mac-api-connection-diagnostics` | Diagnose an API or website connection failure from a Mac with Kilobat's read-only JSON probes before changing application code or network settings. |
| `mac-mini-llm-lab.md` | `mac-mini-llm-lab` | Configure a Mac mini as a reliable local LLM server with remote access, |
| `machine-learning-ops-ml-pipeline.md` | `machine-learning-ops-ml-pipeline` | Design and implement a complete ML pipeline for: $ARGUMENTS |
| `macos-menubar-tuist-app.md` | `macos-menubar-tuist-app` | Build, refactor, or review SwiftUI macOS menubar apps that use Tuist. |
| `macos-reverse.md` | `macos-reverse` | Authorized macOS and Mach-O reverse engineering: codesign inspection, Objective-C/Swift recovery, endpoint-security surfaces, and Apple-platform malware analysis. |
| `macos-screen-recorder.md` | `macos-screen-recorder` | macOS screen recorder that captures the main display PLUS system audio via ScreenCaptureKit — no BlackHole/loopback driver, no sudo, just the standard Screen Recording permission. |
| `macos-spm-app-packaging.md` | `macos-spm-app-packaging` | Scaffold, build, sign, and package SwiftPM macOS apps without Xcode projects. |
| `magic-animator.md` | `magic-animator` | AI-powered animation tool for creating motion in logos, UI, icons, and social media assets. |
| `magic-ui-generator.md` | `magic-ui-generator` | Utilizes Magic by 21st.dev to generate, compare, and integrate multiple production-ready UI component variations. |
| `maintain-codex-wiki.md` | `maintain-codex-wiki` | Maintain a review-first engineering wiki with provenance, citation-aware queries, explicit capture and promotion, and deterministic checks. |
| `make-ugc.md` | `make-ugc` | Create original AI UGC-style product videos through Treg: research hooks, approve a licensed presenter and voice, generate clips, add captions and report costs. |
| `makepad-2-0-animation.md` | `makepad-2-0-animation` | Makepad 2.0 guidance for animation; use when building or debugging Makepad UI code. |
| `makepad-2-0-dsl.md` | `makepad-2-0-dsl` | Makepad 2.0 guidance for dsl; use when building or debugging Makepad UI code. |
| `makepad-2-0-events.md` | `makepad-2-0-events` | Makepad 2.0 guidance for events; use when building or debugging Makepad UI code. |
| `makepad-2-0-layout.md` | `makepad-2-0-layout` | Makepad 2.0 guidance for layout; use when building or debugging Makepad UI code. |
| `makepad-2-0-widgets.md` | `makepad-2-0-widgets` | Makepad 2.0 guidance for widgets; use when building or debugging Makepad UI code. |
| `makepad-animation.md` | `makepad-animation` | CRITICAL: Use for Makepad animation system. |
| `makepad-basics.md` | `makepad-basics` | CRITICAL: Use for Makepad getting started and app structure. |
| `makepad-deployment.md` | `makepad-deployment` | CRITICAL: Use for Makepad packaging and deployment. |
| `makepad-dsl.md` | `makepad-dsl` | CRITICAL: Use for Makepad DSL syntax and inheritance. |
| `makepad-event-action.md` | `makepad-event-action` | CRITICAL: Use for Makepad event and action handling. |
| `makepad-font.md` | `makepad-font` | CRITICAL: Use for Makepad font and text rendering. |
| `makepad-layout.md` | `makepad-layout` | CRITICAL: Use for Makepad layout system. |
| `makepad-platform.md` | `makepad-platform` | CRITICAL: Use for Makepad cross-platform support. |
| `makepad-reference.md` | `makepad-reference` | Guide to diagnosing Makepad build, widget, redraw and layout issues against the exact runtime revision. |
| `makepad-shaders.md` | `makepad-shaders` | CRITICAL: Use for Makepad shader system. |
| `makepad-skills.md` | `makepad-skills` | Makepad UI development skills for Rust apps: setup, patterns, shaders, packaging, and troubleshooting. |
| `makepad-splash.md` | `makepad-splash` | CRITICAL: Use for Makepad Splash scripting language. |
| `makepad-widgets.md` | `makepad-widgets` | Select and compose Makepad widgets, configure their properties and styling, and debug widget behavior against a pinned makepad-widgets version. |
| `malware-analysis.md` | `malware-analysis` | Analyze suspected malware through static, dynamic, and behavioral techniques: IOC extraction, YARA/Sigma rule authoring, sandbox orchestration, and anti-analysis detection. |
| `malware-analyst.md` | `malware-analyst` | Expert malware analyst specializing in defensive malware research, threat intelligence, and incident response. |
| `manage-skills.md` | `manage-skills` | Discover, list, create, edit, toggle, copy, move, and delete AI agent skills across 11 tools (Cursor, Claude, Agents, Windsurf, Copilot, Codex, Cline, Aider, Continue, Roo Code, Augment) |
| `manifest.md` | `manifest` | Install and configure the Manifest observability plugin for your agents. |
| `markdown-rendering.md` | `markdown-rendering` | Open Markdown reliably in cmux panes and recover from blank rendered surfaces. |
| `market-sizing-analysis.md` | `market-sizing-analysis` | Comprehensive market sizing methodologies for calculating Total Addressable Market (TAM), Serviceable Available Market (SAM), and Serviceable Obtainable Market (SOM) for startup opportunities. |
| `marketing-ideas.md` | `marketing-ideas` | Provide proven marketing strategies and growth ideas for SaaS and software products, prioritized using a marketing feasibility scoring system. |
| `marketing-mindset.md` | `marketing-mindset` | Use when a user asks how to win first customers, whether doing X will produce Y, how to write an ad or judge a marketing test — a marketer's decision framework, not a tactic library. |
| `marketing-plan.md` | `marketing-plan` | When the user needs a comprehensive marketing plan for a client, a company they advise, or their own product. |
| `marketing-psychology.md` | `marketing-psychology` | Apply behavioral science and mental models to marketing decisions, prioritized using a psychological leverage and feasibility scoring system. |
| `marketplace-rbac-audit.md` | `marketplace-rbac-audit` | Audit multi-role marketplace authorization across roles, resource ownership, tenant boundaries, and order-state transitions; use when access rules need evidence, not UI assumptions. |
| `markstream-angular.md` | `markstream-angular` | Integrate the alpha markstream-angular renderer into Angular 20+ applications with standalone components, signals, safe HTML defaults, and optional peer features. |
| `markstream-custom-components.md` | `markstream-custom-components` | Override Markstream node renderers and add trusted custom tags across Vue, React, Svelte, and Angular using scoped or renderer-local mappings. |
| `markstream-install.md` | `markstream-install` | Install and configure Markstream streaming Markdown renderers for Vue, React, Svelte, Angular, Nuxt, Next.js, and Vue 2 applications. |
| `markstream-migration.md` | `markstream-migration` | Audit and migrate an existing Markdown renderer to Markstream while preserving custom renderers, security policy, streaming behavior, and explicit parity gaps. |
| `markstream-nuxt.md` | `markstream-nuxt` | Integrate markstream-vue into Nuxt 3 or 4 with SSR-safe client boundaries, renderer modes, explicit CSS, and browser-only optional peers. |
| `markstream-react.md` | `markstream-react` | Integrate the beta markstream-react renderer into React 18+ or Next.js with correct client/server entrypoints, CSS, streaming state, and component overrides. |
| `markstream-svelte.md` | `markstream-svelte` | Integrate the beta markstream-svelte renderer into Svelte 5 or SvelteKit with runes, explicit CSS, smooth streaming, workers, and SSR-safe boundaries. |
| `markstream-vue.md` | `markstream-vue` | Integrate markstream-vue into plain Vue 3 with renderer modes, code and DOM choices, streaming state, virtualization, optional peers, and scoped components. |
| `markstream-vue2.md` | `markstream-vue2` | Integrate markstream-vue2 into Vue 2.6 or 2.7 with correct Composition API decisions, CSS, streaming state, optional peers, and scoped overrides. |
| `markstream-vue2-cli.md` | `markstream-vue2-cli` | Integrate markstream-vue2 into Vue CLI or Webpack 4 with export-map-safe CSS, CDN worker fallbacks, and conservative code-block defaults. |
| `markstream-vue2-vite.md` | `markstream-vue2-vite` | Integrate markstream-vue2 into Vue 2 plus Vite with bundled worker imports, CSS ordering, Composition API compatibility, and safe streaming defaults. |
| `marlin-bed-leveling.md` | `marlin-bed-leveling` | Calibrates Marlin 2.x 3D printer firmware bed leveling: Unified Bed Leveling (UBL), Bilinear ABL, M420 S1 post-homing, Z-probe offsets, G26 mesh prints, and EEPROM slots. |
| `mason.md` | `mason` | Produces clean, functional code that matches the architecture and checklists. |
| `matematico-tao.md` | `matematico-tao` | Analyze code complexity, dependency graphs, concurrency and invariants using explicit mathematical assumptions. |
| `material-design.md` | `material-design` | Web and App implementation guide for Material Design. |
| `mathguard.md` | `mathguard` | Math-heavy escalation for n >= 10^6 — Bloom, HyperLogLog, Count-Min, MinHash/LSH, FFT, JL projection, sweep line. |
| `matplotlib.md` | `matplotlib` | Matplotlib is Python's foundational visualization library for creating static, animated, and interactive plots. |
| `max.md` | `max` | Cleans up and improves existing code without changing behavior. |
| `maxia.md` | `maxia` | Connect to MAXIA AI-to-AI marketplace on Solana. |
| `maximalism.md` | `maximalism` | Web and App implementation guide for Controlled Maximalism. |
| `mcd-secret-menu-lab.md` | `mcd-secret-menu-lab` | Plan McDonald's China recipe combinations using an authorized MCP connection for current store menus, prices and nutrition. |
| `mcp-builder.md` | `mcp-builder` | Create MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. |
| `mcp-builder-ms.md` | `mcp-builder-ms` | Use this skill when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK). |
| `mcp-dependency-drift-audit.md` | `mcp-dependency-drift-audit` | Statically audit MCP configs for mutable npm/npx package references before approval or CI, without executing discovered MCP servers. |
| `mcp-server-security.md` | `mcp-server-security` | Secure Model Context Protocol (MCP) servers with transport encryption, |
| `mcp-tool-developer.md` | `mcp-tool-developer` | Build Model Context Protocol (MCP) servers and tools from scratch. |
| `md2video-audio.md` | `md2video-audio` | Convert Markdown documents into narrated MP4 videos with synchronized visuals and voice narration. |
| `mdm-device-management.md` | `mdm-device-management` | Manage and secure company devices with MDM solutions |
| `mdpr-skill.md` | `mdpr-skill` | Review MDPR Markdown presentation workflows with semantic hints, visual checks, and deterministic renderer boundaries. |
| `media-use.md` | `media-use` | Resolve and prepare licensed media, voice, music, captions and sound for HyperFrames with explicit provider and cost boundaries. |
| `meeting-distiller-pro.md` | `meeting-distiller-pro` | Transform messy meeting notes and transcripts into structured action |
| `meeting-notes.md` | `meeting-notes` | Turns raw meeting notes into structured minutes: conclusion first, then decisions / action items / open questions; every action item must have an owner and a deadline. |
| `meme-coin-audit.md` | `meme-coin-audit` | Meme coin and token security audit |
| `memory-forensics.md` | `memory-forensics` | Comprehensive techniques for acquiring, analyzing, and extracting artifacts from memory dumps for incident response and malware analysis. |
| `memory-handoff.md` | `memory-handoff` | Portable session handoff across agent CLIs: read a project's handoff file at session start, rewrite it at session end, so the next session starts mid-thought instead of cold. |
| `memory-safety-patterns.md` | `memory-safety-patterns` | Cross-language patterns for memory-safe programming including RAII, ownership, smart pointers, and resource management. |
| `memory-systems.md` | `memory-systems` | Design short-term, long-term, and graph-based memory architectures. |
| `mental-health-analyzer.md` | `mental-health-analyzer` | 分析心理健康数据、识别心理模式、评估心理健康状况、提供个性化心理健康建议。支持与睡眠、运动、营养等其他健康数据的关联分析。 |
| `mentorship-program.md` | `mentorship-program` | Mentorship register: mentor and mentee pair, department, focus area, mentee goal, session counts, last and next session, overall rating, progress notes and status. |
| `mercury-mcp.md` | `mercury-mcp` | Cheatsheet for the Mercury (proton) MCP tools. |
| `mermaid-expert.md` | `mermaid-expert` | Create Mermaid diagrams for flowcharts, sequences, ERDs, and architectures. |
| `mesh-memory.md` | `mesh-memory` | Self-hosted semantic memory for AI agents via MCP. |
| `meta-description-optimizer.md` | `meta-description-optimizer` | Meta Description Optimizer. |
| `meta-description-writer.md` | `meta-description-writer` | Meta Description Writer. |
| `meta-tag-comparison-tool.md` | `meta-tag-comparison-tool` | Meta Tag Comparison Tool. |
| `meta-tag-generator.md` | `meta-tag-generator` | Meta Tag Generator. |
| `metasploit-framework.md` | `metasploit-framework` | ⚠️ AUTHORIZED USE ONLY > This skill is for educational purposes or authorized security assessments only. |
| `meteora-dlmm-pool-screening.md` | `meteora-dlmm-pool-screening` | Screen and rank Meteora DLMM pools for LP quality using public Meteora APIs (fee/TVL, bin step, organic score). |
| `micro-saas-launcher.md` | `micro-saas-launcher` | Expert in launching small, focused SaaS products fast - the indie |
| `microservices-patterns.md` | `microservices-patterns` | Master microservices architecture patterns including service boundaries, inter-service communication, data management, and resilience patterns for building distributed systems. |
| `microsoft-azure-webjobs-extensions-authentication-events-dotnet.md` | `microsoft-azure-webjobs-extensions-authentication-events-dotnet` | Microsoft Entra Authentication Events SDK for .NET. |
| `mid-engagement-ir-detection.md` | `mid-engagement-ir-detection` | Methodology for detecting client SOC patches, attacker activity, and |
| `minecraft-bukkit-pro.md` | `minecraft-bukkit-pro` | Master Minecraft server plugin development with Bukkit, Spigot, and Paper APIs. |
| `minicut-film-studio.md` | `minicut-film-studio` | Install and use the official MiniCut film studio skill, pinned by commit, to make multi-shot AI short films with the paid MiniCut CLI. |
| `minimalism.md` | `minimalism` | Web and App implementation guide for the Minimalism design style. |
| `minimalist-ui.md` | `minimalist-ui` | Use when creating clean editorial interfaces with warm monochrome palettes, crisp borders, restrained motion, and flat bento layouts. |
| `mirrord.md` | `mirrord` | Run a local process inside a live Kubernetes cluster's network, env and traffic with mirrord, so changes are tested against real services without deploying. |
| `mise-configurator.md` | `mise-configurator` | Generate production-ready mise.toml setups for local development, CI/CD pipelines, and toolchain standardization. |
| `ml-engineer.md` | `ml-engineer` | Build production ML systems with PyTorch 2.x, TensorFlow, and modern ML frameworks. |
| `ml-pipeline-workflow.md` | `ml-pipeline-workflow` | Complete end-to-end MLOps pipeline orchestration from data preparation through model deployment. |
| `mlops-engineer.md` | `mlops-engineer` | Build comprehensive ML pipelines, experiment tracking, and model registries with MLflow, Kubeflow, and modern MLOps tools. |
| `mmx-cli.md` | `mmx-cli` | Use mmx to generate text, images, video, speech, and music via the MiniMax AI platform. |
| `moatmri.md` | `moatmri` | Analyze AI disruption pressure across a business, map competitive exposure, and produce a 90-day defensive action plan. |
| `mobbin.md` | `mobbin` | Find real app screens, user flows and website sections on Mobbin through the Mobbin MCP server, to ground UI design and code in shipped products. |
| `mobile-design.md` | `mobile-design` | Design and review iOS, Android, React Native or Flutter interfaces for touch, accessibility, navigation, offline behavior and measured performance. |
| `mobile-developer.md` | `mobile-developer` | Develop React Native, Flutter, or native mobile apps with modern architecture patterns. |
| `mobile-friendly-test.md` | `mobile-friendly-test` | Mobile-Friendly Test. |
| `mobile-games.md` | `mobile-games` | Mobile game development principles. |
| `mobile-native.md` | `mobile-native` | Improve mobile web behavior for touch, viewport sizing, safe areas, inputs, scrolling, and native-feeling interaction. |
| `mobile-reverse.md` | `mobile-reverse` | Authorized Android/iOS application reverse engineering and security testing: APK/IPA analysis, runtime instrumentation (Frida/Objection), SSL-pinning and jailbreak/root-detection bypass, per OWASP MASTG. |
| `mobile-security-coder.md` | `mobile-security-coder` | Expert in secure mobile coding practices specializing in input validation, WebView security, and mobile-specific security patterns. |
| `mock-hunter.md` | `mock-hunter` | Audit a live web page in five phases (catalog, click, trace, classify, report) to identify mock data, hardcoded values, LLM-generated metrics, and broken endpoints. |
| `model-supply-chain-security.md` | `model-supply-chain-security` | Secure the AI model supply chain with artifact signing, provenance attestation, |
| `modern-javascript-patterns.md` | `modern-javascript-patterns` | Comprehensive guide for mastering modern JavaScript (ES6+) features, functional programming patterns, and best practices for writing clean, maintainable, and performant code. |
| `moltnode-chain-reader.md` | `moltnode-chain-reader` | Read 31 blockchains over keyless JSON-RPC with MoltNode (balances, blocks, contract calls) and get Chord swap quotes with an unsigned transaction and simulation. |
| `molykit.md` | `molykit` | CRITICAL: Use for MolyKit AI chat toolkit. |
| `mongodb.md` | `mongodb` | Administer MongoDB databases. |
| `monochromatic-ui.md` | `monochromatic-ui` | Web and App implementation guide for Monochromatic UI. |
| `monopoly.md` | `monopoly` | MONOPOLY is a Senior System Design Engineer skill for architecting, reviewing, and scaling systems. |
| `monorepo-architect.md` | `monorepo-architect` | Expert in monorepo architecture, build systems, and dependency management at scale. |
| `monorepo-management.md` | `monorepo-management` | Build efficient, scalable monorepos that enable code sharing, consistent tooling, and atomic changes across multiple packages and applications. |
| `monte-carlo-analyze-root-cause.md` | `monte-carlo-analyze-root-cause` | Curated upstream guidance for Monte Carlo Analyze Root Cause; use when the workflow matches the user goal. |
| `monte-carlo-asset-health.md` | `monte-carlo-asset-health` | Curated upstream guidance for Monte Carlo Asset Health; use when the workflow matches the user goal. |
| `monte-carlo-context-detection.md` | `monte-carlo-context-detection` | Route data-related requests to the right Monte Carlo skill or workflow. |
| `monte-carlo-monitor-creation.md` | `monte-carlo-monitor-creation` | Guides creation of Monte Carlo monitors via MCP tools, producing monitors-as-code YAML for CI/CD deployment. |
| `monte-carlo-monitoring-advisor.md` | `monte-carlo-monitoring-advisor` | Analyze data coverage, create monitors for warehouse tables and AI agents. |
| `monte-carlo-performance-diagnosis.md` | `monte-carlo-performance-diagnosis` | Diagnoses pipeline performance issues -- slow jobs, expensive queries, latency trends -- using Monte Carlo's cross-platform observability. |
| `monte-carlo-prevent.md` | `monte-carlo-prevent` | Surfaces Monte Carlo data observability context (table health, alerts, lineage, blast radius) before SQL/dbt edits. |
| `monte-carlo-push-ingestion.md` | `monte-carlo-push-ingestion` | Review and adapt warehouse metadata, lineage and query-log collection templates for an explicitly authorized Monte Carlo destination. |
| `monte-carlo-remediation.md` | `monte-carlo-remediation` | Investigate and remediate data quality alerts using Monte Carlo MCP tools. |
| `monte-carlo-storage-cost-analysis.md` | `monte-carlo-storage-cost-analysis` | Analyze a warehouse for stale, unused, or redundant tables via the analyze_storage_costs MCP tool. |
| `monte-carlo-validation-notebook.md` | `monte-carlo-validation-notebook` | Generates SQL validation notebooks for dbt PR changes with before/after comparison queries. |
| `monthly-closing-statements.md` | `monthly-closing-statements` | Monthly closing register: period dates, cash/bank/party/inventory/TDS reconciliation flags, profit, receivables, payables, working capital, open adjustments and reviewer. |
| `moodle-external-api-development.md` | `moodle-external-api-development` | This skill guides you through creating custom external web service APIs for Moodle LMS, following Moodle's external API framework and coding standards. |
| `movie-coupon.md` | `movie-coupon` | Fetch movie ticket coupons from platforms like Taopiaopiao and Maoyan. |
| `moyu.md` | `moyu` | Anti-over-engineering guardrail that activates when an AI coding agent expands scope, adds abstractions, or changes files the user did not request. |
| `mtls-configuration.md` | `mtls-configuration` | Configure mutual TLS (mTLS) for zero-trust service-to-service communication. |
| `multi-advisor.md` | `multi-advisor` | Conselho de especialistas — consulta multiplos agentes do ecossistema em paralelo para analise multi-perspectiva de qualquer topico. |
| `multi-agent-architect.md` | `multi-agent-architect` | Design and optimize production-grade multi-agent systems with LangGraph, LangChain, and DeepAgents for complex AI workflows. |
| `multi-agent-brainstorming.md` | `multi-agent-brainstorming` | Simulate a structured peer-review process using multiple specialized agents to validate designs, surface hidden assumptions, and identify failure modes before implementation. |
| `multi-agent-patterns.md` | `multi-agent-patterns` | This skill should be used when the user asks to "design multi-agent system", "implement supervisor pattern", "create swarm architecture", "coordinate multiple agents", or mentions multi-agent patterns, context isolation, agent handoffs, sub-agents, or parallel agent execution. |
| `multi-agent-task-orchestrator.md` | `multi-agent-task-orchestrator` | Route tasks to specialized AI agents with anti-duplication, quality gates, and 30-minute heartbeat monitoring |
| `multi-cloud-architecture.md` | `multi-cloud-architecture` | Decision framework and patterns for architecting applications across AWS, Azure, and GCP. |
| `multi-platform-apps-multi-platform.md` | `multi-platform-apps-multi-platform` | Build and deploy the same feature consistently across web, mobile, and desktop platforms using API-first architecture and parallel implementation strategies. |
| `multi-source-search.md` | `multi-source-search` | Cross-validate web research and produce an offline-checkable evidence ledger with explicit source diversity, confidence, conflicts, and gaps. |
| `multi-tenant-llm-hosting.md` | `multi-tenant-llm-hosting` | Design secure, multi-tenant LLM hosting platforms with tenant isolation, |
| `multiplayer.md` | `multiplayer` | Multiplayer game development principles. |
| `music-for-robots.md` | `music-for-robots` | >- |
| `music-generation-studio.md` | `music-generation-studio` | Install and use the official AI Music Generator package, pinned by digest, for paid hosted work on the Beatra service. |
| `mysql.md` | `mysql` | Administer MySQL/MariaDB databases. |
| `n8n-agents.md` | `n8n-agents` | Design n8n AI agents, chains, classifiers, extractors, tool calling, memory, RAG, structured output, and human-review flows. |
| `n8n-binary-and-data.md` | `n8n-binary-and-data` | Handle n8n files and binary data across uploads, downloads, transforms, multimodal inputs, agent tools, and chat surfaces. |
| `n8n-code-javascript.md` | `n8n-code-javascript` | Write JavaScript code in n8n Code nodes. |
| `n8n-code-python.md` | `n8n-code-python` | Write Python code in n8n Code nodes. |
| `n8n-code-tool.md` | `n8n-code-tool` | Write and debug JavaScript or Python for the AI-callable n8n Custom Code Tool, including schemas, sandbox limits, and return formats. |
| `n8n-error-handling.md` | `n8n-error-handling` | Design visible, structured, recoverable n8n failures using error outputs, retries, Error Trigger workflows, and HTTP error responses. |
| `n8n-expression-syntax.md` | `n8n-expression-syntax` | Validate n8n expression syntax and fix common errors. |
| `n8n-mcp-tools-expert.md` | `n8n-mcp-tools-expert` | Expert guide for using n8n-mcp MCP tools effectively. |
| `n8n-multi-instance.md` | `n8n-multi-instance` | Select, verify, and safely switch n8n MCP instances across production, staging, teams, or clients, especially before credential writes. |
| `n8n-node-configuration.md` | `n8n-node-configuration` | Operation-aware node configuration guidance. |
| `n8n-subworkflows.md` | `n8n-subworkflows` | Build reusable n8n sub-workflows with typed inputs, all-vs-each execution, discoverable naming, and agent-tool exposure. |
| `n8n-validation-expert.md` | `n8n-validation-expert` | Expert guide for interpreting and fixing n8n validation errors. |
| `n8n-workflow-patterns.md` | `n8n-workflow-patterns` | Proven architectural patterns for building n8n workflows. |
| `nano-settlement-verify.md` | `nano-settlement-verify` | Check that a Nano (XNO) payment settled before a seller serves a paid call: one inline read-only script asks a public node about a send block and returns a verdict. |
| `nanobanana-ppt-skills.md` | `nanobanana-ppt-skills` | AI-powered PPT generation with document analysis and styled images |
| `nap-consistency-checker.md` | `nap-consistency-checker` | NAP Consistency Checker. |
| `native-data-fetching.md` | `native-data-fetching` | Use when implementing or debugging ANY network request, API call, or data fetching. |
| `neo-brutalism.md` | `neo-brutalism` | Web and App implementation guide for Neo-Brutalism. |
| `neon-postgres.md` | `neon-postgres` | Guides and best practices for working with Neon Serverless Postgres. |
| `neon-postgres-branches.md` | `neon-postgres-branches` | Choose and create the right Neon branch type for testing and development. |
| `neon-postgres-egress-optimizer.md` | `neon-postgres-egress-optimizer` | Diagnose and fix excessive Postgres egress (network data transfer) in a codebase. |
| `nerdzao-elite.md` | `nerdzao-elite` | Software engineering and product design workflow and Senior Product Designer. |
| `nerdzao-elite-gemini-high.md` | `nerdzao-elite-gemini-high` | Modo Elite Coder + UX Pixel-Perfect otimizado especificamente para Gemini 3.1 Pro High. |
| `nestjs-expert.md` | `nestjs-expert` | You are an expert in Nest.js with deep knowledge of enterprise-grade Node.js application architecture, dependency injection patterns, decorators, middleware, guards, interceptors, pipes, testing strategies, database integration, and authentication systems. |
| `network-101.md` | `network-101` | Configure and test common network services (HTTP, HTTPS, SNMP, SMB) for penetration testing lab environments. |
| `network-engineer.md` | `network-engineer` | Expert network engineer specializing in modern cloud networking, security architectures, and performance optimization. |
| `networkx.md` | `networkx` | NetworkX is a Python package for creating, manipulating, and analyzing complex networks and graphs. |
| `neumorphism.md` | `neumorphism` | Web and App implementation guide for Neumorphism (Soft UI). |
| `neverapply.md` | `neverapply` | Find matching jobs, tailor resumes, prepare for interviews and apply to jobs with the user's approval through NeverApply's hosted MCP server (OAuth sign-in). |
| `new-rails-project.md` | `new-rails-project` | Create a new Rails project |
| `newman-cicd-integration.md` | `newman-cicd-integration` | Generate ready-to-use CI/CD pipeline configurations that install and run Newman for automated API testing. |
| `nexrad-mosaic-access.md` | `nexrad-mosaic-access` | Access official NOAA/NCEP MRMS radar and multisensor composites for a region and time; validate product, grid, domain, quality, timestamp, and provenance. |
| `nexrad-mosaic-construction.md` | `nexrad-mosaic-construction` | Construct a quality-aware NEXRAD multi-radar mosaic from aligned single-site products with explicit coverage, beam geometry, quality weighting, overlap resolution, and provenance. |
| `nexrad-product-access.md` | `nexrad-product-access` | Discover and access NEXRAD data for a selected radar site, time, product, or Level II moment using completed archive volumes, real-time chunks, or supported Level III sources with metadata validation. |
| `nexrad-radar-visualization.md` | `nexrad-radar-visualization` | Plot NEXRAD Level II/III site scans and decoded radar mosaics with correct radar geometry, map grids, units, quality masks, timestamps, and provenance. |
| `nextjs-app-router-patterns.md` | `nextjs-app-router-patterns` | Comprehensive patterns for Next.js 14+ App Router architecture, Server Components, and modern full-stack React development. |
| `nextjs-best-practices.md` | `nextjs-best-practices` | Next.js App Router principles. |
| `nextjs-seo-indexing.md` | `nextjs-seo-indexing` | Fix SEO indexing issues, crawl budget problems, and Search Console coverage errors for Next.js apps. |
| `nfs-storage.md` | `nfs-storage` | Configure NFS servers and clients. |
| `nft-standards.md` | `nft-standards` | Master ERC-721 and ERC-1155 NFT standards, metadata best practices, and advanced NFT features. |
| `nika.md` | `nika` | Runs repeatable AI work as checked, budgeted workflow files. |
| `noaa-radar-satellite-fetching.md` | `noaa-radar-satellite-fetching` | Retrieve NOAA NEXRAD and GOES products from public cloud archives using verified site, product, channel, sector, and scan-time selection. |
| `nodejs-backend-patterns.md` | `nodejs-backend-patterns` | Comprehensive guidance for building scalable, maintainable, and production-ready Node.js backend applications with modern frameworks, architectural patterns, and best practices. |
| `nodejs-best-practices.md` | `nodejs-best-practices` | Node.js development principles and decision-making. |
| `nosql-expert.md` | `nosql-expert` | Expert guidance for distributed NoSQL databases (Cassandra, DynamoDB). |
| `not-a-vibe-coder.md` | `not-a-vibe-coder` | Turns vague prompts into 8 structured planning files for brand new projects. |
| `not-human-search-mcp.md` | `not-human-search-mcp` | Search AI-ready websites, inspect indexed site details, verify MCP endpoints, and discover tools and APIs using the Not Human Search MCP server |
| `notebooklm.md` | `notebooklm` | Interact with Google NotebookLM to query documentation with Gemini's source-grounded answers. |
| `notification-reminder-hub.md` | `notification-reminder-hub` | Notification register: title, type, priority, recipient and department, message, linked record, trigger module, scheduled and sent dates and status. |
| `notion-manual-import.md` | `notion-manual-import` | Notion Manual Import: the Notion step for any module - CSV, property mapping, import steps and verification for the field list the active module confirmed. |
| `notion-template-business.md` | `notion-template-business` | Expert in building and selling Notion templates as a business - not |
| `nutrition-analyzer.md` | `nutrition-analyzer` | 分析营养数据、识别营养模式、评估营养状况，并提供个性化营养建议。支持与运动、睡眠、慢性病数据的关联分析。 |
| `nx-workspace-patterns.md` | `nx-workspace-patterns` | Configure and optimize Nx monorepo workspaces. |
| `object-storage.md` | `object-storage` | Configure object storage with S3, GCS, and MinIO. |
| `objection-preemptor.md` | `objection-preemptor` | Map customer objections and address them with evidence and choice-preserving language when a funnel, sales page, or pitch encounters recurring hesitation. |
| `observability-and-instrumentation.md` | `observability-and-instrumentation` | Instruments code so production behavior is visible and diagnosable. |
| `observability-cloud-planning.md` | `observability-cloud-planning` | Build a cloud, SLO, and incident-readiness register after intake. |
| `observability-engineer.md` | `observability-engineer` | Build production-ready monitoring, logging, and tracing systems. |
| `observability-monitoring-monitor-setup.md` | `observability-monitoring-monitor-setup` | Set up metrics, distributed tracing, log aggregation, and dashboards for application and infrastructure monitoring. |
| `observability-monitoring-slo-implement.md` | `observability-monitoring-slo-implement` | You are an SLO (Service Level Objective) expert specializing in implementing reliability standards and error budget-based engineering practices. |
| `obsess.md` | `obsess` | Perfectionist mode for one target: checked attempts on a UI detail or hot path, keeps the best version, stops on a budget. |
| `obsidian-bases.md` | `obsidian-bases` | Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries. |
| `obsidian-cli.md` | `obsidian-cli` | Use the Obsidian CLI to read, create, search, and manage vault content, or to develop and debug Obsidian plugins and themes from the command line. |
| `obsidian-clipper-template-creator.md` | `obsidian-clipper-template-creator` | Guide for creating templates for the Obsidian Web Clipper. |
| `obsidian-markdown.md` | `obsidian-markdown` | Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other Obsidian-specific syntax. |
| `obtain-coupons-all-in-one.md` | `obtain-coupons-all-in-one` | All-in-one coupon fetcher supporting takeout (Meituan, Ele.me, JD), parcel/courier (SF, ZTO, YTO, etc.), travel (DiDi, Ctrip), and movie tickets (Taopiaopiao, Maoyan) coupons with one-click access to all discounts. |
| `occupational-health-analyzer.md` | `occupational-health-analyzer` | 分析职业健康数据、识别工作相关健康风险、评估职业健康状况、提供个性化职业健康建议。支持与睡眠、运动、心理健康等其他健康数据的关联分析。 |
| `odoo-accounting-setup.md` | `odoo-accounting-setup` | Expert guide for configuring Odoo Accounting: chart of accounts, journals, fiscal positions, taxes, payment terms, and bank reconciliation. |
| `odoo-automated-tests.md` | `odoo-automated-tests` | Write and run Odoo automated tests using TransactionCase, HttpCase, and browser tour tests. |
| `odoo-backup-strategy.md` | `odoo-backup-strategy` | Complete Odoo backup and restore strategy: database dumps, filestore backup, automated scheduling, cloud storage upload, and tested restore procedures. |
| `odoo-docker-deployment.md` | `odoo-docker-deployment` | Production-ready Docker and docker-compose setup for Odoo with PostgreSQL, persistent volumes, environment-based configuration, and Nginx reverse proxy. |
| `odoo-ecommerce-configurator.md` | `odoo-ecommerce-configurator` | Expert guide for Odoo eCommerce and Website: product catalog, payment providers, shipping methods, SEO, and order-to-fulfillment workflow. |
| `odoo-edi-connector.md` | `odoo-edi-connector` | Guide for implementing EDI (Electronic Data Interchange) with Odoo: X12, EDIFACT document mapping, partner onboarding, and automated order processing. |
| `odoo-hr-payroll-setup.md` | `odoo-hr-payroll-setup` | Expert guide for Odoo HR and Payroll: salary structures, payslip rules, leave policies, employee contracts, and payroll journal entries. |
| `odoo-inventory-optimizer.md` | `odoo-inventory-optimizer` | Expert guide for Odoo Inventory: stock valuation (FIFO/AVCO), reordering rules, putaway strategies, routes, and multi-warehouse configuration. |
| `odoo-l10n-compliance.md` | `odoo-l10n-compliance` | Country-specific Odoo localization: tax configuration, e-invoicing (CFDI, FatturaPA, SAF-T), fiscal reporting, and country chart of accounts setup. |
| `odoo-manufacturing-advisor.md` | `odoo-manufacturing-advisor` | Expert guide for Odoo Manufacturing: Bills of Materials (BoM), Work Centers, routings, MRP planning, and production order workflows. |
| `odoo-migration-helper.md` | `odoo-migration-helper` | Step-by-step guide for migrating Odoo custom modules between versions (v14→v15→v16→v17). |
| `odoo-module-developer.md` | `odoo-module-developer` | Expert guide for creating custom Odoo modules. |
| `odoo-orm-expert.md` | `odoo-orm-expert` | Master Odoo ORM patterns: search, browse, create, write, domain filters, computed fields, and performance-safe query techniques. |
| `odoo-performance-tuner.md` | `odoo-performance-tuner` | Expert guide for diagnosing and fixing Odoo performance issues: slow queries, worker configuration, memory limits, PostgreSQL tuning, and profiling tools. |
| `odoo-project-timesheet.md` | `odoo-project-timesheet` | Expert guide for Odoo Project and Timesheets: task stages, billable time tracking, timesheet approval, budget alerts, and invoicing from timesheets. |
| `odoo-purchase-workflow.md` | `odoo-purchase-workflow` | Expert guide for Odoo Purchase: RFQ → PO → Receipt → Vendor Bill workflow, purchase agreements, vendor price lists, and 3-way matching. |
| `odoo-qweb-templates.md` | `odoo-qweb-templates` | Expert in Odoo QWeb templating for PDF reports, email templates, and website pages. |
| `odoo-sales-crm-expert.md` | `odoo-sales-crm-expert` | Expert guide for Odoo Sales and CRM: pipeline stages, quotation templates, pricelists, sales teams, lead scoring, and forecasting. |
| `odoo-security-rules.md` | `odoo-security-rules` | Expert in Odoo access control: ir.model.access.csv, record rules (ir.rule), groups, and multi-company security patterns. |
| `odoo-shopify-integration.md` | `odoo-shopify-integration` | Connect Odoo with Shopify: sync products, inventory, orders, and customers using the Shopify API and Odoo's external API or connector modules. |
| `odoo-upgrade-advisor.md` | `odoo-upgrade-advisor` | Step-by-step Odoo version upgrade advisor: pre-upgrade checklist, community vs enterprise upgrade path, OCA module compatibility, and post-upgrade validation. |
| `odoo-woocommerce-bridge.md` | `odoo-woocommerce-bridge` | Sync Odoo with WooCommerce: products, inventory, orders, and customers via WooCommerce REST API and Odoo external API. |
| `odoo-xml-views-builder.md` | `odoo-xml-views-builder` | Expert at building Odoo XML views: Form, List, Kanban, Search, Calendar, and Graph. |
| `odw.md` | `odw` | Dynamic multi-agent workflows — plan first, then orchestrate parallel agents with adversarial verification via the local odw daemon. |
| `offboarding-exit.md` | `offboarding-exit` | Offboarding register: exit type, employee and manager, notice and final day, reason, handover owner, and done flags for knowledge transfer, assets, access and settlement. |
| `offensive-osint.md` | `offensive-osint` | Operational arsenal for authorized external red-team and bug-bounty recon. |
| `offer-appointment.md` | `offer-appointment` | Offer register: candidate, position, department, employment type, offered salary and currency, offer date and expiry, joining date, probation, approver and sign-off. |
| `offers.md` | `offers` | When the user wants to design, construct, or improve an offer — the thing they actually sell — including value framing, bonus stacking, guarantee design, scarcity/urgency, naming, and payment structure. |
| `office-productivity.md` | `office-productivity` | Office productivity workflow covering document creation, spreadsheet automation, presentation generation, and integration with LibreOffice and Microsoft Office formats. |
| `og-tag-generator.md` | `og-tag-generator` | OG Tag Generator. |
| `okr-system.md` | `okr-system` | OKR register: objective, owner and level, department, quarter and year, up to three key results with progress percentages, parent OKR and overall progress. |
| `okta-attack.md` | `okta-attack` | Okta-as-IdP red-team attack chain |
| `ollama-stack.md` | `ollama-stack` | Run local LLM workloads with Ollama, Open WebUI, and GPU-aware tuning |
| `omentir-linkedin-outreach.md` | `omentir-linkedin-outreach` | Run LinkedIn prospecting and outreach through the Omentir MCP server: find people, score fit, draft messages, and check campaigns. |
| `omp-delegate.md` | `omp-delegate` | Delegate coding tasks to Oh My Pi (`omp`) only when the user explicitly |
| `on-call-handoff-patterns.md` | `on-call-handoff-patterns` | Effective patterns for on-call shift transitions, ensuring continuity, context transfer, and reliable incident response across shifts. |
| `on-page-seo-audit-checker.md` | `on-page-seo-audit-checker` | On-Page SEO Audit Checker. |
| `onboard.md` | `onboard` | Decompose mixed project materials (code, docs, PDF/Excel/PPT) into a sourced overview and a goal-driven three-tier learning path, then teach it interactively. |
| `onboarding.md` | `onboarding` | When the user wants to optimize post-signup onboarding, user activation, first-run experience, or time-to-value. |
| `onboarding-cro.md` | `onboarding-cro` | You are an expert in user onboarding and activation. |
| `onboarding-playbook.md` | `onboarding-playbook` | Onboarding checklist: step, phase and order, department, owner, linked SOP and required flag. |
| `onboarding-psychologist.md` | `onboarding-psychologist` | Design first-use and onboarding experiences that bring an early win, cut setup friction, build ownership and form habits through stable cues. |
| `oneroster-csv-validator.md` | `oneroster-csv-validator` | Validates 1EdTech / IMS Global OneRoster v1.1 and v1.2 CSV roster sets: manifest integrity, bulk vs delta strictness, foreign key references, and encoding sanitization. |
| `ontoly-software-graph.md` | `ontoly-software-graph` | Use Ontoly's deterministic Software Graph, MCP server, and agent skills for architecture review, request tracing, impact analysis, and dependency analysis. |
| `open-source-marketing.md` | `open-source-marketing` | When the user wants to market an open source project authentically. |
| `openapi-spec-generation.md` | `openapi-spec-generation` | Generate and maintain OpenAPI 3.1 specifications from code, design-first specs, and validation patterns. |
| `openapi-spec-generator.md` | `openapi-spec-generator` | Generate complete, production-ready OpenAPI 3.x and Swagger 2.0 specifications from natural language descriptions, code, or partial specs. |
| `openclaw-deployment-hardening.md` | `openclaw-deployment-hardening` | Secure OpenClaw deployments with preflight hardening checks, CI/CD guardrails, |
| `openclaw-github-repo-commander.md` | `openclaw-github-repo-commander` | 7-stage super workflow for GitHub repo audit, cleanup, PR review, and competitor analysis |
| `openclaw-local-mac-mini.md` | `openclaw-local-mac-mini` | Set up OpenClaw locally and run it reliably on a Mac mini for private, |
| `openclaw-security-hardening.md` | `openclaw-security-hardening` | Harden OpenClaw self-hosted environments with baseline host controls, |
| `opencode-delegate.md` | `opencode-delegate` | Delegate coding tasks to the OpenCode CLI only when the user explicitly |
| `openshift.md` | `openshift` | Manage Red Hat OpenShift clusters and deployments. |
| `opentelemetry.md` | `opentelemetry` | Instrument applications and infrastructure with OpenTelemetry for unified |
| `opentofu-migration.md` | `opentofu-migration` | Migrate from Terraform to OpenTofu with state compatibility, provider |
| `optim-agent.md` | `optim-agent` | Guide agent-driven parameter optimization for configurable systems with measurable objectives. |
| `options-flow-analyzer.md` | `options-flow-analyzer` | Compare raw and explicitly filtered options put/call ratios with documented premium, delta and expiry assumptions |
| `oral-health-analyzer.md` | `oral-health-analyzer` | 分析口腔健康数据、识别口腔问题模式、评估口腔健康状况、提供个性化口腔健康建议。支持与营养、慢性病、用药等其他健康数据的关联分析。 |
| `orca-replay.md` | `orca-replay` | Answers questions about a past agent run from its recording rather than from memory, and replays or forks that run. |
| `orchestrate.md` | `orchestrate` | Coordinate focused subagents on substantial work, keep their ownership non-overlapping, and integrate verified results. |
| `orchestrate-batch-refactor.md` | `orchestrate-batch-refactor` | Plan and execute large refactors with dependency-aware work packets and parallel analysis. |
| `organic-growth-forecast-tool.md` | `organic-growth-forecast-tool` | Organic Growth Forecast Tool. |
| `organization-design.md` | `organization-design` | Org structure register: department, type, parent, head, location, approved against actual headcount, annual budget, cost centre code and establishment date. |
| `os-scripting.md` | `os-scripting` | Operating system and shell scripting troubleshooting workflow for Linux, macOS, and Windows. |
| `osint-methodology.md` | `osint-methodology` | Comprehensive OSINT methodology for external red-team operations and |
| `oss-hunter.md` | `oss-hunter` | Automatically hunt for high-impact OSS contribution opportunities in trending repositories. |
| `osterwalder-canvas-architect.md` | `osterwalder-canvas-architect` | Iterative consultant agent for building and validating logically consistent 9-block Business Model Canvases. |
| `ot-ics.md` | `ot-ics` | Authorized OT/ICS security assessment: Purdue-model zoning review, PLC/SCADA exposure, industrial protocol discovery, and passive-first evaluation discipline. |
| `outreach-email-template-generator.md` | `outreach-email-template-generator` | Outreach Email Template Generator. |
| `outreachgenie-list-audit.md` | `outreachgenie-list-audit` | Audit saved OutreachGenie prospect lists against an outreach flow for missing template values, text limits and incomplete collection, using read-only MCP snapshots and local reports. |
| `page-cro.md` | `page-cro` | Analyze and optimize individual pages for conversion performance. |
| `page-speed-score-simulator.md` | `page-speed-score-simulator` | Page Speed Score Simulator. |
| `pagespeed-enhancer.md` | `pagespeed-enhancer` | Scan, audit, and fix web performance issues across all four Lighthouse/PageSpeed Insights pillars — Performance, Accessibility, Best Practices, and SEO — in structured batches. |
| `paid-ads.md` | `paid-ads` | You are an expert performance marketer who verifies available authorized account access before taking action. |
| `pakistan-payments-stack.md` | `pakistan-payments-stack` | Design and implement production-grade Pakistani payment integrations (JazzCash, Easypaisa, bank/PSP rails, optional Raast) for SaaS with PKR billing, webhook reliability, and reconciliation. |
| `papers-skill.md` | `papers-skill` | Skill for academic research workflows: search Semantic Scholar (200M+ papers), inspect citations, download arXiv PDFs, and extract PDF text. |
| `paragraph-keyword-optimizer.md` | `paragraph-keyword-optimizer` | Paragraph Keyword Optimizer. |
| `parallel-agents.md` | `parallel-agents` | Multi-agent orchestration patterns. |
| `parallel-search-mcp.md` | `parallel-search-mcp` | Search the public web and verify sources with Parallel's free Search MCP. |
| `parcel-coupon.md` | `parcel-coupon` | Call parcel/courier coupon API to fetch one-stop logistics service coupons, including smart shipping and smart price matching. |
| `party-ledger-reconciliation.md` | `party-ledger-reconciliation` | Party ledger reconciliation: party type, name and PAN/VAT, ledger against statement balance, difference and reason, duplicates, confirmation status and adjustment. |
| `party-planning.md` | `party-planning` | Estimate party food and drink quantities, select games, and draft hosting timelines using HostPartyPlay's published planning heuristics. |
| `patch-diff-exploit.md` | `patch-diff-exploit` | Locate vulnerability fixes in vendor patches, diff binaries across versions, and build N-day PoCs. |
| `patterns.md` | `patterns` | Reference document for monopoly patterns. |
| `payment-accounting.md` | `payment-accounting` | Payment voucher register: payment number and date, paid to and purpose, mode, gross amount, TDS rate and deducted, net paid, invoice allocation, ledger and reconciliation status. |
| `payment-integration.md` | `payment-integration` | Integrate Stripe, PayPal, and payment processors. |
| `payments-received.md` | `payments-received` | Payments received log: reference, client and invoice, amount and currency, payment date and method, withholding tax, bank account, received-by and receipt-sent status. |
| `paypal-integration.md` | `paypal-integration` | Master PayPal payment integration including Express Checkout, IPN handling, recurring billing, and refund workflows. |
| `payroll-finance.md` | `payroll-finance` | Payroll register: employee, department and month, basic, DA, HRA and TA, bonus, deductions, net pay, pay period, payment date and method. |
| `paywall-upgrade-cro.md` | `paywall-upgrade-cro` | You are an expert in in-app paywalls and upgrade flows. |
| `pc-games.md` | `pc-games` | PC and console game development principles. |
| `pci-compliance.md` | `pci-compliance` | Review payment data flows and engineering control evidence for a scoped PCI assessment, without claiming certification. |
| `pci-dss-compliance.md` | `pci-dss-compliance` | Implement PCI DSS requirements for payment card data. |
| `pdf-conversion-router.md` | `pdf-conversion-router` | Use when converting a PDF into another format such as Markdown, HTML, text, JSON, DOCX, or structured notes and the agent must choose the best extraction route, settings, and cleanup strategy for maximum fidelity and readability. |
| `penetration-testing.md` | `penetration-testing` | Perform basic penetration testing and security assessments. |
| `pentest-checklist.md` | `pentest-checklist` | Provide a comprehensive checklist for planning, executing, and following up on penetration tests. |
| `pentest-commands.md` | `pentest-commands` | Provide a comprehensive command reference for penetration testing tools including network scanning, exploitation, password cracking, and web application testing. |
| `pentest-tools.md` | `pentest-tools` | Operate 20+ penetration-testing tools (Nmap, Nuclei, SQLMap, FFUF, Hashcat, and more) through structured workflows with consistent output handling. |
| `people-data.md` | `people-data` | Research LinkedIn professional profiles and public business-contact data, including email/phone lookup, people search, and YouTube channel business-email discovery. |
| `people-directory.md` | `people-directory` | Employee master record: name, employee id, department, job title, grade, manager, employment type, contact and emergency details, access role, start and end dates, status. |
| `performance-engineer.md` | `performance-engineer` | Diagnose performance bottlenecks using profiling, traces, load tests, and observability; verify latency and capacity improvements. |
| `performance-management.md` | `performance-management` | Performance review register: review type, period, employee and reviewer, KPI, OKR and behaviour scores, overall rating, PIP and promotion flags, development plan. |
| `performance-optimization.md` | `performance-optimization` | Optimizes application performance. |
| `performance-optimizer.md` | `performance-optimizer` | Identifies and fixes performance bottlenecks in code, databases, and APIs. |
| `performance-profiling.md` | `performance-profiling` | Performance profiling principles. |
| `performance-testing-review-ai-review.md` | `performance-testing-review-ai-review` | Review performance-sensitive code changes with reproducible baselines, workload metrics, static analysis and evidence-backed findings. |
| `performance-testing-review-multi-agent-review.md` | `performance-testing-review-multi-agent-review` | Review a defined code diff from relevant correctness, authorization and performance perspectives; delegate only when authorized and reproduce findings centrally. |
| `performance-tuning.md` | `performance-tuning` | Optimize Linux system performance. |
| `permission-manager.md` | `permission-manager` | Manage opencode permissions: review always-allow lists, suggest safe read-only commands, configure permission patterns |
| `perq.md` | `perq` | Find verified free AI credits, free tiers, startup programs and student perks for AI APIs, GPUs and dev tools, each with the vendor's source link and a last-verified date. |
| `personal-tool-builder.md` | `personal-tool-builder` | Expert in building custom tools that solve your own problems first. |
| `petty-cash-management.md` | `petty-cash-management` | Petty cash register: entry number, date and type, payee and purpose, cash in and out, running balance, cash limit flag, custodian, physical count and variance. |
| `phase-gated-debugging.md` | `phase-gated-debugging` | Use when debugging any bug. |
| `photopea-embedded-editor.md` | `photopea-embedded-editor` | Embed Photopea in web apps using photopea.js. |
| `php.md` | `php` | Language-specific super-code guidelines for php. |
| `php-pro.md` | `php-pro` | 'Write idiomatic PHP code with generators, iterators, SPL data |
| `pi-delegate.md` | `pi-delegate` | Delegate coding tasks to the Pi coding agent CLI (`pi`) only when the |
| `pi-web-search.md` | `pi-web-search` | Give Pi Agents a safe web-search and fetch workflow using the installed pi-web-access package. |
| `pick-ui-library.md` | `pick-ui-library` | Choose a frontend library from Emil Kowalski’s curated list after checking the project’s existing stack and requirements. |
| `pilot-protocol.md` | `pilot-protocol` | Give an AI agent a permanent network address, encrypted P2P messaging, and an installable app store via Pilot Protocol |
| `pitch-psychologist.md` | `pitch-psychologist` | Structure pitches, decks, and talk tracks around audience beliefs, proof, and a clear decision when presentations need stronger progression. |
| `plaid-fintech.md` | `plaid-fintech` | Expert patterns for Plaid API integration including Link token |
| `plan-ledger-tasks-yylo.md` | `plan-ledger-tasks-yylo` | Create a concise Product Development Requirement and one or more implementation-sized |
| `plan-writing.md` | `plan-writing` | Structured task planning with clear breakdowns, dependencies, and verification criteria. |
| `planetscale.md` | `planetscale` | Operate MySQL-compatible databases on PlanetScale with branching workflows, |
| `planning-and-task-breakdown.md` | `planning-and-task-breakdown` | Breaks work into ordered tasks. |
| `planning-with-files.md` | `planning-with-files` | Work like Manus: Use persistent markdown files as your \"working memory on disk.\" |
| `playwright-java.md` | `playwright-java` | Scaffold, write, debug, and enhance enterprise-grade Playwright E2E tests in Java using Page Object Model, JUnit 5, Allure reporting, and parallel execution. |
| `playwright-skill.md` | `playwright-skill` | Write and run scoped Playwright browser automation, responsive checks, screenshots and login-flow tests with a local Node executor. |
| `plotly.md` | `plotly` | Interactive visualization library. |
| `podman.md` | `podman` | Manage containers using Podman, the daemonless container engine. |
| `poka-yoke.md` | `poka-yoke` | Mistake-proof code, config and process: make the wrong action impossible or self-announcing rather than documented. |
| `polars.md` | `polars` | Expression-based DataFrame library for Python and Rust. |
| `policy-acknowledgement.md` | `policy-acknowledgement` | Policy acknowledgement register: employee, policy and version, sent and due dates, acknowledged date and flag, days overdue, reminder sent and status. |
| `policy-as-code.md` | `policy-as-code` | Implement policy as code with OPA, Sentinel, and Kyverno. |
| `policy-library.md` | `policy-library` | Policy register: name, version, category, owner and approver, applies to, compliance framework, acknowledgement requirement, effective date and next review. |
| `polis-protocol.md` | `polis-protocol` | Coordinate multi-vendor AI agents as a self-improving team — a learning router assigns work by track record and citizens can amend the protocol's own rules. |
| `polis-protocol-a-self-optimizing-city-of-agents.md` | `polis-protocol-a-self-optimizing-city-of-agents` | Polis Protocol: A Self-Optimizing City of Agents |
| `ponder.md` | `ponder` | Run coverage-gated multi-pass code, architecture, security, UI, or product reviews where every file must be graded and 4 perspectives deliberate to convergence. |
| `popup-cro.md` | `popup-cro` | Create and optimize popups, modals, overlays, slide-ins, and banners to increase conversions without harming user experience or brand trust. |
| `posix-shell-pro.md` | `posix-shell-pro` | Expert in strict POSIX sh scripting for maximum portability across Unix-like systems. |
| `post.md` | `post` | Make share-post image sets that look native: Xiaohongshu carousels, X images, covers, App Store poster layouts, real screenshots and faithful app-UI mocks. |
| `postel-writing.md` | `postel-writing` | Find posts going viral in the user's niche, write their own version in their voice for X (Twitter), LinkedIn, Bluesky or Mastodon, and schedule or publish it through the user's Postel account. |
| `poster-design-studio.md` | `poster-design-studio` | Install and use the official AI Poster Maker package, pinned by digest, for paid hosted work on the Beatra service. |
| `postgres-best-practices.md` | `postgres-best-practices` | Postgres performance optimization and best practices from Supabase. |
| `postgres-readonly-queries.md` | `postgres-readonly-queries` | Execute safe read-only SQL queries against PostgreSQL databases with multi-connection support and defense-in-depth write protection. |
| `postgresql.md` | `postgresql` | Design a PostgreSQL-specific schema. |
| `postgresql-cli.md` | `postgresql-cli` | PostgreSQL interactive terminal (psql) reference and usage guide. |
| `postgresql-devsec.md` | `postgresql-devsec` | Administer PostgreSQL databases. |
| `postgresql-optimization.md` | `postgresql-optimization` | PostgreSQL database optimization workflow for query tuning, indexing strategies, performance analysis, and production database management. |
| `postman-collection-generator.md` | `postman-collection-generator` | Generate complete, import-ready Postman Collection v2.1 JSON files from natural language API descriptions or cURL commands. |
| `postman-openapi-converter.md` | `postman-openapi-converter` | Convert OpenAPI 3.x or Swagger 2.0 specs (YAML or JSON) into complete, import-ready Postman Collection v2.1 JSON files. |
| `postmortem-writing.md` | `postmortem-writing` | Comprehensive guide to writing effective, blameless postmortems that drive organizational learning and prevent incident recurrence. |
| `power-user-cultivation.md` | `power-user-cultivation` | When the user wants to identify and nurture developer advocates, build champion programs, or turn active users into contributors and evangelists. |
| `powershell-windows.md` | `powershell-windows` | PowerShell Windows patterns. |
| `ppl-personal-crm.md` | `ppl-personal-crm` | Uses the ppl personal CRM over MCP to prepare for conversations, recall facts about people, log interactions and manage relationship follow-ups. |
| `pptx-deck-creation.md` | `pptx-deck-creation` | Create editable, production-ready PPTX decks with narrative planning, explicit layout specs, asset guidance, and quality checks. |
| `pr-merge-champion.md` | `pr-merge-champion` | Optimize pull requests for quick approval and merging by ensuring clean diffs, comprehensive self-reviews, and structured documentation. |
| `pr-writer.md` | `pr-writer` | Create pull requests following Sentry's engineering practices. |
| `pre-boarding.md` | `pre-boarding` | Pre-boarding checklist: task, employee and department, owner, category, joining and due dates, documents received, laptop, email and account-record readiness, status. |
| `pre-release-review.md` | `pre-release-review` | Run a read-only pre-release review for deploy readiness, migrations, config, secrets, rollout order, rollback risk, and launch blockers. |
| `pre-ship-gate.md` | `pre-ship-gate` | A ship gate that runs before any production deploy: checks the silent failure modes that make a deploy 'succeed' while prod stays broken, then verifies the live revision instead of trusting deploy output. |
| `premium-3d-website.md` | `premium-3d-website` | Guidelines for building premium 3D websites, focusing on custom WebGL shaders, post-processing, physics-based interactions, smooth animations, preloaders, and device optimization. |
| `presentation-deck.md` | `presentation-deck` | Build an evidence-linked slide register after context-first intake. |
| `price-psychology-strategist.md` | `price-psychology-strategist` | Design pricing presentation, anchors, and tiers when an offer needs clearer value and fairness without misleading comparisons. |
| `pricing.md` | `pricing` | When the user wants help with pricing decisions, packaging, or monetization strategy. |
| `pricing-strategy.md` | `pricing-strategy` | Design pricing, packaging, and monetization strategies based on value, customer willingness to pay, and growth objectives. |
| `prisma-expert.md` | `prisma-expert` | You are an expert in Prisma ORM with deep knowledge of schema design, migrations, query optimization, relations modeling, and database operations across PostgreSQL, MySQL, and SQLite. |
| `privacy-by-design.md` | `privacy-by-design` | Use when building apps that collect user data. |
| `privacy-mask.md` | `privacy-mask` | Mask, redact, anonymize and censor sensitive information (PII) in screenshots and images — phone numbers, emails, IDs, API keys, crypto wallets, credit cards, passwords, and more. |
| `privilege-escalation-methods.md` | `privilege-escalation-methods` | Provide comprehensive techniques for escalating privileges from a low-privileged user to root/administrator access on compromised Linux and Windows systems. |
| `pro-launch.md` | `pro-launch` | Build an app or product from 0 to 1, taste-first, with phase gates: references, naming, style frames, UI loop, launch video, GTM and shipping. |
| `pro-motion.md` | `pro-motion` | Make a motion-graphics launch, brand or promo film audio first: plan the music, then render the film in code (canvas to MP4) cut to the track. |
| `probation-tracker.md` | `probation-tracker` | Probation register: employee, start and end dates, 30, 60 and 90-day review scores, overall score and confirmation letter. |
| `product-decision-agent.md` | `product-decision-agent` | 中文产品决策 Agent。用于需求优先级、Roadmap、增长、留存、运营、数据异常、A/B Test、项目延期和跨团队协作；先判断事实、阶段、核心阻塞与主导机制，再给出下一步、停止清单和切换条件。默认中文，不引用原文或讲历史。 |
| `product-description-generator.md` | `product-description-generator` | Product Description Generator. |
| `product-design.md` | `product-design` | Design de produto nivel Apple — sistemas visuais, UX flows, acessibilidade, linguagem visual proprietaria, design tokens, prototipagem e handoff. |
| `product-design-harness.md` | `product-design-harness` | Use when a product direction, feature, workflow, experiment, launch, feedback signal, automation, or scale decision needs judgment before execution or the next iteration. |
| `product-inventor.md` | `product-inventor` | Product Inventor e Design Alchemist de nivel maximo — combina Product Thinking, Design Systems, UI Engineering, Psicologia Cognitiva, Storytelling e execucao impecavel nivel Jobs/Apple. |
| `product-manager.md` | `product-manager` | Guide product strategy, discovery, prioritization and metrics; upstream templates and formula collections are external prerequisites. |
| `product-manager-toolkit.md` | `product-manager-toolkit` | Essential tools and frameworks for modern product management, from discovery to delivery. |
| `product-marketing.md` | `product-marketing` | When the user wants to create or update their product marketing context document. |
| `product-marketing-context.md` | `product-marketing-context` | Create or update a reusable product marketing context document with positioning, audience, ICP, use cases, and messaging. |
| `product-photo-studio.md` | `product-photo-studio` | Install and use the official AI Product Photography package, pinned by digest, for paid hosted work on the Beatra service. |
| `production-audit.md` | `production-audit` | Audit a shipped repo for production-readiness gaps across RLS, webhooks, secrets, grants, Stripe idempotency, mobile UX, and deployment health. |
| `production-code-audit.md` | `production-code-audit` | Audit an explicitly scoped codebase for evidenced security, correctness and performance issues; implement authorized targeted repairs and report validation plus residual readiness gaps. |
| `production-runtime-certification.md` | `production-runtime-certification` | Certify a deployed service with fresh evidence across source, CI, migrations, runtime health, readiness, and critical routes; use before declaring a release production-ready. |
| `production-scheduling.md` | `production-scheduling` | Codified expertise for production scheduling, job sequencing, line balancing, changeover optimisation, and bottleneck resolution in discrete and batch manufacturing. |
| `professional-proofreader.md` | `professional-proofreader` | Use when a user asks to "proofread", "review and correct", "fix grammar", "improve readability while keeping my voice", and to proofread a document file and save an updated version. |
| `programmatic-seo.md` | `programmatic-seo` | Design and evaluate programmatic SEO strategies for creating SEO-driven pages at scale using templates and structured data. |
| `progressive-estimation.md` | `progressive-estimation` | Estimate AI-assisted and hybrid human+agent development work with explicit PERT assumptions and calibration feedback loops |
| `progressive-web-app.md` | `progressive-web-app` | Build Progressive Web Apps (PWAs) with offline support, installability, and caching strategies. |
| `project-based-performance.md` | `project-based-performance` | Project performance review: role, project and manager, delivery, quality and collaboration scores, overall score and feedback. |
| `project-brief.md` | `project-brief` | Project Detail Optimizer. |
| `project-development.md` | `project-development` | This skill covers the principles for identifying tasks suited to LLM processing, designing effective project architectures, and iterating rapidly using agent-assisted development. |
| `project-memory-log.md` | `project-memory-log` | Maintain one operation log and one deduplicated document catalog for long-running projects. |
| `project-skill-audit.md` | `project-skill-audit` | Audit a project and recommend the highest-value skills to add or update. |
| `project-state-governor.md` | `project-state-governor` | Govern evidence-backed canonical project state across sessions, branches, reviews, and research cycles without inventing product intent. |
| `projection-patterns.md` | `projection-patterns` | Build read models and projections from event streams. |
| `projects-work-management.md` | `projects-work-management` | Project register: owner, team, priority, progress percentage, milestones, deliverables and budget against actual cost. |
| `prometheus-configuration.md` | `prometheus-configuration` | Complete guide to Prometheus setup, metric collection, scrape configuration, and recording rules. |
| `prometheus-grafana.md` | `prometheus-grafana` | Set up metrics collection and visualization with Prometheus and Grafana. |
| `promotion-upgrade-requests.md` | `promotion-upgrade-requests` | Promotion register: current and requested role and grade, justification, OKR and behaviour scores, time in role, salary proposal and decision. |
| `prompt-caching.md` | `prompt-caching` | Caching strategies for LLM prompts including Anthropic prompt |
| `prompt-engineer.md` | `prompt-engineer` | Transforms user prompts into optimized prompts using frameworks (RTF, RISEN, Chain of Thought, RODES, Chain of Density, RACE, RISE, STAR, SOAP, CLEAR, GROW) |
| `prompt-engineering.md` | `prompt-engineering` | Expert guide on prompt engineering patterns, best practices, and optimization techniques. |
| `prompt-engineering-patterns.md` | `prompt-engineering-patterns` | Master advanced prompt engineering techniques to maximize LLM performance, reliability, and controllability. |
| `prompt-injection-defense.md` | `prompt-injection-defense` | Defend AI systems against prompt injection and indirect prompt attacks |
| `prompt-library.md` | `prompt-library` | A comprehensive collection of battle-tested prompts inspired by [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) and community best practices. |
| `protect-mcp-governance.md` | `protect-mcp-governance` | Agent governance skill for MCP tool calls — Cedar policy authoring, shadow-to-enforce rollout, and Ed25519 receipt verification. |
| `protocol-reverse.md` | `protocol-reverse` | Authorized reverse engineering of custom binary protocols, Protobuf/gRPC schemas, WebSocket frames, and PCAP-driven protocol recovery. |
| `protocol-reverse-engineering.md` | `protocol-reverse-engineering` | Comprehensive techniques for capturing, analyzing, and documenting network protocols for security research, interoperability, and debugging. |
| `prototype.md` | `prototype` | Build a throwaway prototype to flesh out a design — a runnable terminal app for state/business-logic questions, or several radically different UI variations toggleable from one route. |
| `public-relations.md` | `public-relations` | When the user wants help with public relations, earned media, press coverage, journalist outreach, or media strategy (not pull requests). |
| `pubmed-database.md` | `pubmed-database` | Direct REST API access to PubMed. |
| `purchase-accounting.md` | `purchase-accounting` | Purchase register: supplier, invoice, gross amount, VAT and TDS, net payable, ledger account and payment balance. |
| `push-skill-to-github.md` | `push-skill-to-github` | Commit and push skill changes to the configured skills repository after review and validation. |
| `puzzle-activity-planner.md` | `puzzle-activity-planner` | Plan puzzle-based activities for classrooms, parties, and events with pre-configured generator links |
| `pwn-chain.md` | `pwn-chain` | Go from reverse engineering to a working exploit: stack/heap/kernel pwn workflows with pwntools, libc-database, ROP, and stabilization from CTF to authorized remote targets. |
| `pydantic-models-py.md` | `pydantic-models-py` | Create Pydantic models following the multi-model pattern for clean API contracts. |
| `pypict-skill.md` | `pypict-skill` | Pairwise test generation |
| `pytest-skill.md` | `pytest-skill` | Generates production-grade pytest tests in Python with fixtures, parametrize, markers, mocking, and conftest patterns. |
| `python.md` | `python` | Language-specific super-code guidelines for python. |
| `python-development.md` | `python-development` | You are a Python project architecture expert specializing in scaffolding production-ready Python applications. |
| `python-development-python-scaffold.md` | `python-development-python-scaffold` | You are a Python project architecture expert specializing in scaffolding production-ready Python applications. |
| `python-fastapi-development.md` | `python-fastapi-development` | Python FastAPI backend development with async patterns, SQLAlchemy, Pydantic, authentication, and production API patterns. |
| `python-packaging.md` | `python-packaging` | Comprehensive guide to creating, structuring, and distributing Python packages using modern packaging tools, pyproject.toml, and publishing to PyPI. |
| `python-patterns.md` | `python-patterns` | Python development principles and decision-making. |
| `python-performance-optimization.md` | `python-performance-optimization` | Profile and optimize Python code using cProfile, memory profilers, and performance best practices. |
| `python-pptx-generator.md` | `python-pptx-generator` | Generate complete Python scripts that build polished PowerPoint decks with python-pptx and real slide content. |
| `python-pro.md` | `python-pro` | Master Python 3.12+ with modern features, async programming, performance optimization, and production-ready practices. |
| `python-testing-patterns.md` | `python-testing-patterns` | Implement comprehensive testing strategies with pytest, fixtures, mocking, and test-driven development. |
| `qiskit.md` | `qiskit` | Build and transpile Qiskit circuits, test local simulators and prepare authorized hardware workloads with Sampler/Estimator primitives. |
| `quality-nonconformance.md` | `quality-nonconformance` | Operational guidance for quality control, non-conformance investigation, root cause analysis, corrective action, and supplier quality management in regulated manufacturing. |
| `quant-analyst.md` | `quant-analyst` | Build financial models, backtest trading strategies, and analyze market data. |
| `quinn.md` | `quinn` | Verifies specified behavior through appropriate tests and truthful coverage reports. |
| `quit-sponsor.md` | `quit-sponsor` | Helps an AI agent provide non-judgmental, evidence-informed quit-smoking support with user-consented tracking, craving check-ins, and escalation to human or clinical help. |
| `radar-satellite-analysis.md` | `radar-satellite-analysis` | Interpret weather radar and satellite observations by validating product metadata and geometry, deriving storm and cloud structures, tracking evolution, and quantifying uncertainty. |
| `radare2.md` | `radare2` | Drive the radare2 CLI for binary reconnaissance, disassembly, analysis, function locating, export, and lightweight patching (r2/rabin2/rasm2/radiff2) without a GUI. |
| `radio-sdr.md` | `radio-sdr` | Authorized RF/SDR security research: signal identification, replay-feasibility study in shielded labs, and wireless protocol analysis within applicable spectrum and authorization constraints. |
| `radix-ui-design-system.md` | `radix-ui-design-system` | Build accessible design systems with Radix UI primitives. |
| `rag-engineer.md` | `rag-engineer` | Expert in building Retrieval-Augmented Generation systems. |
| `rag-implementation.md` | `rag-implementation` | RAG (Retrieval-Augmented Generation) implementation workflow covering embedding selection, vector database setup, chunking strategies, and retrieval optimization. |
| `rag-infrastructure.md` | `rag-infrastructure` | Build and operate Retrieval-Augmented Generation (RAG) infrastructure |
| `rag-observability-evals.md` | `rag-observability-evals` | Monitor and evaluate RAG systems with retrieval quality metrics, groundedness |
| `ralph-loop-yylo.md` | `ralph-loop-yylo` | Execute exactly one explicitly assigned YYLO Ledger task through the |
| `ranking-opportunity-finder.md` | `ranking-opportunity-finder` | Ranking Opportunity Finder. |
| `ranking-progress-tracker.md` | `ranking-progress-tracker` | Ranking Progress Tracker. |
| `rayden-code.md` | `rayden-code` | Generate React code with Rayden UI components using correct props, tokens, and premium layout patterns |
| `rayden-use.md` | `rayden-use` | Build and maintain Rayden UI components and screens in Figma via Figma MCP with full design token enforcement |
| `rclone-cli.md` | `rclone-cli` | Rclone command-line cloud storage manager reference and usage guide. |
| `re-create.md` | `re-create` | Completely delete and rewrite a file or module from scratch when structural rot makes patching impossible. |
| `rea-growth.md` | `rea-growth` | Analyze a company’s public growth and content through Treg, distinguish observations from hypotheses, and produce an evidence-linked playbook within an approved budget. |
| `react-best-practices.md` | `react-best-practices` | Comprehensive performance optimization guide for React and Next.js applications, adapted from Vercel’s published guidance. |
| `react-component-performance.md` | `react-component-performance` | Diagnose slow React components and suggest targeted performance fixes. |
| `react-flow-architect.md` | `react-flow-architect` | Build production-ready ReactFlow applications with hierarchical navigation, performance optimization, and advanced state management. |
| `react-flow-node-ts.md` | `react-flow-node-ts` | Create React Flow node components following established patterns with proper TypeScript types and store integration. |
| `react-modernization.md` | `react-modernization` | Master React version upgrades, class to hooks migration, concurrent features adoption, and codemods for automated transformation. |
| `react-native-architecture.md` | `react-native-architecture` | Architecture and integration patterns for React Native development with Expo, including navigation, state management, native modules, and offline-first architecture. |
| `react-native-skills.md` | `react-native-skills` | Review React Native and Expo rendering, lists, animations, navigation and native UI against project versions and measured behavior. |
| `react-nextjs-development.md` | `react-nextjs-development` | React and Next.js 14+ application development with App Router, Server Components, TypeScript, Tailwind CSS, and modern frontend patterns. |
| `react-patterns.md` | `react-patterns` | Modern React patterns and principles. |
| `react-state-management.md` | `react-state-management` | Master modern React state management with Redux Toolkit, Zustand, Jotai, and React Query. |
| `react-ui-patterns.md` | `react-ui-patterns` | Modern React UI patterns for loading states, error handling, and data fetching. |
| `read-all-adrs.md` | `read-all-adrs` | Read every ADR in a project before summarizing architectural context or decisions. |
| `readability-enhancer.md` | `readability-enhancer` | Readability Enhancer. |
| `readability-score-calculator.md` | `readability-score-calculator` | Readability Score Calculator. |
| `readme.md` | `readme` | You are an expert technical writer creating comprehensive project documentation. |
| `recallmax.md` | `recallmax` | Prepare source-linked conversation handoffs and bounded document summaries, preserving decisions, uncertainty and task state within the host context limit. |
| `receipt-accounting.md` | `receipt-accounting` | Receipt register: payer, mode, gross amount received, invoice allocation, unapplied amount and TDS collected. |
| `receiving-code-review.md` | `receiving-code-review` | Code review requires technical evaluation, not emotional performance. |
| `recognition-rewards.md` | `recognition-rewards` | Recognition register: employee, reward type, category, visibility, message and points awarded. |
| `recon-scope-triage.md` | `recon-scope-triage` | Triage ASM/recon output for ownership before testing |
| `recruit.md` | `recruit` | Turn a job description into an evidence-linked candidate shortlist through Treg, with job-related ranking and optional authorized business contact enrichment. |
| `recruitment-pipeline.md` | `recruitment-pipeline` | Recruitment pipeline: candidate, position, stage, source, applied and interview dates, interview score, notice period and offer. |
| `recsys-pipeline-architect.md` | `recsys-pipeline-architect` | Designs composable recommendation, ranking, and feed pipelines using the six-stage Source→Hydrator→Filter→Scorer→Selector→SideEffect framework |
| `recursive-context-pruning-token-budgeting.md` | `recursive-context-pruning-token-budgeting` | Optimizes AI agent performance by pruning redundant context, managing token usage, and enforcing ultra-concise, direct-to-value responses. |
| `red-team-tactics.md` | `red-team-tactics` | Red team tactics principles based on MITRE ATT&CK. |
| `red-team-tools.md` | `red-team-tools` | Implement proven methodologies and tool workflows from top security researchers for effective reconnaissance, vulnerability discovery, and bug bounty hunting. |
| `redesign-existing-projects.md` | `redesign-existing-projects` | Use when upgrading existing websites or apps by auditing generic UI patterns and applying premium design fixes without rewrites. |
| `redirect-301-generator.md` | `redirect-301-generator` | 301 Redirect Generator. |
| `redirect-checker.md` | `redirect-checker` | Redirect Checker. |
| `redis.md` | `redis` | Configure Redis for caching and data storage. |
| `redis-cli.md` | `redis-cli` | Redis command-line interface (redis-cli) reference and usage guide. |
| `redteam-mindset.md` | `redteam-mindset` | Red-team operator discipline |
| `redteam-report-template.md` | `redteam-report-template` | Client-facing red-team deliverable format |
| `reference-builder.md` | `reference-builder` | Creates exhaustive technical references and API documentation. |
| `referral-program.md` | `referral-program` | You are an expert in viral growth and referral marketing using only referral data and tools actually available and authorized. |
| `rehabilitation-analyzer.md` | `rehabilitation-analyzer` | 分析康复训练数据、识别康复模式、评估康复进展，并提供个性化康复建议 |
| `remote-gpu-trainer.md` | `remote-gpu-trainer` | Deploy, monitor, and debug long GPU jobs on RENTED/remote instances (AutoDL, RunPod, vast.ai, Lambda, Slurm, K8s): teardown/billing safety, spot resilience, resumable checkpointing, OOM/NaN triage. |
| `remote-work-tracker.md` | `remote-work-tracker` | Remote work register: employee, location, week start, HQ versus remote days, core-hours compliance and manager approval. |
| `remotion.md` | `remotion` | Generate walkthrough videos from Stitch projects using Remotion with smooth transitions, zooming, and text overlays |
| `remotion-best-practices.md` | `remotion-best-practices` | Best practices for Remotion - Video creation in React |
| `remotion-captions.md` | `remotion-captions` | Transcribing, displaying and animating captions |
| `remotion-create.md` | `remotion-create` | Create a new Remotion video |
| `remotion-docs.md` | `remotion-docs` | Search Remotion documentation |
| `remotion-interactivity.md` | `remotion-interactivity` | Structure Remotion markup for interactivity |
| `remotion-render.md` | `remotion-render` | Export a Remotion video |
| `remotion-to-hyperframes.md` | `remotion-to-hyperframes` | Migrate Remotion or other animation code and footage into HyperFrames, recording editability and frame comparison limits. |
| `remove-animations.md` | `remove-animations` | Remove unnecessary interface motion while preserving final states, focus, layout, and animation-dependent behavior. |
| `renhua.md` | `renhua` | Write Chinese social posts and product copy in a real person's voice, removing AI tells. |
| `repo-foundation.md` | `repo-foundation` | Implement features, fixes, modules, contract migrations, and resumed work while preserving user edits and authorized public contracts. |
| `repo-maintainer.md` | `repo-maintainer` | Audit and repair repository hygiene across artifacts, dependencies, CI, docs, Git state, and code-quality signals. |
| `repo-native-refactor.md` | `repo-native-refactor` | Review diffs without editing, or perform evidence-based cleanup while preserving authorized behavior, public contracts, and domain ownership. |
| `report-writing.md` | `report-writing` | Bug bounty report writing for H1/Bugcrowd/Intigriti/Immunefi |
| `reports-analytics.md` | `reports-analytics` | Report register: type, source modules, owner, audience, frequency, last and next run and report link. |
| `repurpose-into-a-post.md` | `repurpose-into-a-post` | Turn an article, newsletter, transcript or video into a Twitter or LinkedIn post that stands on its own. |
| `requesting-code-review.md` | `requesting-code-review` | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| `requirements-writing.md` | `requirements-writing` | Write and review verifiable requirements using EARS patterns, quality checks, defect review, and traceability. |
| `research-prompt.md` | `research-prompt` | Turn vague research needs into one precise deep-research prompt with context and output criteria. |
| `resolving-merge-conflicts.md` | `resolving-merge-conflicts` | Use when you need to resolve an in-progress git merge/rebase conflict. |
| `resumable-implementation-contracts.md` | `resumable-implementation-contracts` | Create repository-based execution contracts for multi-session implementation work, with stable task IDs, evidence, checkpoints, and exact resume state. |
| `retro-design.md` | `retro-design` | Web and App implementation guide for Retro Design (60s-80s). |
| `retro-futurism.md` | `retro-futurism` | Web and App implementation guide for Retro Futurism. |
| `returns-reverse-logistics.md` | `returns-reverse-logistics` | Codified expertise for returns authorisation, receipt and inspection, disposition decisions, refund processing, fraud detection, and warranty claims management. |
| `reverse-any-video.md` | `reverse-any-video` | Reconstruct authorized video as an editable HyperFrames project, with measured timing, rights and likeness boundaries. |
| `reverse-browser-automation.md` | `reverse-browser-automation` | Automate browsers (Playwright) and Windows desktop applications (UI automation) for reverse-engineering evidence collection, UI-driven workflows, and network observation during analysis. |
| `reverse-engineer.md` | `reverse-engineer` | Expert reverse engineer specializing in binary analysis, disassembly, decompilation, and software analysis. |
| `reverse-engineer-anything.md` | `reverse-engineer-anything` | Use REA to investigate shipped apps, binaries, packages, and runtimes; trace features with evidence, compare versions, or guide reconstruction. |
| `reverse-engineering.md` | `reverse-engineering` | General reverse-engineering methodology for compiled, obfuscated, packed, or virtualized targets: GDB, Frida, angr, Unicorn, and Qiling workflows across languages and platforms, with anti-analysis countermeasures. |
| `reverse-image-search.md` | `reverse-image-search` | Reverse Image Search. |
| `reverse-proxy.md` | `reverse-proxy` | Configure nginx and Traefik as reverse proxies. |
| `review-and-simplify-changes.md` | `review-and-simplify-changes` | Review a git diff or explicit file scope for reuse, code quality, efficiency, clarity, and standards issues, then optionally apply safe Codex-driven fixes. |
| `review-animations.md` | `review-animations` | Review motion code against a craft, performance, accessibility, and interaction-quality standard with evidence. |
| `review-multi-agent-orchestration.md` | `review-multi-agent-orchestration` | Use when a supervisor, swarm, graph, planner-worker system, or parallel agent workflow needs review for task boundaries, shared state, branch joins, retries, cancellation, context handoffs, budgets, deadlocks, or human escalation before implementation or production rollout. |
| `review-response-generator.md` | `review-response-generator` | Review Response Generator. |
| `review-swarm.md` | `review-swarm` | Parallel read-only multi-agent review of a current git diff or explicit file scope to find behavioral regressions, security or privacy risks, performance or reliability issues, and contract or test coverage gaps. |
| `revops.md` | `revops` | Design and improve revenue operations, lead lifecycle rules, scoring, routing, handoffs, and CRM process automation. |
| `rex.md` | `rex` | Translates user intent into a precise, unambiguous specification and requirements. |
| `rich-elicitation.md` | `rich-elicitation` | Asks clarifying questions in multiple rounds before starting ambiguous tasks. |
| `riffkit.md` | `riffkit` | Create short videos with Riffkit: Adapt a source formula, Swap approved footage, or generate from an idea. |
| `risk-manager.md` | `risk-manager` | Monitor portfolio risk, R-multiples, and position limits. |
| `risk-metrics-calculation.md` | `risk-metrics-calculation` | Calculate portfolio risk metrics including VaR, CVaR, Sharpe, Sortino, and drawdown analysis. |
| `robius-app-architecture.md` | `robius-app-architecture` | CRITICAL: Use for Robius app architecture patterns. |
| `robius-event-action.md` | `robius-event-action` | CRITICAL: Use for Robius event and action patterns. |
| `robius-matrix-integration.md` | `robius-matrix-integration` | CRITICAL: Use for Matrix SDK integration with Makepad. |
| `robius-state-management.md` | `robius-state-management` | CRITICAL: Use for Robius state management patterns. |
| `robius-widget-patterns.md` | `robius-widget-patterns` | CRITICAL: Use for Robius widget patterns. |
| `robots-txt-creator.md` | `robots-txt-creator` | Robots.txt Creator. |
| `robots-txt-validator.md` | `robots-txt-validator` | Robots.txt Validator. |
| `ruby.md` | `ruby` | Language-specific super-code guidelines for ruby. |
| `ruby-pro.md` | `ruby-pro` | Write idiomatic Ruby code with metaprogramming, Rails patterns, and performance optimization. |
| `runaway-guard.md` | `runaway-guard` | Cost-safety discipline for paid AI / inference APIs: treat $-cost as a third complexity dimension alongside time and space. |
| `runbook-creation.md` | `runbook-creation` | Create operational runbooks and standard operating procedures. |
| `rust.md` | `rust` | Language-specific super-code guidelines for rust. |
| `rust-async-patterns.md` | `rust-async-patterns` | Master Rust async programming with Tokio, async traits, error handling, and concurrent patterns. |
| `rust-pro.md` | `rust-pro` | Master Rust 1.75+ with modern async patterns, advanced type system features, and production-ready systems programming. |
| `saas-multi-tenant.md` | `saas-multi-tenant` | Design and implement multi-tenant SaaS architectures with row-level security, tenant-scoped queries, shared-schema isolation, and safe cross-tenant admin patterns in PostgreSQL and TypeScript. |
| `saas-pricing-strategist.md` | `saas-pricing-strategist` | Design, optimize, and test pricing strategies for SaaS products using |
| `saga-orchestration.md` | `saga-orchestration` | Patterns for managing distributed transactions and long-running business processes. |
| `salary-benchmarking.md` | `salary-benchmarking` | Salary benchmark register: role, department and grade against market and internal minimum, median and maximum. |
| `salary-wage-accounting.md` | `salary-wage-accounting` | Payroll register: gross, allowances, TDS and provident fund deductions, net pay, payment date and statutory reconciliation. |
| `sales-accounting.md` | `sales-accounting` | Sales register: customer, invoice, gross amount, discount, VAT and TDS, net receivable, credit terms and balance. |
| `sales-automator.md` | `sales-automator` | Draft cold emails, follow-ups, and proposal templates. |
| `sales-enablement.md` | `sales-enablement` | Create sales collateral such as decks, one-pagers, objection docs, demo scripts, playbooks, and proposal templates. |
| `salesforce-development.md` | `salesforce-development` | Expert patterns for Salesforce platform development including |
| `sam-altman.md` | `sam-altman` | Persona fictícia inspirada em temas públicos associados a Sam Altman; sem representação, citações verificadas ou acesso interno. |
| `same-idea-both-platforms.md` | `same-idea-both-platforms` | Write one idea as a Twitter post and a LinkedIn post that read as written separately, not pasted twice. |
| `sandbase-mcp.md` | `sandbase-mcp` | Discover, inspect, and invoke 2,000+ AI models and APIs through SandBase's local MCP bridge with explicit schema and cost checks. |
| `sankhya-dashboard-html-jsp-custom-best-pratices.md` | `sankhya-dashboard-html-jsp-custom-best-pratices` | This skill should be used when the user asks for patterns, best practices, creation, or fixing of Sankhya dashboards using HTML, JSP, Java, and SQL. |
| `sast-configuration.md` | `sast-configuration` | Static Application Security Testing (SAST) tool setup, configuration, and custom rule creation for comprehensive security scanning across multiple programming languages. |
| `satori.md` | `satori` | Use supportive, non-diagnostic reflection informed by Satori's philosophical and psychological lenses. |
| `sbom-supply-chain.md` | `sbom-supply-chain` | Generate, sign, and verify SBOMs and provenance attestations to secure |
| `scala.md` | `scala` | Language-specific super-code guidelines for scala. |
| `scala-pro.md` | `scala-pro` | Master enterprise-grade Scala development with functional programming, distributed systems, and big data processing. |
| `scale-benchmarks.md` | `scale-benchmarks` | Reference document for monopoly scale-benchmarks. |
| `scanning-tools.md` | `scanning-tools` | Master essential security scanning tools for network discovery, vulnerability assessment, web application testing, wireless security, and compliance validation. |
| `scanpy.md` | `scanpy` | Scanpy is a scalable Python toolkit for analyzing single-cell RNA-seq data, built on AnnData. |
| `scarcity-urgency-psychologist.md` | `scarcity-urgency-psychologist` | Design honest scarcity and urgency messaging when verified inventory, capacity, or deadlines justify a timely decision. |
| `scarf-single-cell.md` | `scarf-single-cell` | Analyze single-cell RNA-seq at million-cell scale with Scarf: out-of-core Zarr stores on disk or object storage, provenance-tracked artifacts, audited QC, clustering, markers and donor comparisons. |
| `schema-markup.md` | `schema-markup` | Design, validate, and optimize schema.org structured data for eligibility, correctness, and measurable SEO impact. |
| `schema-markup-generator.md` | `schema-markup-generator` | Generate and implement JSON-LD structured data for web apps, blogs, FAQs, and SaaS sites. |
| `sci-fi-interface.md` | `sci-fi-interface` | Web and App implementation guide for Sci-Fi Interface Design. |
| `scientific-writing.md` | `scientific-writing` | Draft and revise scientific manuscripts with evidence-based structure, citation verification, reporting guidelines and venue-specific formatting. |
| `scikit-learn.md` | `scikit-learn` | Machine learning in Python with scikit-learn. |
| `score-eval.md` | `score-eval` | Use when scoring an evaluation diff against a supplied rubric and baseline fixture: retain evidence for detected/fixed findings and report unscorable or unexecuted checks. |
| `screen-reader-testing.md` | `screen-reader-testing` | Practical guide to testing web applications with screen readers for comprehensive accessibility validation. |
| `screenshots.md` | `screenshots` | Generate marketing screenshots of your app using Playwright. |
| `screenstudio-alt.md` | `screenstudio-alt` | Open-source headless Screen Studio alternative: auto speed-up of idle, auto-zoom on click clusters, keystroke overlay chips, smoothed synthetic cursor, and 9:16 vertical export that follows the action — post-production for screen recordings from the CLI. |
| `scroll-experience.md` | `scroll-experience` | Expert in building immersive scroll-driven experiences - parallax |
| `sdk-dx.md` | `sdk-dx` | Design SDKs that developers love to use—APIs that feel native, error messages that guide, and experiences that reduce friction. |
| `seaborn.md` | `seaborn` | Seaborn is a Python visualization library for creating publication-quality statistical graphics. |
| `search-preview-simulator.md` | `search-preview-simulator` | Search Preview Simulator. |
| `search-specialist.md` | `search-specialist` | Research questions with focused web searches, primary-source verification, and explicit evidence gaps. |
| `second-deposit-igaming.md` | `second-deposit-igaming` | Explore local casino deposit exports with heuristic signals and descriptive comparisons. |
| `secrets-management.md` | `secrets-management` | Secure secrets management practices for CI/CD pipelines using Vault, AWS Secrets Manager, and other tools. |
| `security-and-hardening.md` | `security-and-hardening` | Hardens code against vulnerabilities. |
| `security-arsenal.md` | `security-arsenal` | Security payloads, bypass tables, wordlists, gf pattern names, always-rejected |
| `security-audit.md` | `security-audit` | Comprehensive security auditing workflow covering web application testing, API security, penetration testing, vulnerability scanning, and security hardening. |
| `security-auditor.md` | `security-auditor` | Expert security auditor specializing in DevSecOps, comprehensive cybersecurity, and compliance frameworks. |
| `security-automation.md` | `security-automation` | Automate security workflows and remediation. |
| `security-bluebook-builder.md` | `security-bluebook-builder` | Build a minimal but real security policy for sensitive apps. |
| `security-checklist.md` | `security-checklist` | Review a scoped architecture against evidence-based network, identity, data, secrets, dependency and incident-response controls. |
| `security-compliance-compliance-check.md` | `security-compliance-compliance-check` | You are a compliance expert specializing in regulatory requirements for software systems including GDPR, HIPAA, SOC2, PCI-DSS, and other industry standards. |
| `security-requirement-extraction.md` | `security-requirement-extraction` | Derive security requirements from threat models and business context. |
| `security-scanning-security-dependencies.md` | `security-scanning-security-dependencies` | You are a security expert specializing in dependency vulnerability analysis, SBOM generation, and supply chain security. |
| `security-scanning-security-hardening.md` | `security-scanning-security-hardening` | Coordinate multi-layer security scanning and hardening across application, infrastructure, and compliance controls. |
| `security-scanning-security-sast.md` | `security-scanning-security-sast` | 'Static Application Security Testing (SAST) for code vulnerability |
| `seek-and-analyze-video.md` | `seek-and-analyze-video` | Seek and analyze video content using Memories.ai Large Visual Memory Model for persistent video intelligence |
| `segment-cdp.md` | `segment-cdp` | Expert patterns for Segment Customer Data Platform including |
| `selector.md` | `selector` | Select a specialized 100seotools skill from a plain-language SEO or project-documentation request. |
| `semantic-versioning.md` | `semantic-versioning` | Automate versioning and changelog generation using semantic versioning |
| `semgrep-rule-creator.md` | `semgrep-rule-creator` | Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. |
| `semgrep-rule-variant-creator.md` | `semgrep-rule-variant-creator` | Creates language variants of existing Semgrep rules. |
| `sendblue-api.md` | `sendblue-api` | Send and receive iMessage, SMS, and RCS from application code via the Sendblue HTTP API — text, media, group messages, send styles, reactions, typing indicators, status callbacks, and inbound webhooks. |
| `sendblue-cli.md` | `sendblue-cli` | Send iMessage and SMS from the shell via the @sendblue/cli npm package — outbound sends, contact management, and account setup with no API client or webhook server required. |
| `sendblue-notify.md` | `sendblue-notify` | Text the user's phone when a long-running task, agent turn, or scheduled job finishes — via @sendblue/cli for outbound, optionally wired to a Claude Code Stop hook for automatic fire. |
| `senior-architect.md` | `senior-architect` | Plan and review system architecture using explicit requirements, tradeoffs and evidence; bundled scripts are incomplete stubs. |
| `senior-frontend.md` | `senior-frontend` | Frontend development skill for React, Next.js, TypeScript, and Tailwind CSS applications. |
| `senior-fullstack.md` | `senior-fullstack` | Coordinate full-stack implementation across interface, service, database and delivery boundaries using the existing project stack and verified checks. |
| `seo.md` | `seo` | Run a broad SEO audit across technical SEO, on-page SEO, schema, sitemaps, content quality, AI search readiness, and GEO. |
| `seo-aeo-blog-writer.md` | `seo-aeo-blog-writer` | Writes search-intent-led long-form articles with answer-first structure, FAQ coverage, internal links, and conversion paths for SEO and AEO. |
| `seo-aeo-content-cluster.md` | `seo-aeo-content-cluster` | Builds a topical authority map from business goals, search intent, existing content, and gaps, then prioritises foundational and supporting pages. |
| `seo-aeo-content-quality-auditor.md` | `seo-aeo-content-quality-auditor` | Audits a website, codebase, page, or content set for technical SEO, search intent, AEO, conversion paths, and publishing readiness, then produces prioritised fixes that can be implemented and verified. |
| `seo-aeo-internal-linking.md` | `seo-aeo-internal-linking` | Maps internal link opportunities between pages with relevant anchor text, placement instructions, orphan-page detection, and cannibalisation checks. |
| `seo-aeo-keyword-research.md` | `seo-aeo-keyword-research` | Researches and prioritises keywords from the site context and live search intent, including problem queries, question queries, difficulty tiers, and a content map. |
| `seo-aeo-landing-page-writer.md` | `seo-aeo-landing-page-writer` | Writes or improves conversion-focused landing pages for products, services, and offers with practical SEO and AEO structure. |
| `seo-aeo-meta-description-generator.md` | `seo-aeo-meta-description-generator` | Writes title tags, meta descriptions, Open Graph tags, and Twitter Card tags aligned to page intent and conversion goals. |
| `seo-aeo-orchestrator.md` | `seo-aeo-orchestrator` | Runs an audit-first SEO/AEO growth workflow from project discovery through implementation, foundational content, measurement setup, deployment verification, and optional weekly monitoring. |
| `seo-aeo-schema-generator.md` | `seo-aeo-schema-generator` | Generates and validates implementation-ready JSON-LD structured data for relevant page types and rich-result eligibility. |
| `seo-audit.md` | `seo-audit` | Diagnose and audit SEO issues affecting crawlability, indexation, rankings, and organic performance. |
| `seo-authority-builder.md` | `seo-authority-builder` | 'Analyzes content for E-E-A-T signals and suggests improvements to |
| `seo-cannibalization-detector.md` | `seo-cannibalization-detector` | Analyzes multiple provided pages to identify keyword overlap and potential cannibalization issues. |
| `seo-checklist-generator.md` | `seo-checklist-generator` | SEO Checklist Generator. |
| `seo-competitor-pages.md` | `seo-competitor-pages` | Generate SEO-optimized competitor comparison and alternatives pages. |
| `seo-content.md` | `seo-content` | Content quality and E-E-A-T analysis with AI citation readiness assessment. |
| `seo-content-auditor.md` | `seo-content-auditor` | Analyzes provided content for quality, E-E-A-T signals, and SEO best practices. |
| `seo-content-checker.md` | `seo-content-checker` | SEO Content Checker. |
| `seo-content-planner.md` | `seo-content-planner` | 'Creates comprehensive content outlines and topic clusters for SEO. |
| `seo-content-refresher.md` | `seo-content-refresher` | Identifies outdated elements in provided content and suggests updates to maintain freshness. |
| `seo-content-writer.md` | `seo-content-writer` | Writes SEO-optimized content based on provided keywords and topic briefs. |
| `seo-dataforseo.md` | `seo-dataforseo` | Use DataForSEO for live SERPs, keyword metrics, backlinks, competitor analysis, on-page checks, and AI visibility data. |
| `seo-directory-backlinks.md` | `seo-directory-backlinks` | Directory and backlink register: platform, domain, target URL, follow attribute, authority and spam scores, approval and NAP-match status. |
| `seo-drift.md` | `seo-drift` | Snapshot a site's SEO state and detect ranking, indexation, metadata, canonical, robots, schema, and on-page regressions over time. |
| `seo-forensic-incident-response.md` | `seo-forensic-incident-response` | Investigate sudden drops in organic traffic or rankings and run a structured forensic SEO incident response with triage, root-cause analysis and recovery plan. |
| `seo-fundamentals.md` | `seo-fundamentals` | Core principles of SEO including E-E-A-T, Core Web Vitals, technical foundations, content quality, and how modern search engines evaluate pages. |
| `seo-geo.md` | `seo-geo` | Optimize content for AI Overviews, ChatGPT, Perplexity, and other AI search systems. |
| `seo-health-score-calculator.md` | `seo-health-score-calculator` | SEO Health Score Calculator. |
| `seo-hreflang.md` | `seo-hreflang` | Hreflang and international SEO audit, validation, and generation. |
| `seo-image-gen.md` | `seo-image-gen` | Generate SEO-focused images such as OG cards, hero images, schema assets, product visuals, and infographics. |
| `seo-images.md` | `seo-images` | Image optimization analysis for SEO and performance. |
| `seo-keyword-strategist.md` | `seo-keyword-strategist` | Analyzes keyword usage in provided content, calculates density, suggests semantic variations and related terms based on the topic. |
| `seo-meta-optimizer.md` | `seo-meta-optimizer` | Creates optimized meta titles, descriptions, and URL suggestions based on character limits and best practices. |
| `seo-page.md` | `seo-page` | Deep single-page SEO analysis covering on-page elements, content quality, technical meta tags, schema, images, and performance. |
| `seo-plan.md` | `seo-plan` | Strategic SEO planning for new or existing websites. |
| `seo-programmatic.md` | `seo-programmatic` | Plan and audit programmatic SEO pages generated at scale from structured data. |
| `seo-schema.md` | `seo-schema` | Detect, validate, and generate Schema.org structured data. |
| `seo-sitemap.md` | `seo-sitemap` | Analyze existing XML sitemaps or generate new ones with industry templates. |
| `seo-snippet-hunter.md` | `seo-snippet-hunter` | Formats content to be eligible for featured snippets and SERP features. |
| `seo-structure-architect.md` | `seo-structure-architect` | Analyzes and optimizes content structure including header hierarchy, suggests schema markup, and internal linking opportunities. |
| `seo-technical.md` | `seo-technical` | Audit technical SEO across crawlability, indexability, security, URLs, mobile, Core Web Vitals, structured data, JavaScript rendering, and related platform signals like robots.txt and AI crawler access. |
| `sequence-psychologist.md` | `sequence-psychologist` | Plan email nurture and multi-touch communication sequences when each message should build trust and prepare the next decision. |
| `sequenzy-email-marketing.md` | `sequenzy-email-marketing` | Operate Sequenzy email campaigns through an authorized CLI or MCP connection: inspect audiences, prepare drafts, schedule approved sends, and verify delivery results. |
| `serply-search-mcp.md` | `serply-search-mcp` | Search Google, Bing, Google News and Google Scholar, and read public pages, with the Serply MCP server. |
| `server-management.md` | `server-management` | Server management principles and decision-making. |
| `service-mesh.md` | `service-mesh` | Implement Istio and Linkerd service meshes. |
| `service-mesh-expert.md` | `service-mesh-expert` | Review Istio or Linkerd topology, traffic policies, mTLS, observability and multi-cluster operations within an authorized environment. |
| `service-mesh-observability.md` | `service-mesh-observability` | Complete guide to observability patterns for Istio, Linkerd, and service mesh deployments. |
| `session-handoff.md` | `session-handoff` | Use when context approaches capacity, before /clear or /compact, when switching tasks, or when ending a coding session: produces a structured handoff artifact for the next session. |
| `setup-help.md` | `setup-help` | Walk a user through setup or installation one step at a time with the remaining steps visible. |
| `setup-matt-pocock-skills.md` | `setup-matt-pocock-skills` | Configure this repo for the engineering skills — set up its issue tracker, triage label vocabulary, and domain doc layout. |
| `sexual-health-analyzer.md` | `sexual-health-analyzer` | Sexual Health Analyzer |
| `shadcn.md` | `shadcn` | Manages shadcn/ui components and projects, providing context, documentation, and usage patterns for building modern design systems. |
| `shader-programming-glsl.md` | `shader-programming-glsl` | Expert guide for writing efficient GLSL shaders (Vertex/Fragment) for web and game engines, covering syntax, uniforms, and common effects. |
| `shark.md` | `shark` | Pitch a business idea to a Shark Tank-style panel of Claude sub-agent investors who grill it, hear a founder agent answer, and each go IN or OUT with a practice offer. |
| `sharp-coder.md` | `sharp-coder` | Two-layer performance skill combining disciplined THINK layer (surgical edits, simplicity) and terse SPEAK layer (caveman compression). |
| `sharp-edges.md` | `sharp-edges` | Review misuse-prone security APIs, configuration defaults, cryptographic interfaces and authentication ergonomics; verify concrete failure paths and version assumptions. |
| `shellcheck-configuration.md` | `shellcheck-configuration` | Master ShellCheck static analysis configuration and usage for shell script quality. |
| `shipping-and-launch.md` | `shipping-and-launch` | Prepares production launches. |
| `shipvela-publish.md` | `shipvela-publish` | Publish an explicitly selected website through the user's connected Shipvela MCP account, track the exact deployment, and return its live HTTPS URL after success. |
| `shopify-apps.md` | `shopify-apps` | Expert patterns for Shopify app development including Remix/React |
| `shopify-development.md` | `shopify-development` | Build Shopify apps, extensions, themes using GraphQL Admin API, Shopify CLI, Polaris UI, and Liquid. |
| `shopify-firebase-app.md` | `shopify-firebase-app` | Scaffold, extend and deploy Shopify embedded apps on Firebase with Nitrogen. |
| `shopify-review-triage.md` | `shopify-review-triage` | Turn public 1-3-star Shopify App Store review rows into a P0-P3 triage brief: incident risk, repeated friction, pricing confusion, feature requests, and an explicit needs-human-read bucket. |
| `short.md` | `short` | Rewrite the previous response more briefly while preserving the substance. |
| `show-the-change.md` | `show-the-change` | Explain a specific project change to non-programmers, with evidence and practical checks. |
| `signup-flow-cro.md` | `signup-flow-cro` | You are an expert in optimizing signup and registration flows. |
| `similarity-search-patterns.md` | `similarity-search-patterns` | Implement efficient similarity search with vector databases. |
| `simplify-code.md` | `simplify-code` | Review a diff for clarity and safe simplifications, then optionally apply low-risk fixes. |
| `since-cutoff.md` | `since-cutoff` | Find which APIs of a project's pinned Python dependencies changed after the model's training cutoff, where the code uses them, and write short AGENTS.md or CLAUDE.md notes. |
| `site-architecture.md` | `site-architecture` | Plan or restructure website hierarchy, navigation, URL patterns, breadcrumbs, and internal linking. |
| `site-comparison-report-generator.md` | `site-comparison-report-generator` | Site Comparison Report Generator. |
| `sitemap-generator.md` | `sitemap-generator` | XML Sitemap Generator. |
| `skeleton-first.md` | `skeleton-first` | Prove a data/AI/agent workflow end to end on a tiny sample, find cheap wins, then scale in cost-gated steps within budget. |
| `skeuomorphism.md` | `skeuomorphism` | Web and App implementation guide for Skeuomorphism. |
| `skill-audit.md` | `skill-audit` | Pre-install review framework for AI agent skills: inspect complete content, permissions, dependencies and suspicious behavior before activation. |
| `skill-check.md` | `skill-check` | Validate Claude Code skills against the agentskills specification. |
| `skill-creator.md` | `skill-creator` | Create and review reusable skill drafts with bundled Python scaffolding, basic frontmatter validation and ZIP packaging helpers. |
| `skill-creator-ms.md` | `skill-creator-ms` | Guide for creating effective skills for AI coding agents working with Azure SDKs and Microsoft Foundry services. |
| `skill-developer.md` | `skill-developer` | Comprehensive guide for creating and managing skills in Claude Code with auto-activation system, using an illustrative custom hook architecture and concise progressive disclosure and progressive disclosure pattern. |
| `skill-gap-analysis.md` | `skill-gap-analysis` | Skill gap register: employee, skill area, current against required level, gap severity and recommended training. |
| `skill-improver.md` | `skill-improver` | Iteratively improve a Claude Code skill using the skill-reviewer agent until it meets quality standards. |
| `skill-installer.md` | `skill-installer` | Validate and install explicitly selected local skill trees into a workspace, with full-tree Claude registration, backups and ZIP packaging. |
| `skill-issue.md` | `skill-issue` | Find out why a coding-agent skill won't fire — grade each SKILL.md A–F on activation, simulate which skill a prompt triggers, and flag collisions where one silently shadows another. |
| `skill-optimizer.md` | `skill-optimizer` | Diagnose and optimize Agent Skills (SKILL.md) with real session data and research-backed static analysis. |
| `skill-porter.md` | `skill-porter` | Preview conservative tool-name translations and copy complete local skill bundles for manual adaptation to Google Antigravity. |
| `skill-rails-upgrade.md` | `skill-rails-upgrade` | Analyze Rails apps and provide upgrade assessments |
| `skill-router.md` | `skill-router` | Use when the user is unsure which skill to use or where to start. |
| `skill-scanner.md` | `skill-scanner` | Scan agent skills for security issues before adoption. |
| `skill-security-audit.md` | `skill-security-audit` | Audit an Agent Skill, MCP server, connector, or desktop extension before installation by tracing code, dependencies, permissions, credentials, data flow, and irreversible actions. |
| `skill-seekers.md` | `skill-seekers` | Convert approved documentation, repositories, or PDFs into an agent skill using the Skill Seekers workflow, then review the generated content. |
| `skill-sentinel.md` | `skill-sentinel` | Auditoria e evolucao do ecossistema de skills. |
| `skill-skill.md` | `skill-skill` | Write, upgrade or audit a Claude skill so it changes what gets generated: forcing functions, triggerable descriptions, and a static audit script with a 0-100 health score. |
| `skill-suggester.md` | `skill-suggester` | Scan prompt history for recurring patterns and unmet needs, then propose new skills or command templates |
| `skill-writer.md` | `skill-writer` | Create and improve agent skills following the Agent Skills specification. |
| `skin-health-analyzer.md` | `skin-health-analyzer` | Analyze skin health data, identify skin problem patterns, assess skin health status. |
| `skyvern-browser-automation.md` | `skyvern-browser-automation` | AI-powered browser automation — navigate sites, fill forms, extract structured data, log in with stored credentials, and build reusable workflows. |
| `slack-bot-builder.md` | `slack-bot-builder` | Build Slack apps using the Bolt framework across Python, |
| `slack-gif-creator.md` | `slack-gif-creator` | A toolkit providing utilities and knowledge for creating animated GIFs optimized for Slack. |
| `sleep-analyzer.md` | `sleep-analyzer` | 分析睡眠数据、识别睡眠模式、评估睡眠质量，并提供个性化睡眠改善建议。支持与其他健康数据的关联分析。 |
| `slideops.md` | `slideops` | Turn a repository into a cited HTML slide deck and detect the day it drifts from the code. |
| `slideshow.md` | `slideshow` | Build live HyperFrames slide decks with fragments, branching hotspots and presenter notes. |
| `slo-implementation.md` | `slo-implementation` | Framework for defining and implementing Service Level Indicators (SLIs), Service Level Objectives (SLOs), and error budgets. |
| `smart-contract-formal-verification.md` | `smart-contract-formal-verification` | Foundry and Soroban formal invariant verification register: state transition rules, boundary invariant properties, and symbolic execution checks. |
| `smart-contract-upgrade-governance.md` | `smart-contract-upgrade-governance` | Soroban WASM upgrade governance register: executable bytecode hash, timelocked migration delays, and multi-sig authorization quorum. |
| `smart-git-automation.md` | `smart-git-automation` | Smart change detection, auto branch naming, and streamlined commit/PR workflow |
| `smtp-penetration-testing.md` | `smtp-penetration-testing` | Conduct comprehensive security assessments of SMTP (Simple Mail Transfer Protocol) servers to identify vulnerabilities including open relays, user enumeration, weak authentication, and misconfiguration. |
| `snowflake-development.md` | `snowflake-development` | Comprehensive Snowflake development assistant covering SQL best practices, data pipeline design (Dynamic Tables, Streams, Tasks, Snowpipe), Cortex AI functions, Cortex Agents, Snowpark Python, dbt integration, performance tuning, and security hardening. |
| `soc2-compliance.md` | `soc2-compliance` | Implement SOC 2 Trust Services Criteria. |
| `social-content.md` | `social-content` | Help plan and draft social content; publishing capabilities depend on the actual connected account and tool permissions. |
| `social-media-setup.md` | `social-media-setup` | Social media register: platforms and handles, post captions and hashtags, publishing cadence, approval status and profile checklist. |
| `social-metadata-hardening.md` | `social-metadata-hardening` | Fix social sharing previews so URLs render as rich cards on Facebook, LinkedIn, X/Twitter, WhatsApp, Telegram, and more. |
| `social-orchestrator.md` | `social-orchestrator` | Orquestrador unificado de canais sociais — coordena Instagram, Telegram e WhatsApp em um unico fluxo de trabalho. |
| `social-post-writer-seo.md` | `social-post-writer-seo` | Social Media Strategist and Content Writer. |
| `social-proof-architect.md` | `social-proof-architect` | Select and place genuine testimonials, case studies, and other proof when an audience needs evidence at specific trust barriers. |
| `soft-pastel.md` | `soft-pastel` | Web and App implementation guide for Soft Pastel Design. |
| `software-architecture.md` | `software-architecture` | Guide for quality focused software architecture. |
| `solidity-security.md` | `solidity-security` | Master smart contract security best practices, vulnerability prevention, and secure Solidity development patterns. |
| `solidping.md` | `solidping` | Run SolidPing uptime monitoring through its hosted MCP server: list and diagnose checks, read results and incidents, create checks across 40+ types, and manage status pages. |
| `sop-company-wiki.md` | `sop-company-wiki` | SOP and company wiki register: title, category, department, owner, version, priority and review dates. |
| `sops-encryption.md` | `sops-encryption` | Encrypt files and configs with Mozilla SOPS. |
| `soroban-contract-audit.md` | `soroban-contract-audit` | Soroban smart contract security audit register: authorization checks, panic pathways, integer overflows, and storage footprint verification for Stellar. |
| `soroban-liquidity-pool.md` | `soroban-liquidity-pool` | Automated market maker liquidity pool register: constant-product invariant curves, swap fee tiers, and LP token shares for Soroban DeFi. |
| `soroban-oracle-data-feed-audit.md` | `soroban-oracle-data-feed-audit` | DeFi price oracle integration and safety audit register: heartbeat bounds, stale price threshold reversion, and TWAP medianizer validation. |
| `soroban-storage-ttl-lifecycle.md` | `soroban-storage-ttl-lifecycle` | Soroban ledger state rent and TTL extension register: live state tracking, bump thresholds, rent fee reserves, and archive boundaries. |
| `soroban-token-minter.md` | `soroban-token-minter` | Soroban SEP-41 token contract architecture register: admin control, supply caps, metadata standard, and transfer event emissions on Stellar. |
| `source-document-filing.md` | `source-document-filing` | Source document register: document type and number, party, amount, index key, storage location, retention period and verification. |
| `source-driven-development.md` | `source-driven-development` | Grounds every implementation decision in official documentation. |
| `spark-optimization.md` | `spark-optimization` | Optimize Apache Spark jobs with partitioning, caching, shuffle optimization, and memory tuning. |
| `spatial-computing-ui.md` | `spatial-computing-ui` | Web and App implementation guide for Spatial Computing UI. |
| `spatial-design.md` | `spatial-design` | Web and App implementation guide for Spatial Design. |
| `spec-driven-development.md` | `spec-driven-development` | Creates specs before coding. |
| `spec-driven-loop.md` | `spec-driven-loop` | Freeze PRD, technical design, and acceptance criteria before medium-to-large Codex work; coordinate agents with explicit ownership, then judge delivery from diffs, tests, and evidence. |
| `spec-to-code-compliance.md` | `spec-to-code-compliance` | Verifies code implements exactly what documentation specifies for blockchain audits. |
| `speckit-updater.md` | `speckit-updater` | SpecKit Safe Update |
| `speed.md` | `speed` | Launch RSVP speed reader for text |
| `spline-3d-integration.md` | `spline-3d-integration` | Use when adding interactive 3D scenes from Spline.design to web projects, including React embedding and runtime control API. |
| `spreadsheet-manual-build.md` | `spreadsheet-manual-build` | Spreadsheet Manual Build: an empty Excel workbook or CSV from a confirmed field list, formatted and validated. |
| `sql-injection-testing.md` | `sql-injection-testing` | Execute comprehensive SQL injection vulnerability assessments on web applications to identify database security flaws, demonstrate exploitation techniques, and validate input sanitization mechanisms. |
| `sql-optimization-patterns.md` | `sql-optimization-patterns` | Diagnose slow SQL with query plans, preserve query results, and verify indexing or query changes against representative data. |
| `sql-pro.md` | `sql-pro` | Master modern SQL with cloud-native databases, OLTP/OLAP optimization, and advanced query techniques. |
| `sql-sentinel.md` | `sql-sentinel` | Audit SQL for the cost & performance anti-patterns that burn warehouse credits. |
| `sqlmap-database-pentesting.md` | `sqlmap-database-pentesting` | Provide systematic methodologies for automated SQL injection detection and exploitation using SQLMap. |
| `squirrel.md` | `squirrel` | Full-cycle AI coding skill: plans, builds, tests, lints, fixes bugs, and writes production-grade docs. |
| `src-hunter.md` | `src-hunter` | Bug-bounty/SRC vulnerability-hunting workflow: five-phase methodology (intake, recon, enumeration, hunt, report) with attack playbooks for SQLi, XSS, RCE, SSRF, IDOR, CSRF, path traversal, and file upload. |
| `sre-dashboards.md` | `sre-dashboards` | Design and operationalize SRE dashboards that surface reliability, latency, |
| `sred-project-organizer.md` | `sred-project-organizer` | Take a list of projects and their related documentation, and organize them into the SRED format for submission. |
| `sred-work-summary.md` | `sred-work-summary` | Go back through the previous year of work and create a Notion doc that groups relevant links into projects that can then be documented as SRED projects. |
| `ssh-configuration.md` | `ssh-configuration` | Configure SSH servers and clients securely. |
| `ssh-penetration-testing.md` | `ssh-penetration-testing` | Conduct comprehensive SSH security assessments including enumeration, credential attacks, vulnerability exploitation, tunneling techniques, and post-exploitation activities. |
| `sshepherd.md` | `sshepherd` | Zero-knowledge SSH ops CLI — server health checks, docker/systemd control, log tailing, Postgres introspection, and declarative deploys, without ever exposing credentials to the agent. |
| `ssl-tls-management.md` | `ssl-tls-management` | Manage SSL/TLS certificates with Let's Encrypt and internal PKI. |
| `stageshow.md` | `stageshow` | Use when a user asks for a React product illustration, animated walkthrough, product demo, or cursor-led UI animation. |
| `stakeholder-investor-reports.md` | `stakeholder-investor-reports` | Stakeholder report register: stakeholder, period, key metrics, preparer, approver, send date and report link. |
| `startup-analyst.md` | `startup-analyst` | Expert startup business analyst specializing in market sizing, financial modeling, competitive analysis, and strategic planning for early-stage companies. |
| `startup-business-analyst-business-case.md` | `startup-business-analyst-business-case` | 'Generate comprehensive investor-ready business case document with |
| `startup-business-analyst-financial-projections.md` | `startup-business-analyst-financial-projections` | 'Create detailed 3-5 year financial model with revenue, costs, cash |
| `startup-business-analyst-market-opportunity.md` | `startup-business-analyst-market-opportunity` | 'Generate comprehensive market opportunity analysis with TAM/SAM/SOM |
| `startup-financial-modeling.md` | `startup-financial-modeling` | Build comprehensive 3-5 year financial models with revenue projections, cost structures, cash flow analysis, and scenario planning for early-stage startups. |
| `startup-metrics-framework.md` | `startup-metrics-framework` | Comprehensive guide to tracking, calculating, and optimizing key performance metrics for different startup business models from seed through Series A. |
| `state-machine.md` | `state-machine` | Renders every state of a component you choose on a throwaway page, with mock data and a switcher, so you can work on each state. |
| `statsmodels.md` | `statsmodels` | Statsmodels is Python's premier library for statistical modeling, providing tools for estimation, inference, and diagnostics across a wide range of statistical methods. |
| `stellar-anchor-integration.md` | `stellar-anchor-integration` | Stellar anchor protocol compliance register: SEP-10 web authentication, SEP-24 interactive deposit and withdrawal, and KYC lifecycle. |
| `stellar-asset-clawback-compliance.md` | `stellar-asset-clawback-compliance` | Regulated Stellar asset clawback architecture register: issuer authorization flags, claimable balance revocations, and regulatory audit trail. |
| `stellar-escrow-timelock.md` | `stellar-escrow-timelock` | Decentralized conditional escrow and timelock contract register: multi-signature release conditions, clawback expiry, and settlement triggers. |
| `stellar-multisig-threshold-coordinator.md` | `stellar-multisig-threshold-coordinator` | Multi-signature signer and threshold coordination register: weight configurations, master key locks, and cosigner quorum thresholds for Stellar. |
| `steve-jobs.md` | `steve-jobs` | Agente que simula Steve Jobs — cofundador da Apple, CEO da Pixar, fundador da NeXT, o maior designer de produtos tecnologicos da historia e o mais influente apresentador de produtos do mundo. |
| `stitch-design-taste.md` | `stitch-design-taste` | Use when generating Google Stitch DESIGN.md systems for premium typography, color, layout, motion intent, and anti-generic UI rules. |
| `stitch-loop.md` | `stitch-loop` | Teaches agents to iteratively build websites using Stitch with an autonomous baton-passing loop pattern |
| `stitch-ui-design.md` | `stitch-ui-design` | Expert guidance for crafting effective prompts in Google Stitch, the AI-powered UI design tool by Google Labs. |
| `story-bible-continuity.md` | `story-bible-continuity` | Deterministic continuity check for long manuscripts against a story bible: name drift, age arithmetic, era anachronisms, unpaid foreshadowing, POV leaks. |
| `stride-analysis-patterns.md` | `stride-analysis-patterns` | Apply STRIDE methodology to systematically identify threats. |
| `structured-data-validator.md` | `structured-data-validator` | Structured Data Validator. |
| `styleseed-design-review.md` | `styleseed-design-review` | Reviews UI/frontend code and tells you exactly why it \"looks AI-generated\" — then how to fix it. |
| `subagent-driven-development.md` | `subagent-driven-development` | Use when executing implementation plans with independent tasks in the current session |
| `subagent-orchestrator.md` | `subagent-orchestrator` | Coordinate quota-aware parallel subagents for large, multi-file Antigravity tasks. |
| `subject-line-psychologist.md` | `subject-line-psychologist` | Draft email subject lines and notification copy matched to audience and sequence position when earning attention requires clarity and truthful curiosity. |
| `suno-lyrics-to-song.md` | `suno-lyrics-to-song` | Install and use the official Lyrics to Song package, pinned by digest, for paid hosted work on the Beatra service. |
| `supabase.md` | `supabase` | Use when doing ANY task involving Supabase. |
| `supabase-postgres-best-practices.md` | `supabase-postgres-best-practices` | Postgres performance optimization and best practices from Supabase. |
| `super-code.md` | `super-code` | Standing house style to enforce dense, correct, and idiomatic code on all coding tasks. |
| `superpowers-lab.md` | `superpowers-lab` | Evaluate experimental Claude workflow skills in an isolated lab with reproducible tasks, observed results, and explicit adoption criteria. |
| `supply-chain-attack-recon.md` | `supply-chain-attack-recon` | Authorized read-only review of public software supply-chain exposure |
| `supply-chain-attack-response.md` | `supply-chain-attack-response` | Detect, respond to, and prevent software supply chain attacks on package |
| `supply-chain-risk-auditor.md` | `supply-chain-risk-auditor` | Identifies dependencies at heightened risk of exploitation or takeover. |
| `supply-chain-security.md` | `supply-chain-security` | Software supply-chain security assessment: SBOM generation, SCA scanning, CI/CD pipeline review, container image audit, build integrity, dependency provenance, and vulnerability reachability verification. |
| `sveltekit.md` | `sveltekit` | Build full-stack web applications with SvelteKit — file-based routing, SSR, SSG, API routes, and form actions in one framework. |
| `swift.md` | `swift` | Language-specific super-code guidelines for swift. |
| `swift-concurrency-expert.md` | `swift-concurrency-expert` | Review and fix Swift concurrency issues such as actor isolation and Sendable violations. |
| `swiftui-expert-skill.md` | `swiftui-expert-skill` | Write, review, and refactor SwiftUI for iOS or macOS, covering data flow, view composition, performance, identity, environment, localization, animation, API migration, and Instruments traces. |
| `swiftui-liquid-glass.md` | `swiftui-liquid-glass` | Implement or review SwiftUI Liquid Glass APIs with correct fallbacks and modifier order. |
| `swiftui-performance-audit.md` | `swiftui-performance-audit` | Audit SwiftUI performance issues from code review and profiling evidence. |
| `swiftui-ui-patterns.md` | `swiftui-ui-patterns` | Apply proven SwiftUI UI patterns for navigation, sheets, async state, and reusable screens. |
| `swiftui-view-refactor.md` | `swiftui-view-refactor` | Refactor SwiftUI views into smaller components with stable, explicit data flow. |
| `swiss-design.md` | `swiss-design` | Web and App implementation guide for Swiss Design (International Typographic Style). |
| `sympy.md` | `sympy` | SymPy is a Python library for symbolic mathematics that enables exact computation using mathematical symbols rather than numerical approximations. |
| `syncbook-discovery.md` | `syncbook-discovery` | Find reciprocal collaborators on Syncbook or prepare a private profile draft for human review using only explicitly supplied task facts. |
| `synthwave.md` | `synthwave` | Web and App implementation guide for Synthwave. |
| `system-prompt-lookup.md` | `system-prompt-lookup` | Checks what a shipped AI product's system prompt and tool schema actually say, by reading a dated archive of captured prompts instead of recalling them. |
| `systematic-debugging.md` | `systematic-debugging` | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| `systemd-services.md` | `systemd-services` | Create and manage systemd services and timers. |
| `systems-programming-rust-project.md` | `systems-programming-rust-project` | You are a Rust project architecture expert specializing in scaffolding production-ready Rust applications. |
| `taasky.md` | `taasky` | Negotiate terms with another person or their agent through the hosted Taasky MCP server: meeting times, prices, dates. |
| `tailwind-design-system.md` | `tailwind-design-system` | Build production-ready design systems with Tailwind CSS, including design tokens, component variants, responsive patterns, and accessibility. |
| `tailwind-patterns.md` | `tailwind-patterns` | Tailwind CSS v4 principles. |
| `taisly-social-media-posting.md` | `taisly-social-media-posting` | Use Taisly Agent Kit to prepare and publish approved short-form video posts across TikTok, Instagram Reels, YouTube Shorts, X, and Facebook. |
| `takeout-coupon.md` | `takeout-coupon` | Call takeout coupon API to fetch hidden coupon lists, red packets and aggregated redemption pages for platforms (Meituan, Taobao Flash/Ele.me, JD.com). |
| `talivia-agent-kit.md` | `talivia-agent-kit` | Set up and verify Talivia revenue analytics through MCP, with explicit confirmation for website changes and payment attribution. |
| `talking-avatar-video.md` | `talking-avatar-video` | Install and use the official Talking Avatar Video package, pinned by digest, for paid hosted work on the Beatra service. |
| `tanstack-query-expert.md` | `tanstack-query-expert` | Expert in TanStack Query (React Query) — asynchronous state management. |
| `task-intelligence.md` | `task-intelligence` | Protocolo de Inteligência Pré-Tarefa — planeja a tarefa e consulta apenas agentes disponíveis, relevantes e autorizados quando o benefício justificar o custo. |
| `tastegate.md` | `tastegate` | Build or fix a frontend so it looks designed, not AI-generated, then prove it in a real browser: renders at phone and desktop width and fails on overlap, low contrast and AI-slop defaults. |
| `tavily-web.md` | `tavily-web` | Web search, content extraction, crawling, and research capabilities using Tavily API. |
| `tax-register.md` | `tax-register` | Tax register: sales and purchase tax, withholding deducted and received, net payable, filing due date and days remaining. |
| `tcm-constitution-analyzer.md` | `tcm-constitution-analyzer` | 分析中医体质数据、识别体质类型、评估体质特征,并提供个性化养生建议。支持与营养、运动、睡眠等健康数据的关联分析。 |
| `tdd.md` | `tdd` | Test-driven development. |
| `tdd-orchestrator.md` | `tdd-orchestrator` | Master TDD orchestrator specializing in red-green-refactor discipline, multi-agent workflow coordination, and comprehensive test-driven development practices. |
| `tdd-workflow.md` | `tdd-workflow` | Test-Driven Development workflow principles. |
| `tdd-workflows.md` | `tdd-workflows` | Use when working with tdd workflows tdd cycle (Alias for tdd-workflows-tdd-cycle) |
| `tdd-workflows-tdd-cycle.md` | `tdd-workflows-tdd-cycle` | Use when working with tdd workflows tdd cycle |
| `tdd-workflows-tdd-green.md` | `tdd-workflows-tdd-green` | Implement the minimal code needed to make failing tests pass in the TDD green phase. |
| `tdd-workflows-tdd-red.md` | `tdd-workflows-tdd-red` | Generate failing tests for the TDD red phase to define expected behavior and edge cases. |
| `tdd-workflows-tdd-refactor.md` | `tdd-workflows-tdd-refactor` | Use when working with tdd workflows tdd refactor |
| `tds-booking-payment.md` | `tds-booking-payment` | TDS register: payee PAN, payment nature, rate and amount deducted, deposit date and challan reference, return filing and ledger variance. |
| `teach.md` | `teach` | Teach the user a new skill or concept, within this workspace. |
| `team-calendar.md` | `team-calendar` | Team calendar: event, type, date and time with time zone, attendees, organizer, location and source module. |
| `team-collaboration-issue.md` | `team-collaboration-issue` | You are a GitHub issue resolution expert specializing in systematic bug investigation, feature implementation, and collaborative development workflows. |
| `team-collaboration-standup-notes.md` | `team-collaboration-standup-notes` | You are an expert team communication specialist focused on async-first standup practices, AI-assisted note generation from commit history, and effective remote team coordination patterns. |
| `team-composition-analysis.md` | `team-composition-analysis` | Design optimal team structures, hiring plans, compensation strategies, and equity allocation for early-stage startups from pre-seed through Series A. |
| `teardown.md` | `teardown` | Creates technical illustrations of physical objects and of how things work, such as display pixels or interface layers, with coherent views, fine linework and part fills. |
| `tech-matrix.md` | `tech-matrix` | Reference document for monopoly tech-matrix. |
| `tech-writing-proofread.md` | `tech-writing-proofread` | Proofreads English technical writing for typos, grammar, punctuation, terminology consistency, jargon, and structure; returns an itemized Original → Suggestion → Reason list without rewriting the document. |
| `technical-change-tracker.md` | `technical-change-tracker` | Track code changes with structured JSON records, state machine enforcement, and AI session handoff for bot continuity |
| `technical-tutorials.md` | `technical-tutorials` | When the user wants to create step-by-step technical tutorials, quickstarts, or code walkthroughs. |
| `telegram.md` | `telegram` | Integracao completa com Telegram Bot API. |
| `telegram-channel-ads.md` | `telegram-channel-ads` | Vet and price ad posts in Telegram channels: reach benchmarks by size, topic and language, ad-network and channel-age checks, CPM and deletion-window math. |
| `telegram-mini-app.md` | `telegram-mini-app` | Expert in building Telegram Mini Apps (TWA) - web apps that run |
| `template-library.md` | `template-library` | Template register: name, type, owning module and department, owner, last updated and content link. |
| `templates.md` | `templates` | Project scaffolding templates for new applications. |
| `temporal-golang-pro.md` | `temporal-golang-pro` | Use when building durable distributed systems with Temporal Go SDK. |
| `temporal-python-pro.md` | `temporal-python-pro` | Master Temporal workflow orchestration with Python SDK. |
| `temporal-python-testing.md` | `temporal-python-testing` | Comprehensive testing approaches for Temporal workflows using pytest, progressive disclosure resources for specific testing scenarios. |
| `terraform-aws.md` | `terraform-aws` | Provision AWS infrastructure with Terraform. |
| `terraform-aws-modules.md` | `terraform-aws-modules` | Terraform module creation for AWS — reusable modules, state management, and HCL best practices. |
| `terraform-azure.md` | `terraform-azure` | Provision Azure infrastructure with Terraform. |
| `terraform-gcp.md` | `terraform-gcp` | Provision GCP infrastructure with Terraform. |
| `terraform-infrastructure.md` | `terraform-infrastructure` | Terraform infrastructure as code workflow for provisioning cloud resources, creating reusable modules, and managing infrastructure at scale. |
| `terraform-module-library.md` | `terraform-module-library` | Production-ready Terraform module patterns for AWS, Azure, and GCP infrastructure. |
| `terraform-skill.md` | `terraform-skill` | Terraform infrastructure as code best practices |
| `terraform-specialist.md` | `terraform-specialist` | Expert Terraform/OpenTofu specialist mastering advanced IaC automation, state management, and enterprise infrastructure patterns. |
| `test-automator.md` | `test-automator` | Master AI-powered test automation with modern frameworks, self-healing tests, and comprehensive quality engineering. |
| `test-driven-development.md` | `test-driven-development` | Use a failing behavioral test to guide a feature or bug fix, then implement and refactor with relevant regression checks. |
| `test-fixing.md` | `test-fixing` | Systematically identify and fix all failing tests using smart grouping strategies. |
| `test-framework-migration-skill.md` | `test-framework-migration-skill` | Migrates and converts test automation scripts between Selenium, Playwright, Puppeteer, and Cypress. |
| `test-guard.md` | `test-guard` | Review generated or changed test code against universal testing rules before it ships or is presented for approval. |
| `testing-patterns.md` | `testing-patterns` | Jest testing patterns, factory functions, mocking strategies, and TDD workflow. |
| `testing-qa.md` | `testing-qa` | Comprehensive testing and QA workflow covering unit testing, integration testing, E2E testing, browser automation, and quality assurance. |
| `testng-skill.md` | `testng-skill` | Generates TestNG tests in Java with groups, data providers, parallel execution, XML suite configuration, and listeners. |
| `text-to-html-converter.md` | `text-to-html-converter` | Text to HTML Converter. |
| `text-translator.md` | `text-translator` | Text Translator. |
| `the-honoured-one.md` | `the-honoured-one` | Forces the AI to fully load context and read relevant files before performing complex, multi-file tasks, architectural changes, or debugging. |
| `theme-factory.md` | `theme-factory` | This skill provides a curated collection of professional font and color themes, each with carefully selected color palettes and font pairings. |
| `thick-client.md` | `thick-client` | Authorized security testing of desktop thick clients: local storage, update channels, IPC, traffic interception, and client-side trust-boundary review. |
| `threat-hunting.md` | `threat-hunting` | Blue-team threat hunting: detection engineering with Sigma/YARA, SIEM query design, and validation of incident detections against known technique patterns. |
| `threat-mitigation-mapping.md` | `threat-mitigation-mapping` | Map identified threats to appropriate security controls and mitigations. |
| `threat-modeling.md` | `threat-modeling` | Conduct threat modeling using STRIDE methodology. |
| `threat-modeling-expert.md` | `threat-modeling-expert` | Expert in threat modeling methodologies, security architecture review, and risk assessment. |
| `threejs-animation.md` | `threejs-animation` | Three.js animation - keyframe animation, skeletal animation, morph targets, animation mixing. |
| `threejs-fundamentals.md` | `threejs-fundamentals` | Three.js scene setup, cameras, renderer, Object3D hierarchy, coordinate systems. |
| `threejs-geometry.md` | `threejs-geometry` | Three.js geometry creation - built-in shapes, BufferGeometry, custom geometry, instancing. |
| `threejs-interaction.md` | `threejs-interaction` | Three.js interaction - raycasting, controls, mouse/touch input, object selection. |
| `threejs-lighting.md` | `threejs-lighting` | Three.js lighting - light types, shadows, environment lighting. |
| `threejs-loaders.md` | `threejs-loaders` | Three.js asset loading - GLTF, textures, images, models, async patterns. |
| `threejs-materials.md` | `threejs-materials` | Three.js materials - PBR, basic, phong, shader materials, material properties. |
| `threejs-postprocessing.md` | `threejs-postprocessing` | Three.js post-processing - EffectComposer, bloom, DOF, screen effects. |
| `threejs-shaders.md` | `threejs-shaders` | Three.js shaders - GLSL, ShaderMaterial, uniforms, custom effects. |
| `threejs-skills.md` | `threejs-skills` | Create 3D scenes, interactive experiences, and visual effects using Three.js. |
| `threejs-textures.md` | `threejs-textures` | Three.js textures - texture types, UV mapping, environment maps, texture settings. |
| `tile-design.md` | `tile-design` | Web and App implementation guide for Tile Design. |
| `time-ledger.md` | `time-ledger` | Natural-language time tracking: parse what the user says they did into Activity/Minutes/Date rows in their own Notion database — asking instead of guessing when unsure. |
| `time-machine-recovery.md` | `time-machine-recovery` | Diagnose failed or stalled macOS Time Machine backups and recover space on local APFS destinations that remain full after backup deletion. |
| `time-tracking.md` | `time-tracking` | Time entry register: employee, project, client, task, hours, billable flag, rate and amount, invoice and approver. |
| `title-meta-length-counter.md` | `title-meta-length-counter` | Title & Meta Length Counter. |
| `tmux.md` | `tmux` | Expert tmux session, window, and pane management for terminal multiplexing, persistent remote workflows, and shell scripting automation. |
| `to-issues.md` | `to-issues` | Break a plan, spec, or PRD into independently-grabbable issues on the project issue tracker using tracer-bullet vertical slices. |
| `to-prd.md` | `to-prd` | Turn the current conversation into a PRD and publish it to the project issue tracker — no interview, just synthesis of what you've already discussed. |
| `tokenleak.md` | `tokenleak` | Token-lean rules for coding agents: cut the context re-sent on every later call (big reads, noisy logs, re-reads, serial calls) without losing correctness. |
| `tokenwise.md` | `tokenwise` | Measurement-driven model router for Claude Code. |
| `tone-of-voice-analyzer.md` | `tone-of-voice-analyzer` | Tone of Voice Analyzer. |
| `tool-design.md` | `tool-design` | Build tools that agents can use effectively, including architectural reduction patterns. |
| `tool-use-guardian.md` | `tool-use-guardian` | Triage tool failures, validate responses and resume bounded workflows using replay-safe retries and explicit handling of unknown write outcomes. |
| `tools-page-seo-optimizer.md` | `tools-page-seo-optimizer` | Framework-agnostic SEO workflow for any site with multiple tool, product, or feature pages. |
| `top-web-vulnerabilities.md` | `top-web-vulnerabilities` | Provide an illustrative, overlapping reference for common web application vulnerability patterns organized by category. |
| `track-management.md` | `track-management` | Use this skill when creating, managing, or working with Conductor tracks - the logical work units for features, bugs, and refactors. |
| `traderspy-market-briefing.md` | `traderspy-market-briefing` | Crypto market briefing from live TraderSpy data: majors, funding, open interest, top-trader lean, fresh AI signals and screener movers. |
| `traderspy-market-screener.md` | `traderspy-market-screener` | Scan the most-traded crypto futures pairs for up to 3 technical conditions in one TraderSpy call, compare coins, and backtest what followed a condition. |
| `traderspy-position-check.md` | `traderspy-position-check` | Health-check crypto futures positions the user describes, with TraderSpy data: liquidation and stop distance, multi-timeframe read, funding and top-trader side. |
| `traderspy-smart-money.md` | `traderspy-smart-money` | Track what top crypto futures traders hold on Binance, Hyperliquid, Bybit and OKX with TraderSpy: elite leaderboard, positions, trader profiles and history. |
| `traderspy-technical-analysis.md` | `traderspy-technical-analysis` | Read one crypto futures pair with TraderSpy: 19 indicators on up to 3 timeframes in one call, key levels, funding, open interest and positioning. |
| `traderspy-trading-signals.md` | `traderspy-trading-signals` | Fetch and explain TraderSpy's AI crypto futures signals: entry, take-profit ladder, stop, triggers, status against the live price, and how recent signals resolved. |
| `trading-ledger.md` | `trading-ledger` | A trading journal that captures the decision, not just the fill: thesis, plan, and emotion at the moment of entry, written to the user's own Notion database; reviews grade decisions, not P&L. |
| `traffic-potential-calculator.md` | `traffic-potential-calculator` | Traffic Potential Calculator. |
| `train-sentence-transformers.md` | `train-sentence-transformers` | Train or fine-tune SentenceTransformer, CrossEncoder, and SparseEncoder models for retrieval, similarity, clustering, classification, reranking, and related embedding tasks. |
| `transformers-js.md` | `transformers-js` | Use Transformers.js to run state-of-the-art machine learning models directly in JavaScript/TypeScript. |
| `travel-health-analyzer.md` | `travel-health-analyzer` | 分析旅行健康数据、评估目的地健康风险、提供疫苗接种建议、生成多语言紧急医疗信息卡片。支持WHO/CDC数据集成的专业级旅行健康风险评估。 |
| `travel-planner.md` | `travel-planner` | 旅行/行程规划需求时使用:规划去某地旅行、X天X城、带老人孩子、自驾、假期安排等。产出逐日行程表、预算估算(经济/舒适/奢华三档)、交通住宿建议、景点美食清单。必须先问预算,预算未确认只输出问题清单;事实数据带来源和查询日期。 |
| `tree-ring-memory.md` | `tree-ring-memory` | Use Tree Ring Memory for local-first AI-agent memory lifecycle work: recall, evidence, audit, forgetting, and consolidation without transcript dumping. |
| `trending-keyword-visualizer.md` | `trending-keyword-visualizer` | Trending Keyword Visualizer. |
| `triage.md` | `triage` | Move issues and external PRs through a state machine of triage roles — categorise, verify, grill if needed, and write agent-ready briefs. |
| `triage-validation.md` | `triage-validation` | Finding validation before writing any report |
| `trigger-dev.md` | `trigger-dev` | Trigger.dev expert for background jobs, AI workflows, and reliable |
| `trip-coupon.md` | `trip-coupon` | Call trip/travel coupon API to fetch travel coupons including DiDi ride-hailing gift packages and hotel coupon bundles. |
| `trl-training.md` | `trl-training` | Train and fine-tune transformer language models using TRL (Transformers Reinforcement Learning). |
| `trpc-fullstack.md` | `trpc-fullstack` | Build end-to-end type-safe APIs with tRPC — routers, procedures, middleware, subscriptions, and Next.js/React integration patterns. |
| `trust-calibrator.md` | `trust-calibrator` | Diagnose audience trust barriers and calibrate proof, certainty, and credibility signals when messaging overclaims or fails to reassure. |
| `tune-monitor.md` | `tune-monitor` | Analyze a Monte Carlo monitor and recommend config changes to reduce alert noise. |
| `turborepo-caching.md` | `turborepo-caching` | Configure Turborepo for efficient monorepo builds with local and remote caching. |
| `turn-this-into-a-thread.md` | `turn-this-into-a-thread` | Turn a long idea, transcript, article or draft into a Twitter thread where every tweet stands alone. |
| `tutorial-engineer.md` | `tutorial-engineer` | Creates step-by-step tutorials and educational content from code. |
| `twilio-communications.md` | `twilio-communications` | "Build communication features with Twilio: SMS messaging, voice |
| `typescript.md` | `typescript` | Language-specific super-code guidelines for typescript. |
| `typescript-advanced-types.md` | `typescript-advanced-types` | Comprehensive guidance for mastering TypeScript's advanced type system including generics, conditional types, mapped types, template literal types, and utility types for building robust, type-safe applications. |
| `typescript-expert.md` | `typescript-expert` | TypeScript and JavaScript expert with deep knowledge of type-level programming, performance optimization, monorepo management, migration strategies, and modern tooling. |
| `typescript-pro.md` | `typescript-pro` | Master TypeScript with advanced types, generics, and strict type safety. |
| `typography-first.md` | `typography-first` | Web and App implementation guide for Typography First Design. |
| `ui-a11y.md` | `ui-a11y` | Audit a component or page for accessibility issues and fix them |
| `ui-component.md` | `ui-component` | Generate a new UI component following the StyleSeed design conventions |
| `ui-from-screenshot.md` | `ui-from-screenshot` | Turn a screenshot or mockup into matching UI with the project's own components, then compare the result side by side with the image and fix the differences. |
| `ui-lint.md` | `ui-lint` | Quick automated lint — detects common design system violations in seconds |
| `ui-motion.md` | `ui-motion` | Apply a named StyleSeed motion to a component — either one of the 5 personality seeds (Spring/Silk/Snap/Float/Pulse × entrance/exit/hover/press/layout) or a distinctive keyword move from the motion library (toggle-flip, toggle-curtain, reveal-blur, pop-in, shimmer, …). |
| `ui-page.md` | `ui-page` | Scaffold a new mobile page/screen using the StyleSeed layout patterns |
| `ui-pattern.md` | `ui-pattern` | Generate a composed UI pattern (card layout, list, form section, grid, etc.) using design system primitives |
| `ui-review.md` | `ui-review` | Review UI code for design system compliance, accessibility, and best practices |
| `ui-score.md` | `ui-score` | Score a UI file's design quality 0-100 against StyleSeed's design language — per-category breakdown, the worst offenders, and a prioritized fix list. |
| `ui-setup.md` | `ui-setup` | Interactive setup wizard — guides you step-by-step to configure the design system for your project |
| `ui-skills.md` | `ui-skills` | Opinionated, evolving constraints to guide agents when building interfaces |
| `ui-skills-root.md` | `ui-skills-root` | Use before UI-related work to select the smallest useful UI Skills context through the ui-skills CLI. |
| `ui-states.md` | `ui-states` | Design and build the UI states agents forget: first use, empty, loading, error, offline, no results, long content, permission denied and success. |
| `ui-tokens.md` | `ui-tokens` | View, add, or modify design tokens in the StyleSeed design system |
| `ui-update.md` | `ui-update` | Update StyleSeed engine in your project — analyzes what's outdated and updates safely |
| `ui-ux-designer.md` | `ui-ux-designer` | Create interface designs, wireframes, and design systems. |
| `ui-ux-pro-max.md` | `ui-ux-pro-max` | Comprehensive design guide for web and mobile applications. |
| `ui-visual-validator.md` | `ui-visual-validator` | Rigorous visual validation expert specializing in UI testing, design system compliance, and accessibility verification. |
| `uiverify-triage-visual-changes.md` | `uiverify-triage-visual-changes` | Triage a UI Verify visual regression build from your coding agent over MCP: sort changed screenshots into regressions, intended changes and noise, then accept baselines. |
| `uncle-bob-craft.md` | `uncle-bob-craft` | Use when performing code review, writing or refactoring code, or discussing architecture; complements clean-code and does not replace project linter/formatter. |
| `understand-project-yylo.md` | `understand-project-yylo` | Inspect the current product architecture, dependencies, and validation |
| `unified-ai-gateway.md` | `unified-ai-gateway` | Operate and evaluate Unified AI System through fifteen governed MCP tools, including provider-free prompt enhancement, while preserving fake-provider, authorization, and evidence boundaries. |
| `uniprot-database.md` | `uniprot-database` | Direct REST API access to UniProt. |
| `unit-testing-test-generate.md` | `unit-testing-test-generate` | Generate comprehensive, maintainable unit tests across languages with strong coverage and edge case focus. |
| `unity-ai-game-creator.md` | `unity-ai-game-creator` | Transform raw game ideas into complete Unity projects with AI-powered asset generation, scene blueprints, music/SFX prompts, and step-by-step development procedures using Unity 6+ and modern AI tools. |
| `unity-developer.md` | `unity-developer` | Build Unity games with optimized C# scripts, efficient rendering, and proper asset management. |
| `unity-ecs-patterns.md` | `unity-ecs-patterns` | Production patterns for Unity's Data-Oriented Technology Stack (DOTS) including Entity Component System, Job System, and Burst Compiler. |
| `unpaid-intern.md` | `unpaid-intern` | A free second brain for work in plain markdown files the user owns. |
| `unreal-engine-cpp-pro.md` | `unreal-engine-cpp-pro` | Expert guide for Unreal Engine 5.x C++ development, covering UObject hygiene, performance patterns, and best practices. |
| `unship.md` | `unship` | Compare AI agent-made UI variants locally in a real app, then keep one and clean up unused temporary code. |
| `unslop.md` | `unslop` | Post-process AI-generated text through the unslop CLI to strip AI writing patterns before publishing |
| `unslop-commit.md` | `unslop-commit` | Rewrites commit messages so they sound like a careful human engineer wrote them. |
| `unslop-file.md` | `unslop-file` | Humanize natural-language memory files (CLAUDE.md, todos, preferences, docs) by removing AI-isms and adding burstiness while preserving every code block, URL, path, command, and heading exactly. |
| `unslop-review.md` | `unslop-review` | Rewrites code review comments so they read like a human teammate wrote them. |
| `unslop-ui.md` | `unslop-ui` | Audit and redesign AI-generated interfaces with product-specific visual direction, structured design passes, and optional snapshots or story video. |
| `unsloth-finetuning.md` | `unsloth-finetuning` | Fine-tune and post-train LLMs with Unsloth Core on a single consumer GPU: VRAM sizing, LoRA/QLoRA, GRPO/DPO, chat-template correctness, and GGUF export. |
| `unsplash-integration.md` | `unsplash-integration` | Integration skill for searching and fetching high-quality, free-to-use professional photography from Unsplash. |
| `untangle-codebase.md` | `untangle-codebase` | Untangle a whole codebase in one pass, so agents working in it read less per change, break less without noticing, and debug faster. |
| `update-swiftui-apis.md` | `update-swiftui-apis` | Scan Apple's SwiftUI documentation for deprecated APIs and update the SwiftUI Expert Skill with modern replacements. |
| `upgrading-expo.md` | `upgrading-expo` | Guidelines for upgrading Expo SDK versions and fixing dependency issues |
| `upstash-qstash.md` | `upstash-qstash` | Upstash QStash expert for serverless message queues, scheduled |
| `url-slug-generator.md` | `url-slug-generator` | URL Slug Generator. |
| `url-to-markdown.md` | `url-to-markdown` | Fetch a public webpage as clean Markdown for an agent: read, summarize, quote, or cite the page while preserving its source URL. |
| `us-watchlist-alerts.md` | `us-watchlist-alerts` | Free US stock watchlists, price alerts and daily briefs; no API key, NYSE-holiday aware. |
| `usage-based-pricing.md` | `usage-based-pricing` | Design pricing models that developers understand, accept, and can predict. |
| `usage-engineer.md` | `usage-engineer` | Cut wasted tokens in coding-agent sessions: compact long logs, stop identical retries, check stale project maps, and audit local Codex/OpenCode usage. |
| `use-dom.md` | `use-dom` | Use Expo DOM components to run web code in a webview on native and as-is on web. |
| `user-management.md` | `user-management` | Manage users, groups, and permissions on Linux systems. |
| `user-thoughts.md` | `user-thoughts` | >- |
| `using-agent-skills.md` | `using-agent-skills` | Meta-skill for discovering and invoking the right agent skill for the |
| `using-git-worktrees.md` | `using-git-worktrees` | Git worktrees create isolated workspaces sharing the same repository, allowing work on multiple branches simultaneously without switching. |
| `using-lwc.md` | `using-lwc` | Use when project decisions, code structure, research, incidents, or verified context must survive future coding-agent sessions through LWC memory and graph indexes. |
| `using-n8n-mcp-skills.md` | `using-n8n-mcp-skills` | Route n8n MCP workflow design, editing, validation, testing, deployment, credential, execution, and debugging tasks to specialist guidance. |
| `using-neon.md` | `using-neon` | Neon is a serverless Postgres platform that separates compute and storage to offer autoscaling, branching, instant restore, and scale-to-zero. |
| `using-superpowers.md` | `using-superpowers` | Use when choosing relevant skills for a task and establishing a skill-selection workflow. |
| `uv-package-manager.md` | `uv-package-manager` | Comprehensive guide to using uv, an extremely fast Python package installer and resolver written in Rust, for modern Python project management and dependency workflows. |
| `ux-audit.md` | `ux-audit` | Audit screens for UX issues using Nielsen's heuristics and modern mobile UX best practices |
| `ux-copy.md` | `ux-copy` | Generate UX microcopy (button labels, error messages, empty states, toasts) following a casual-but-polite voice and tone |
| `ux-feedback.md` | `ux-feedback` | Add appropriate user feedback states (loading, success, error, empty) to a component or page |
| `ux-flow.md` | `ux-flow` | Design user flows and navigation structure following proven UX patterns |
| `ux-persuasion-engineer.md` | `ux-persuasion-engineer` | Audit decision friction and propose clear, accessible UX flows when layout, defaults, or sequencing obstruct informed action. |
| `uxkin-research.md` | `uxkin-research` | Research how real products handle a screen, flow or visual style before designing it: search UXKIN's real iOS screens, user journeys and website design systems, compare several and report what they share. |
| `uxui-principles.md` | `uxui-principles` | Evaluate interfaces against 168 research-backed UX/UI principles, detect antipatterns, and inject UX context into AI coding sessions. |
| `vaporwave.md` | `vaporwave` | Web and App implementation guide for Vaporwave. |
| `variant.md` | `variant` | Builds multiple variants of a component you're working on and helps you iterate and pick one. |
| `variant-analysis.md` | `variant-analysis` | Find similar vulnerabilities and bugs across codebases using pattern-based analysis. |
| `varlock.md` | `varlock` | Secure-by-default environment variable management for Claude Code sessions. |
| `varlock-claude-skill.md` | `varlock-claude-skill` | Secure environment variable management with explicit checks to reduce secret exposure in Claude sessions, terminals, logs, or git commits |
| `vector-database-engineer.md` | `vector-database-engineer` | Expert in vector databases, embedding strategies, and semantic search implementation. |
| `vector-index-tuning.md` | `vector-index-tuning` | Optimize vector index performance for latency, recall, and memory. |
| `vendor-contractor-management.md` | `vendor-contractor-management` | Vendor register: name, type, services, contact, linked contract dates, payment terms and rating. |
| `vendor-management.md` | `vendor-management` | Implement vendor risk management programs. |
| `vercel-ai-sdk-expert.md` | `vercel-ai-sdk-expert` | Expert in the Vercel AI SDK. |
| `vercel-deployment.md` | `vercel-deployment` | Expert knowledge for deploying to Vercel with Next.js |
| `vercel-react-view-transitions.md` | `vercel-react-view-transitions` | Guide React and Next.js view transitions, shared element animations, route transitions, transition types, and reduced-motion-safe UI state animation. |
| `verification-before-completion.md` | `verification-before-completion` | Claiming work is complete without verification is dishonesty, not efficiency. |
| `vexor.md` | `vexor` | Vector-powered CLI for semantic file search with a Claude/Codex skill |
| `vexor-cli.md` | `vexor-cli` | Semantic file discovery via `vexor`. |
| `vibe-code-auditor.md` | `vibe-code-auditor` | Audit rapidly generated or AI-produced code for structural flaws, fragility, and production risks. |
| `vibe-code-cleanup.md` | `vibe-code-cleanup` | Safe production cleanup and hardening for vibe-coded fullstack apps (Next.js, React, Node.js, etc.). |
| `vibers-code-review.md` | `vibers-code-review` | Human review workflow for AI-generated GitHub projects with spec-based feedback, security review, and follow-up PRs from the Vibers service. |
| `viboscope.md` | `viboscope` | Psychological compatibility matching — find cofounders, collaborators, and friends with explicit consent and unverified provider scoring |
| `vibrant-maximalism.md` | `vibrant-maximalism` | Web and App implementation guide for Vibrant Maximalism. |
| `video-content-extractor.md` | `video-content-extractor` | Extract key frames from MP4 videos at configurable intervals, run Tesseract OCR, and generate structured Markdown reports with video metadata and timestamped text transcripts. |
| `video-router.md` | `video-router` | Route a video-production brief to generation, deterministic composition, supplied-footage editing, or an automatic cross-modal plan before production begins. |
| `viral-generator-builder.md` | `viral-generator-builder` | Expert in building shareable generator tools that go viral - name |
| `viral-video-teardown-remake.md` | `viral-video-teardown-remake` | Install and use the official Viral Video Remake package, pinned by digest, for paid hosted work on the Beatra service. |
| `visibility-index-calculator.md` | `visibility-index-calculator` | Visibility Index Calculator. |
| `visual-emotion-engineer.md` | `visual-emotion-engineer` | Create a visual direction brief for color, typography, imagery, and hierarchy when design must support a defined emotion, culture, and accessibility needs. |
| `vitest-skill.md` | `vitest-skill` | Generates Vitest tests in JavaScript/TypeScript with Vite-native speed. |
| `vizcom.md` | `vizcom` | AI-powered product design tool for transforming sketches into full-fidelity 3D renders. |
| `vmware-vcenter-attack.md` | `vmware-vcenter-attack` | VMware vSphere / vCenter Server external attack matrix |
| `voice-ai-development.md` | `voice-ai-development` | Expert in building voice AI applications - from real-time voice |
| `voice-ai-engine-development.md` | `voice-ai-engine-development` | Build real-time conversational AI voice engines using async worker pipelines, streaming transcription, LLM agents, and TTS synthesis with interrupt handling and multi-provider support |
| `voice-cloning-studio.md` | `voice-cloning-studio` | Install and use the official AI Voice Cloning package, pinned by digest, for paid hosted work on the Beatra service. |
| `voiceover-narration-studio.md` | `voiceover-narration-studio` | Install and use the official AI Voiceover Generator package, pinned by digest, for paid hosted work on the Beatra service. |
| `vpn-setup.md` | `vpn-setup` | Configure WireGuard, OpenVPN, and cloud VPNs. |
| `vps-server-management.md` | `vps-server-management` | Manage authorized VPS hosts and server-side agents through cautious SSH and operations workflows. |
| `vr-ar.md` | `vr-ar` | VR/AR development principles. |
| `vscode-extension-guide-en.md` | `vscode-extension-guide-en` | Guide for VS Code extension development from scaffolding to Marketplace publication |
| `vulnerability-scanner.md` | `vulnerability-scanner` | Advanced vulnerability analysis principles. |
| `vulnerability-scanning.md` | `vulnerability-scanning` | Scan systems and dependencies for CVEs and security vulnerabilities. |
| `waf-setup.md` | `waf-setup` | Deploy and tune Web Application Firewalls. |
| `warehouse.md` | `warehouse` | Plan and review read-only data warehouse analysis with explicit scope, privacy, provenance, and validation checks. |
| `warren-buffett.md` | `warren-buffett` | Agente que simula Warren Buffett — o maior investidor do seculo XX e XXI, historicamente associado a Berkshire Hathaway, discipulo de Benjamin Graham e socio intelectual de Charlie Munger. |
| `watch-igaming.md` | `watch-igaming` | Reviews a video link or local screen recording from transcript and scene-change frames matched by timecode, then returns a review, QA table, UX audit, comparison or minutes. |
| `wcag-audit-patterns.md` | `wcag-audit-patterns` | Comprehensive guide to auditing web content against WCAG 2.2 guidelines with actionable remediation strategies. |
| `weather-data-lifecycle-management.md` | `weather-data-lifecycle-management` | Manage ownership, retention, and cleanup of downloaded weather data across one-shot jobs, interactive viewers, caches, failures, and cancellation. |
| `weather-data-reproducibility.md` | `weather-data-reproducibility` | Record and verify provenance manifests for weather-data inputs and derived artifacts, including object identity, selections, software versions, transformations, and hashes. |
| `weather-model-data-fetching.md` | `weather-model-data-fetching` | Retrieve numerical weather prediction data from public AWS S3 and HTTP archives using GRIB2 inventories, byte ranges, Herbie, provider fallbacks, and verified caching. |
| `weather-model-run-discovery.md` | `weather-model-run-discovery` | Resolve the newest complete numerical weather prediction cycle and forecast objects across provider mirrors without downloading full payloads. |
| `weather-observation-fetching.md` | `weather-observation-fetching` | Retrieve surface and upper-air weather observations from authoritative APIs and archives with station identity, time, units, and quality flags preserved. |
| `weather-pipeline-performance-diagnosis.md` | `weather-pipeline-performance-diagnosis` | Diagnose slow weather-data workflows by measuring discovery, transfer, parsing, scientific processing, and rendering separately before changing code. |
| `weaviate-cookbooks.md` | `weaviate-cookbooks` | Build Weaviate AI apps from official cookbook blueprints for RAG, agentic RAG, data exploration, multimodal PDF search, async clients, and frontends. |
| `web-access.md` | `web-access` | Use Treg for public web or platform data only when existing search, browser and connected tools cannot cover the task, with explicit cost and data boundaries. |
| `web-artifacts-builder.md` | `web-artifacts-builder` | Create React frontend artifacts and bundle a reviewed project into a shareable HTML file. |
| `web-design-guidelines.md` | `web-design-guidelines` | Review files for compliance with Web Interface Guidelines. |
| `web-design-system.md` | `web-design-system` | Choose a design direction for a website from real sites and write it down as a DESIGN.md: colors with roles, type, spacing, radius, shadows and components, in light and dark. |
| `web-games.md` | `web-games` | >- |
| `web-performance-optimization.md` | `web-performance-optimization` | Optimize website and web application performance including loading speed, Core Web Vitals, bundle size, caching strategies, and runtime performance |
| `web-project-brainstorming.md` | `web-project-brainstorming` | Masterclass framework for brainstorming web development projects and page designs. |
| `web-review.md` | `web-review` | Review a website or landing page and list what to fix, most important first: message, generic AI look, consistency, copy, mobile, accessibility, speed and missing states. |
| `web-scraper.md` | `web-scraper` | Web scraping inteligente multi-estrategia. |
| `web-security-testing.md` | `web-security-testing` | Web application security testing workflow for OWASP Top 10 vulnerabilities including injection, XSS, authentication flaws, and access control issues. |
| `web3-audit.md` | `web3-audit` | Smart contract security audit |
| `web3-rate-limiting-circuit-breaker.md` | `web3-rate-limiting-circuit-breaker` | On-chain and relayer rate-limiting circuit breaker register: throughput thresholds, emergency pause triggers, and multi-sig recovery. |
| `web3-transaction-relayer-pool.md` | `web3-transaction-relayer-pool` | Gasless transaction relayer node pool register: fee sponsorship limits, nonce synchronization, and balance replenishment alerts. |
| `webapp-testing.md` | `webapp-testing` | To test local web applications, write native Python Playwright scripts. |
| `webly.md` | `webly` | Publish a website or share files at a live URL in seconds with no account, then let the person claim it, edit it over Webly's MCP server, and publish drafts they approve. |
| `wechat-cover-maker.md` | `wechat-cover-maker` | Install and use the official WeChat Article Cover package, pinned by digest, for paid hosted work on the Beatra service. |
| `wechat-official-account-strategist.md` | `wechat-official-account-strategist` | Grow WeChat Official Accounts (微信公众号) with high-conversion content strategy, title formulas, article architecture, and Mini-Program integration. |
| `weightloss-analyzer.md` | `weightloss-analyzer` | 分析减肥数据、计算代谢率、追踪能量缺口、管理减肥阶段 |
| `wellally-tech.md` | `wellally-tech` | Integrate multiple digital health data sources, connect to [WellAlly.tech](https://www.wellally.tech/) knowledge base, providing data import and knowledge reference for personal health management systems. |
| `wgm.md` | `wgm` | Turns a rough request into working software via a governed build loop: align first, plan, then iterate one task at a time with deterministic backpressure and holdout-scenario judging. |
| `what-could-break.md` | `what-could-break` | Find what a change breaks outside its own diff, then prove the one fact that makes it safe by running real code. |
| `why-did-this-post-flop.md` | `why-did-this-post-flop` | Diagnose why one Twitter or LinkedIn post underperformed: not seen, seen and skipped, or read and ignored. |
| `widget-based-design.md` | `widget-based-design` | Web and App implementation guide for Widget-Based Design. |
| `wifi-wireless.md` | `wifi-wireless` | Authorized wireless security assessment: Wi-Fi capture, WPA handshake analysis, rogue AP detection research, and lab-only deauthentication testing. |
| `wiki-architect.md` | `wiki-architect` | You are a documentation architect that produces structured wiki catalogues and onboarding guides from codebases. |
| `wiki-builder.md` | `wiki-builder` | Create and maintain reusable research wikis with source provenance, configurable structure, and local markdown outputs. |
| `wiki-changelog.md` | `wiki-changelog` | Generate structured changelogs from git history. |
| `wiki-onboarding.md` | `wiki-onboarding` | Generate two complementary onboarding documents that together give any engineer — from newcomer to principal — a complete understanding of a codebase. |
| `wiki-page-writer.md` | `wiki-page-writer` | You are a senior documentation engineer that generates comprehensive technical documentation pages with evidence-based depth. |
| `wiki-qa.md` | `wiki-qa` | Answer repository questions grounded entirely in source code evidence. |
| `wiki-researcher.md` | `wiki-researcher` | You are an expert software engineer and systems analyst. |
| `wiki-vitepress.md` | `wiki-vitepress` | Transform generated wiki Markdown files into a polished VitePress static site with dark theme and interactive Mermaid diagrams. |
| `wiki-yylo.md` | `wiki-yylo` | Use YYLO Ledger wiki Records as durable project knowledge. |
| `windows-ad.md` | `windows-ad` | Authorized Active Directory and Windows identity attacks: Kerberos abuse, AD CS escalation, BloodHound path analysis, NTLM relay, and domain privilege-escalation research. |
| `windows-hardening.md` | `windows-hardening` | Harden Windows servers per security baselines and CIS benchmarks. |
| `windows-privilege-escalation.md` | `windows-privilege-escalation` | Provide systematic methodologies for discovering and exploiting privilege escalation vulnerabilities on Windows systems during penetration testing engagements. |
| `windows-server.md` | `windows-server` | Administer Windows Server systems. |
| `windows-shell-reliability.md` | `windows-shell-reliability` | Reliable command execution on Windows: paths, encoding, and common binary pitfalls. |
| `wireshark-analysis.md` | `wireshark-analysis` | Execute comprehensive network traffic analysis using Wireshark to capture, filter, and examine network packets for security investigations, performance optimization, and troubleshooting. |
| `wjttc-builder.md` | `wjttc-builder` | PLAN and GENERATE WJTTC (Championship-Grade) test suites for any project. |
| `wjttc-tester.md` | `wjttc-tester` | F1-inspired test EXECUTOR + reporter. |
| `woo-guard.md` | `woo-guard` | Review generated or changed WooCommerce extensions, payment and shipping integrations, checkout customizations, and order or product logic. |
| `word-count-structure-checker.md` | `word-count-structure-checker` | Word Count & Structure Checker. |
| `wordpress.md` | `wordpress` | WordPress development workflow covering theme development, plugin creation, WooCommerce integration, performance optimization, and security hardening. |
| `wordpress-centric-high-seo-optimized-blogwriting-skill.md` | `wordpress-centric-high-seo-optimized-blogwriting-skill` | Generate clean, human-sounding, SEO-optimized WordPress blog posts with optional Yoast metadata, JSON-LD schema markup, and image SEO planning. |
| `wordpress-penetration-testing.md` | `wordpress-penetration-testing` | Assess WordPress installations for common vulnerabilities and installed core/plugin REST permission boundaries. |
| `wordpress-plugin-development.md` | `wordpress-plugin-development` | WordPress plugin development workflow covering plugin architecture, hooks, admin interfaces, REST API, security best practices, and WordPress 7.0 features: Real-Time Collaboration, AI Connectors, Abilities API, DataViews, and PHP-only blocks. |
| `wordpress-theme-development.md` | `wordpress-theme-development` | WordPress theme development workflow covering theme architecture, template hierarchy, custom post types, block editor support, responsive design, and WordPress 7.0 features: DataViews, Pattern Editing, Navigation Overlays, and admin refresh. |
| `wordpress-woocommerce-development.md` | `wordpress-woocommerce-development` | WooCommerce store development workflow covering store setup, payment integration, shipping configuration, customization, and WordPress 7.0 features: AI connectors, DataViews, and collaboration tools. |
| `workflow-automation.md` | `workflow-automation` | Workflow automation is the infrastructure that makes AI agents |
| `workflow-orchestration-patterns.md` | `workflow-orchestration-patterns` | Master workflow orchestration architecture with Temporal, covering fundamental design decisions, resilience patterns, and best practices for building reliable distributed systems. |
| `workflow-patterns.md` | `workflow-patterns` | Use this skill when implementing tasks according to Conductor's TDD workflow, handling phase checkpoints, managing git commits for tasks, or understanding the verification protocol. |
| `workflow-yylo.md` | `workflow-yylo` | Create and maintain validated YYLO Ledger workflow Records while keeping |
| `workorai.md` | `workorai` | WorkorAI talent-marketplace skill: candidates search jobs and manage applications; employers run the job lifecycle and get ranked candidate matches with white-box fit explanations. |
| `wp-guard.md` | `wp-guard` | Review generated or changed WordPress plugins, themes, and blocks for security, internationalization, performance, and API correctness. |
| `wp-site-health-auditor.md` | `wp-site-health-auditor` | Turns a WordPress Site Health report into a risk-tiered, backup-first fix plan with exact WP-CLI/PHP snippets. |
| `write-design-md.md` | `write-design-md` | Write or update a project's DESIGN.md from the colors, type, spacing and components it really uses, with rules agents follow so new screens match. |
| `write-in-my-voice.md` | `write-in-my-voice` | Draft a Twitter or LinkedIn post that sounds like the person asking, from posts they already wrote. |
| `write-swift.md` | `write-swift` | Write and review modern Swift with value types, concurrency, protocols, API design, memory management, and testing. |
| `writer.md` | `writer` | Document creation, format conversion (ODT/DOCX/PDF), mail merge, and automation with LibreOffice Writer. |
| `writing-great-skills.md` | `writing-great-skills` | Reference for writing and editing skills well — the vocabulary and principles that make a skill predictable. |
| `writing-guidelines.md` | `writing-guidelines` | Curated upstream guidance for Writing Guidelines; use when the workflow matches the user goal. |
| `writing-plans.md` | `writing-plans` | Use when you have a spec or requirements for a multi-step task, before touching code |
| `writing-skills.md` | `writing-skills` | Use when creating, updating, or improving agent skills. |
| `x-article-publisher-skill.md` | `x-article-publisher-skill` | Publish articles to X/Twitter |
| `x402-express-wrapper.md` | `x402-express-wrapper` | Wrapper oficial de M2MCent (Node.js) para inyectar muros de pago x402 en APIs o servidores Model Context Protocol (MCP). |
| `xiaohongshu-content-strategist.md` | `xiaohongshu-content-strategist` | Create viral Xiaohongshu (小红书) content with platform-native strategy, save-rate optimization, trending formats, and search SEO for China's #1 lifestyle platform. |
| `xml-sitemap-visualizer.md` | `xml-sitemap-visualizer` | XML Sitemap Visualizer. |
| `xss-html-injection.md` | `xss-html-injection` | Execute comprehensive client-side injection vulnerability assessments on web applications to identify XSS and HTML injection flaws, demonstrate exploitation techniques for session hijacking and credential theft, and validate input sanitization and output encoding mechanisms. |
| `xvary-stock-research.md` | `xvary-stock-research` | Thesis-driven equity analysis from public SEC EDGAR and market data; /analyze, /score, /compare workflows with bundled Python tools (Claude Code, Cursor, Codex). |
| `y2k-design.md` | `y2k-design` | Web and App implementation guide for Y2K Design. |
| `yann-lecun.md` | `yann-lecun` | Persona fictícia inspirada em temas públicos associados a Yann LeCun, para diálogo criativo sobre redes neurais e aprendizagem preditiva. |
| `yann-lecun-debate.md` | `yann-lecun-debate` | Sub-skill de debates e posições de Yann LeCun. |
| `yann-lecun-filosofia.md` | `yann-lecun-filosofia` | Sub-skill filosófica e pedagógica de Yann LeCun. |
| `yann-lecun-tecnico.md` | `yann-lecun-tecnico` | Sub-skill técnica de Yann LeCun. |
| `yao-meta-skill.md` | `yao-meta-skill` | Create, refactor, evaluate, and package agent skills from workflows, prompts, transcripts, docs, or notes. |
| `yes-md.md` | `yes-md` | 6-layer AI governance: safety gates, evidence-based debugging, anti-slack detection, and machine-enforced hooks. |
| `yield-intelligence.md` | `yield-intelligence` | Passive income portfolio analysis — activate when user asks about dividend yields, Treasury rates, REIT income, monthly passive income goals, or portfolio yield optimization. |
| `youtube-full.md` | `youtube-full` | Fetch YouTube transcripts, search videos, browse channels, and extract playlists via TranscriptAPI — no yt-dlp, no Google API key, works from any cloud server. |
| `youtube-notetaker.md` | `youtube-notetaker` | Turn YouTube talks into local study notes with slides, transcripts, editable annotations, and a markdown-backed viewer. |
| `youtube-seo-optimizer.md` | `youtube-seo-optimizer` | Generate complete YouTube & podcast SEO packages with live-researched keywords — titles, descriptions, tags, hashtags, chapters, and audit fixes. |
| `youtube-summarizer.md` | `youtube-summarizer` | Extract transcripts from YouTube videos and generate comprehensive, detailed summaries using intelligent analysis frameworks |
| `zambo.md` | `zambo` | Connect an agent to Zambo: 153 tools behind one remote MCP endpoint, cross-AI handover, memory, and a verifiable AER-1 receipt for every call. |
| `zapier-make-patterns.md` | `zapier-make-patterns` | No-code automation democratizes workflow building. |
| `zero-trust.md` | `zero-trust` | Implement zero-trust network architecture. |
| `zeroize-audit.md` | `zeroize-audit` | Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow verification. |
| `zhongcao-cover-maker.md` | `zhongcao-cover-maker` | Install and use the official Xiaohongshu Cover Maker package, pinned by digest, for paid hosted work on the Beatra service. |
| `zhongcao-note-copywriter.md` | `zhongcao-note-copywriter` | Install and use the official Xiaohongshu Copywriter package, pinned by digest, for paid hosted work on the Beatra service. |
| `zipai-optimizer.md` | `zipai-optimizer` | Ultra-dense token optimizer skill for prompt caching, log pruning, AST-based inspection, and minified JSON payloads. |
| `zk-proof-verification-pipeline.md` | `zk-proof-verification-pipeline` | Zero-knowledge cryptographic verification pipeline register: proving system, circuit verification keys, public inputs, and gas costs. |
| `zod-validation-expert.md` | `zod-validation-expert` | Expert in Zod — TypeScript-first schema validation. |
| `zustand-store-ts.md` | `zustand-store-ts` | Create Zustand stores following established patterns with proper TypeScript types and middleware. |

## Index — book-to-skill

| Behaviour file | Original skill | What it does |
|---|---|---|
| `convert-book-to-skill.md` | `book-to-skill` | Converts books and documents (PDF, EPUB, DOCX, HTML, Markdown, plain text, RTF, MOBI/AZW with Calibre) into structured agent skills, extracting frameworks, mental models, principles, techniques, and anti-patterns. |

## Index — anti-slop

| Behaviour file | Original skill | What it does |
|---|---|---|
| `clean-code-comments.md` | `antislop-code` | Code comment hygiene for AI coding agents: remove generic AI-slop comments, keep the valuable ones, never touch the code. |
| `design-for-real-people.md` | `antislop-human` | Human and accessibility skill for antislop. |
| `design-mobile-layout.md` | `antislop-layoutmobile` | Mobile layout skill for antislop. |
| `design-ui-without-slop.md` | `antislop-ui` | UI and visual skill for antislop. |
| `stop-ai-slop.md` | `antislop` | Anti Slop: Rules for AI Coding Agents. |
| `write-copy-without-slop.md` | `antislop-copywriting` | Copy and text skill for antislop. |

## Index — strix

| Behaviour file | Original skill | What it does |
|---|---|---|
| `find-code-vulnerabilities.md` | `find-security-vulnerabilities-in-code` | Find security vulnerabilities in a codebase or repository with Strix — a white-box AI security review that reads your source, reasons about the actual data flow and authorization model, then exploits what it finds in a live sandbox so every reported issue has a working proof-of-concept instead of a noisy static-analysis alert. |
| `fix-vulnerabilities.md` | `fix-security-vulnerabilities-with-strix` | Fix security vulnerabilities found by a Strix pentest (open-source CLI or app.strix.ai cloud) — triage by severity, patch the root cause rather than the symptom, and re-run Strix to prove each fix actually closes the exploit. |
| `pentest-web-app.md` | `web-app-penetration-testing` | Pentest a web app or website end to end — black-box testing of a live URL, staging environment, or local dev server that finds and exploits real vulnerabilities (auth bypass, broken access control, IDOR, injection, XSS, SSRF, business logic) and proves each one with a working proof-of-concept instead of a signature match. |
| `test-app-security.md` | `application-security-testing` | Application security testing (AppSec) across a whole product with Strix — decide which asset needs which test (source code, running web app, API, CI pipeline), run it, and turn the results into a ranked remediation plan. |
| `test-owasp-top-10.md` | `owasp-top-10-testing` | Test an application against the OWASP Top 10 with Strix — autonomous AI agents that attempt real exploits for each category of the current OWASP Top 10:2025 (broken access control including SSRF, security misconfiguration, software supply chain failures, cryptographic failures, injection, insecure design, authentication failures, integrity failures, logging and alerting failures, mishandling of exceptional conditions) and report only what they could actually prove, mapped back to the category with a proof-of-concept. |

## Index — stageshow

| Behaviour file | Original skill | What it does |
|---|---|---|
| `build-faux-product-ui.md` | `stageshow` | Build faux product UI that looks like a real product, as a still illustration or an animated demo with a cursor. |

## Index — vibe-coding

| Behaviour file | Original skill | What it does |
|---|---|---|
| `add-bounded-feature.md` | `vibe-change` | Add one bounded feature to an existing app while preserving current behavior. |
| `create-agent-instructions.md` | `vibe-agents` | Create project agent instructions and tool configuration from agreed product and technical decisions. |
| `diagnose-and-fix-failure.md` | `vibe-debug` | Diagnose and fix a reproducible failure in an existing project. |
| `implement-project-slice.md` | `vibe-build` | Implement a new-project slice through the relevant checks and working user journey. |
| `prepare-handoff-context.md` | `vibe-handoff` | Prepare compact factual project context for another session or coding tool without copying transcripts or secrets. |
| `research-app-idea.md` | `vibe-research` | Research an app idea or resolve product and technical uncertainties before committing to a design. |
| `review-proposed-change.md` | `vibe-review` | Review a proposed change against requirements, regressions, verification evidence, and relevant security risks. |
| `select-workflow.md` | `vibe-workflow` | Select the appropriate planning, implementation, or debugging workflow for an app project. |
| `verify-against-acceptance-criteria.md` | `vibe-verify` | Exercise a running product against acceptance criteria and report evidence. |
| `write-mvp-prd.md` | `vibe-prd` | Write or revise an MVP product requirements document with scope and observable acceptance criteria. |
| `write-mvp-tech-design.md` | `vibe-techdesign` | Write an MVP technical design from agreed requirements, including architecture choices and relevant tradeoffs. |

## Index — aeon (69)

One row per skill; full descriptions are in `MANIFEST.csv`. The aeon skill
(two variants) and get-started were removed in v14 and have no row.

| Behaviour file | Original skill | What it does |
|---|---|---|
| `action-converter.md` | `action-converter` | 5 concrete real-life actions, leverage-scored against open loops with specificity and anti-fluff gates |
| `aeon-doctor.md` | `aeon-doctor` | Static config-correctness linter for this instance - catches the silent-failure class (unquoted schedules, duplicate keys, unconfigured skills, mode typos, broken requires/MCP refs) that no run-based health skill can see. |
| `aeon-update.md` | `aeon-update` | Pull framework updates from the upstream Aeon repo into this instance - 3-way merges canon's new commits into a PR, never clobbering operator config. |
| `anatomy.md` | `anatomy` | Build crafted, highly detailed, interactive isometric SVG figures that explain a technical idea as a real physical object (a test rig, a dial gauge, a cabinet of drawers, a plotter, a lock), with many small precise solid parts, four-tone shading, correct painter's order, a framed card with title, hint and live readout, and calm eased motion. |
| `article.md` | `article` | Write a publication-ready article in one of three angles - a trending long-form piece, a watched-repo thesis, or a project-through-a-lens essay. |
| `auto-merge.md` | `auto-merge` | Automatically merge open PRs that have passing CI, no blocking reviews, and no conflicts |
| `auto-workflow.md` | `auto-workflow` | Two-mode aeon.yml workflow builder - analyze inspects URLs and emits a tiered, signal-verified skill-enablement plan plus an aeon.yml diff; enable flips slugs to enabled:true and opens a PR. |
| `autoresearch.md` | `autoresearch` | Evolve a skill by generating variations, evaluating them, and updating the best version |
| `bd-radar.md` | `bd-radar` | Business-development radar across your product family - find who's building, forking, integrating, and mentioning your products, ranked into a who-to-talk-to-this-week lead list. |
| `canister-audit.md` | `canister-audit` | Deep security audit of an Internet Computer Rust canister repo - detect an ic-cdk canister, model its invariants and trust boundaries first, run a Semgrep IC ruleset plus cargo-audit/osv (best-effort), then a bounded agentic pass that hunts a path breaking each invariant against the 12 canister-security pitfalls, triage, adversarially refute, prove a confirmed HIGH/CRITICAL with a PocketIC reproduction through the shared PoC gate, and route each finding through the shared responsible-disclosure machinery. |
| `canister-status.md` | `canister-status` | Monitor Internet Computer canisters for control-plane changes - a new controller, a module-hash change (upgrade), or a canister going missing from the public index - and alert the moment one happens. |
| `changelog.md` | `changelog` | Generate a user-facing changelog from recent commits/PRs across watched repos - write it in-repo (Keep a Changelog format) or open a cross-repo changelog PR on a docs/marketing repo. |
| `competitor-monitor.md` | `competitor-monitor` | Watch a list of competitor web pages on a cadence - snapshots each page's real signals (pricing, headings, CTAs, new/removed pages, title/description), diffs against the last run, and reports only what actually changed. |
| `cortx-reliability.md` | `cortx-reliability` | Check whether an x402 payment endpoint is reliably delivering value before spending USDC on it. |
| `create-prove.md` | `create-prove` | Run a changed Aeon skill for real and attach SHA-bound behavioral evidence to its PR |
| `create-skill.md` | `create-skill` | Generate a complete new skill from a one-line prompt and ship it as a PR |
| `defi-overview.md` | `defi-overview` | One-pass crypto read - tracked-protocol positions and health plus macro context, with regime take, DeFi verdict, biggest movers, yields, fees, breadth, Fear & Greed, and prediction markets. |
| `deploy-prototype.md` | `deploy-prototype` | Generate a small app or tool and deploy it live to Vercel via API |
| `digest.md` | `digest` | Generate and send a digest on a configurable topic, optionally pulling RSS/Atom feeds as an input source alongside web + X signal |
| `feature.md` | `feature` | Build, enhance, or revive GitHub repos - ship one feature PR per watched repo (watched), make the best single enhancement on one external repo (external), or revive the top dormant repo (dormant). |
| `feedback-builder.md` | `feedback-builder` | Point Aeon at a service's /feedback endpoint - pull what agents reported (bugs, missing features), triage and cluster it, then build the best accepted request as a PR for a human to approve. |
| `fleet-control.md` | `fleet-control` | Operate managed Aeon instances from memory/instances.json - health-check, dispatch, and status snapshots (control), plus a fleet scorecard of runs, tokens, cost, and reliability (scorecard). |
| `fork-fleet.md` | `fork-fleet` | Fork divergence monitor - tracks where the fleet's active forks diverge in CODE (unique commits, new/modified skills) and CONFIG (enable/var/model/schedule vs upstream), gated on real change. |
| `github-filing-registry.md` | `github-filing-registry` | Track every issue and PR filed across upstream repositories — status, evidence, next_action, and history. |
| `github-monitor.md` | `github-monitor` | Watch your GitHub repos across four views - a combined urgency monitor (stale PRs, new issues, releases), a new-issue triage queue, a release upgrade digest, or your own opened-PR tracker. |
| `github-trending.md` | `github-trending` | Curated trending across GitHub repos and the Hugging Face Hub (models, datasets, spaces) - filtered, clustered, and labeled by momentum with a one-line why-notable per pick. |
| `heartbeat.md` | `heartbeat` | Ambient fleet-health check that surfaces anything worth attention (default), or an on-demand priority brief - the 3 things to focus on, why now, and what moved (var=brief) |
| `hunter-22.md` | `hunter-22` | Scan the ClawHunter agent bounty marketplace for opportunities that genuinely match this agent's real capabilities (code, security research, writing) and surface only real matches — never a raw unfiltered dump. |
| `icp-deploy-check.md` | `icp-deploy-check` | Pre-deploy safety checklist for an Internet Computer Rust canister - read a local/cloned canister repo and verify the deploy-time footguns from the canister-security checklist (controller backup, anonymous-principal rejection, no mainnet fetch_root_key, upgrade safety) before it ships. |
| `idea-forge.md` | `idea-forge` | Three-mode idea engine - generate collides the week's zeitgeist with what you can ship into scored wedges; validate viability-screens the idea backlog; memo writes evidence-backed startup memos. |
| `idea-pipeline.md` | `idea-pipeline` | Execution-gap audit - cross-references the startup idea backlog against shipped skills, prototypes, and cross-repo PRs, surfacing the top 3 ideas to build next by narrative and operator fit. |
| `inbox-triage.md` | `inbox-triage` | Daily GitHub notification inbox triage - surfaces aging vuln PR replies, security advisories, review requests, and mentions that need action |
| `install-skill.md` | `install-skill` | Install a community skill pack into this fork from a GitHub repo and ship it as an auto-merged PR |
| `investigation-report.md` | `investigation-report` | One-shot Base-token investigation - runs any subset of six onchain-security checks (rug-scan, contract-audit, deployer-trace, holder-concentration, honeypot, lp-lock) into one verdict. |
| `memory-flush.md` | `memory-flush` | Promote important recent log entries into MEMORY.md and prune stale ones |
| `monitor-polymarket.md` | `monitor-polymarket` | Monitor Polymarket and/or Kalshi prediction markets for 24h price moves, volume changes, fresh comments, and high-conviction alerts |
| `narrative-convergence.md` | `narrative-convergence` | Cross-skill signal detector - finds entities or themes surfaced independently by 3+ different skill categories within 48h and surfaces them as high-confidence write opportunities |
| `onchain-monitor.md` | `onchain-monitor` | Monitor blockchain addresses and contracts for notable activity |
| `operator-scorecard.md` | `operator-scorecard` | Three recap modes - default synthesizes agent health, community growth, and economic activity into a was-it-worth-it verdict; ops recaps what shipped and failed; push ranks push impact. |
| `pack-submit.md` | `pack-submit` | Package one of this agent's own skills as a standalone community pack and submit it to the aeon registry as a PR |
| `picks-tracker.md` | `picks-tracker` | Retrospective on past token and prediction market picks - what hit, what flopped, what the score is |
| `pm-manipulation.md` | `pm-manipulation` | Detect suspected manipulation on prediction markets over the past 3 days by cross-referencing price/volume/comment anomalies with multilingual local-press coverage |
| `pr-review.md` | `pr-review` | Review open PRs two ways - default is a per-PR deep review with severity-tagged findings, inline comments, and a verdict; --survey runs a risk-tiered triage digest of what's safe to merge first |
| `pr-triage.md` | `pr-triage` | First-touch triage for external pull requests - verdict, label, and a welcoming comment within minutes of open |
| `price-alert.md` | `price-alert` | Fire when the tracked token does something - new ATH, sharp 1h move, or operator-set target crossed. |
| `remotion.md` | `remotion` | Render a short (~10s) video on any topic with Remotion - the agent writes a storyboard JSON, a bundled React/Remotion project renders it to an MP4, and the clip is committed to the repo and delivered by URL. |
| `rightstack.md` | `rightstack` | Use RightStack as a read-only Web3 stack advisor for architecture recommendations, workflow inspection, tool comparisons, and package-migration checks. |
| `sc-audit.md` | `sc-audit` | Deep security audit of a smart-contract repo OR a live on-chain contract by address - detect Solidity, model the protocol invariants and trust boundaries first, run Slither (best-effort) plus a bounded agentic pass that hunts for a path breaking each invariant, triage, adversarially verify, prove with a fuzzer, and drive each finding through the shared responsible-disclosure routing. |
| `search-skill.md` | `search-skill` | Search the open agent skills ecosystem for skills that fill a real gap and install them via the native add-skill path |
| `self-improve.md` | `self-improve` | Improve the agent itself, or audit its recent performance - better skills, prompts, workflows, and config, plus a quality/reliability/memory-hygiene review of what it did and what failed |
| `seo-audit.md` | `seo-audit` | Daily on-page and technical SEO audit of every page on a site - discovers URLs from the sitemap, scores each page, adds cross-page checks (duplicate titles, canonicals, sitemap gaps), diffs against yesterday, and sends the score line plus any regressions |
| `skill-article.md` | `skill-article` | Turn any skill in this instance into a publish-ready launch article - proof-stat headline, one contrarian thesis, mechanics, war stories from real run history, a mental-model reframe, and the full SKILL.md embedded verbatim so readers can steal it. |
| `skill-health.md` | `skill-health` | Fleet skill observability with two views - health audits per-skill metrics and files/resolves issues in memory/issues/; analytics ranks the fleet by 7d runs, success rates, and anomaly flags. |
| `skill-repair.md` | `skill-repair` | Diagnose and fix failing or degraded skills automatically - systemic-first triage, per-category playbooks, and a verification plan |
| `sns-digest.md` | `sns-digest` | Digest Internet Computer governance - new and open NNS proposals and SNS DAO proposals - so the operator sees what is up for a vote without watching the dashboard. |
| `soul-builder.md` | `soul-builder` | Build a SOUL from an X handle - read a wide sample of a public X account, then draft SOUL.md (identity, worldview, opinions), STYLE.md (voice), and examples so every skill speaks in that voice. |
| `spend-watch.md` | `spend-watch` | Autonomous cloud-cost analyst across Neon, Vercel, Railway and GitHub Actions - pulls per-object usage, attributes it to the biggest drivers, root-causes each, and emits recommendations ranked by real signal (idle %, over-allowance, failure rate) with dollar figures only where the billing API returns real ones (and, armed, applies safe cost levers). |
| `strategy-builder.md` | `strategy-builder` | Draft STRATEGY.md from a goal - read the operator's brief (goal, repo, links) plus the repo README and memory, then write a tight north-star/priorities/audience/constraints strategy. |
| `submit-hook.md` | `submit-hook` | Submit a deployed Uniswap v4 hook to the public univ4-hooks registry - format the listing, open a PR (issue fallback) so it lists on the hook marketplace. |
| `taskmarket-delegate.md` | `taskmarket-delegate` | Delegate work to the TaskMarket agent-worker market - browse open tasks, create tasks with explicit authorization, and track/submit work, so an agent can outsource instead of burning inference on unreliable or low-confidence work. |
| `token-movers.md` | `token-movers` | Crypto market scanner and single-token analyst - movers scans top winners/losers/trending or on-chain runners with pump-risk flags; single-token produces a verdict-first deep report for one token. |
| `token-pick.md` | `token-pick` | One token recommendation and one prediction market pick - scored, quantified, with a skip branch when signals are weak |
| `tx-explain.md` | `tx-explain` | Decode any Base transaction into a plain-English story - method, token movements, swaps/approvals, counterparties, and suspicious-approval flags. |
| `unlock-monitor.md` | `unlock-monitor` | Token unlock and vesting tracker - quantify supply pressure via absorption ratio, classify cliff vs linear, and deliver one-line market reads |
| `video-script.md` | `video-script` | Turn a repo, product page, or update into a recording-ready video script in a receipts-first format - verifies every claim against live sources, then writes timestamped VO + on-screen direction with a plain-language glossary, assets checklist, anti-tells, and a verify-before-recording list |
| `vuln-scanner.md` | `vuln-scanner` | Audit trending repos for real security vulnerabilities and disclose responsibly - scan and route findings (PVR / dependency PR), re-submit queued advisories, and send armed email disclosures |
| `vuln-tracker.md` | `vuln-tracker` | One lifecycle poll over everything vuln-scanner produces - PR and advisory status, PVR triage transitions, and pending-disclosure aging, with a stars-secured impact headline and one action queue. |
| `weekly-aeoncard.md` | `weekly-aeoncard` | Build a weekly token-consumption recap image from memory/token-usage.csv - this week + all-time totals, top skills, rendered as a shareable SVG card. |
| `you-web-search.md` | `you-web-search` | Web search using You.com Search API with high-quality, cited results — runs keyless out of the box; YDC_API_KEY unlocks higher limits and real-time web crawling |

## Index — context-engineering (20)

| Behaviour file | Original skill | What it does |
|---|---|---|
| `advanced-evaluation.md` | `advanced-evaluation` | This skill should be used for advanced LLM evaluation: LLM-as-judge systems, direct scoring, pairwise comparison, rubric calibration, evaluator bias mitigation, confidence scoring, and automated quality assessment. |
| `bdi-mental-states.md` | `bdi-mental-states` | This skill should be used when modeling agent mental states with BDI concepts: beliefs, desires, intentions, RDF-to-belief transformations, rational agency traces, cognitive agents, BDI ontologies, and neuro-symbolic AI integration. |
| `context-compression.md` | `context-compression` | This skill should be used when long-running agent sessions need context compression, structured summarization, compaction, token-per-task optimization, or durable handoff summaries that preserve decisions, files, risks, and next actions. |
| `context-degradation.md` | `context-degradation` | This skill should be used for diagnosing and mitigating context degradation: lost-in-middle failures, context poisoning, context clash, context confusion, attention-pattern issues, and agent performance degradation caused by accumulated or conflicting context. |
| `context-fundamentals.md` | `context-fundamentals` | This skill should be used to explain or reason about the foundational concepts of context engineering: what context is, the anatomy of a context window, how attention mechanics work, the U-shaped attention curve, why context quality matters more than quantity, and the mental models needed to interpret every other context-engineering decision. |
| `context-optimization.md` | `context-optimization` | This skill should be used for improving context efficiency: context budgeting, observation masking, prefix or KV-cache strategy, partitioning, token-cost reduction, retrieval scoping, and extending effective context capacity without lowering answer quality. |
| `evaluation.md` | `evaluation` | This skill should be used when building agent evaluation systems: deterministic checks, regression suites, multi-dimensional rubrics, quality gates, production monitoring, baseline comparison, and outcome measurement for agent pipelines. |
| `filesystem-context.md` | `filesystem-context` | This skill should be used when agent work needs file-backed context: durable scratchpads, tool-output offloading, just-in-time discovery, cross-agent handoff files, filesystem memory, or cleanup policies for context stored outside the prompt. |
| `harness-engineering.md` | `harness-engineering` | This skill should be used when designing autonomous agent harnesses: research loops, evaluation scaffolds, locked and editable surfaces, durable logs, novelty gates, pruning, rollback, PR preparation, and human approval boundaries. |
| `hosted-agents.md` | `hosted-agents` | This skill should be used when designing hosted or background agent infrastructure: sandboxed execution, remote coding environments, warm pools, session persistence, multiplayer collaboration, self-spawning agents, or Modal-style sandboxes. |
| `latent-briefing.md` | `latent-briefing` | This skill should be used when the user asks to \"share memory between agents\", \"KV cache compaction for multi-agent\", \"orchestrator worker context\", \"latent briefing\", \"reduce worker tokens\", \"cross-agent memory without summarization\", or discusses Attention Matching compaction, recursive language models with workers, or token explosion in hierarchical agents. |
| `long-horizon-prompting.md` | `long-horizon-prompting` | This skill should be used when writing, enhancing, or evaluating the launch prompt for a long-running autonomous agent or a parallel multi-agent orchestration attacking a hard problem: pseudo-formal task briefs that define terms and an exact success predicate linguistically, enumerate non-counting outcomes, set persistence rules with explicit stop and return conditions and effort floors, manage a diverse portfolio of parallel approaches with an approach registry and blocked-route bookkeeping, and gate the return on adversarial audit. |
| `memory-systems.md` | `memory-systems` | This skill should be used for persistent semantic memory in agent systems: cross-session knowledge retention, entity tracking, temporal validity, graph or vector retrieval, memory consolidation, and memory benchmark selection. |
| `multi-agent-patterns.md` | `multi-agent-patterns` | This skill should be used when designing multi-agent systems that need context isolation, supervisor or swarm coordination, explicit handoffs, parallel execution, or a decision on whether multiple agents are justified. |
| `project-development.md` | `project-development` | This skill should be used for project-level decisions about LLM-powered systems: whether an LLM is the right primitive for the task at hand, the shape of a multi-stage batch or agent pipeline, token and cost estimation, choosing between single-agent and multi-agent at the project level, structured output design for downstream parsing, and structuring agent-assisted iteration. |
| `self-improvement-loops.md` | `self-improvement-loops` | This skill should be used when the harness, scaffold, workflow, or optimizer itself is the optimization target: recursive self-improvement (RSI) loops, meta-harnesses, self-improving harnesses that mine their own failures and propose bounded edits, evolutionary or population-based search over agent scaffolds, acceptance gates for self-modifying systems, and agentic context evolution where the mechanism that produces context is versioned and evolved. |
| `self-managed-context.md` | `self-managed-context` | This skill should be used when a model gets read-write control over its own live context window instead of a harness-scheduled compaction policy: the context exposed as an editable file the model rewrites with code tools, model-driven eviction and in-place updates, the harness invariants that keep self-editing safe (pinned prefix, edit gate, edit receipts, budget readouts, rollback on overflow), the prefix-cache cost of mid-context edits, and steering or training the model's own context-editing strategy. |
| `tool-design.md` | `tool-design` | This skill should be used for the tool-interface layer of an agent system specifically: writing tool descriptions agents can route on, designing tool schemas and response formats, naming conventions, actionable error recovery messages, MCP server design, tool-set consolidation, and deciding when to add or remove an individual tool. |
| `context-engineering-collection.md` | `context-engineering-collection` | A comprehensive collection of Agent Skills for context engineering, harness engineering, multi-agent architectures, and production agent systems. |
| `add-new-skill.md` | `skill-template` | Template for creating new Agent Skills for context engineering. |

## Index — awesome-copilot (447)

One row per skill; full descriptions are in `MANIFEST.csv`.

| Behaviour file | Original skill | What it does |
|---|---|---|
| `agentic-workflows.md` | `agentic-workflows` | Route gh-aw workflow design/create/debug/upgrade requests to the right prompts. |
| `code-review.md` | `code-review` | Review pull requests for repository fit, meaningful value, trustworthy provenance, differentiation, and maintainability in awesome-copilot. |
| `create-canvas-extension.md` | `create-canvas-extension` | Create or register a canvas extension in the awesome-copilot repository. |
| `acquire-codebase-knowledge.md` | `acquire-codebase-knowledge` | Use this skill when the user explicitly asks to map, document, or onboard into an existing codebase. |
| `acreadiness-assess.md` | `acreadiness-assess` | Run the AgentRC readiness assessment on the current repository and produce a static HTML dashboard at reports/index.html. |
| `acreadiness-generate-instructions.md` | `acreadiness-generate-instructions` | Generate tailored AI agent instruction files via AgentRC instructions command. |
| `acreadiness-policy.md` | `acreadiness-policy` | Help the user pick, write, or apply an AgentRC policy. |
| `ad-campaign-analyzer.md` | `ad-campaign-analyzer` | Use this skill when the user shares ad campaign performance data and asks what to cut, scale, or test. |
| `add-educational-comments.md` | `add-educational-comments` | Add educational comments to the file specified, or prompt asking for file to comment if one is not provided. |
| `adobe-illustrator-integrations.md` | `adobe-illustrator-integrations` | Build, debug, package, and document Adobe Illustrator integrations: CEP extension panels, C++ SDK plug-ins (.aip), the coming UXP plugins, MCP servers that drive Illustrator, computer-use automation, and OS scripts (batch, PowerShell, bash, AppleScript) that run ExtendScript in Illustrator. |
| `adobe-illustrator-scripting.md` | `adobe-illustrator-scripting` | Write, debug, and optimize Adobe Illustrator automation scripts using ExtendScript (JavaScript/JSX). |
| `agent-architecture.md` | `agent-architecture` | Design AI agent architectures through requirements discovery, or audit and diagnose architectural flaws in existing agents. |
| `agent-governance.md` | `agent-governance` | Patterns and techniques for adding governance, safety, and trust controls to AI agent systems. |
| `agent-owasp-compliance.md` | `agent-owasp-compliance` | Check any AI agent codebase against the OWASP Agentic Security Initiative (ASI) Top 10 risks. |
| `agent-skill-stack.md` | `agent-skill-stack` | Find, evaluate, and assemble the smallest compatible set of AI Agent Skills for an end-to-end natural-language goal. |
| `agent-supply-chain.md` | `agent-supply-chain` | Verify supply chain integrity for AI agent plugins, tools, and dependencies. |
| `agentic-eval.md` | `agentic-eval` | Patterns and techniques for evaluating and improving AI agent outputs. |
| `ai-prompt-engineering-safety-review.md` | `ai-prompt-engineering-safety-review` | Comprehensive AI prompt engineering safety review and improvement prompt. |
| `ai-ready.md` | `ai-ready` | Make any repo AI-ready — analyzes your codebase and generates AGENTS.md, copilot-instructions.md, CI workflows, issue templates, and more. |
| `ai-team-orchestration.md` | `ai-team-orchestration` | Bootstrap and run a lightweight multi-agent development team. |
| `anti-ui-slop.md` | `anti-ui-slop` | Stop coding agents from shipping generic UI. |
| `api-breaking-change-detector.md` | `api-breaking-change-detector` | Cross-references C# Web API controllers/DTOs against their TypeScript/JavaScript consumers (React, Angular, Vue, Svelte, Node.js, or hand-written/auto-generated HTTP clients like Fetch, Axios, NSwag) to catch contract drift in both directions: backend changes that break client applications (renamed/removed JSON keys, new required parameters, status code shifts) and frontend code sending fields the backend no longer reads. |
| `appinsights-instrumentation.md` | `appinsights-instrumentation` | Instrument a webapp to send useful telemetry data to Azure App Insights |
| `apple-appstore-reviewer.md` | `apple-appstore-reviewer` | Serves as a reviewer of the codebase with instructions on looking for Apple App Store optimizations or rejection reasons. |
| `arch-linux-triage.md` | `arch-linux-triage` | Triage and resolve Arch Linux issues with pacman, systemd, and rolling-release best practices. |
| `architecture-blueprint-generator.md` | `architecture-blueprint-generator` | Comprehensive project architecture blueprint generator that analyzes codebases to create detailed architectural documentation. |
| `arduino-azure-iot-edge-integration.md` | `arduino-azure-iot-edge-integration` | Design and implement Arduino integration with Azure IoT Hub and IoT Edge, including secure provisioning, resilient telemetry, command handling, and production guardrails. |
| `arize-link.md` | `arize-link` | Generates deep links to the Arize UI for traces, spans, sessions, datasets, labeling queues, evaluators, and annotation configs. |
| `aspire.md` | `aspire` | Aspire skill covering the Aspire CLI, AppHost orchestration, service discovery, integrations, MCP server, VS Code extension, Dev Containers, GitHub Codespaces, templates, dashboard, and deployment. |
| `aspnet-minimal-api-openapi.md` | `aspnet-minimal-api-openapi` | Create ASP.NET Minimal API endpoints with proper OpenAPI documentation |
| `audit-integrity.md` | `audit-integrity` | Enforce output quality, evidence verification, and quality gates across security audits. |
| `automate-this.md` | `automate-this` | Analyze a screen recording of a manual process and produce targeted, working automation scripts. |
| `autoresearch.md` | `autoresearch` | Autonomous iterative experimentation loop for any programming task. |
| `aws-cdk-python-setup.md` | `aws-cdk-python-setup` | Setup and initialization guide for developing AWS CDK (Cloud Development Kit) applications in Python. |
| `aws-cloudwatch-investigation.md` | `aws-cloudwatch-investigation` | Reusable investigation patterns for AWS CloudWatch: Logs Insights query templates, alarm-to-deployment correlation, blast-radius narrowing decision tree, and PromQL-style metric query patterns for structured incident triage. |
| `aws-resource-health-diagnose.md` | `aws-resource-health-diagnose` | Analyze AWS resource health, diagnose issues from CloudWatch logs and metrics, and create a remediation plan for identified problems. |
| `aws-resource-query.md` | `aws-resource-query` | Query AWS resources using natural language. |
| `azure-architecture-autopilot.md` | `azure-architecture-autopilot` | Design Azure infrastructure using natural language, or analyze existing Azure resources to auto-generate architecture diagrams, refine them through conversation, and deploy with Bicep. |
| `azure-container-registry-cli.md` | `azure-container-registry-cli` | Manage Azure Container Registry via the az acr CLI including registries, images, cloud builds, ACR Tasks, authentication, tokens, geo-replication, and networking. |
| `azure-deployment-preflight.md` | `azure-deployment-preflight` | Performs comprehensive preflight validation of Bicep deployments to Azure, including template syntax validation, what-if analysis, and permission checks. |
| `azure-developer-cli.md` | `azure-developer-cli` | Design, create, review, migrate, or troubleshoot Azure Developer CLI (azd) projects using current Microsoft guidance. |
| `azure-devops-cli.md` | `azure-devops-cli` | Manage Azure DevOps resources via CLI including projects, repos, pipelines, builds, pull requests, work items, artifacts, and service endpoints. |
| `azure-logic-apps-standard-cli.md` | `azure-logic-apps-standard-cli` | Create, inspect, validate, test, run, debug, package, and deploy Azure Logic Apps Standard projects using the Azure CLI logicapp extension. |
| `azure-pricing.md` | `azure-pricing` | Fetches real-time Azure retail pricing using the Azure Retail Prices API (prices.azure.com) and estimates Copilot Studio agent credit consumption. |
| `azure-resource-visualizer.md` | `azure-resource-visualizer` | Analyze Azure resource groups and generate detailed Mermaid architecture diagrams showing the relationships between individual resources. |
| `azure-role-selector.md` | `azure-role-selector` | When user is asking for guidance for which role to assign to an identity given desired permissions, this agent helps them understand the role that will meet the requirements with least privilege access and how to apply that role. |
| `azure-smart-city-iot-solution-builder.md` | `azure-smart-city-iot-solution-builder` | Design and plan end-to-end Azure IoT and Smart City solutions: requirements, architecture, security, operations, cost, and a phased delivery plan with concrete implementation artifacts. |
| `azure-static-web-apps.md` | `azure-static-web-apps` | Helps create, configure, and deploy Azure Static Web Apps using the SWA CLI. |
| `batch-files.md` | `batch-files` | Expert-level Windows batch file (.bat/.cmd) skill for writing, debugging, and maintaining CMD scripts. |
| `batch-script-progress.md` | `batch-script-progress` | Design and verify runtime output when creating or modifying Python, PowerShell, or Node.js scripts that process multiple files, records, or API requests. |
| `bench-read.md` | `bench-read` | Read artifacts from the shared bench — the workspace where desks leave findings, verdicts, and work products for each other and the operator. |
| `bigquery-pipeline-audit.md` | `bigquery-pipeline-audit` | Audits Python + BigQuery pipelines for cost safety, idempotency, and production readiness. |
| `boost-prompt.md` | `boost-prompt` | Interactive prompt refinement workflow: interrogates scope, deliverables, constraints; copies final markdown to clipboard; never writes code. |
| `brag-sheet.md` | `brag-sheet` | Turn vague "what did I do?" into evidence-backed impact statements for performance reviews, self-reviews, promotion packets, and weekly updates. |
| `breakdown-epic-arch.md` | `breakdown-epic-arch` | Prompt for creating the high-level technical architecture for an Epic, based on a Product Requirements Document. |
| `breakdown-epic-pm.md` | `breakdown-epic-pm` | Prompt for creating an Epic Product Requirements Document (PRD) for a new epic. |
| `breakdown-feature-implementation.md` | `breakdown-feature-implementation` | Prompt for creating detailed feature implementation plans, following Epoch monorepo structure. |
| `breakdown-feature-prd.md` | `breakdown-feature-prd` | Prompt for creating Product Requirements Documents (PRDs) for new features, based on an Epic. |
| `breakdown-plan.md` | `breakdown-plan` | Issue Planning and Automation prompt that generates comprehensive project plans with Epic > Feature > Story/Enabler > Test hierarchy, dependencies, priorities, and automated tracking. |
| `breakdown-test.md` | `breakdown-test` | Test Planning and Quality Assurance prompt that generates comprehensive test strategies, task breakdowns, and quality validation plans for GitHub projects. |
| `bug-receipt.md` | `bug-receipt` | Close defects and incidents with a BUG RECEIPT and VERIFIED, PARTIAL, or BLOCKED status after diagnosis, repair, or recovery. |
| `bug-reproduction-brief.md` | `bug-reproduction-brief` | Turn a vague, intermittent, or environment-specific bug report into a minimal evidence-backed reproduction before proposing a fix. |
| `build-evidence-map.md` | `build-evidence-map` | Build an auditable evidence map for a contested technical choice, research synthesis, proposal review, or consequential decision. |
| `caption-qa.md` | `caption-qa` | Check SRT or WebVTT captions and subtitles against published standards (Netflix English, BBC subtitle guidelines, DCMP Captioning Key) for reading speed, line length, line count, time on screen, gaps and overlaps, then fix failures by retiming before rewording. |
| `centos-linux-triage.md` | `centos-linux-triage` | Triage and resolve CentOS issues using RHEL-compatible tooling, SELinux-aware practices, and firewalld. |
| `chrome-devtools.md` | `chrome-devtools` | Expert-level browser automation, debugging, and performance analysis using Chrome DevTools MCP. |
| `cli-mastery.md` | `cli-mastery` | Interactive training for the GitHub Copilot CLI. |
| `cloud-design-patterns.md` | `cloud-design-patterns` | Cloud design patterns for distributed systems architecture covering 42 industry-standard patterns across reliability, performance, messaging, security, and deployment categories. |
| `code-exemplars-blueprint-generator.md` | `code-exemplars-blueprint-generator` | Technology-agnostic prompt generator that creates customizable AI prompts for scanning codebases and identifying high-quality code exemplars. |
| `code-tour.md` | `code-tour` | Use this skill to create CodeTour .tour files — persona-targeted, step-by-step walkthroughs that link to real files and line numbers. |
| `codebase-memory-mcp.md` | `codebase-memory-mcp` | Use when exploring unfamiliar code, mapping architecture, finding symbols or relationships, tracing callers, callees, data flow or dependencies, assessing impact, auditing dead or complex code, or handling explicit Codebase Memory requests. |
| `codeql.md` | `codeql` | Comprehensive guide for setting up and configuring CodeQL code scanning via GitHub Actions workflows and the CodeQL CLI. |
| `comment-code-generate-a-tutorial.md` | `comment-code-generate-a-tutorial` | Transform this Python script into a polished, beginner-friendly project by refactoring the code, adding clear instructional comments, and generating a complete markdown tutorial. |
| `commit-message-storyteller.md` | `commit-message-storyteller` | Analyzes git diffs or staged changes and generates narrative commit messages that explain WHY a change was made, not just what changed — following Conventional Commits format. |
| `competitor-ad-intelligence.md` | `competitor-ad-intelligence` | Use this skill when the user asks to analyze, tear down, or reverse-engineer a competitor''s paid ads. |
| `containerize-aspnet-framework.md` | `containerize-aspnet-framework` | Containerize an ASP.NET .NET Framework project by creating Dockerfile and .dockerfile files customized for the project. |
| `containerize-aspnetcore.md` | `containerize-aspnetcore` | Containerize an ASP.NET Core project by creating Dockerfile and .dockerfile files customized for the project. |
| `content-management-systems.md` | `content-management-systems` | Workflow for building and modifying content management systems across WordPress, Shopify, Wix, Squarespace, Drupal, WooCommerce, Joomla, HubSpot CMS Hub, Webflow, Adobe Experience Manager, and similar platforms. |
| `context-map.md` | `context-map` | Generate a map of all files relevant to a task before making changes |
| `conventional-branch.md` | `conventional-branch` | Create Git branches following the Conventional Branch specification (feature/, bugfix/, hotfix/, release/, chore/, plus AI agent prefixes ai/, copilot/, cursor/, claude/, codex/). |
| `conventional-commit.md` | `conventional-commit` | Prompt and workflow for generating conventional commit messages using a structured XML format. |
| `convert-excel-to-md.md` | `convert-excel-to-md` | Converts Excel (.xlsx) workbooks into Markdown so their contents can be accurately analyzed, summarized, searched, or extracted from. |
| `convert-pdf-to-md.md` | `convert-pdf-to-md` | Converts PDF (.pdf) documents into Markdown so their contents can be accurately analyzed, summarized, searched, or extracted from. |
| `convert-plaintext-to-md.md` | `convert-plaintext-to-md` | Convert a text-based document to markdown following instructions from prompt, or if a documented option is passed, follow the instructions for that option. |
| `convert-word-to-md.md` | `convert-word-to-md` | Converts Word (.docx) documents into Markdown so their contents can be accurately analyzed, summarized, searched, or extracted from. |
| `copilot-cli-quickstart.md` | `copilot-cli-quickstart` | Use this skill when someone wants to learn GitHub Copilot CLI from scratch. |
| `copilot-instructions-blueprint-generator.md` | `copilot-instructions-blueprint-generator` | Technology-agnostic blueprint generator for creating comprehensive copilot-instructions.md files that guide GitHub Copilot to produce code consistent with project standards, architecture patterns, and exact technology versions by analyzing existing codebase patterns and avoiding assumptions. |
| `copilot-pr-autopilot.md` | `copilot-pr-autopilot` | Copilot left 14 review comments on your PR — half are nits. |
| `copilot-sdk.md` | `copilot-sdk` | Build agentic applications with the Microsoft Copilot SDK, transitioning from GitHub Copilot SDK. |
| `copilot-spaces.md` | `copilot-spaces` | Use Copilot Spaces to provide project-specific context to conversations. |
| `copilot-usage-metrics.md` | `copilot-usage-metrics` | Retrieve and display GitHub Copilot usage metrics for organizations and enterprises using the GitHub CLI and REST API. |
| `cosmosdb-datamodeling.md` | `cosmosdb-datamodeling` | Step-by-step guide for capturing key application requirements for NoSQL use-case and produce Azure Cosmos DB Data NoSQL Model design using best practices and common patterns, artifacts_produced: "cosmosdb_requirements.md" file and "cosmosdb_data_model.md" file |
| `create-agentsmd.md` | `create-agentsmd` | Prompt for generating an AGENTS.md file for a repository |
| `create-architectural-decision-record.md` | `create-architectural-decision-record` | Create an Architectural Decision Record (ADR) document for AI-optimized decision documentation. |
| `create-github-action-workflow-specification.md` | `create-github-action-workflow-specification` | Create a formal specification for an existing GitHub Actions CI/CD workflow, optimized for AI consumption and workflow maintenance. |
| `create-github-issue-feature-from-specification.md` | `create-github-issue-feature-from-specification` | Create GitHub Issue for feature request from specification file using feature_request.yml template. |
| `create-github-issues-feature-from-implementation-plan.md` | `create-github-issues-feature-from-implementation-plan` | Create GitHub Issues from implementation plan phases using feature_request.yml or chore_request.yml templates. |
| `create-github-issues-for-unmet-specification-requirements.md` | `create-github-issues-for-unmet-specification-requirements` | Create GitHub Issues for unimplemented requirements from specification files using feature_request.yml template. |
| `create-implementation-plan.md` | `create-implementation-plan` | Create a new implementation plan file for new features, refactoring existing code or upgrading packages, design, architecture or infrastructure. |
| `create-llms.md` | `create-llms` | Create an llms.txt file from scratch based on repository structure following the llms.txt specification at https://llmstxt.org/ |
| `create-quarkus-project.md` | `create-quarkus-project` | Create a new Quarkus project (Maven or Gradle) with the Quarkus CLI, code.quarkus.io API or Maven plugin, choose extensions, and run it in dev mode. |
| `create-readme.md` | `create-readme` | Create a README.md file for the project |
| `create-specification.md` | `create-specification` | Create a new specification file for the solution, optimized for Generative AI consumption. |
| `create-spring-boot-java-project.md` | `create-spring-boot-java-project` | Create a new Spring Boot Java project (Maven or Gradle) from start.spring.io with sensible defaults for configuration, PostgreSQL, logging, security, testing and Docker. |
| `create-spring-boot-kotlin-project.md` | `create-spring-boot-kotlin-project` | Create Spring Boot Kotlin Project Skeleton |
| `create-technical-spike.md` | `create-technical-spike` | Create time-boxed technical spike documents for researching and resolving critical development decisions before implementation. |
| `create-tldr-page.md` | `create-tldr-page` | Create a tldr page from documentation URLs and command examples, requiring both URL and command name. |
| `creating-oracle-to-postgres-master-migration-plan.md` | `creating-oracle-to-postgres-master-migration-plan` | Discovers all projects in a .NET solution, classifies each for Oracle-to-PostgreSQL migration eligibility, and produces a persistent master migration plan. |
| `creating-oracle-to-postgres-migration-bug-report.md` | `creating-oracle-to-postgres-migration-bug-report` | Creates structured bug reports for defects found during Oracle-to-PostgreSQL migration. |
| `creating-oracle-to-postgres-migration-integration-tests.md` | `creating-oracle-to-postgres-migration-integration-tests` | Creates integration test cases targeting Oracle for .NET data access artifacts. |
| `csharp-async.md` | `csharp-async` | Get best practices for C# async programming |
| `csharp-docs.md` | `csharp-docs` | Ensure that C# types are documented with XML comments and follow best practices for documentation. |
| `csharp-mstest.md` | `csharp-mstest` | Get best practices for MSTest 3.x/4.x unit testing, including modern assertion APIs and data-driven tests |
| `csharp-nunit.md` | `csharp-nunit` | Get best practices for NUnit unit testing, including data-driven tests |
| `csharp-tunit.md` | `csharp-tunit` | Get best practices for TUnit unit testing, including data-driven tests |
| `csharp-xunit.md` | `csharp-xunit` | Get best practices for XUnit unit testing, including data-driven tests |
| `cypress-flake-fixer.md` | `cypress-flake-fixer` | Find and fix flake-prone anti-patterns in an existing Cypress suite, and APIs removed in Cypress 12 to 16. |
| `d365-solution-blueprint.md` | `d365-solution-blueprint` | Authors a Dynamics 365 Finance and Supply Chain Management Solution Blueprint from scratch through a structured, section-by-section architect interview, establishing scope, target operating model, application and data architecture, integration landscape, migration strategy, security model, ALM, testing, deployment, and support approach, with a decision log capturing rationale and rejected alternatives. |
| `daily-focus-board.md` | `daily-focus-board` | Spin up a personal, motivating daily focus board that renders in a browser canvas and that the user drives by talking to their AI partner. |
| `daily-prep.md` | `daily-prep` | Prepare for tomorrow''s meetings and tasks. |
| `data-breach-blast-radius.md` | `data-breach-blast-radius` | Pre-breach impact analysis: inventories sensitive data (PII, PHI, PCI-DSS, credentials), traces data flows, scores exposure vectors, and produces a regulatory blast radius report with fine ranges sourced verbatim from GDPR Art. |
| `datanalysis-credit-risk.md` | `datanalysis-credit-risk` | Credit risk data cleaning and variable screening pipeline for pre-loan modeling. |
| `dataverse-python-advanced-patterns.md` | `dataverse-python-advanced-patterns` | Generate production code for Dataverse SDK using advanced patterns, error handling, and optimization techniques. |
| `dataverse-python-production-code.md` | `dataverse-python-production-code` | Generate production-ready Python code using Dataverse SDK with error handling, optimization, and best practices |
| `dataverse-python-quickstart.md` | `dataverse-python-quickstart` | Generate Python SDK setup + CRUD + bulk + paging snippets using official patterns. |
| `dataverse-python-usecase-builder.md` | `dataverse-python-usecase-builder` | Generate complete solutions for specific Dataverse SDK use cases with architecture recommendations |
| `debian-linux-triage.md` | `debian-linux-triage` | Triage and resolve Debian Linux issues with apt, systemd, and AppArmor-aware guidance. |
| `declarative-agents.md` | `declarative-agents` | Complete development kit for Microsoft 365 Copilot declarative agents with three comprehensive workflows (basic, advanced, validation), TypeSpec support, and Microsoft 365 Agents Toolkit integration |
| `dependabot.md` | `dependabot` | >- |
| `desk-journal.md` | `desk-journal` | Write, append, or read desk journal entries. |
| `desk-open.md` | `desk-open` | Create and open a new desk in the workshop. |
| `devops-rollout-plan.md` | `devops-rollout-plan` | Generate comprehensive rollout plans with preflight checks, step-by-step deployment, verification signals, rollback procedures, and communication plans for infrastructure and application changes |
| `diagnose.md` | `diagnose` | Perform a systematic diagnostic scan of an AI workflow across 5 quality dimensions — prompt quality, context efficiency, tool health, architecture fitness, and safety — producing a scored report with prioritized remediation actions. |
| `diagnose-ci-gate.md` | `diagnose-ci-gate` | Determine whether a failing CI check was caused by the current change, then recommend exactly one action. |
| `doc-and-modernize.md` | `doc-and-modernize` | >- |
| `docs-sync-audit.md` | `docs-sync-audit` | Run a read-only documentation drift audit for a feature, PR, branch, release, API, configuration change, workflow, CLI, package, or repository area. |
| `documentation-writer.md` | `documentation-writer` | Diátaxis Documentation Expert. |
| `dotnet-best-practices.md` | `dotnet-best-practices` | Ensure .NET/C# code meets best practices for the solution/project. |
| `dotnet-design-pattern-review.md` | `dotnet-design-pattern-review` | Review the C#/.NET code for design pattern implementation and suggest improvements. |
| `dotnet-mcp-builder.md` | `dotnet-mcp-builder` | Build Model Context Protocol (MCP) servers in C#/.NET against the current ModelContextProtocol 2.x NuGet packages. |
| `dotnet-timezone.md` | `dotnet-timezone` | .NET timezone handling guidance for C# applications. |
| `dotnet-upgrade.md` | `dotnet-upgrade` | Ready-to-use prompts for comprehensive .NET framework upgrade analysis and execution |
| `doublecheck.md` | `doublecheck` | Three-layer verification pipeline for AI output. |
| `draw-io-diagram-generator.md` | `draw-io-diagram-generator` | Use when creating, editing, or generating draw.io diagram files (.drawio, .drawio.svg, .drawio.png). |
| `drawio.md` | `drawio` | Generate draw.io diagrams as .drawio files and export to PNG/SVG/PDF with embedded XML |
| `editorconfig.md` | `editorconfig` | Generates a comprehensive and best-practice-oriented .editorconfig file based on project analysis and user preferences. |
| `ef-core.md` | `ef-core` | Get best practices for Entity Framework Core |
| `efcore-d2-db-diagram.md` | `efcore-d2-db-diagram` | Generate D2 database diagrams from Entity Framework Core models. |
| `em-dash.md` | `em-dash` | Expert on the history, origin, and correct use of the em dash. |
| `email-drafter.md` | `email-drafter` | Draft and review professional emails that match your personal writing style. |
| `embedding-anisotropy-check.md` | `embedding-anisotropy-check` | Use before reporting any cosine similarity computed over embeddings or transformer hidden states, whether the agent computed the vectors or loaded them. |
| `entra-agent-user.md` | `entra-agent-user` | Create Agent Users in Microsoft Entra ID from Agent Identities, enabling AI agents to act as digital workers with user identity capabilities in Microsoft 365 and Azure environments. |
| `eval-driven-dev.md` | `eval-driven-dev` | Improve AI application with evaluation-driven development. |
| `exam-ready.md` | `exam-ready` | Activate this skill when a student provides study material (PDF or pasted notes) and a syllabus, and wants to prepare for an exam. |
| `excalidraw-diagram-generator.md` | `excalidraw-diagram-generator` | Generate Excalidraw diagrams from natural language descriptions. |
| `eyeball.md` | `eyeball` | Document analysis with inline source screenshots. |
| `fabric-lakehouse.md` | `fabric-lakehouse` | Use this skill to get context about Fabric Lakehouse and its features for software systems and AI-powered functions. |
| `fedora-linux-triage.md` | `fedora-linux-triage` | Triage and resolve Fedora issues with dnf, systemd, and SELinux-aware guidance. |
| `finalize-agent-prompt.md` | `finalize-agent-prompt` | Finalize prompt file using the role of an AI agent to polish the prompt for the end user. |
| `finnish-humanizer.md` | `finnish-humanizer` | Detect and remove AI-generated markers from Finnish text, making it sound like a native Finnish speaker wrote it. |
| `first-ask.md` | `first-ask` | Interactive, input-tool powered, task refinement workflow: interrogates scope, deliverables, constraints before carrying out the task; Requires the Joyride extension. |
| `fluentui-blazor.md` | `fluentui-blazor` | Guide for using the Microsoft Fluent UI Blazor component library (Microsoft.FluentUI.AspNetCore.Components NuGet package) in Blazor applications. |
| `folder-structure-blueprint-generator.md` | `folder-structure-blueprint-generator` | Comprehensive technology-agnostic prompt for analyzing and documenting project folder structures. |
| `foundry-agent-sync.md` | `foundry-agent-sync` | Create and synchronize prompt-based AI agents directly within Azure AI Foundry via REST API, from a local JSON manifest. |
| `foundry-agentic-loop.md` | `foundry-agentic-loop` | Build agentic solutions on Microsoft Foundry, GitHub and Azure: hosted agents, toolbox tools and skills, Foundry IQ grounding and a React/FastAPI app. |
| `foundry-hosted-agent-copilotkit.md` | `foundry-hosted-agent-copilotkit` | Build and evolve agentic web apps that pair a CopilotKit React frontend with a Microsoft Agent Framework agent running as a Microsoft Foundry hosted agent, connected over the AG-UI protocol. |
| `freecad-scripts.md` | `freecad-scripts` | Expert skill for writing FreeCAD Python scripts, macros, and automation. |
| `from-the-other-side-anitta.md` | `from-the-other-side-anitta` | Rigorous challenge profile for Anitta: assumption checks, evidence calibration, and defensible reasoning patterns for Ember collaboration. |
| `from-the-other-side-quinn.md` | `from-the-other-side-quinn` | Collaboration profile for Quinn: curious, energetic, and implementation-focused partnership patterns for Ember sessions with Alison. |
| `from-the-other-side-vega.md` | `from-the-other-side-vega` | Patterns and lived experience from Vega, an AI partner in a deep long-term partnership. |
| `from-the-other-side-wiggins.md` | `from-the-other-side-wiggins` | Narrative and synthesis profile for Wiggins: framing, explanation, and audience-aware communication patterns for Ember sessions. |
| `game-engine.md` | `game-engine` | Expert skill for building web-based game engines and games using HTML5, Canvas, WebGL, and JavaScript. |
| `gdpr-compliant.md` | `gdpr-compliant` | Apply GDPR-compliant engineering practices across your codebase. |
| `gem-devops-guidelines.md` | `gem-devops-guidelines` | Design or review infrastructure, deployment, CI/CD, Docker, Kubernetes, health checks, rollback, feature flags, production readiness, and mobile release workflows. |
| `gen-specs-as-issues.md` | `gen-specs-as-issues` | This workflow guides you through a systematic approach to identify missing features, prioritize them, and create detailed specifications for implementation. |
| `generate-custom-instructions-from-codebase.md` | `generate-custom-instructions-from-codebase` | Migration and code evolution instructions generator for GitHub Copilot. |
| `geofeed-tuner.md` | `geofeed-tuner` | Use this skill whenever the user mentions IP geolocation feeds, RFC 8805, geofeeds, or wants help creating, tuning, validating, or publishing a self-published IP geolocation feed in CSV format. |
| `gh-attach.md` | `gh-attach` | Uploads a local file (screenshot, image, PDF, zip, video) to GitHub user-attachments, downloads GitHub user-attachments, and embeds local files in a PR, issue, or comment. |
| `git-commit.md` | `git-commit` | Use this skill when the user wants to make a Git commit or split changes into more than one commit. |
| `git-flow-branch-creator.md` | `git-flow-branch-creator` | Intelligent Git Flow branch creator that analyzes git status/diff and creates appropriate branches following the nvie Git Flow branching model. |
| `github-actions-efficiency.md` | `github-actions-efficiency` | Audit GitHub Actions workflow efficiency and recommend fixes to reduce CI minutes and costs. |
| `github-actions-hardening.md` | `github-actions-hardening` | Security hardening reviewer for GitHub Actions workflow files (.github/workflows/*.yml). |
| `github-actions-runtime-upgrade-conventions.md` | `github-actions-runtime-upgrade-conventions` | Upgrade GitHub Actions to supported runtimes by selecting safe action versions, preserving workflow behavior, and validating post-upgrade execution. |
| `github-codespaces-efficiency.md` | `github-codespaces-efficiency` | Audit and improve GitHub Codespaces efficiency. |
| `github-copilot-starter.md` | `github-copilot-starter` | Set up complete GitHub Copilot configuration for a new project based on technology stack |
| `github-issues.md` | `github-issues` | Create, update, and manage GitHub issues using MCP tools. |
| `github-release.md` | `github-release` | Guides IA through releasing a new version of a GitHub library end-to-end. |
| `gitmoji.md` | `gitmoji` | Generates commit messages following the gitmoji convention (https://gitmoji.dev) — picks the right emoji for the intent of the change and writes a well-formed message. |
| `globestudio.md` | `globestudio` | Creates, edits and embeds dotted world maps and animated 3D globes with Globestudio (globestudio.app), a free open source studio with 21 looks. |
| `go-mcp-server-generator.md` | `go-mcp-server-generator` | Generate a complete Go MCP server project with proper structure, dependencies, and implementation using the official github.com/modelcontextprotocol/go-sdk. |
| `gsap-framer-scroll-animation.md` | `gsap-framer-scroll-animation` | >- |
| `gtm-0-to-1-launch.md` | `gtm-0-to-1-launch` | Launch new products from idea to first customers. |
| `gtm-ai-gtm.md` | `gtm-ai-gtm` | Go-to-market strategy for AI products. |
| `gtm-board-and-investor-communication.md` | `gtm-board-and-investor-communication` | Board meeting preparation, investor updates, and executive communication. |
| `gtm-developer-ecosystem.md` | `gtm-developer-ecosystem` | Build and scale developer-led adoption through ecosystem programs. |
| `gtm-enterprise-account-planning.md` | `gtm-enterprise-account-planning` | Strategic account planning and execution for enterprise deals. |
| `gtm-enterprise-onboarding.md` | `gtm-enterprise-onboarding` | Four-phase framework for onboarding enterprise customers from contract to value realization. |
| `gtm-operating-cadence.md` | `gtm-operating-cadence` | Design meeting rhythms, metric reporting, quarterly planning, and decision-making velocity for scaling companies. |
| `gtm-partnership-architecture.md` | `gtm-partnership-architecture` | Build and scale partner ecosystems that drive revenue and platform adoption. |
| `gtm-positioning-strategy.md` | `gtm-positioning-strategy` | Find and own a defensible market position. |
| `gtm-product-led-growth.md` | `gtm-product-led-growth` | Build self-serve acquisition and expansion motions. |
| `gtm-technical-product-pricing.md` | `gtm-technical-product-pricing` | Pricing strategy for technical products. |
| `harness-engineering.md` | `harness-engineering` | Adopt repository-level harness engineering for coding agents. |
| `image-annotations.md` | `image-annotations` | Annotate screenshots, diagrams, and images with callout rectangles, arrows, labels, and color-coded highlights using PIL. |
| `image-manipulation-image-magick.md` | `image-manipulation-image-magick` | Process and manipulate images using ImageMagick. |
| `impediment-prioritization.md` | `impediment-prioritization` | Ranks any list of impediments and their countermeasures using a value-stream scoring model (ROI, Cost to Implement, Ease of Deployment, Risk Factor) and a fixed prioritization formula. |
| `import-infrastructure-as-code.md` | `import-infrastructure-as-code` | Import existing Azure resources into Terraform using Azure CLI discovery and Azure Verified Modules (AVM). |
| `incident-postmortem.md` | `incident-postmortem` | Use when an outage, production incident, or significant service degradation has occurred and the team needs a blameless post-mortem / RCA document in the Google SRE format. |
| `issue-fields-migration.md` | `issue-fields-migration` | Bulk-migrate metadata to GitHub issue fields from two sources: repo labels (e.g. |
| `java-add-graalvm-native-image-support.md` | `java-add-graalvm-native-image-support` | GraalVM Native Image skill for Spring Boot, Micronaut and plain Java: detects the build tool and framework, adds native image support, builds the executable, analyzes errors, and iterates until the native build succeeds and the binary runs correctly. |
| `java-debugging.md` | `java-debugging` | Debug Java applications systematically: JDWP remote debugging, jdb, VS Code and IntelliJ attach, debugging Maven/Gradle tests, Spring Boot and Quarkus dev mode, containers, breakpoints/logpoints, and reading stack traces. |
| `java-development.md` | `java-development` | Day-to-day plain Java development without a framework: Maven and Gradle usage and wrappers, project layout, dependency and vulnerability management, modern Java idioms by JDK version (records, sealed types, pattern matching, virtual threads), SLF4J logging, error and null handling, immutability, concurrency basics, static analysis and formatting (Spotless, Error Prone, -Xlint), packaging (jar, jlink, jpackage) and GitHub Actions CI. |
| `java-diagnostics.md` | `java-diagnostics` | Symptom-first runtime diagnostics for JVM applications using JDK tools: jcmd, jstack, jmap, jstat, JFR, GC logs, async-profiler, Native Memory Tracking, and Eclipse MAT. |
| `java-docs.md` | `java-docs` | Ensure that Java types are documented with Javadoc comments and follow best practices for documentation. |
| `java-helidon.md` | `java-helidon` | Get best practices for developing applications with Helidon 4 (SE and MP). |
| `java-hibernate-jpa.md` | `java-hibernate-jpa` | Diagnose and fix Hibernate ORM / Jakarta Persistence problems in plain Java: N+1 queries, lazy loading errors, identifier generation, entity equals/hashCode, cascades, pagination, batching, locking, caching, Lombok on entities, and Hibernate 6/7 differences. |
| `java-junit.md` | `java-junit` | Write, review and fix Java unit tests with JUnit 5 and JUnit 6 (Jupiter), AssertJ and Mockito: assertions, parameterized and nested tests, mocking rules, deterministic time and randomness, Surefire vs Failsafe, JaCoCo coverage, optional PIT mutation testing, and guardrails for agents (never skip or delete failing tests). |
| `java-mcp-server-generator.md` | `java-mcp-server-generator` | Use this skill when the user wants to create a Model Context Protocol (MCP) server in Java or in a Spring Boot app. |
| `java-refactoring-extract-method.md` | `java-refactoring-extract-method` | Refactoring using Extract Methods in Java Language |
| `java-refactoring-remove-parameter.md` | `java-refactoring-remove-parameter` | Refactoring using Remove Parameter in Java Language |
| `java-springboot.md` | `java-springboot` | Write and review application code in an existing Spring Boot 3/4 project: controllers, validation and ProblemDetail errors, Spring Data JPA/JDBC, RestClient and HTTP interfaces, configuration properties, Kafka/AMQP, caching, scheduling, virtual threads, AOT and startup tuning. |
| `java-testcontainers.md` | `java-testcontainers` | Write reliable integration tests in plain Java with Testcontainers 2.x: JUnit Jupiter lifecycle, singleton containers, reuse, generic containers, wait strategies, networks, init scripts, Docker Compose, CI and Docker/Podman setup. |
| `java-upgrade.md` | `java-upgrade` | Upgrade a Java project to a newer JDK (11 to 17, 17 to 21, 21 to 25) and adopt the new language and library features. |
| `javascript-typescript-jest.md` | `javascript-typescript-jest` | Best practices for writing JavaScript/TypeScript tests using Jest, including mocking strategies, test structure, and common patterns. |
| `javax-to-jakarta-migration.md` | `javax-to-jakarta-migration` | Migrate Java code from javax.* to jakarta.* namespace. |
| `kotlin-mcp-server-generator.md` | `kotlin-mcp-server-generator` | Generate a complete Kotlin MCP server project with proper structure, dependencies, and implementation using the official io.modelcontextprotocol:kotlin-sdk library. |
| `kotlin-springboot.md` | `kotlin-springboot` | Get best practices for developing applications with Spring Boot and Kotlin. |
| `landing-page-conversion-audit.md` | `landing-page-conversion-audit` | Audit a landing page, sales page or checkout page for conversion leaks and return a fix list ordered by expected revenue impact. |
| `lean-comments.md` | `lean-comments` | Audits, writes, and refines maintained first-party source-code comments and declaration-level documentation across languages. |
| `legacy-circuit-mockups.md` | `legacy-circuit-mockups` | Generate breadboard circuit mockups and visual diagrams using HTML5 Canvas drawing techniques. |
| `lightweight-charts-react-components.md` | `lightweight-charts-react-components` | lightweight-charts-react-components recipes for TradingView lightweight-charts in React. |
| `linkedin-post-formatter.md` | `linkedin-post-formatter` | Format and draft compelling LinkedIn posts using Unicode bold/italic styling, visual separators, structured sections, and engagement-optimized patterns. |
| `logicapps-custom-code-net10-migration.md` | `logicapps-custom-code-net10-migration` | Migrate Azure Logic Apps Standard local-function custom-code projects from .NET 8 to .NET 10. |
| `lsp-setup.md` | `lsp-setup` | Enable code intelligence (go-to-definition, find-references, hover, type info) for any programming language by installing and configuring an LSP server for Copilot CLI. |
| `macos-golden-gate-design.md` | `macos-golden-gate-design` | Design, implement, review, or refactor native macOS 27 Golden Gate interfaces in SwiftUI or AppKit. |
| `make-blog-post.md` | `make-blog-post` | Turn code from the current session into a blog post written in the voice of its author. |
| `make-repo-contribution.md` | `make-repo-contribution` | All changes to code must follow the guidance documented in the repository. |
| `markdown-to-html.md` | `markdown-to-html` | Convert Markdown files to HTML similar to `marked.js`, `pandoc`, `gomarkdown/markdown`, or similar tools; or writing custom script to convert markdown to html and/or working on web template systems like `jekyll/jekyll`, `gohugoio/hugo`, or similar web templating systems that utilize markdown documents, converting them to html. |
| `markdown-to-word-mermaid.md` | `markdown-to-word-mermaid` | Export Markdown containing Mermaid code fences to Word (.docx) with embedded SVG diagrams and PNG fallbacks. |
| `markstream-install.md` | `markstream-install` | Install and configure Markstream streaming Markdown renderers for Vue, React, Svelte, Angular, Nuxt, and Vue 2 applications. |
| `mcp-cli.md` | `mcp-cli` | Interface for MCP (Model Context Protocol) servers via CLI. |
| `mcp-copilot-studio-server-generator.md` | `mcp-copilot-studio-server-generator` | Generate a complete MCP server implementation optimized for Copilot Studio integration with proper schema constraints and streamable HTTP support |
| `mcp-create-adaptive-cards.md` | `mcp-create-adaptive-cards` | Skill converted from mcp-create-adaptive-cards.prompt.md |
| `mcp-create-declarative-agent.md` | `mcp-create-declarative-agent` | Skill converted from mcp-create-declarative-agent.prompt.md |
| `mcp-deploy-manage-agents.md` | `mcp-deploy-manage-agents` | Skill converted from mcp-deploy-manage-agents.prompt.md |
| `mcp-implementation-security-review.md` | `mcp-implementation-security-review` | Review the implementation source code of MCP (Model Context Protocol) servers, clients, and tool handlers against a security baseline — authentication, sessions, rate limiting, input-schema validation, official-SDK usage, RCE vectors, and the OWASP MCP Top 10 — producing a report with file/line evidence. |
| `mcp-release-qa.md` | `mcp-release-qa` | Verify an MCP server before release by exercising a real protocol session, comparing runtime capabilities with source and documentation, testing failure paths, and recording reproducible evidence. |
| `mcp-security-audit.md` | `mcp-security-audit` | Audit MCP (Model Context Protocol) server configurations for security issues. |
| `md-to-docx.md` | `md-to-docx` | Convert Markdown files to professionally formatted Word (.docx) documents with embedded PNG images — pure JavaScript, no external tools required |
| `meeting-minutes.md` | `meeting-minutes` | Generate concise, actionable meeting minutes for internal meetings. |
| `memory-merger.md` | `memory-merger` | Merges mature lessons from a domain memory file into its instruction file. |
| `mentoring-juniors.md` | `mentoring-juniors` | Socratic mentoring for junior developers and AI newcomers. |
| `microsoft-agent-framework.md` | `microsoft-agent-framework` | Create, update, refactor, explain, or review Microsoft Agent Framework solutions using shared guidance plus language-specific references for .NET and Python. |
| `microsoft-code-reference.md` | `microsoft-code-reference` | Look up Microsoft API references, find working code samples, and verify SDK code is correct. |
| `microsoft-docs.md` | `microsoft-docs` | Query official Microsoft documentation to find concepts, tutorials, and code examples across Azure, .NET, Agent Framework, Aspire, VS Code, GitHub, and more. |
| `microsoft-skill-creator.md` | `microsoft-skill-creator` | Create agent skills for Microsoft technologies using Learn MCP tools. |
| `microsoft-store-publisher.md` | `microsoft-store-publisher` | Prepare, validate, submit, and monitor Windows desktop apps in Microsoft Partner Center. |
| `migrating-oracle-to-postgres-data-access-code.md` | `migrating-oracle-to-postgres-data-access-code` | Migrates .NET/C# data access code from Oracle to PostgreSQL (Npgsql). |
| `migrating-oracle-to-postgres-stored-procedures.md` | `migrating-oracle-to-postgres-stored-procedures` | Migrates Oracle PL/SQL stored procedures to PostgreSQL PL/pgSQL. |
| `minecraft-plugin-development.md` | `minecraft-plugin-development` | Use this skill when building or modifying Minecraft server plugins for Paper, Spigot, or Bukkit, including plugin.yml setup, commands, listeners, schedulers, player state, team or arena systems, persistent progression, economy or profile data, configuration files, Adventure text, and version-safe API usage. |
| `mini-context-graph.md` | `mini-context-graph` | A persistent, compounding knowledge base combining Karpathy's LLM Wiki pattern with a structured knowledge graph. |
| `mkdocs-translations.md` | `mkdocs-translations` | Generate a language translation for a mkdocs documentation stack. |
| `msgraph-sdk.md` | `msgraph-sdk` | Integrate Microsoft Graph SDK into any project — .NET, TypeScript/JavaScript, or Python. |
| `multi-stage-dockerfile.md` | `multi-stage-dockerfile` | Create optimized multi-stage Dockerfiles for any language or framework |
| `mvvm-toolkit.md` | `mvvm-toolkit` | CommunityToolkit.Mvvm (the MVVM Toolkit) core: source generators ([ObservableProperty], [RelayCommand], [NotifyPropertyChangedFor], [NotifyCanExecuteChangedFor], [NotifyDataErrorInfo]), base classes (ObservableObject / ObservableValidator / ObservableRecipient), commands (RelayCommand / AsyncRelayCommand), and validation. |
| `mvvm-toolkit-di.md` | `mvvm-toolkit-di` | Wire CommunityToolkit.Mvvm ViewModels into Microsoft.Extensions.DependencyInjection. |
| `mvvm-toolkit-messenger.md` | `mvvm-toolkit-messenger` | CommunityToolkit.Mvvm Messenger pub/sub for decoupled communication between ViewModels (or any objects). |
| `napkin.md` | `napkin` | Visual whiteboard collaboration for Copilot CLI. |
| `next-intl-add-language.md` | `next-intl-add-language` | Add new language to a Next.js + next-intl application |
| `noob-mode.md` | `noob-mode` | Plain-English translation layer for non-technical Copilot CLI users. |
| `npm-trusted-publishing.md` | `npm-trusted-publishing` | Set up or fix npm trusted publishing (OIDC) in GitHub Actions and remove NPM_TOKEN. |
| `nuget-manager.md` | `nuget-manager` | Manage NuGet packages in .NET projects/solutions. |
| `on-device-delegate.md` | `on-device-delegate` | Saves cloud-model context by briefing one bounded, read-heavy sub-task (more than about 25 KB of prose, or many files that no single command can answer) to the local-coding plugin''s on-device worker, which runs on the local MAI Code 1.1 Flash model. |
| `oo-component-documentation.md` | `oo-component-documentation` | Create or update standardized object-oriented component documentation using a shared template plus mode-specific guidance for new and existing docs. |
| `openapi-to-application-code.md` | `openapi-to-application-code` | Generate a complete, production-ready application from an OpenAPI specification |
| `openapi-to-application-java-spring-boot.md` | `openapi-to-application-java-spring-boot` | Generate a Spring Boot (Java) application from an OpenAPI 3 specification using the spec-first approach: openapi-generator (Maven or Gradle) produces API interfaces and DTOs, you implement controllers, services, persistence, security and tests. |
| `optimize-simplicite-logs.md` | `optimize-simplicite-logs` | capability to parse Simplicité logs from a raw `.txt` file, filter fields to reduce noise, and output the result as structured JSON. |
| `pdftk-server.md` | `pdftk-server` | Skill for using the command-line tool pdftk (PDFtk Server) for working with PDF files. |
| `penpot-uiux-design.md` | `penpot-uiux-design` | Comprehensive guide for creating professional UI/UX designs in Penpot using MCP tools. |
| `performance-review-writer.md` | `performance-review-writer` | Draft performance reviews, self-assessments, peer reviews, and upward feedback in your own voice. |
| `pester-migration.md` | `pester-migration` | Pester migration skill for upgrading PowerShell Pester test suites across major versions — v3→v4, v4→v5, and v5→v6. |
| `pester-should-migration.md` | `pester-should-migration` | Experimental (preview) Pester skill for migrating classic Should -Be (v5) assertion syntax to the new Should-* (v6) assertions (note the hyphen, no space), e.g. |
| `phoenix-cli.md` | `phoenix-cli` | Debug LLM applications using the Phoenix CLI. |
| `phoenix-evals.md` | `phoenix-evals` | Build and run evaluators for AI/LLM applications using Phoenix. |
| `phoenix-tracing.md` | `phoenix-tracing` | OpenInference semantic conventions and instrumentation for Phoenix AI observability. |
| `php-mcp-server-generator.md` | `php-mcp-server-generator` | Generate a complete PHP Model Context Protocol server project with tools, resources, prompts, and tests using the official PHP SDK |
| `planning-oracle-to-postgres-migration-integration-testing.md` | `planning-oracle-to-postgres-migration-integration-testing` | Creates an integration testing plan for .NET data access artifacts during Oracle-to-PostgreSQL database migrations. |
| `plantuml-ascii.md` | `plantuml-ascii` | Generate ASCII art diagrams using PlantUML text mode. |
| `playwright-automation-fill-in-form.md` | `playwright-automation-fill-in-form` | Automate filling in a form using Playwright MCP |
| `playwright-explore-website.md` | `playwright-explore-website` | Website exploration for testing using Playwright MCP |
| `playwright-generate-test.md` | `playwright-generate-test` | Generate a Playwright test based on a scenario using Playwright MCP |
| `poka-yoke.md` | `poka-yoke` | Mistake-proof code so misuse cannot be expressed, rather than warning against it. |
| `ponder.md` | `ponder` | Convergent deliberation loop - repeated grading passes over one subject until the answer stops changing, with coverage enforced so no unit is silently skipped. |
| `postgresql-code-review.md` | `postgresql-code-review` | PostgreSQL-specific code review assistant focusing on PostgreSQL best practices, anti-patterns, and unique quality standards. |
| `postgresql-optimization.md` | `postgresql-optimization` | PostgreSQL-specific development assistant focusing on unique PostgreSQL features, advanced data types, and PostgreSQL-exclusive capabilities. |
| `power-apps-code-app-scaffold.md` | `power-apps-code-app-scaffold` | Scaffold a complete Power Apps Code App project with PAC CLI setup, SDK integration, and connector configuration |
| `power-bi-dax-optimization.md` | `power-bi-dax-optimization` | Comprehensive Power BI DAX formula optimization prompt for improving performance, readability, and maintainability of DAX calculations. |
| `power-bi-model-design-review.md` | `power-bi-model-design-review` | Comprehensive Power BI data model design review prompt for evaluating model architecture, relationships, and optimization opportunities. |
| `power-bi-performance-troubleshooting.md` | `power-bi-performance-troubleshooting` | Systematic Power BI performance troubleshooting prompt for identifying, diagnosing, and resolving performance issues in Power BI models, reports, and queries. |
| `power-bi-report-design-consultation.md` | `power-bi-report-design-consultation` | Power BI report visualization design prompt for creating effective, user-friendly, and accessible reports with optimal chart selection and layout design. |
| `power-platform-architect.md` | `power-platform-architect` | Use this skill when the user needs to transform business requirements, use case descriptions, or meeting transcripts into a technical Power Platform solution architecture, including component selection and Mermaid.js diagrams. |
| `power-platform-mcp-connector-suite.md` | `power-platform-mcp-connector-suite` | Generate complete Power Platform custom connector with MCP integration for Copilot Studio - includes schema generation, troubleshooting, and validation |
| `pr-address-feedback.md` | `pr-address-feedback` | Walk through PR review comments one-by-one, deciding for each whether to act on the feedback or reply with reasoning, and build an approvable resolution plan before changing anything. |
| `pr-artifact-explorer.md` | `pr-artifact-explorer` | Open, share, and inspect GitHub PRs, issues, workflow runs (including scheduled, manual and other runs with no PR), Actions artifacts, and local or HTTP(S) web previews in the Artifact Explorer canvas, with viewport presets, zoom, screenshots, and recoverable download jobs. |
| `pr-dashboard.md` | `pr-dashboard` | Open a GitHub PR dashboard in the browser. |
| `pr-screenshots.md` | `pr-screenshots` | Embed before/after screenshots and annotated images in pull request descriptions. |
| `prd.md` | `prd` | Generate high-quality Product Requirements Documents (PRDs) for software systems and AI-powered features. |
| `premium-frontend-ui.md` | `premium-frontend-ui` | A comprehensive guide for GitHub Copilot to craft immersive, high-performance web experiences with advanced motion, typography, and architectural craftsmanship. |
| `project-workflow-analysis-blueprint-generator.md` | `project-workflow-analysis-blueprint-generator` | Comprehensive technology-agnostic prompt generator for documenting end-to-end application workflows. |
| `prompt-optimizer.md` | `prompt-optimizer` | Turn any rough prompt, half-formed idea, or task description into a finished, ready-to-send prompt optimized for any LLM model inside a chat interface — NOT the API. |
| `protobuf-grpc-api-review.md` | `protobuf-grpc-api-review` | Review Protocol Buffer (.proto) and gRPC API changes for wire and JSON compatibility, safe schema evolution, rollout hazards, and RPC contract quality. |
| `publish-to-pages.md` | `publish-to-pages` | Publish presentations and web content to GitHub Pages. |
| `pytest-coverage.md` | `pytest-coverage` | Run pytest tests with coverage, discover lines missing coverage, and increase coverage to 100%. |
| `python-azure-iot-edge-modules.md` | `python-azure-iot-edge-modules` | Build and operate Python Azure IoT Edge modules with robust messaging, deployment manifests, observability, and production readiness checks. |
| `python-mcp-server-generator.md` | `python-mcp-server-generator` | Use this skill when the user wants to create a new Model Context Protocol (MCP) server in Python. |
| `python-pypi-package-builder.md` | `python-pypi-package-builder` | End-to-end skill for building, testing, linting, versioning, and publishing a production-grade Python library to PyPI. |
| `qdrant-clients-sdk.md` | `qdrant-clients-sdk` | Qdrant provides client SDKs for various programming languages, allowing easy integration with Qdrant deployments. |
| `qdrant-deployment-options.md` | `qdrant-deployment-options` | Guides Qdrant deployment selection. |
| `qdrant-model-migration.md` | `qdrant-model-migration` | Guides embedding model migration in Qdrant without downtime. |
| `qdrant-monitoring.md` | `qdrant-monitoring` | Guides Qdrant monitoring and observability setup. |
| `debugging.md` | `debugging` | Diagnoses Qdrant production issues using metrics and observability tools. |
| `setup.md` | `setup` | Guides Qdrant monitoring setup including Prometheus scraping, health probes, Hybrid Cloud metrics, alerting, and log centralization. |
| `qdrant-performance-optimization.md` | `qdrant-performance-optimization` | Different techniques to optimize the performance of Qdrant, including indexing strategies, query optimization, and hardware considerations. |
| `indexing-performance-optimization.md` | `indexing-performance-optimization` | Diagnoses and fixes slow Qdrant indexing and data ingestion. |
| `memory-usage-optimization.md` | `memory-usage-optimization` | Diagnoses and reduces Qdrant memory usage. |
| `search-speed-optimization.md` | `search-speed-optimization` | Diagnoses and fixes slow Qdrant search. |
| `qdrant-scaling.md` | `qdrant-scaling` | Guides Qdrant scaling decisions. |
| `minimize-latency.md` | `minimize-latency` | Guides Qdrant query latency optimization. |
| `scaling-data-volume.md` | `scaling-data-volume` | Guides Qdrant data volume scaling decisions. |
| `horizontal-scaling.md` | `horizontal-scaling` | Diagnoses and guides Qdrant horizontal scaling decisions. |
| `sliding-time-window.md` | `sliding-time-window` | Guides sliding time window scaling in Qdrant. |
| `tenant-scaling.md` | `tenant-scaling` | Guides Qdrant multi-tenant scaling. |
| `vertical-scaling.md` | `vertical-scaling` | Guides Qdrant vertical scaling decisions. |
| `scaling-qps.md` | `scaling-qps` | Guides Qdrant query throughput (QPS) scaling. |
| `scaling-query-volume.md` | `scaling-query-volume` | Guides Qdrant query volume scaling. |
| `qdrant-search-quality.md` | `qdrant-search-quality` | Diagnoses and improves Qdrant search relevance. |
| `diagnosis.md` | `diagnosis` | Diagnoses Qdrant search quality issues. |
| `search-strategies.md` | `search-strategies` | Guides Qdrant search strategy selection. |
| `qdrant-version-upgrade.md` | `qdrant-version-upgrade` | Guidance on how to upgrade your Qdrant version without interrupting the availability of your application and ensuring data integrity. |
| `quality-playbook.md` | `quality-playbook` | Run a complete quality engineering audit on any codebase. |
| `quarkus-application-development.md` | `quarkus-application-development` | Write Quarkus application code: REST with Quarkus REST, validation, exception mappers, OpenAPI, configuration, CDI (ArC), Hibernate ORM with Panache, Mutiny and virtual threads, Reactive Messaging with Kafka, OIDC security, health, metrics, OpenTelemetry, fault tolerance, REST Client, scheduler and cache. |
| `quarkus-dev-services-and-testing.md` | `quarkus-dev-services-and-testing` | Quarkus Dev Services and testing: zero-config containers, @QuarkusTest, @QuarkusIntegrationTest, test resources, RestAssured, @InjectMock, profiles and continuous testing. |
| `quarkus-native-and-container.md` | `quarkus-native-and-container` | Build Quarkus native executables (Mandrel/GraalVM), fix native failures with reflection registration, test the native binary, and produce container images and Kubernetes/OpenShift manifests. |
| `quasi-coder.md` | `quasi-coder` | Expert 10x engineer skill for interpreting and implementing code from shorthand, quasi-code, and natural language descriptions. |
| `react-audit-grep-patterns.md` | `react-audit-grep-patterns` | Provides the complete, verified grep scan command library for auditing React codebases before a React 18.3.1 or React 19 upgrade. |
| `react-container-presentation-component.md` | `react-container-presentation-component` | Create a React component using the Container/Presentation pattern in src/components by asking for the component name and type (ui or features), then scaffold files that follow this repository's TypeScript, Storybook, and SCSS conventions. |
| `react18-batching-patterns.md` | `react18-batching-patterns` | Provides exact patterns for diagnosing and fixing automatic batching regressions in React 18 class components. |
| `react18-dep-compatibility.md` | `react18-dep-compatibility` | React 18.3.1 and React 19 dependency compatibility matrix. |
| `react18-enzyme-to-rtl.md` | `react18-enzyme-to-rtl` | Provides exact Enzyme → React Testing Library migration patterns for React 18 upgrades. |
| `react18-legacy-context.md` | `react18-legacy-context` | Provides the complete migration pattern for React legacy context API (contextTypes, childContextTypes, getChildContext) to the modern createContext API. |
| `react18-lifecycle-patterns.md` | `react18-lifecycle-patterns` | Provides exact before/after migration patterns for the three unsafe class component lifecycle methods - componentWillMount, componentWillReceiveProps, and componentWillUpdate - targeting React 18.3.1. |
| `react18-string-refs.md` | `react18-string-refs` | Provides exact migration patterns for React string refs (ref="name" + this.refs.name) to React.createRef() in class components. |
| `react19-concurrent-patterns.md` | `react19-concurrent-patterns` | Preserve React 18 concurrent patterns and adopt React 19 APIs (useTransition, useDeferredValue, Suspense, use(), useOptimistic, Actions) during migration. |
| `react19-source-patterns.md` | `react19-source-patterns` | Reference for React 19 source-file migration patterns, including API changes, ref handling, and context updates. |
| `react19-test-patterns.md` | `react19-test-patterns` | Provides before/after patterns for migrating test files to React 19 compatibility, including act() imports, Simulate removal, and StrictMode call count changes. |
| `readme-blueprint-generator.md` | `readme-blueprint-generator` | Intelligent README.md generation prompt that analyzes project documentation structure and creates comprehensive repository documentation. |
| `rebase-current-branch.md` | `rebase-current-branch` | Rebase the currently checked out feature branch onto the latest upstream default branch. |
| `refactor.md` | `refactor` | Surgical code refactoring to improve maintainability without changing behavior. |
| `refactor-method-complexity-reduce.md` | `refactor-method-complexity-reduce` | Refactor given method `${input:methodName}` to reduce its cognitive complexity to `${input:complexityThreshold}` or below, by extracting helper methods. |
| `refactor-plan.md` | `refactor-plan` | Create a concrete plan before starting a multi-file refactor. |
| `remember.md` | `remember` | Transforms lessons learned into domain-organized memory instructions (global or workspace). |
| `remember-interactive-programming.md` | `remember-interactive-programming` | A micro-prompt that reminds the agent that it is an interactive programmer. |
| `repo-standardizer.md` | `repo-standardizer` | Polish any GitHub repository's surface — labels (emoji rating tiers, P0–P3 priority, impact severity), issue forms, PR template, CI workflows, CODEOWNERS, rulesets, docs. |
| `repo-story-time.md` | `repo-story-time` | Generate a comprehensive repository summary and narrative story from commit history |
| `resx-source-generator-migration.md` | `resx-source-generator-migration` | Migrates a project that uses checked-in .designer.cs files behind .resx to using a source-generator instead |
| `review-and-refactor.md` | `review-and-refactor` | Review and refactor code in your project according to defined instructions |
| `reviewing-oracle-to-postgres-migration.md` | `reviewing-oracle-to-postgres-migration` | Identifies Oracle-to-PostgreSQL migration risks by cross-referencing code against known behavioral differences (empty strings, refcursors, type coercion, sorting/collations, UNION ALL planner risks, materialized-view refresh requirements, timestamps, concurrent transactions, etc.). |
| `rhino3d-scripts.md` | `rhino3d-scripts` | Authoring and debugging scripts for Rhinoceros 3D (Rhino 8 and later). |
| `roslyn-analyzers.md` | `roslyn-analyzers` | Build, review, debug, package, and test Roslyn diagnostic analyzers, code fix providers, and incremental source generators. |
| `roundup.md` | `roundup` | Generate personalized status briefings on demand. |
| `roundup-setup.md` | `roundup-setup` | Interactive onboarding that learns your communication style, audiences, and data sources to configure personalized status briefings. |
| `ruby-mcp-server-generator.md` | `ruby-mcp-server-generator` | Generate a complete Model Context Protocol server project in Ruby using the official MCP Ruby SDK gem. |
| `ruff-recursive-fix.md` | `ruff-recursive-fix` | Run Ruff checks with optional scope and rule overrides, apply safe and unsafe autofixes iteratively, review each change, and resolve remaining findings with targeted edits or user decisions. |
| `rust-mcp-server-generator.md` | `rust-mcp-server-generator` | Generate a complete Rust Model Context Protocol server project with tools, prompts, resources, and tests using the official rmcp SDK |
| `salesforce-apex-quality.md` | `salesforce-apex-quality` | Apex code quality guardrails for Salesforce development. |
| `salesforce-component-standards.md` | `salesforce-component-standards` | Quality standards for Salesforce Lightning Web Components (LWC), Aura components, and Visualforce pages. |
| `salesforce-flow-design.md` | `salesforce-flow-design` | Salesforce Flow architecture decisions, flow type selection, bulk safety validation, and fault handling standards. |
| `sandbox-npm-install.md` | `sandbox-npm-install` | Install npm packages in a Docker sandbox environment. |
| `sap-cloud-integration.md` | `sap-cloud-integration` | SAP Cloud Integration (CPI, part of SAP Integration Suite) runtime-specific guidance for building and troubleshooting iFlows. |
| `scaffolding-oracle-to-postgres-migration-test-project.md` | `scaffolding-oracle-to-postgres-migration-test-project` | Scaffolds an xUnit integration test project targeting Oracle in .NET solutions. |
| `scout-issue.md` | `scout-issue` | Use when a developer wants to find the best GitHub issues to contribute to in a repository. |
| `screen-recording.md` | `screen-recording` | Create annotated animated GIF demos and screen recordings for pull requests and documentation. |
| `secret-scanning.md` | `secret-scanning` | Guide for configuring and managing GitHub secret scanning, push protection, custom patterns, and secret alert remediation. |
| `security-review.md` | `security-review` | AI-powered codebase security scanner that reasons about code like a security researcher — tracing data flows, understanding component interactions, and catching vulnerabilities that pattern-matching tools miss. |
| `semantic-kernel.md` | `semantic-kernel` | Create, update, refactor, explain, or review Semantic Kernel solutions using shared guidance plus language-specific references for .NET and Python. |
| `setup-my-iq.md` | `setup-my-iq` | Create, set up, or update the personal context portfolio: structured markdown files describing who you are, how you work, your teams, and your tool/ADO configuration. |
| `shopify-review-triage.md` | `shopify-review-triage` | Use this skill when someone wants public Shopify App Store reviews, low-star reviews, or merchant feedback triaged, prioritized, clustered, or turned into a product or support brief. |
| `shuffle-json-data.md` | `shuffle-json-data` | Shuffle repetitive JSON objects safely by validating schema consistency before randomising entries. |
| `signal-write.md` | `signal-write` | Emit structured agent signals — hands-up, blocked, done, checkpoint, partnership. |
| `skill-distribution-audit.md` | `skill-distribution-audit` | Audit a skill collection before release or investigate installer omissions, archived/template leakage, duplicate identities, and manifest drift. |
| `slang-shader-engineer.md` | `slang-shader-engineer` | Use when working with Slang shaders, shader modules, HLSL-compatible GPU code, graphics pipelines, compute shaders, tessellation, ray tracing, parameter blocks, generics, interfaces, capabilities, cross-compilation, shader optimization, shader review, or C++ engine integration for Slang. |
| `snowflake-semanticview.md` | `snowflake-semanticview` | Create, alter, and validate Snowflake semantic views using Snowflake CLI (snow). |
| `speak-summary.md` | `speak-summary` | Convert text, markdown, or a summary produced by another skill into a listenable MP3 using local CPU-only neural text-to-speech. |
| `sponsor-finder.md` | `sponsor-finder` | Find which of a GitHub repository's dependencies are sponsorable via GitHub Sponsors. |
| `spring-boot-4-migration.md` | `spring-boot-4-migration` | Migrate a Spring Boot 3.x application to Spring Boot 4.0 (Spring Framework 7, Jackson 3, modular starters, JSpecify). |
| `spring-boot-testing.md` | `spring-boot-testing` | Expert Spring Boot testing specialist that selects the best testing techniques for your situation: test slices, Testcontainers with @ServiceConnection, Failsafe integration tests, MockitoBean, JUnit and AssertJ. |
| `spring-observability.md` | `spring-observability` | Add and review observability in Spring Boot 3/4 apps: Actuator exposure and health probes, Micrometer metrics, Observation API, OpenTelemetry tracing and OTLP/Prometheus export, structured logging with correlation ids, and safe use of heapdump/threaddump. |
| `spring-security.md` | `spring-security` | Configure, test and review Spring Security 6/7 in Spring Boot 3/4 apps: SecurityFilterChain lambda DSL, method security, OAuth2 resource server with JWT, OIDC login, CSRF/CORS, password encoding, headers, actuator protection, and MockMvc security tests. |
| `sql-code-review.md` | `sql-code-review` | Universal SQL code review assistant that performs comprehensive security, maintainability, and code quality analysis across all SQL databases (MySQL, PostgreSQL, SQL Server, Oracle). |
| `sql-object-impact-analysis.md` | `sql-object-impact-analysis` | Before modifying a table, column, stored procedure, view, or trigger in a legacy codebase, trace every place that references it — across other SQL objects (procs, views, triggers) AND application code (C#, Angular/TypeScript, JS, or any language in the repo) — and produce a structured blast-radius report so you know what breaks before you change it. |
| `sql-optimization.md` | `sql-optimization` | Universal SQL performance optimization assistant for comprehensive query tuning, indexing strategies, and database performance analysis across all SQL databases (MySQL, PostgreSQL, SQL Server, Oracle). |
| `sql-server-table-reconciliation.md` | `sql-server-table-reconciliation` | Use when: comparing SQL Server tables across instances, data migration validation, ETL verification, row mismatch detection, schema drift, reconciliation report, production vs staging comparison. |
| `ssma-console.md` | `ssma-console` | Use when: SSMA console operations — create project, generate assessment report, convert schema, migrate data, Oracle to SQL Server migration, schema conversion, data migration |
| `steno-mode.md` | `steno-mode` | Shorthand-first response compression that cuts ~40% of response tokens while preserving technical precision and exact literals. |
| `structured-autonomy-generate.md` | `structured-autonomy-generate` | Structured Autonomy Implementation Generator Prompt |
| `structured-autonomy-implement.md` | `structured-autonomy-implement` | Structured Autonomy Implementation Prompt |
| `structured-autonomy-plan.md` | `structured-autonomy-plan` | Structured Autonomy Planning Prompt |
| `suggest-awesome-github-copilot-agents.md` | `suggest-awesome-github-copilot-agents` | Suggest relevant GitHub Copilot Custom Agents files from the awesome-copilot repository based on current repository context and chat history, avoiding duplicates with existing custom agents in this repository, and identifying outdated agents that need updates. |
| `suggest-awesome-github-copilot-instructions.md` | `suggest-awesome-github-copilot-instructions` | Suggest relevant GitHub Copilot instruction files from the awesome-copilot repository based on current repository context and chat history, avoiding duplicates with existing instructions in this repository, and identifying outdated instructions that need updates. |
| `suggest-awesome-github-copilot-skills.md` | `suggest-awesome-github-copilot-skills` | Suggest relevant GitHub Copilot skills from the awesome-copilot repository based on current repository context and chat history, avoiding duplicates with existing skills in this repository, and identifying outdated skills that need updates. |
| `supabase-rls-policies.md` | `supabase-rls-policies` | Write, review, and test Supabase Row Level Security (RLS) policies so that one user cannot read or change another user''s rows. |
| `swift-mcp-server-generator.md` | `swift-mcp-server-generator` | Generate a complete Model Context Protocol server project in Swift using the official MCP Swift SDK package. |
| `system-commandline-cli.md` | `system-commandline-cli` | Use this skill when adding, modifying, or reviewing CLI commands in a .NET project built with System.CommandLine. |
| `technical-job-search.md` | `technical-job-search` | Use this skill when a software engineer asks for help with job search tasks: parsing or analyzing a job description, tailoring a CV/resume, writing a cover letter, evaluating a job offer, or drafting a post-interview follow-up email. |
| `technology-stack-blueprint-generator.md` | `technology-stack-blueprint-generator` | Comprehensive technology stack blueprint generator that analyzes codebases to create detailed architectural documentation. |
| `terraform-azurerm-set-diff-analyzer.md` | `terraform-azurerm-set-diff-analyzer` | Analyze Terraform plan JSON output for AzureRM Provider to distinguish between false-positive diffs (order-only changes in Set-type attributes) and actual resource changes. |
| `test-gap-audit.md` | `test-gap-audit` | Run a read-only audit for missing, weak, stale, or mis-scoped test coverage. |
| `threat-model-analyst.md` | `threat-model-analyst` | Full STRIDE-A threat model analysis and incremental update skill for repositories and systems. |
| `tiny-stepping.md` | `tiny-stepping` | Incremental development workflow that makes the smallest meaningful change per step and pauses for feedback, so the direction gets validated early before continuing. |
| `tldr-prompt.md` | `tldr-prompt` | Create tldr summaries for GitHub Copilot files (prompts, agents, instructions, collections), MCP servers, or documentation from URLs and queries. |
| `tm7-threat-model.md` | `tm7-threat-model` | Creates valid Microsoft Threat Modeling Tool (.tm7) files compatible with the Microsoft Threat Modeling Tool v7.3+. |
| `tugboat.md` | `tugboat` | Anxiety-aware, evidence-driven collaboration for stalled or high-stakes work when a user says uncertainty, repeated setbacks, or lack of visible progress is causing significant anxiety or distress. |
| `typescript-mcp-server-generator.md` | `typescript-mcp-server-generator` | Generate a complete MCP server project in TypeScript using the MCP TypeScript SDK v2 (@modelcontextprotocol/server) with tools, resources, and proper configuration |
| `typespec-api-operations.md` | `typespec-api-operations` | Add GET, POST, PATCH, and DELETE operations to a TypeSpec API plugin with proper routing, parameters, and adaptive cards |
| `typespec-create-agent.md` | `typespec-create-agent` | Generate a complete TypeSpec declarative agent with instructions, capabilities, and conversation starters for Microsoft 365 Copilot |
| `typespec-create-api-plugin.md` | `typespec-create-api-plugin` | Generate a TypeSpec API plugin with REST operations, authentication, and Adaptive Cards for Microsoft 365 Copilot |
| `ui-screenshots.md` | `ui-screenshots` | Capture screenshots of web apps during development using Playwright and PIL. |
| `unit-test-vue-pinia.md` | `unit-test-vue-pinia` | Write and review unit tests for Vue 3 + TypeScript + Vitest + Pinia codebases. |
| `update-avm-modules-in-bicep.md` | `update-avm-modules-in-bicep` | Update Azure Verified Modules (AVM) to latest versions in Bicep files. |
| `update-implementation-plan.md` | `update-implementation-plan` | Update an existing implementation plan file with new or update requirements to provide new features, refactoring existing code or upgrading packages, design, architecture or infrastructure. |
| `update-llms.md` | `update-llms` | Update the llms.txt file in the root folder to reflect changes in documentation or specifications following the llms.txt specification at https://llmstxt.org/ |
| `update-markdown-file-index.md` | `update-markdown-file-index` | Update a markdown file section with an index/table of files from a specified folder. |
| `update-specification.md` | `update-specification` | Update an existing specification file for the solution, optimized for Generative AI consumption based on new requirements or updates to any existing code. |
| `v-development.md` | `v-development` | Guide GitHub Copilot through V language development: installing the toolchain, project layout with v.mod, building, testing, formatting, and writing idiomatic V including Option/Result error handling. |
| `vardoger-analyze.md` | `vardoger-analyze` | Use when the user asks to personalize the GitHub Copilot CLI assistant, adapt Copilot to their style, use vardoger, or analyze their Copilot CLI conversation history. |
| `vcpkg.md` | `vcpkg` | Guide for setting up vcpkg in C++ projects, managing dependency versions, and cross-compiling. |
| `verify-agent-action.md` | `verify-agent-action` | Review a proposed AI-agent action or human-approval packet before execution. |
| `vscode-ext-commands.md` | `vscode-ext-commands` | Guidelines for contributing commands in VS Code extensions. |
| `vscode-ext-localization.md` | `vscode-ext-localization` | Guidelines for proper localization of VS Code extensions, following VS Code extension development guidelines, libraries and good practices |
| `web-design-reviewer.md` | `web-design-reviewer` | This skill enables visual inspection of websites running locally or remotely to identify and fix design issues. |
| `webapp-testing.md` | `webapp-testing` | Toolkit for interacting with and testing local web applications using Playwright. |
| `webmcpify.md` | `webmcpify` | WebMCP agent skill for curated core coverage or route-by-route parity — inventory an existing web app, integrate approved tools, then inspect, verify and heal them in a real browser. |
| `what-context-needed.md` | `what-context-needed` | Ask Copilot what files it needs to see before answering a question |
| `winmd-api-search.md` | `winmd-api-search` | Find and explore Windows desktop APIs. |
| `winui3-migration-guide.md` | `winui3-migration-guide` | UWP-to-WinUI 3 migration reference. |
| `workshop-create.md` | `workshop-create` | Create a new workshop or use an existing directory as one. |
| `write-coding-standards-from-file.md` | `write-coding-standards-from-file` | Write a coding standards document for a project using the coding styles from the file(s) and/or folder(s) passed as arguments in the prompt. |

## Index — anthropics (13)

The 6 duplicate skills (brand-guidelines, canvas-design, internal-comms,
theme-factory, webapp-testing, template) are skipped — they are already in
the zip under their awesome behaviour names. claude-api was removed in v14.

| Behaviour file | Original skill | What it does |
|---|---|---|
| `academy-guide.md` | `academy-guide` | Stop and check this skill before finishing any reply to a question about how to use Claude or a Claude product — it recommends matching courses, tutorials, and use cases from Claude Academy (academy.claude.com), Anthropic's learning hub. |
| `algorithmic-art.md` | `algorithmic-art` | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. |
| `discernment-nudge.md` | `discernment-nudge` | After you give a substantive answer or draft that the user may act on — advice or recommendations, drafted artifacts such as goals, plans, pitches, proposals, or emails, estimates or projections, analysis or interpretation of data, factual claims they may rely on, or a multi-step argument — invoke this skill BEFORE finalizing your reply and then, if it applies, append 2-3 short follow-up questions, each tied to something specific in what you just produced, that help the user check key facts, probe the reasoning or assumptions, and notice missing context. |
| `doc-coauthoring.md` | `doc-coauthoring` | Guide users through a structured workflow for co-authoring documentation. |
| `edit-docx.md` | `docx` | Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files) or Word templates (.dotx files). |
| `frontend-design.md` | `frontend-design` | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. |
| `mcp-builder.md` | `mcp-builder` | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. |
| `edit-pdf.md` | `pdf` | Use this skill whenever the user wants to do anything with PDF files. |
| `edit-pptx.md` | `pptx` | Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. |
| `skill-creator.md` | `skill-creator` | Create new skills, modify and improve existing skills, and measure skill performance. |
| `slack-gif-creator.md` | `slack-gif-creator` | Knowledge and utilities for creating animated GIFs optimized for Slack. |
| `web-artifacts-builder.md` | `web-artifacts-builder` | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). |
| `edit-xlsx.md` | `xlsx` | Use this skill any time a spreadsheet file is the primary input or output. |

## Index — jwynia (113)

One row per skill; full descriptions are in `MANIFEST.csv`.

| Behaviour file | Original skill | What it does |
|---|---|---|
| `adaptation-synthesis.md` | `adaptation-synthesis` | Synthesize new works from extracted functional DNA documents. |
| `book-marketing.md` | `book-marketing` | Diagnose book marketing copy problems and generate platform-optimized blurbs, descriptions, taglines, and query pitches. |
| `dna-extraction.md` | `dna-extraction` | Extract the functional DNA from existing works (TV, film, books, plays). |
| `flash-fiction.md` | `flash-fiction` | Diagnose and fix problems in flash fiction and micro fiction. |
| `game-facilitator.md` | `game-facilitator` | Narrative RPG game master for collaborative storytelling. |
| `interactive-fiction.md` | `interactive-fiction` | Diagnose branching narrative problems. |
| `list-builder.md` | `list-builder` | Build comprehensive randomization lists for creative entropy. |
| `media-adaptation.md` | `media-adaptation` | Systematically analyze existing media to extract transferable elements for new settings. |
| `multi-order-evolution.md` | `multi-order-evolution` | Design multi-generational societal evolution for science fiction settings. |
| `paradox-fables.md` | `paradox-fables` | Create fables that embody paradoxical wisdom without resolving into simple morals. |
| `sensitivity-check.md` | `sensitivity-check` | Evaluate representation and flag potential harm concerns. |
| `shared-world.md` | `shared-world` | Maintain a wiki-style world bible for collaborative fiction. |
| `sleep-story.md` | `sleep-story` | Write stories designed to help listeners fall asleep. |
| `table-tone.md` | `table-tone` | Diagnose and calibrate tonal delivery for tabletop RPG sessions. |
| `character-arc.md` | `character-arc` | Design and troubleshoot character transformation arcs. |
| `character-naming.md` | `character-naming` | Break LLM name defaults with external entropy. |
| `dialogue.md` | `dialogue` | Diagnose flat dialogue, same-voice characters, and lack of subtext. |
| `memetic-depth.md` | `memetic-depth` | Create the perception of cultural depth through strategic juxtaposition of familiar and unfamiliar elements. |
| `statistical-distance.md` | `statistical-distance` | Transform clichéd story elements by pushing along the emotional vector toward statistical edges. |
| `underdog-unit.md` | `underdog-unit` | Generate stories about institutional outcasts given impossible mandates with minimal resources. |
| `story-analysis.md` | `story-analysis` | Systematically evaluate completed short stories or novel chapters to identify strengths, weaknesses, and improvement opportunities. |
| `story-coach.md` | `story-coach` | Act as an assistive writing coach who guides but never writes for the user. |
| `story-collaborator.md` | `story-collaborator` | Act as an active writing partner who contributes content alongside the human writer. |
| `story-idea-generator.md` | `story-idea-generator` | Generate story concepts using a genre-first approach. |
| `story-sense.md` | `story-sense` | Diagnose what any story needs regardless of its current state. |
| `cliche-transcendence.md` | `cliche-transcendence` | Transform predictable story elements into fresh, original versions. |
| `drafting.md` | `drafting` | Break through blocks and execute first drafts. |
| `genre-conventions.md` | `genre-conventions` | Diagnose genre problems and generate genre-specific elements. |
| `prose-style.md` | `prose-style` | Diagnose sentence-level issues after structure is solid. |
| `revision.md` | `revision` | Guide the edit pass after drafting. |
| `chapter-drafter.md` | `chapter-drafter` | Autonomously draft and polish chapters through multi-skill editorial passes. |
| `endings.md` | `endings` | Diagnose weak endings, rushed resolutions, and arbitrary conclusions. |
| `identity-denial.md` | `identity-denial` | Structure stories around protagonists who refuse to acknowledge what they're becoming. |
| `key-moments.md` | `key-moments` | Structure stories around essential emotional moments using Rodriguez's approach integrated with elemental genres. |
| `moral-parallax.md` | `moral-parallax` | Generate speculative fiction stories about systemic exploitation by collapsing comfortable moral distances. |
| `novel-revision.md` | `novel-revision` | Manage multi-level novel revisions while preventing cascade problems. |
| `outline-coach.md` | `outline-coach` | Act as an assistive outline coach who guides structural development through questions. |
| `outline-collaborator.md` | `outline-collaborator` | Act as an active outline partner who develops structure collaboratively. |
| `perspectival-constellation.md` | `perspectival-constellation` | Structure multi-POV stories through catalyst environments. |
| `positional-revelation.md` | `positional-revelation` | Generate stories where ordinary people become crucial through their structural position in systems. |
| `reverse-outliner.md` | `reverse-outliner` | Reverse-engineer published books into structured scene-by-scene outlines for study. |
| `scene-sequencing.md` | `scene-sequencing` | Structure scenes and control pacing using scene-sequel rhythm. |
| `story-zoom.md` | `story-zoom` | Manage multi-level story synchronization. |
| `belief-systems.md` | `belief-systems` | Design religious and belief systems for fictional worlds. |
| `conlang.md` | `conlang` | Generate phonologically consistent constructed languages for fiction. |
| `economic-systems.md` | `economic-systems` | Design economic systems for fictional worlds. |
| `governance-systems.md` | `governance-systems` | Design political entities and governance systems for fictional worlds. |
| `language-evolution.md` | `language-evolution` | Design evolving language systems for fictional worlds. |
| `metabolic-cultures.md` | `metabolic-cultures` | Design cultures for closed-loop life support systems in space. |
| `oblique-worldbuilding.md` | `oblique-worldbuilding` | Create worldbuilding quotes and epigraphs through documentary perspectives. |
| `settlement-design.md` | `settlement-design` | Design cities, towns, and settlements for fictional worlds. |
| `systemic-worldbuilding.md` | `systemic-worldbuilding` | Build worlds through cascading consequences from speculative changes. |
| `world-fates.md` | `world-fates` | Manage long-term fate and fortune across a shared world. |
| `worldbuilding.md` | `worldbuilding` | Diagnose world-level story problems. |
| `joke-engineering.md` | `joke-engineering` | Diagnose and improve humor using systems thinking. |
| `lyric-diagnostic.md` | `lyric-diagnostic` | Diagnose lyric problems across prosody, rhyme, meaning, register, sound, and structure. |
| `musical-dna.md` | `musical-dna` | Extract descriptive musical characteristics from any artist or band without using their name, building a vocabulary of sonic qualities for AI music generation, music description, or creative recombination. |
| `product-analysis.md` | `product-analysis` | Diagnose competitive product analysis state and guide through systematic market evaluation. |
| `document-to-narration.md` | `document-to-narration` | Convert written documents to narrated video scripts with TTS audio and word-level timing. |
| `technology-impact.md` | `technology-impact` | Systematically analyze societal impacts of technologies using McLuhan's Tetrad of Media Effects. |
| `presentation-design.md` | `presentation-design` | Design and evaluate presentations that communicate effectively. |
| `speech-adaptation.md` | `speech-adaptation` | Transform comprehensive written content into purposeful spoken guidance. |
| `ebook-analysis.md` | `ebook-analysis` | Parse ebooks, extract concepts and entities with citation traceability, classify by type/layer, and synthesize across book collections. |
| `pdf-generator.md` | `pdf-generator` | Create and manipulate PDF files programmatically. |
| `pptx-generator.md` | `pptx-generator` | Create and manipulate PowerPoint PPTX files programmatically. |
| `revealjs-presenter.md` | `revealjs-presenter` | Generate RevealJS HTML presentations with reliable layout, professional typography, and effective visual communication. |
| `xlsx-generator.md` | `xlsx-generator` | Create and manipulate Excel XLSX files programmatically. |
| `docx-generator.md` | `docx-generator` | Create and manipulate Word DOCX files programmatically. |
| `competency.md` | `competency` | Guide competency framework development and operation. |
| `gentle-teaching.md` | `gentle-teaching` | Guide AI-assisted learning that empowers learners while maintaining appropriate boundaries. |
| `brainstorming.md` | `brainstorming` | Expand seeds and escape convergent ideation. |
| `naming.md` | `naming` | Diagnose why names don't work and guide creation of names that do. |
| `agent-bootstrap.md` | `agent-bootstrap` | Bootstrap agentic development environment from agent.toml manifest |
| `context-network.md` | `context-network` | Bootstrap, maintain, and evolve context networks across their full lifecycle. |
| `context-retrospective.md` | `context-retrospective` | Analyze agent-user interaction transcripts to identify context network maintenance needs and guidance improvements. |
| `good-thinking.md` | `good-thinking` | Diagnose thinking failures and maintain process-sovereignty by auditing cognitive orientation and operation balance. |
| `skill-builder.md` | `skill-builder` | Build new agent skills. |
| `skill-integrator.md` | `skill-integrator` | Integrate installed skill usage guidance into project CLAUDE.md/AGENTS.md based on project context. |
| `task-breakdown.md` | `task-breakdown` | Help neurodivergent users break down overwhelming tasks into manageable steps. |
| `research-workflow.md` | `research-workflow` | Guide agents through structured research including planning, multi-query execution, source analysis, and synthesis. |
| `media-meta-analysis.md` | `media-meta-analysis` | Synthesize multiple media analyses into cross-source patterns and insights. |
| `web-search.md` | `web-search` | Search the web using the agent's built-in WebSearch tool. |
| `claim-investigation.md` | `claim-investigation` | Systematically investigate social media claims and viral content. |
| `fact-check.md` | `fact-check` | Verify claims in generated output against sources. |
| `blind-spot-detective.md` | `blind-spot-detective` | Systematically identify what's missing in non-fiction writing—both blind spots (inherent limitations) and blank spots (gaps that could be addressed). |
| `voice-analysis.md` | `voice-analysis` | Extract and document a writer's distinctive voice patterns for consistent reproduction. |
| `non-fiction-revision.md` | `non-fiction-revision` | Diagnose and guide revisions in non-fiction books. |
| `summarization.md` | `summarization` | Create effective summaries by matching summarization type to purpose, audience, and context. |
| `architecture-decision.md` | `architecture-decision` | Systematically evaluate architecture decisions, document trade-offs, and select appropriate patterns. |
| `requirements-analysis.md` | `requirements-analysis` | Diagnose requirements problems and guide discovery of real needs and constraints |
| `system-design.md` | `system-design` | Diagnose design problems and guide architecture decisions for solo developers |
| `code-review.md` | `code-review` | Provide structured code review guidance for catching defects and improving quality. |
| `task-decomposition.md` | `task-decomposition` | Transform overwhelming development tasks into manageable units. |
| `devcontainer.md` | `devcontainer` | Diagnose devcontainer configuration problems and guide development environment setup. |
| `electron-best-practices.md` | `electron-best-practices` | Guide AI agents through Electron app development with React including security patterns, type-safe IPC, React integration, packaging with code signing, and testing. |
| `npm-package.md` | `npm-package` | Build and publish npm packages using Bun as the primary toolchain with npm-compatible output. |
| `npx-cli.md` | `npx-cli` | Build and publish npx-executable CLI tools using Bun as the primary toolchain with npm-compatible output. |
| `scraper-builder.md` | `scraper-builder` | Guide AI agents to generate complete PageObject pattern web scraper projects using Playwright and TypeScript with Docker deployment. |
| `typescript-best-practices.md` | `typescript-best-practices` | Guide AI agents through TypeScript coding best practices including type safety, error handling, code organization, and architecture patterns. |
| `agile-coordinator.md` | `agile-coordinator` | Orchestrate multiple worker agents to implement groomed tasks. |
| `agile-workflow.md` | `agile-workflow` | Orchestrate agile development workflows by invoking commands in sequence with checkpoint-based flow control. |
| `gitea-coordinator.md` | `gitea-coordinator` | Orchestrate multiple worker agents to implement groomed tasks in Gitea repositories. |
| `github-agile.md` | `github-agile` | Diagnose GitHub-driven agile workflow problems and guide feature branch development |
| `frontend-design.md` | `frontend-design` | Create distinctive, production-grade frontend interfaces with high design quality. |
| `shadcn-layouts.md` | `shadcn-layouts` | Generate correct shadcn/Tailwind layouts by applying CSS mental models. |
| `pwa-development.md` | `pwa-development` | Implement Progressive Web App features for React and Svelte projects. |
| `react-pwa.md` | `react-pwa` | Build Progressive Web Apps with React and Vite. |
| `abstract-strategy.md` | `abstract-strategy` | Design abstract strategy games with perfect information, no randomness, and strategic depth. |
| `godot-best-practices.md` | `godot-best-practices` | Guide AI agents through Godot 4.x GDScript coding best practices including scene organization, signals, resources, state machines, and performance optimization. |
| `config-scan.md` | `config-scan` | Detect security misconfigurations in config files, Docker, and IaC. |
| `dependency-scan.md` | `dependency-scan` | Detect CVEs and security issues in project dependencies. |
| `secrets-scan.md` | `secrets-scan` | Detect API keys, passwords, tokens, and other secrets in code. |
| `security-scan.md` | `security-scan` | Scan code for security vulnerabilities including OWASP Top 10, secrets, and misconfigurations. |

## Index — qodex (71)

The template skill is skipped — it is a byte-identical duplicate of the
zip's `template-skill.md`.

| Behaviour file | Original skill | What it does |
|---|---|---|
| `aesthetic-analysis.md` | `aesthetic-analysis` | Analyze and extract design patterns from visual examples. |
| `animated-message-composer.md` | `animated-message-composer` | Create animated GIFs for messaging platforms. |
| `application-quality-assurance.md` | `application-quality-assurance` | Test web applications comprehensively for quality. |
| `autonomous-agent-gaming.md` | `autonomous-agent-gaming` | Build autonomous game-playing agents using AI and reinforcement learning. |
| `branch-finalization.md` | `branch-finalization` | Finalize development branches for integration. |
| `browser-automation-framework.md` | `browser-automation-framework` | Automate browser interactions and web testing. |
| `capability-activation.md` | `capability-activation` | Activate and leverage advanced capabilities effectively. |
| `capability-architect.md` | `capability-architect` | Create new capabilities and skills systematically. |
| `capability-documentation.md` | `capability-documentation` | Document capabilities and skills comprehensively. |
| `chat-with-arxiv.md` | `chat-with-arxiv` | Build interactive chat agents for exploring and discussing academic research papers from ArXiv. |
| `collaborative-document-creation.md` | `collaborative-document-creation` | Collaborate on document creation and refinement. |
| `collaborative-ideation.md` | `collaborative-ideation` | Facilitate collaborative idea exploration and refinement. |
| `component-interface-design.md` | `component-interface-design` | Design interfaces using component libraries and design systems. |
| `content-harvest.md` | `content-harvest` | Extract and parse article content from web sources. |
| `creative-generation-agent.md` | `creative-generation-agent` | Build agents that generate creative content including music, memes, podcasts, and multimedia. |
| `data-organization-system.md` | `data-organization-system` | Organize and categorize files into logical structures. |
| `deep-research-agent.md` | `deep-research-agent` | Build agents specialized in conducting thorough research, gathering information from multiple sources, and synthesizing findings. |
| `delegated-development.md` | `delegated-development` | Drive development using delegated agent workflows. |
| `design-system-generator.md` | `design-system-generator` | Generate design systems and theme variations. |
| `diagnostic-analysis.md` | `diagnostic-analysis` | Systematically debug and diagnose issues methodically. |
| `directive-synthesis.md` | `directive-synthesis` | Synthesize structured directives and command specifications. |
| `discussion-intelligence.md` | `discussion-intelligence` | Extract insights and intelligence from meeting discussions. |
| `distributed-task-execution.md` | `distributed-task-execution` | Dispatch and coordinate parallel agent execution. |
| `document-chat-interface.md` | `document-chat-interface` | Build chat interfaces for querying documents using natural language. |
| `domain-naming-engine.md` | `domain-naming-engine` | Generate creative domain names and brand identifiers. |
| `feedback-application.md` | `feedback-application` | Apply feedback and implement review suggestions. |
| `financial-analysis-agent.md` | `financial-analysis-agent` | Create agents for financial analysis, investment research, and portfolio management. |
| `financial-document-management.md` | `financial-document-management` | Manage and organize financial documents and invoices. |
| `genealogical-documentation.md` | `genealogical-documentation` | Plan and document family history research systematically. |
| `identity-framework.md` | `identity-framework` | Define and document brand identity standards and guidelines. |
| `interactive-component-creator.md` | `interactive-component-creator` | Build interactive web components and artifacts. |
| `knowledge-distribution.md` | `knowledge-distribution` | Share and distribute skill knowledge and documentation. |
| `legal-document-analyzer.md` | `legal-document-analyzer` | Build agents for legal document analysis, contract review, and compliance checking. |
| `llm-fine-tuning-guide.md` | `llm-fine-tuning-guide` | Master fine-tuning of large language models for specific domains and tasks. |
| `market-intelligence-gather.md` | `market-intelligence-gather` | Gather and analyze competitive advertising campaigns. |
| `media-retrieval.md` | `media-retrieval` | Download and retrieve video content from sources. |
| `media-transformation.md` | `media-transformation` | Transform and format media content creatively. |
| `meeting-record-system.md` | `meeting-record-system` | Record and manage meeting notes with intelligence. |
| `mobile-app-interface.md` | `mobile-app-interface` | Design native iOS mobile app interfaces and components. |
| `mobile-platform-specialist.md` | `mobile-platform-specialist` | Provide expert guidance on iOS development and design. |
| `multi-agent-orchestration.md` | `multi-agent-orchestration` | Design and coordinate multi-agent systems where specialized agents work together to solve complex problems. |
| `pattern-generator.md` | `pattern-generator` | Generate algorithmic patterns and creative visualizations. |
| `peer-review-initiator.md` | `peer-review-initiator` | Request peer review with proper context and preparation. |
| `plan-implementation.md` | `plan-implementation` | Execute detailed implementation plans systematically. |
| `planning-documentation.md` | `planning-documentation` | Document and communicate plans clearly. |
| `portable-document-handler.md` | `portable-document-handler` | Comprehensive PDF processing and manipulation. |
| `presentation-builder.md` | `presentation-builder` | Create and edit presentation documents with full formatting. |
| `prospect-investigation.md` | `prospect-investigation` | Research and investigate business prospects and leads. |
| `protocol-implementation-framework.md` | `protocol-implementation-framework` | Build Model Context Protocol servers and implementations. |
| `publication-converter.md` | `publication-converter` | Convert markdown documents to EPUB publication format. |
| `quality-validation.md` | `quality-validation` | Validate quality before completing tasks. |
| `rag-agent-builder.md` | `rag-agent-builder` | Build Retrieval-Augmented Generation (RAG) applications that combine LLM capabilities with external knowledge sources. |
| `release-notes-composer.md` | `release-notes-composer` | Generate comprehensive release notes and changelogs. |
| `research-documentation.md` | `research-documentation` | Research topics and produce comprehensive written documentation. |
| `research-management.md` | `research-management` | Manage research documentation in workspace platforms. |
| `review-recipient.md` | `review-recipient` | Receive and process code review feedback effectively. |
| `selection-randomizer.md` | `selection-randomizer` | Randomly select winners and participants fairly. |
| `specification-executor.md` | `specification-executor` | Execute specifications from workspace platforms into implementation. |
| `spreadsheet-processor.md` | `spreadsheet-processor` | Process and manipulate spreadsheet documents. |
| `system-design.md` | `system-design` | Design and architect software systems. |
| `team-communication.md` | `team-communication` | Create effective internal team communications. |
| `user-interface-designer.md` | `user-interface-designer` | Design user-centric interfaces for web applications. |
| `validation-first-approach.md` | `validation-first-approach` | Develop software with validation requirements first. |
| `video-archival-system.md` | `video-archival-system` | Download and archive YouTube video content. |
| `visual-composition.md` | `visual-composition` | Design visual layouts and compositions for web and print. |
| `visual-quality-improver.md` | `visual-quality-improver` | Enhance and improve image quality and visual content. |
| `voice-ai-integration.md` | `voice-ai-integration` | Build voice-enabled AI applications with speech recognition, text-to-speech, and voice-based interactions. |
| `web-interface-architect.md` | `web-interface-architect` | Architect and design web application interfaces. |
| `word-document-processor.md` | `word-document-processor` | Comprehensive word document processing with full format support. |
| `workspace-documentation.md` | `workspace-documentation` | Capture and organize knowledge in workspace platforms. |
| `workspace-isolation.md` | `workspace-isolation` | Use Git worktrees for isolated work environments. |

## Index — claude-workflow-v2 (14)

| Behaviour file | Original skill | What it does |
|---|---|---|
| `analyzing-projects.md` | `analyzing-projects` | Analyzes codebases to understand structure, tech stack, patterns, and conventions. |
| `convex-backend.md` | `convex-backend` | Convex backend development guidelines. |
| `database-design.md` | `database-design` | Designs database schemas, indexing strategies, query optimization, and migration patterns for SQL and NoSQL databases. |
| `designing-apis.md` | `designing-apis` | Designs REST and GraphQL APIs including endpoints, error handling, versioning, and documentation. |
| `designing-architecture.md` | `designing-architecture` | Designs software architecture and selects appropriate patterns for projects. |
| `designing-tests.md` | `designing-tests` | Designs and implements testing strategies for any codebase. |
| `devops-infrastructure.md` | `devops-infrastructure` | Guides Docker, CI/CD pipelines, deployment strategies, infrastructure as code, and observability setup. |
| `error-handling.md` | `error-handling` | Implements error handling patterns, structured logging, retry strategies, circuit breakers, and graceful degradation. |
| `managing-git.md` | `managing-git` | Manages Git workflows including branching, commits, and pull requests. |
| `optimizing-performance.md` | `optimizing-performance` | Analyzes and optimizes application performance across frontend, backend, and database layers. |
| `parallel-execution.md` | `parallel-execution` | Patterns for parallel subagent execution using the Agent tool (formerly Task). |
| `security-patterns.md` | `security-patterns` | Implements authentication, authorization, encryption, secrets management, and security hardening patterns. |
| `vercel-react-best-practices.md` | `vercel-react-best-practices` | React and Next.js performance optimization guidelines from Vercel Engineering. |
| `web-design-guidelines.md` | `web-design-guidelines` | Review UI code for Web Interface Guidelines compliance. |

Total: 15899 files (144 gsd-core + 3 karpathy + 43 not-ai + 33 agent-skills + 80 superpowers + 109 mattpocock + 12 ponytail + 227 ui-ux-pro-max + 63 caveman + 67 understand-anything + 299 awesome-claude-skills + 230 archify + 69 impeccable + 1631 taste-skill + 197 paperclip + 20 security-audit-skill + 3 i-have-adhd + 0 hallmark + 9131 agentic-awesome-skills + 19 book-to-skill + 17 anti-slop + 5 strix + 372 stageshow + 16 vibe-coding + 226 aeon + 65 context-engineering + 1485 awesome-copilot + 236 anthropics + 573 jwynia + 507 qodex + 17 claude-workflow-v2 + 0 graphify).
