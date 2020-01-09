'''
function int[]/list grep(string haystack, string needle)

[2,14]
'''

def solution(haystack, needle):
    listofinteger=[]
    if len(needle)>len(haystack):
        return listofinteger
    needleLength=len(needle)
    j=0
    for i in range(len(haystack)):
        if needle==haystack[i:needleLength+i]:
            listofinteger.append(i)
    return listofinteger
#         while j<needleLength-1:
#             print(haystack[i+j])
#             print(i,"i is ")
#             print(j,"j is")
# #             if needle[j]==haystack[i + j]:
#             j+=1
    

haystack = "abc"
needle = "abc"
print(solution(haystack,needle))
