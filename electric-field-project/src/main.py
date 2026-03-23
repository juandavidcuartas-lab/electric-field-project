import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Cargar datos
data = pd.read_csv("../data/data_potencial.csv", header=None)
V = data.map(lambda x: float(str(x).replace(',', '.'))).to_numpy()

nx, ny = V.shape[1], V.shape[0]

x = np.linspace(-6, 6, nx)
y = np.linspace(-6, 6, ny)

X, Y = np.meshgrid(x, y)

# Gradiente
dx = x[1] - x[0]
dy = y[1] - y[0]

dVdy, dVdx = np.gradient(V, dy, dx)

Ex = -dVdx
Ey = -dVdy

# ===== GRÁFICA =====
plt.figure(figsize=(10, 8))

# 🔹 Equipotenciales (suaves y claras)
contour = plt.contour(
    X, Y, V,
    levels=40,
    cmap="viridis"
)

plt.clabel(contour, inline=True, fontsize=8)

# 🔹 Campo eléctrico (limpio)
step = 2
plt.streamplot(
    X, Y, Ex, Ey,
    density=1.2,
    color="black",
    linewidth=1
)
plt.colorbar(contour, label="Potential (V)")
# 🔹 Estética
plt.xlabel("x (cm)")
plt.ylabel("y (cm)")
plt.title("Electric Field and Equipotential Lines")

plt.axhline(0, linewidth=0.5)
plt.axvline(0, linewidth=0.5)

plt.grid(alpha=0.3)

# Guardar
plt.savefig("results/campo_final.png", dpi=300, bbox_inches="tight")

plt.show()