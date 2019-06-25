if __name__ == '__main__':
    mapdict =({})
    nestedlist = []
    i=0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        #nestedlist.append([])
        #nestedlist.append[i].append(score)
        #i+=1
        mapdict.update({name:score})

    newlist = list(mapdict)
    print (mapdict)
    print ("new space ________")
    print (newlist)
    print ("new space ________")
    print (nestedlist)


if __name__ == '__main__':
    mapdict =({})
    nestedlist = []
    scorelist = []
    marksheet = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        #nestedlist.append(name)
        #scorelist.append(score)
        marksheet+=[[name,score]]
        scorelist+=[score]
        #nestedlist.append([])
        #nestedlist.append[i].append(score)
        #i+=1
        #mapdict.update({name:score})
    b = sorted(list(set(scorelist)))[1]

    for a,c in sorted(marksheet):
        if c==b:
            print(a)
    #scorelist.append(nestedlist)
    #newlist = list(mapdict)
    #print (mapdict)
    #print ("new space _____newlist___")
    #print (newlist)
    #print ("new space ___nestedlist_____")
    #print (nestedlist)
    #print ("new space ___scorelist_____")
    #print (scorelist)
    #print ("new space ____marksheet___")
    #print (marksheet)
    #print ("what is b? ")
    #print (b)
    #print ("new space ___scorelist[5]____")
    #print (scorelist[5])
    #print ("new space ___scorelist[5][0]____")
    #print (scorelist1)
    

