#solution
if (len(code) % 3 != 0):
    print('ERROR')
else:
    o = ''
    for n in range(0, len(code), 3):
        c = code[n:n+3]
        o += chr(int(c))
    print(o)

    
# not working    
code = input()
r=''
if len(code)<=5:
    print('ERROR')
else:
    code =code[1:]
    a=''
    for i in code:
        a+=i
        a=int(a)
        if chr(a).isalpha():
            r+=chr(a)
            a=''
        a=str(a)
    print(r)



input
067111100105110103
output
Coding

08013
ERROR

input
048054056049049049049049055048057056049048056049048049048051050048054053049049053048057057049048053049048053
output
068111117098108101032065115099105105


input
095126063061041040047038037036035034033060062043045047042081087069082084089085073079080065083068070071072074075076090088067086066078077059058045113119101114116121117105111112097115100102103104106107108122120099118098110109044046
output
_~?=)(/&%$#"!<>+-/*QWERTYUIOPASDFGHJKLZXCVBNM;:-qwertyuiopasdfghjklzxcvbnm,.
