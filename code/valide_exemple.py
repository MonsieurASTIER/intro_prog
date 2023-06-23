import io
import sys
from exemple import function_test


print("start message")
retour = function_test()
if retour == 10:
    print("TECHIO> success true")
    print("TECHIO> Bien jouer!!")
else:
    print("TECHIO> success false")
    print("TECHIO> rater")

print("all is okay")
