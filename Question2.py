students_data=dict()
n=int(input("NUMBER OF STUDENTS:\n"))
sum_final=[]
# basically marks[0] stores the marks and marks[1] stores maths marks and marks[2] cse and marks [3] scinece
for i in range(n):
  sum=0;
  student_name=input("NAME:\n")
  marks=[]
  student_roll= int(input("ROLL NUMBER:\n"))
  marks.append(student_roll)
  student_marks_Maths=int(input("MATHS MARKS:\n"))
  marks.append(student_marks_Maths)
  sum=sum+student_marks_Maths
  student_marks_CSE=int(input("CSE MARKS\n"))
  marks.append(student_marks_CSE)
  sum=sum+student_marks_CSE
  student_marks_Science=int(input("SCIENCE MARKS\n"))
  marks.append(student_marks_Science)
  sum=sum+student_marks_Science
  sum_final.append(sum)
  marks.append(sum)
  students_data[student_name]=marks

#print(students_data[name])
#  print name and roll number
for key,value in students_data.items():
	print(key, ':', value[0])
print("NAME OF STUDENT\n")
name=input("Enter name\n")
print("NAME:\n")
print(name)
print("ROLL NUMBER:\n")
print(students_data[name][0])
print("MATHS MARKS:\n")
print(students_data[name][1])
print("CSE MARKS:\n")
print(students_data[name][2])
print("SCIENCE MARKS:\n")
print(students_data[name][3])
print("MEAN MARKS: \n")
answer=students_data[name][1]+students_data[name][2]+students_data[name][3]
answer=answer/3

print(answer)
print("MEDIAN: \n")
# print(students_data[name][2])
median=0
num1=students_data[name][1]
num2=students_data[name][2]
num3=students_data[name][3]
if(num2>num1 and num1>num3 or num3>num1 and num1>num2):
    median=num1

if(num1>num2 and num2>num3 or num3>num2 and num2>num1):
    median=num2
 
if(num1>num3 and num3>num2 or num2>num3 and num3>num1):
    median=num3
print(median)
sum_final.sort(reverse=True)
ans_index=sum_final.index(students_data[name][4])
ans_index=ans_index+1
print("RANK: \n")
print(ans_index)