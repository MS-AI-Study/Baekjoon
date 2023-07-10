members = []
for i in range(int(input())):
    age, name = input().split()
    members.append((int(age), name))
members.sort(key=lambda x: x[0])

for member in members:
    print(member[0], member[1])