d = int(input())

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

s = int((d/1000)%60)
m = int((d/(1000*60))%60)
h = int((d/(1000*60*60))%24)
days = int(d/(1000*60*60*24))

rep = []
if days > 0:
    rep.append(str(days) + 'd')
if h > 0:
    rep.append(str(h) + 'h')
if m > 0:
    rep.append(str(m) + 'm')
if s > 0 or len(rep) == 0:
    rep.append(str(s) + 's')
print(' '.join(rep))
