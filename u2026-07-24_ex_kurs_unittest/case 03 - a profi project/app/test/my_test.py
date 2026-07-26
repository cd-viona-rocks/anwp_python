# also ... unittest kommt aus Python i.e. einfach importieren
import unittest

# - - - 

# aber bei siblings Folders geht es nicht so
# hier muss du sagen, woher deine Datei kommt, weil . . . "import sieht nur nach unten"
# dein Folder steht zur Seite

# ich mag Path. Ich finde es einfacher und übersichtlicher
# jetzt ist immer das Gleich: Path(__file__) bin ich (die Datei)

from pathlib import Path
import sys

_TEST_DIR = Path(__file__).resolve().parent         # aus __file__ (diese Datei) finde den Vater (test/)
_SRC_DIR = (_TEST_DIR.parent / "src").resolve()     # dann geht 1x nach oben (app/) und wieder nach unten (src/)
sys.path.insert(0, str(_SRC_DIR))                   # dann registrire du src/ für imports

# da du src/ registriert hast, must du von src/ aufrufen. angenommen ist, src/ ist bereits bekannt
from my_file import my_complicated_function

# - - -

# dann wiederholt sich alles. wir haben nur die Dateien getrennt.

class TestMyComplicatedFunction(unittest.TestCase):

    def test_sum_one(self):
        self.assertEqual(my_complicated_function(1),2)

    def test_sum_ten(self):
        self.assertEqual(my_complicated_function(10),11)

    def test_input_validation(self):
        with self.assertRaisesRegex(ValueError, r"integer"):
            my_complicated_function("10")

# <empfohlen> nur hier, kannst du deine Execution beschutzen
if __name__ == "__main__":
    unittest.main()

    # dann, da wir Tester sind:
    # > python my_test.py

    # gleich output: Ran 3 tests ... OK
    # Gut!