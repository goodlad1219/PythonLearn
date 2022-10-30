# ls=[]
# for i in range(100):
#     ls.append(i)

# print(ls)

# In copmprehension we write it as:
x = int(input())
y = int(input())
z = int(input())
n = int(input())

ls =[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k != n)]
print(ls)