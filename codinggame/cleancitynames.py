import sys
import math


n = int(input())
city_names = []
for i in range(n):
    city_names.append(input())
m = int(input())
uncleaned_city_names=[]
for i in range(m):
    uncleaned_city_names.append(input())
    
def fmt(city):
    
    result = city[0].lower() + ''.join(sorted(city.lower())).replace(' ', '')
    print(city,result, file=sys.stderr)
    return result
    

for city in uncleaned_city_names:

    
    cleaned = [c for c in city_names if fmt(city)==fmt(c)][0]
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    print(cleaned)




