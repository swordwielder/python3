iterator=0
final=""
for i in input:
    if i.isalpha():
        final+= i.lower() if iterator%2 else i.upper()
        iterator+=1
    else:
        final+=i

print(final)
