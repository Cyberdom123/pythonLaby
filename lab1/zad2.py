import re

source = r"Szczęść boże dzień dobry, siemanko witam w mojej kuchni"
pattern = r"(boże)"
wynik = re.sub(pattern, "Boże", source)
print(wynik)