'''Project question 2- Read a text file and display the number of vowels
                              /consonants/uppercase/lowercase character in the file.
'''
# solution:-
f=open('data.txt','r')
data=f.read()
vowels = 0
consonant = 0
lower=0
upper=0
for i in range(0, len(data)):  
    ch = data[i]
    if (ch.islower()==True):
        lower+=1
    if(ch.isupper()==True):
        upper+=1
    if ( (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z') ):
        ch = ch.lower() 
        if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'): 
            vowels += 1
        else: 
            consonant += 1
    
print("Vowels :", vowels) 
print("Consonant :", consonant)  
print("lowercase :", lower)  
print("uppercase :", upper) 
