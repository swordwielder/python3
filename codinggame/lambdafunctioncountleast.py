l = [int(i) for i in input().split()]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(min(l, key=lambda x: (l.count(x), l[::-1].index(x))))


