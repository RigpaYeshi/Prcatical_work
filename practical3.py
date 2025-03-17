arrayname=["Yeshi", 170 , 1.7 , True, None]
firstarrayname = len(arrayname)
arrayname.append("Passang")
secondarrayname = len(arrayname)
print(firstarrayname-secondarrayname)
print(arrayname)

nameofanimal=["dogs", "cats","monkeys","gorilla"]
nameofanimal.append("chimpanzee")
arraylength = len(nameofanimal)
for index in range(arraylength):
    print(nameofanimal[index])

name_of_animals=["dogs", "cats","monkeys","gorilla"]
length_of_array=len(name_of_animals)

index=0
while index<length_of_array:
    print(name_of_animals[index])
    index=index+1

generated_number=[0,1,2,3,4,5,6,7,8,9]
new_stack=[]
index=9
while index> -1:
    new_stack.append(generated_number[index])
    index=index-1
new_stack.pop(0)
print(new_stack)



