# ich mag, built-in vorher, dann pip libraries, dann meine
# aber mach es wie du möchtest
 
import unittest

from my_file import my_complicated_function

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