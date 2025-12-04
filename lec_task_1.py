import random

list1 = []
list2 = []
list3 = []

for i in range(3):
   list1.append(random.randint(0, 100))
   list2.append(random.randint(0, 100))
   list3.append(random.randint(0, 100))

print('1 list:', list1)
print('2 list:', list2)
print('3 list:', list3)
    
max = max(max(list1), max(list2), max(list3))
print('max:',max)

sum = sum(list1) + sum(list2) + sum(list3)
print('sum:',sum)






N = 5

def randomer():
   return [random.randint(0, 100) for _ in range(N)]
           
array_1, array_2, array_3 = randomer(), randomer(), randomer()
print(array_1, array_2, array_3)
