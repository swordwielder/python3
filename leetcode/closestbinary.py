n = 3
binary_count=str(bin(n)[2:]).count('1')
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

def find(num):
    for i in range(num+1,1000):
        if str(bin(i)[2:]).count('1') == binary_count:
            return i
        
print(find(500))
