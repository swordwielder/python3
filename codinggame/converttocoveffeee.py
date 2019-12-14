tweet = input().split()
maxidx=0
maxlen=0
found=False
for i in range(len(tweet)):
    if len(tweet[i]) >= maxlen and tweet[i][0] == 'c':
        maxlen= len(tweet[i])
        maxidx=i
        found=True

if found:
    tweet[maxidx] = 'covfefe'
else:
    tweet[len(tweet)-1]+='covfefe'
        
print(*tweet)


