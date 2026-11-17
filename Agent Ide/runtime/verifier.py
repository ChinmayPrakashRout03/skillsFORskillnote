"""
SkillNote Adaptive Runtime — Evidence-Based Verification Engine
Maintained solely and independently by Chinmay Prakash Rout (ChinmayPrakashRout03)
GitHub: https://github.com/ChinmayPrakashRout03/skillsFORskillnote

Enforces: Proof Before Claims.
No test executed = Status is NOT VERIFIED (never Passed).
"""

import subprocess
import time
import json
import hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List, Optional

EVIDENCE_DIR = Path(__file__).resolve().parent.parent / ".skillnote" / "evidence"


def execute_verification_check(
    command: str,
    project_dir: str = ".",
    check_name: str = "Test Suite",
    timeout_sec: int = 120
) -> Dict[str, Any]:
    """
    Executes a real shell verification command and captures observable evidence.
    """
    cwd = Path(project_dir).resolve()
    start_time = time.time()
    iso_timestamp = datetime.now(timezone.utc).isoformat()

    try:
        proc = subprocess.run(
            command,
            shell=True,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            timeout=timeout_sec
        )
        duration_ms = round((time.time() - start_time) * 1000, 2)
        exit_code = proc.returncode
        stdout = proc.stdout.strip()
        stderr = proc.stderr.strip()
        timed_out = False
    except subprocess.TimeoutExpired as e:
        duration_ms = round((time.time() - start_time) * 1000, 2)
        exit_code = -1
        stdout = e.stdout.strip() if e.stdout else ""
        stderr = "Command timed out after " + str(timeout_sec) + " seconds."
        timed_out = True
    except Exception as e:
        duration_ms = round((time.time() - start_time) * 1000, 2)
        exit_code = -1
        stdout = ""
        stderr = f"Execution error: {str(e)}"
        timed_out = False

    status = "PASSED" if (exit_code == 0 and not timed_out) else "FAILED"

    # Trim outputs if excessively long (keep last 40 lines)
    stdout_lines = stdout.splitlines()
    if len(stdout_lines) > 40:
        stdout_trimmed = "[... truncated ...]\n" + "\n".join(stdout_lines[-40:])
    else:
        stdout_trimmed = stdout

    stderr_lines = stderr.splitlines()
    if len(stderr_lines) > 40:
        stderr_trimmed = "[... truncated ...]\n" + "\n".join(stderr_lines[-40:])
    else:
        stderr_trimmed = stderr

    evidence = {
        "check_name": check_name,
        "status": status,
        "command": command,
        "working_directory": str(cwd),
        "exit_code": exit_code,
        "duration_ms": duration_ms,
        "timestamp": iso_timestamp,
        "stdout": stdout_trimmed,
        "stderr": stderr_trimmed
    }

    # Save evidence to disk
    save_evidence_record(evidence)
    return evidence


def save_evidence_record(evidence: Dict[str, Any]) -> Path:
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    cmd_hash = hashlib.sha256(evidence["command"].encode()).hexdigest()[:8]
    filename = f"evidence_{ts}_{cmd_hash}.json"
    file_path = EVIDENCE_DIR / filename
    file_path.write_text(json.dumps(evidence, indent=2), encoding="utf-8")
    return file_path


def format_evidence_markdown(evidence: Dict[str, Any]) -> str:
    status_emoji = "✔ PASSED" if evidence["status"] == "PASSED" else "❌ FAILED"
    return f"""### Evidence-Based Verification: {evidence['check_name']}
- **Status**: `{status_emoji}` (Exit Code: `{evidence['exit_code']}`)
- **Command**: `{evidence['command']}`
- **Execution Time**: `{evidence['duration_ms']} ms`
- **Timestamp**: `{evidence['timestamp']}`

```text
{evidence['stdout'] or evidence['stderr'] or '(no output)'}
```
"""


def unverified_claim_block(claim: str, reason: str = "No test command was executed.") -> str:
    """Explicitly marks unverified assertions instead of allowing fake passes."""
    return f"""### ⚠️ Verification Status: NOT VERIFIED
- **Claim**: {claim}
- **Reason**: {reason}
- **Required Action**: Execute an actual test or lint command before marking complete.
"""
