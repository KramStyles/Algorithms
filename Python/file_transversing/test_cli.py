from datetime import datetime, timedelta
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))

from cli import run


class TestCli(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        # Delete log file if it exists
        log_file = Path(__file__).resolve().parent / "cleanup.log"
        if log_file.exists():
            log_file.unlink()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_run_accepts_a_valid_directory(self):
        # sys.argv = ["cli.py", "--directory", self.temp_dir.name, "--days", "30"]
        base_path = Path(self.temp_dir.name).absolute()

        now = datetime.now()
        old_time = (now - timedelta(days=40)).timestamp()
        new_time = (now - timedelta(days=5)).timestamp()

        # Create files, days in the past
        for num in range(7):
            created_file = base_path / f"file_{num}.txt"
            # created_file.parent.mkdir(parents=True, exist_ok=True)
            created_file.write_text("Text information")
            if num in [1, 2, 3]:
                # Make it a newer file
                os.utime(created_file, (new_time, new_time))
            else:
                os.utime(created_file, (old_time, old_time))

        files = [item for item in base_path.iterdir() if item.is_file()]
        self.assertEqual(len(files), 7)

        run(directory=base_path, days=30)
        self.assertTrue(Path(self.temp_dir.name).exists())
        files = [item.name for item in base_path.iterdir() if item.is_file()]
        self.assertEqual(len(files), 3)
        self.assertIn("file_1.txt", files)
        self.assertIn("file_2.txt", files)


if __name__ == "__main__":
    unittest.main()
