class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 1:
            return "1"
        a = "1"
        for _ in range(n-1):
		# Initialize c , b and temp for each loop
            c = 0
            b = ""
            temp = a[0]
            for j in a:
                if j == temp:
                    c += 1
                else:
					# If number changed, Check the current string and count how many times
                    b = b + str(c) + str(temp)
                    temp = j
                    c = 1
            b = b + str(c) + str(j)
            a = b
        return (str(a))
