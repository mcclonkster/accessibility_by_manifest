from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from pptx_docx_workflow.paths import discover_pptx_files, is_real_pptx, plan_runs, safe_name


class PathPlanningTests(unittest.TestCase):
    def test_is_real_pptx_skips_powerpoint_lock_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            real = root / "deck.pptx"
            lock = root / "~$deck.pptx"
            real.write_bytes(b"")
            lock.write_bytes(b"")

            self.assertTrue(is_real_pptx(real))
            self.assertFalse(is_real_pptx(lock))

    def test_discover_pptx_files_respects_recursive_flag(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            nested = root / "nested"
            nested.mkdir()
            top = root / "top.pptx"
            child = nested / "child.pptx"
            top.write_bytes(b"")
            child.write_bytes(b"")

            self.assertEqual(discover_pptx_files(root, recursive=False), [top])
            self.assertEqual(discover_pptx_files(root, recursive=True), [child, top])

    def test_safe_name_removes_problematic_output_folder_characters(self) -> None:
        self.assertEqual(safe_name("9 Lifespan/Development!"), "9_Lifespan_Development")

    def test_plan_runs_uses_per_deck_output_folders_in_batch_mode(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            out = root / "out"
            decks = [root / "Deck One.pptx", root / "Deck Two.pptx"]
            for deck in decks:
                deck.write_bytes(b"")

            runs = plan_runs(decks, root, out)

            self.assertEqual(runs[0].output_dir, out / "Deck_One_workflow_output")
            self.assertEqual(runs[1].output_dir, out / "Deck_Two_workflow_output")


if __name__ == "__main__":
    unittest.main()
