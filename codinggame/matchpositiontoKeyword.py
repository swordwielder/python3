keyword = input()
message = input()
w=''
dic={k:v for k,v in zip(sorted(keyword),message)}
for i in keyword:
    w+=dic[i]

print(w)

