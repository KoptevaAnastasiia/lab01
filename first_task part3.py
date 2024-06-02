import numpy as np
import matplotlib.pyplot as plt

# Ініціалізація тривимірного графіка
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Визначення вершин куба
points = np.array([[0, 0, 0],
                   [1, 0, 0],
                   [1, 1, 0],
                   [0, 1, 0],
                   [0, 0, 1],
                   [1, 0, 1],
                   [1, 1, 1],
                   [0, 1, 1]])

ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='b', marker='o')





def scaling ():
    ask = int(input("ask the num "));

    points[:, 1] *= ask

    i = 0;
    while i != len(points):
        points[i, 0] *= ask
        i += 1
    ax.scatter( points[:, 0], points[:, 1], points[:, 2], c='r', marker='o')


def rotation_of_the_object_3d( angle, ask):
    rad = np.radians(angle)
    R1 = np.array([   # по x
            [1, 0, 0],
            [0, np.cos(rad), -np.sin(rad)],
            [0, np.sin(rad), np.cos(rad)]
        ])
    R2 = np.array([   # по y
            [np.cos(rad), 0, np.sin(rad)],
            [0, 1, 0],
            [-np.sin(rad), 0, np.cos(rad)]
        ])
    R3  = np.array([  # по z
            [np.cos(rad), -np.sin(rad), 0],
            [np.sin(rad), np.cos(rad), 0],
            [0, 0, 1]
        ])
    if ask == "x":
        rotated_points =  np.dot(points, R1)


    if ask == "y":
        rotated_points = np.dot(points, R2)

    if ask == "z":
        rotated_points = np.dot(points, R3)



    ax.scatter( rotated_points[:, 0], rotated_points[:, 1], rotated_points[:, 2], c='r', marker='o')








# ax.scatter(translated_points[:, 0], translated_points[:, 1], translated_points[:, 2], c='r', marker='o')




scaling()

ask = input(" x y z")


rotation_of_the_object_3d(90, ask)






ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')



ax.set_xlim([-1, 2])
ax.set_ylim([-1, 2])
ax.set_zlim([-1, 2])

plt.show()