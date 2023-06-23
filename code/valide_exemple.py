import io
import sys
from exemple import function_test

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def test_Verif():
    try:
        retour = function_test()
        assert retour == 10," assert verifier"
        print("TECHIO> success true")
        send_msg("victoire","bien jouer ")

    except AssertionError as e:
        print("TECHIO> success false")
        send_msg("Echecs","recommence")

if __name__ == "__main__":
    test_Verif()
