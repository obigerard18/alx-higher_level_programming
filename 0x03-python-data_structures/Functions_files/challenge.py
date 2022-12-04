#!/usr/bin/python3
names = ['Andrea','Dario','Fredy','Laura','Ana','Dani']

for i, e in enumerate(names):
    print (i, e)
names = ['Andrea','Dario','Fredy','Laura','Ana','Dani']
names.sort(key=lambda item: len(item))
print(names)
