import numpy as np

Ai = [[1,2,3,4,5,6],[2,6,9,12,15,18],[3,10,18,24,30,36],[4,14,27,40,50,60],[5,18,36,56,75,90],[6,22,45,72,100,126]]

bi=[-12,20,3]

def decompLU(A):
  n=len(A)
  L=np.zeros((n,n))
  U=np.zeros((n,n))
  s=0
  s1=0

  for i in range(n):
    for j in range(i,n):
      s=0
      for k in range(i):
        s=s+L[i][k]*U[k][j]
      U[i][j]=A[i][j]-s
    L[i][i]=1
    for j in range(i+1,n):
      s1=0
      for k in range(i):
        s1=s1+L[j][k]* U[k][i]
      L[j][i]=(A[j][i]-s1)/U[i][i]
  return L, U

L, U= decompLU(Ai)

print("L: \n%s" % L)
print("U: \n%s" % U)