x=[7,4,6,8,4,3,7,1,1,2,2,3]
ptr=0
for i in range(len(x)):
    if x[i]<=3:  # any condition
        x[ptr],x[i]=x[i],x[ptr]
        ptr+=1
print(x)