N=int(input("Enter the number\n"))
if(N%2!=0):
    
    print("Error")
    
else:
  N=N//2;
  for i in range(N):
     for j in range(i+1):
       print(' ',end='')
     for j in range (i,N):
       print('*',end='')
     for j in range (i,N):
       print('*',end='')
     print()
  for i in range(N):
    for j in range(i,N):
      print(' ',end='')
    for j in range (i+1):
      print('*',end='')
    for j in range (i+1):
      print('*',end='')
    print()
        