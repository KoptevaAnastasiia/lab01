import numpy as np
import matplotlib.pyplot as plt



def rotation_of_the_object(points, angle):
    rad = np.radians(angle)
    rotation_matrix = np.array([
        [np.cos(rad), -np.sin(rad)],
        [np.sin(rad ), np.cos(rad)]
    ])
    return points.dot(rotation_matrix)


heart = np.array([
    [0, -1], [1, 1], [0.5, 2], [0, 1.5], [-0.5, 2], [-1, 1], [0, -1]
])

vector = np.array([
    [-1, -0.5] ,[-1, -1],[-0.5 , -1] ,[-1, -1], [1, 2]
])



plt.figure(figsize=(8,8))  # створює полотно в розмірі 6 на 6 дюймів


plt.plot(heart[:, 0], heart[:, 1], marker='o', label='Heart')
plt.plot(vector[:, 0], vector[:, 1], marker='o', label='Vector')
plt.grid(True) # будує розмірність на графіку
plt.axis('equal') # вирівнює
plt.show()












ask = int(input('chose'))


if ask:
    rotated_heart = rotation_of_the_object(heart, 50)
    rotated_vector = rotation_of_the_object(vector, 50)

    # Візуалізація обернутих об'єктів з обраним кутом
    plt.figure(figsize=(8, 8))  # створює полотно в розмірі 8 на 8 дюймів
    plt.plot(rotated_heart[:, 0], rotated_heart[:, 1], marker='o' )
    plt.plot(rotated_vector[:, 0], rotated_vector[:, 1], marker='o' )
    plt.grid(True)  # будує розмірність на графіку
    plt.axis('equal')  # вирівнює
    plt.show()


