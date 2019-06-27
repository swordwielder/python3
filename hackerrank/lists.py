
if __name__ == '__main__':
    N = int(input())
    #print ("N is currently",N)
    #allcommands = ["insert","print", "remove","append","sort","pop","reverse"]
    inputcommand = {}
    newlist =[]
    for line in range(N):
        command, *line = input().split()
        values=list(map(int,line))
        inputcommand[command]=values
        if command =="insert":
            newlist.insert(inputcommand[command][0],inputcommand[command][1])
        if command =="remove":
            newlist.remove(inputcommand[command][0])
        if command =="append":
            newlist.append(inputcommand[command][0])
        if command=="sort":
            newlist.sort()
        if command=="print":
            print(newlist)
        if command=="pop":
            newlist.pop()
        if command=="reverse":
            newlist.reverse()





