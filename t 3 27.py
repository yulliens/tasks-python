newspaper = range(1, 76)
magazine = range(77, 104)
both = range(21, 34)
m1 = set()
m2 = set()
m3 = set()
for i in range(1, 76):
    m1.add(i)
for i in range(77, 104):
    m2.add(i)
for i in range(21, 34):
    m3.add(i)
print(len((m1|m2)-m3))