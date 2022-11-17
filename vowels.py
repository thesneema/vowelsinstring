list1=input("enter any word")
list2=["a","e","i","o","u"]
list=[]
for x in list1:
    if(x in list2 and x not in list):
        list.append(x)
print("vowels in the word are:",list)
