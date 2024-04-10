# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


matrix=[
        [70,85,100,90],
        [60,30,0,100],
        [40,100,100,80]
        ]

print(matrix[2][3])

matrix=[1][2]="reprobado"

print(matrix[1][2])
#%%

l=[1,3,7,9,11,15]

r=l[2:5]
# print(r)

# for item in l:
#     print(item)
    
    

for index, item in enumerate(l):
    print(index,"",item)
#%%
cal=[70,100,90]
nom=["juan","maria","pedro"]

# for n,c in zip(nom,cal):
#     print(n,"",c)
    
for index in range(0,len(l)):
    print(l[index])