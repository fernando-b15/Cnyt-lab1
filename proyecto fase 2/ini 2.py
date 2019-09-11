m=[[0,0,0,0,0,0],[0,0,0,1,0,0],[0,1,0,0,0,1],[0,0,1,0,0,0],[0,0,0,0,1,0],[1,0,0,0,0,0]]
v=[6,5,4,3,2,1]

for k in range(3000):
    res=[]
    for j in m:
        cont=0
        for i in range(len(v)):
           
            cont+=j[i]*v[i]
        res.append(cont)

    v=res
print(res)    
