newspaper = range(1, 76)
magazine = range(77, 104)
both = range(21, 34)
a1 = set()
a2 = set()
a3 = set()
for i in range(1, 76):
    a1.add(i)
for i in range(77, 104):
    a2.add(i)
for i in range(21, 34):
    a3.add(i)
print(len((a1|a2)-a3))