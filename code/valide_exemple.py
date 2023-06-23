import io
import sys
from exemple import function_test

def test_Verif():
    try:
        retour = function_test()
        assert retour == 10," assert verifier"
        print("TECHIO> success true")
        print("TECHIO> message bien jouer!!")

    except AssertionError as e:
        print("TECHIO> success false")
        print("TECHIO> message recommence avec 10")

if __name__ == "__main__":
    test_Verif()
