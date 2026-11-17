"""
SkillNote Adaptive Runtime — Context Controller
Maintained solely and independently by Chinmay Prakash Rout (ChinmayPrakashRout03)
GitHub: https://github.com/ChinmayPrakashRout03/skillsFORskillnote

Principle: "Load less. Execute more. Verify everything. Restrict only what is necessary."
"""

from pathlib import Path
from typing import Dict, Any, List


CORE_DIRECTIVE = """# SkillNote Adaptive Runtime
Maintained solely and independently by Chinmay Prakash Rout (ChinmayPrakashRout03)
Repository: https://github.com/ChinmayPrakashRout03/skillsFORskillnote

## 🛡️ Core Invariants (Apply to ALL modes):
1. **Proof Before Claims**: Never claim a test, lint, or security check passed without executing a real command and reporting its exit code. If no command was run, mark as 'NOT VERIFIED'.
2. **Zero Fake Scaffolding**: No `# TODO: implement later` or dummy mock functions in production code.
3. **Selective Reading**: Read only the files necessary for this task slice.
"""


def load_skill_body(abs_path: str, max_words: int = 1200) -> str:
    """Reads a skill file, truncating secondary reference material if too long."""
    p = Path(abs_path)
    if not p.exists():
        return ""
    text = p.read_text(encoding="utf-8", errors="ignore")
    words = text.split()
    if len(words) > max_words:
        return " ".join(words[:max_words]) + f"\n\n[... truncated {len(words)-max_words} words of reference material ...]"
    return text


def build_adaptive_context(routed_task: Dict[str, Any]) -> str:
    """
    Builds a minimal, high-signal instruction payload tailored to the task mode.
    """
    mode = routed_task.get("mode", "standard")
    prompt = routed_task.get("prompt", "")
    budget = routed_task.get("token_budget", "20,000")
    skills = routed_task.get("selected_skills", [])

    output = [CORE_DIRECTIVE]
    output.append(f"\n## 🎯 Task: \"{prompt}\"")
    output.append(f"**Active Mode**: `{mode.upper()}` (Token Budget: `{budget}` tokens)")
    output.append(f"**Strategy**: {routed_task.get('mode_description', '')}\n")

    if mode == "experimental":
        output.append("""### 🧪 Experimental Mode Directives:
- You are free to explore alternative algorithms, test competing hypotheses, and propose unconventional architectures.
- Best practices serve as guidance, not rigid dogmas.
- Document trade-offs, measure performance, and compare alternatives.
- Invariants: Security, user permissions, and test verification remain strictly enforced.
""")
    elif mode == "micro":
        output.append("""### ⚡ Micro Mode Directives:
- Minimal analysis: address the exact defect or line change directly.
- Do not add unnecessary architecture or extra files.
- Run targeted test and deliver immediately.
""")
    elif mode == "complex":
        output.append("""### 🏗️ Complex Mode Directives:
- Decompose into verifiable phases.
- Produce architecture spec and Mermaid sequence/dependency diagrams before modifying files.
- Require formal verification and security audit before completion.
""")

    # Inject selected skills
    if skills:
        output.append(f"\n## 📚 Selected Targeted Skills ({len(skills)} loaded on-demand):")
        for idx, s in enumerate(skills, 1):
            output.append(f"\n### [{idx}/{len(skills)}] {s['title']} ({s['category']}/{s['name']})")
            body = load_skill_body(s["abs_path"])
            output.append(body)
    else:
        output.append("\n*No heavy skill overhead required. Rely on core engineering standards and test assertions.*")

    return "\n".join(output)
