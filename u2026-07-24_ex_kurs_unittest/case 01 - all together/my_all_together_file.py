# Hallo Kollegen,
# diese Art von Architectur ist nicht empfohlen, weil unorgenisiert ist

# hier habt ihr eine Funktion, also zwei, aber ich muss nur testen, was ich testen muss
# dann zwei Funktionen, aber nur eine wird getestet. das musst ihr entscheiden.

def my_complicated_function(a: int) -> int:
    """ increments a by one """

    if not isinstance(a, int):
        raise ValueError("a must be an integer")

    return a+1


# Gut. Ich habe meine Funktion, sie macht was und da wir cooler und Profis sind
# wir checken unserer Inputs

# dann testen wir ein paar Fälle, aber bevor, lass uns das Ding "if __name__" erklären

# nehmen wir an, ihr importiert diese Datei, aus irgendwelchen Grund.
# bei dem "import" wird die ganze Datei durchgeführt, aber das wollen wir nicht ! ! !
# weil wir hier nicht so Profis wurden und haben wir alle zusammen geschrieben.

# dann trennen wir die Funktion aus dem Test mittels ein "if __name__"

# pass auf! wie schreibt man ein import -> from <module, normalerweise filename> import <function>
# genau hier kriegt die Module eine Name, welcher genau die Dateiname ist

# Außer  . . .  er selbst wird durchgeführt, dann kriegt er bei dem sogennanten Runtime, den Name "__main__"

if __name__ == "__main__":
    # dieses Block wird nur durchgeführt, wenn diese Datei direkt durchgeführt wird
    # so trennen wir Test aus der Funktion, die wir eventuell irgendwo nutzen wollen.

    import unittest
    # das sollst du da oben importieren. ich mache dummerweise hier, damit zusammen steht, aber es ist falsch, mindestens ungeeignet

    class TestMyComplicatedFunction(unittest.TestCase):
        # ich brauche eine Klasse. Die nenne ich wie ich will. Aber sie muss die Klasse TestCase vererben ! ! !
        # Siehe mal: unittest ist viel mehr wie eine Klasse. Unser import unittest hat Klassen und TestCse ist einer davon.

        # siehe darunter, ich rufe unittest.main() und die Method main() von unittest macht die Magie.

        # ich überlege mir ein paar schlaue tests: 
        # wenn a is str, fehler; 
        # wenn a = 1, returns 2; 
        # wenn a 10, returns 11; 
        # 
        # und das ich ist die ganze Schlauigkeit die ich gerade habe.

        # - - mein Tests - - 
        # pro Test brauche ich eine Test Funktion, die für main dürchgeführt wird.
        # es gibt zwei Methoden aus TestCase, die ich hier testen möchte:

        def test_sum_one(self):
            self.assertEqual(my_complicated_function(1),2)

        def test_sum_ten(self):
            self.assertEqual(my_complicated_function(10),11)

        # also . . ein "Equal" ist leicht zu testen
        # definiere deine Funktion, gib ihr ein "self", call the self mit "assertEqual"
        # und gib deine Funktion mit args und das erwartet Ergebnis -> Einfach so ! ! !

        # Testing Errors

        # um Fehler zu testen ist ein bisschen kompliziert. da von oben weiß du schon, was für ein Fehler kommt
        # dann nenne deine Testfunktion sinnvoll und erzeuge ein neues Kontext mit "with". da drin rufst du deine Funktion

        def test_input_validation(self):
            with self.assertRaisesRegex(ValueError, r"integer"):
                my_complicated_function("10")
                # Siehe Mal. Kein Output deklariert hier, weil kein returns erreicht wird. 

        # That's all Folks !

    unittest.main()
    # wenn du das hier laufen lässt, siehst du das folgende Output
    # drei Tests durchgführt und keinen Fehler. Gut! Meine Funktion kann fürs Produktion weitergegeben werden.

    # ...
    # ----------------------------------------------------------------------
    # Ran 3 tests in 0.001s

    # OK
