if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    a=()
    b=()
    new = ()
    for i in range(n):
        if i== 0:
            b=(integer_list[i],)
        else:
            new = b +(integer_list[i], )
            b = new   
        

    print(hash(new))
    
    
