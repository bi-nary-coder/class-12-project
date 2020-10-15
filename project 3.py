'''
Project question -Create a binary file with name and roll number. Search for a given roll
                  number and display the name, if not found display appropriate
                  message. 
'''
# Solution:-
f=open('student marks.dat', 'wb')
n=int(input("enter the total number of names"))
for i in range(n):
    roll=str(input("Enter the roll number")+"\n")
    name=str(input("Enter the name")+"\n")
    f.write(roll.encode("utf-8"))
    f.write(name.encode("utf-8"))
f.close()
f=open('student marks.dat', 'rb')
data=f.readlines()
print (data)
roll=str(input("enter the roll number you want to find")+'\n')
roll=roll.encode('utf-8')
if roll in data:
    print ((data[data.index(roll)+1]).decode('utf-8'))
else:
    print(f({roll},'not found'))
f.close()
