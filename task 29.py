a=451
b=0
while a>0:
    digit = a % 10
    a = a // 10
    b = b * 10
    b = b + digit
print(b)