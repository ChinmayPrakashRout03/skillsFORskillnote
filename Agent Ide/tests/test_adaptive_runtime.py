"""
Unit Tests for SkillNote Adaptive Runtime
Maintained solely and independently by Chinmay Prakash Rout (ChinmayPrakashRout03)
GitHub: https://github.com/ChinmayPrakashRout03/skillsFORskillnote
"""

import sys
import unittest
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from runtime.indexer import get_stats, DB_PATH
from runtime.router import classify_task_mode, route_request, search_skills
from runtime.verifier import execute_verification_check


class TestSkillNoteAdaptiveRuntime(unittest.TestCase):

    def test_catalog_indexed(self):
        """Verifies SQLite FTS5 catalog has indexed skills."""
        self.assertTrue(DB_PATH.exists(), "catalog.sqlite must exist on disk")
        stats = get_stats(DB_PATH)
        self.assertGreater(stats["total_files"], 3000, "Should have indexed 3000+ skill files")
        self.assertEqual(stats["categories"], 32, "Should have exactly 32 categories")

    def test_task_mode_classification(self):
        """Verifies Micro, Standard, Complex, and Experimental classifications."""
        # Micro
        r_micro = classify_task_mode("fix null check in login.py")
        self.assertEqual(r_micro["mode"], "micro")
        self.assertEqual(r_micro["max_skills"], 1)

        # Experimental
        r_exp = classify_task_mode("invent a novel cache eviction algorithm")
        self.assertEqual(r_exp["mode"], "experimental")

        # Complex
        r_cplx = classify_task_mode("build high-throughput distributed microservice payment architecture")
        self.assertEqual(r_cplx["mode"], "complex")

        # Standard
        r_std = classify_task_mode("implement user profile settings page in react")
        self.assertEqual(r_std["mode"], "standard")

    def test_smart_bm25_routing(self):
        """Verifies search_skills returns relevant skills within token budget."""
        results = search_skills("jwt authentication", limit=3)
        self.assertGreater(len(results), 0, "Should find relevant skills for jwt authentication")
        first = results[0]
        self.assertIn("jwt", first["name"].lower() + first["title"].lower() + first["description"].lower())

    def test_evidence_verification_engine(self):
        """Verifies execute_verification_check captures real exit codes and stdout."""
        # Successful check
        ev_pass = execute_verification_check("python3 -c 'print(\"PASS_OK\")'")
        self.assertEqual(ev_pass["status"], "PASSED")
        self.assertEqual(ev_pass["exit_code"], 0)
        self.assertIn("PASS_OK", ev_pass["stdout"])

        # Failing check
        ev_fail = execute_verification_check("python3 -c 'import sys; sys.exit(42)'")
        self.assertEqual(ev_fail["status"], "FAILED")
        self.assertEqual(ev_fail["exit_code"], 42)


if __name__ == "__main__":
    unittest.main()
