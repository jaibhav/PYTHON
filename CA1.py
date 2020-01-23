main_list=[];

len=int(input("Enter the number of elements in list="));

for i in range(len):
 in_val=int(input("Enter the element->"));
 main_list.append(in_val);

even_list=[];
odd_list=[];

for i in main_list:
 if(i%2==0):
  even_list.append(i);
 else:
  odd_list.append(i);

print("All elements are->",main_list);
print("Even elements are->",even_list);
print("Odd elements are->",odd_list);
  
  


