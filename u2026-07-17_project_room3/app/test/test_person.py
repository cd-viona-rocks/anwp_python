import unittest

import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parents[1]
CLASSES_DIR = APP_DIR / "classes"
sys.path.insert(0, str(CLASSES_DIR))

from person import Person

class TestPerson(unittest.TestCase):
    def test_person_cannot_be_instantiated_directly(self):
        with self.assertRaisesRegex(TypeError, "abstract|instantiate"):
            Person()


if __name__ == "__main__":
    unittest.main()

    # log tests
    # 21 1355 072026 tested test_person_cannot_be_instantiated_directly
