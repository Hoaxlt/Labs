a = int(input()) #вводим коэффициенты
b = int(input())
c = int(input())
D = 0
korni = []

D = b ** 2 - 4 * a * c #Ищем дискриминант
if D >= 0:
    if D > 0:
        korni.append((-b + D**0.5) / (2*a)) #ищем корни
        korni.append((-b - D**0.5) / (2*a))
    else:
        korni.append(-b/(2*a))
if D < 0:
    print("Корней нет")
print(korni)
