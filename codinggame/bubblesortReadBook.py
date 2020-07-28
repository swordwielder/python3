
#solution
B=[input().split(",") for _ in range(int(input()))]
T=0
while B!=sorted(B):
 for i in range(len(B)-1):
  a,b=B[i:i+2]
  if a>b:B[i],B[i+1]=b,a;T+=int(a[1])+int(b[1])
print(T)


#solution 2
n = int(input())
a=[]
books={}
for i in range(n):
    line = input().split(',')
    a.append(line[0])
    books[line[0]] = line[1]

for i in a:
    print(i)
print(books)





The Globglogabgalab loves books. He also prefers that all his books be sorted alphabetically by title. Unfortunately, some vandals broke into his basement last night and jumbled all his books! Now he needs to sort them again.

The Globglogabgalab sorts his books using the bubble sort method: He goes through the books on the bookshelf, from left to right, and compares each book with the book to the right. If the two books are in the wrong order, he swaps them. He repeats this process until all the books are in order.

But the Globglogabgalab loves books so much, that each time he swaps 2 books, he gets sidetracked and reads both of the books before swapping them.
You need to figure out how long it will take the Globglogabgalab to sort a given bookshelf.
Input
Line 1: An integer N for the number of books on the bookshelf.
Next N lines: Each represent a book on the bookshelf, in order from left to right, in the format book title (string),minutes taken to read the book (integer).
Output
The time (in minutes) that it will take for the Globglogabgalab to sort the bookshelf.
Constraints
book titles will only contain lowercase letters and spaces.
All book titles are unique.
50 > N > 1
100,000 > minutes taken to read the book > 0
Example
Input
3
the hitchhikers guide to the galaxy,42
fifty shades of grey,124
the c programming language,598
Output
806
Console output
100%
aprasath
