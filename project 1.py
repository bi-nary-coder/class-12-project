# Project question 1- Read a text file line by line and display each words separated by a # .

# Solution:-

f=open('data.txt','r')
data=f.readlines()
for i in data:
    a=i.split()
    for j in a:
        print(j,end="#")