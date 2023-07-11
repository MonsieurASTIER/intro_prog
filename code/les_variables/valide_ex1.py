import io
import sys
import re


def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def test_Verif():
    try:
        sys.stdout=io.StringIO()
        rep = sys.stdout.getvalue().split("\n")
        for i,reponse in enumerate(rep):
            print(str(i) + " : " + str(reponse))
            if reponse != 22
                print("TECHIO> success false")
                send_msg("Echecs","Ce n'est pas la sortie attendu")
        print("TECHIO> success true")


    except AssertionError as e:
        print("TECHIO> success false")
        send_msg("Echecs","recommence")

if __name__ == "__main__":
    test_Verif()
