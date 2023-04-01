
fact_num = int(input("Enter number: "))
fact = 1
i = 0
if fact_num < 0:
    print('Must be positive')
elif fact_num == 0:
    print('factorial of '+str(fact_num)+' is', fact)
else:
    for i in range(1, fact_num+1):
        fact = fact*i
    print('factorial of '+str(fact_num)+' is', fact)
