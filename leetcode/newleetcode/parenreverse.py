def solution(s):
    st=[]
    for i in range(0, len(s)):
        if s[i] != ')':
            st.append(s[i])
        else:
            k = []
            while len(st)!=0 and st[-1]!='(':
                k.append(st.pop())
            st.pop()
            k = k[::-1]
            while len(k)!=0:
                st.append(k.pop())
    print("".join(st))

solution("((io)(love)(i))")

#(ievolio)
