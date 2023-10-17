import re

source = r"Szczęść boże dzień dobry, siemanko witam w mojej kuchni"
pattern = r"(dobry)"
wynik = re.sub(pattern, "chujowy jak jasny chuj", source)
print(wynik)