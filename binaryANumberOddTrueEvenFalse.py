print('true' if bin(int(input())).count('1')%2==1 else 'false')

#method 2
print(str(bin(int(input())).count('1')%2>0).lower())
