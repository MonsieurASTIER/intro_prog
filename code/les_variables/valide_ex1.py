import sys
import io
import re


print("F1")
#sys.stdout=io.StringIO()
print("F2")


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
                #assert False , ("echec ABCD")
        print(str(rep))
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")


if __name__ == "__main__":
    print("main")
    test_Verif()
