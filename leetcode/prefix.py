
def longestCommonPrefix(strs):
    l=list(zip(*strs))
    print(list(zip(*strs)))
    print(l)
    check =""
    if not strs:
        return ""
    for i in l:
        if len(set(i))==1:
            check+=i[0]
        else:
            break
    return check


def longestCommonprefixes(strs):

    strs.sort(key=lambda x:len(x))
    print(strs)
    prefix=""
    for i in range(len(strs[0])):
        if all(x[:i+1] == strs[0][:i+1] for x in strs):
            prefix=strs[0][:i+1]
        else:
            break
    return prefix


if __name__ == '__main__':
    print(longestCommonprefixes(["flow","flower","flag","fa"]))

 #
 # check =""
 #        if strs:
 #            check = strs[0]
 #        else:
 #            return ""
 #
 #        for i in strs:
 #
 #            while check not in i:
 #                check = check[:-1]
 #
 #
 #        return check
