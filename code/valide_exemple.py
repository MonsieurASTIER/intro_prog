import io
import sys

print("start message")
sys.stdout = io.StringIO()
rep = sys.stdout.getvalue().split("\n")
print(str(rep))
for el in rep:
    print(str(el))
    print("TECHIO> success false")
    print("TECHIO> Bien jouer!!")

print("all is okay")
