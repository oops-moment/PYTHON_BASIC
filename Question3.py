data=[]
N=10
for i in range(N):
   name=input("Enter the name\n")
   data.append(name)
choice=input("Enter your choice out of ascending/descending\n")
if(choice == 'ascending'):
    data.sort()
if(choice == 'descending'):
    data.sort(reverse=True)
print(data)
lateral_entry=input("Enter the lateral name you wanna insert\n")
data.append(lateral_entry)
if(choice == 'ascending'):
    data.sort()
if(choice=='descending'):
    data.sort(reverse=True)
print(data)
