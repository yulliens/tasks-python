price1 = int(input('25'))
price2 = int(input('100'))
price3 = int(input('310'))
if price1 <= price2 and price2 <= price3:
   print('Акция!')
print('К оплате:', (price1 + price2 + price3)/2)