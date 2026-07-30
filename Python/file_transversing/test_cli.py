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
        run(directory=self.temp_dir.name, days=30)
        self.assertTrue(Path(self.temp_dir.name).exists())


if __name__ == "__main__":
    unittest.main()
