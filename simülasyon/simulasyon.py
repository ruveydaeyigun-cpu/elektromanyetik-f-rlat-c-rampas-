import math
import matplotlib.pyplot as plt

# Sabit değerler
g = 9.81
C = 0.01
V = 200
eta = 0.05

# Girişler
m = float(input("Kutle (kg): "))
aci = float(input("Aci (derece): "))

# Hesaplamalar
v0 = math.sqrt(eta * C * V**2 / m)
aci_rad = math.radians(aci)

# Yörünge noktaları
x_list = []
y_list = []
t = 0
dt = 0.001

while True:
    x = v0 * math.cos(aci_rad) * t
    y = v0 * math.sin(aci_rad) * t - 0.5 * g * t**2
    if y < 0:
        break
    x_list.append(x)
    y_list.append(y)
    t += dt

menzil = x_list[-1]

print("Cikis hizi:", round(v0, 2), "m/s")
print("Menzil:", round(menzil, 2), "m")

# Grafik
plt.plot(x_list, y_list)
plt.xlabel("Yatay mesafe (m)")
plt.ylabel("Yukseklik (m)")
plt.title("Eğik Atış Yörüngesi")
plt.grid(True)
plt.show()