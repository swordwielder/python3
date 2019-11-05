n = 4

numbers=''.join([str(i) for i in range(1,5)])
print(numbers)

for i in range(1,n+1):
    print(i*'+'+numbers)
    numbers= numbers[:-1]
