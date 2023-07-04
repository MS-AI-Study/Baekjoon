data = 0.0
grade_mapping = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}
j = 0
for i in range(20):
    str = input().split(' ')
    if (str[2] != 'P'):
        j += float(str[1])
        data += float(str[1])*float(grade_mapping.get(str[2]))

print(data/j)