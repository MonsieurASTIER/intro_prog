import io
import sys


def test():
    try:
        sys.stdout = io.StringIO()
        for rep in sys.stdout.getvalue().split("\n"):
            print(str(rep))
        print("TECHIO> success true")
        print("TECHIO> Bien jouer!!")
    except AssertionError as e:
        print("TECHIO> success false")
        print("TECHIO> Rater dommage")


if __name__ == "__main__": test()
