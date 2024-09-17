import math
try:
    r=float(input("Nhap ban kinh: "))
    cv=r*math.pi*2
    dt=r**2
    print("Chu vu = ",cv)
    print("dien tich = ",dt)
except:
    print("Loi roi")