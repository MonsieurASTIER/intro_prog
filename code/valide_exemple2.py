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
            
        print("TECHIO> success true")
        print("ceci est la sortie Standard, c'est ici que sortira le résultat de ton programme ;)")
        send_msg("Information","Ceci est la sortie des messages d information, c'est ici que je te transmettrait des information en cas de réussite/échecs")

    except AssertionError as e:
        print("TECHIO> success false")
        send_msg("Echecs","recommence")

if __name__ == "__main__":
    test_Verif()
