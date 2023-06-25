pair= []
marks = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    a= [name,score]
    pair.append(a)
    marks.append(score)
    
pair.sort()
marks  = list(set(marks))
marks.sort()

for i in range(0,len(pair)):
    if (marks[1] == pair[i][1]):
        print (pair[i][0])

    
   
