
sys.stdout = io.StringIO()
for rep in sys.stdout.getvalue().split("\n")
    print(str(rep))
print("TECHIO> success true")
print("TECHIO> Bien jouer!!")
