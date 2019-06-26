import statistics

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    averages = []
    i=0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        #print ("score is " ) 
        #print (scores)
        averages.append(format(statistics.mean(scores),'.2f'))
    query_name = input()
    
    for each in student_marks:
        if each == query_name:
            break
        i+=1

    print (averages[i])
    #print ("the average is --------")
    #print (averages)
    #print (student_marks)
    #print (query_name)


