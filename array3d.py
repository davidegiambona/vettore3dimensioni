import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Definiamo un vettore in 3 dimensioni
vector = np.array([1, 2, 3])

# Creazione della figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Punto iniziale (origine) e punto finale del vettore
origin = np.array([0, 0, 0])
ax.quiver(origin[0], origin[1], origin[2], vector[0], vector[1], vector[2])

# Impostiamo limiti per una migliore visualizzazione
ax.set_xlim([0, vector[0]+1])
ax.set_ylim([0, vector[1]+1])
ax.set_zlim([0, vector[2]+1])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Rappresentazione di un vettore 3D nello spazio')

plt.show()
