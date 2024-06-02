import numpy as np
import matplotlib.pyplot as plt




heart = np.array([
    [0, -1], [1, 1], [0.5, 2], [0, 1.5], [-0.5, 2], [-1, 1], [0, -1]
])
scaling_matrix = np.array([
    [2, 0],
    [0, 2]
])





angle = 101

rad = np.radians(angle)
rotation_matrix = np.array([
        [np.cos(rad), -np.sin(rad)],
        [np.sin(rad ), np.cos(rad)]
    ])





heart = np.dot(heart, scaling_matrix)

heart = np.dot(heart, rotation_matrix)




plt.plot(heart[:, 0], heart[:, 1], marker='o', label='Heart')
plt.grid(True)  # будує розмірність на графіку
plt.axis('equal')  # вирівнює
plt.show()

