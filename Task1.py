import math

def gravitation(m1, m2, r):
    G = 6.6743*math.pow(10,-11) 
    return G * m1 * m2 / math.pow(r, 2)

m1 = 5.97600*math.pow(10,24)

planet = input("Введите название планеты: ")
planet = planet.lower()
if planet == "луна":
    m2 = 7.342*math.pow(10,22)
    r = 3.844*math.pow(10,8)
elif planet == "марс":
    m2 = 6.39*math.pow(10,23)
    r = 2.28*math.pow(10,11)
elif planet == "венера":
    m2 = 4.8685*math.pow(10,24)
    r = 1.082*math.pow(10,11)

try:
    F = gravitation(m1, m2, r)
    print("Сила притяжения между Землей и", planet + ":", F, "Н")
except:
    print("Планета не найдена")
finally:    exit(0)
