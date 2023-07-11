import io
import sys
import re


def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def test_Verif():
    print("test_verif")
    try:
        print("iA")
        sys.stdout=io.StringIO()
        print("B")
        rep = sys.stdout.getvalue().split("\n")
        print("inside the try")
        for i,reponse in enumerate(rep):
            print(str(i) + " : " + str(reponse))
            if reponse != 22:
                print("TECHIO> success false")
                send_msg("Echecs","Ce n'est pas la sortie attendu")
                assert False , ("echec")
        print(str(rep))
    except Exception as e:
        print("exception")
        print(e)

if __name__ == "__main__":
    print("main")
    test_Verif()
