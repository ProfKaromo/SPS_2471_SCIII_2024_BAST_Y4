#Data Stractures and their operations.
#List
mylist1 = ['Jane','John','Kim']
print(type(mylist1))
print(mylist1)
#Access Items
print(mylist1[0])

#Negative index
print(mylist1[-1])

mylist2 = ['Kirinyaga','Embu','Nyeri','Kiambu','Nakuru','Meru','Kilifi','Mombasa']
print(mylist2[2:4])

print(mylist1)

#Tuples
name = input("What is your name:").strip()
if len(name)>0:
    print('Hello',{name})
else:
    print('Hello there')