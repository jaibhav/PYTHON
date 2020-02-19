string_main=input("Enter a string=")

char=input("Enter a character to find its first and last occurence=")

flag=0
first_index=0

last_index=0

for i in range(0,len(string_main)):
    if(string_main[i]==char):
        flag=1
        first_index=i
        break

for i in range(0,len(string_main)):
    if(string_main[i]==char):
        last_index=i
        

if(flag):
    print("First occurence is at index=",first_index)
    print("Last occurence is at index=",last_index)
else:
    print("Character not found in string.")

