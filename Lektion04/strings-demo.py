# Konkatenering (sammanfogning) av två strängar
str1 = "Hej"
str2 = "världen"
str3 = str1 + " " + str2 + "!"
print(str3)
print("Längden på strängen är: ", len(str3))

print("Lite text och annat smått och gott.\nLite mer text och annat.")
print("""
    Rad 1:\tEtt
    Rad 2:\tTvå
    Rad 3:\tTre
""")

print("Exempel på escape-tecken är: \\n som betyder ny rad")

# Indexering
str1 = "ABC"
print("Första tecknet : ", str1[0])

# Iteration av karaktärer
letters = 'ABC'
i = 0
while i < len(letters):
    print(letters[i])
    i += 1

for letter in letters:
    print(letter)