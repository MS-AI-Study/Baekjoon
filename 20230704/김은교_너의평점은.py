count = 0
amount_sum = 0
score_sum = 0
result = 0

for i in range(20):
    subject, amount, abc = input().split()
    amount = float(amount)
    
    if abc == 'A+':
        score = 4.5
    elif abc == 'A0':
        score = 4.0
    elif abc == 'B+':
        score = 3.5
    elif abc == 'B0':
        score = 3.0
    elif abc == 'C+':
        score = 2.5
    elif abc == 'C0':
        score = 2.0
    elif abc == 'D+':
        score = 1.5
    elif abc == 'D0':
        score = 1.0
    elif abc =='F':
        score = 0.0
    else:
        score = 0.0
        continue

    amount_sum += amount
    score_sum = score_sum + score*amount
    
result = score_sum/amount_sum
print(result)