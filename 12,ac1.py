str=input("Enter a word: ")
char=input("Enter an alphabet: ")
i=0
count=0
while i<len(str):
    if (str[i]==char):
        count=count+1
    i=i+1
print("The total nuber of times",char,"has apperared is: ",count)