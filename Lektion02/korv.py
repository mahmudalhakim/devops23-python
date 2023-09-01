print("---------------------------")
print(".: KORVKOLLEN 1.0.1 :.")
print("---------------------------")
print("Hur många elever vill ha... ")

_2_Korv = int(input("2 vanliga korvar     > "))
_3_Korv = int(input("3 vanliga korvar     > "))
_2_Vego = int(input("2 vegetariska korvar > "))
_3_Vego = int(input("3 vegetariska korvar > "))

korvPack = round((2 * _2_Korv + 3 * _3_Korv) / 8 + 0.5)
vegoPack = round((2 * _2_Vego + 3 * _3_Vego) / 4 + 0.5)
drick = _2_Korv + _3_Korv + _2_Vego + _3_Vego

pris = float(20.95 * korvPack + 34.95 * vegoPack + 13.95 * drick)

print("---------------------------")
print("-       Inköpslista       -")
print("---------------------------")
print("| Vanlig korv:  ", korvPack, "förpackningar")
print("| Vegansk korv: ", vegoPack, "förpackningar")
print("| Dryck:        ", drick, "drick")

print("---------------------------")
print("| ", pris, "SEK")
print("---------------------------")
