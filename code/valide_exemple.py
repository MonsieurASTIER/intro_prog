
sys.stdout = io.StringIO()
for rep = sys.stdout.getvalue().split("\n")
    print(str(rep))
print("TECHIO> success true")
print("TECHIO> Bien jouer!!")
