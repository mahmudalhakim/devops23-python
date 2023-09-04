users = ["Adam", "Lisa", "Sven", "Lina"]
print(users)
print(users[0])  # Adam
print(users[1])  # Lisa
print(users[2])  # Sven
print(users[3])  # Lina

users[0] = 'Mahmud'
print(users)
# ['Mahmud', 'Lisa', 'Sven', 'Lina']

users.append('Mahmud')
print(users)
# ['Mahmud', 'Adam', 'Lisa', 'Sven', 'Lina', 'Mahmud']

del users[0]
print(users)
# ['Lisa', 'Sven', 'Lina', 'Mahmud']

users.remove("Mahmud")
print(users)
# ['Lisa', 'Sven', 'Lina']

users.sort()
print(users)
# ['Lina', 'Lisa', 'Sven']
