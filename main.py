import numpy as np
import matplotlib.pyplot as plt



def reflection_x():
    vector[:, 1] *= -1
    heart[:, 1] *= -1






def reflection_y():
    i = 0 ;
    while i != len(vector):
        vector[i, 0] *= -1

        i += 1
    i = 0
    while i != len(heart):
        heart[i, 0] *= -1

        i += 1

    # vector[0, :] *= -1
    # heart[0, :] *= -1
    #


def scaling ():
    ask = int(input("ask the num "));

    vector[:, 1] *= ask
    heart[:, 1] *= ask

    i = 0;
    while i != len(vector):
        vector[i, 0] *= ask

        i += 1
    i = 0
    while i != len(heart):
        heart[i, 0] *= ask

        i += 1


def scaling_new (point):
    ask = int(input("ask the num "));
    f = np.array([
        [ask, 0],
        [0, ask]
    ])
    new_matrix = np.dot(point , f)



def rotation_of_the_object(points, angle):
    rad = np.radians(angle)
    rotation_matrix = np.array([
        [np.cos(rad), -np.sin(rad)],
        [np.sin(rad ), np.cos(rad)]
    ])
    return points.dot(rotation_matrix)


def rotation_of_the_object_y (points, angle):
    rad = np.radians(angle)
    rotation_matrix = np.array([
        [np.cos(rad), 0],
        [0, 1]
    ])
    return np.dot(points, rotation_matrix)


def rotation_of_the_object_x (points, angle):
    rad = np.radians(angle)
    rotation_matrix = np.array([
        [1, 0],
        [0, np.cos(rad)]
    ])
    return np.dot(points, rotation_matrix)










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


if ask == 1:
    heart = rotation_of_the_object(heart, 50)
    vector = rotation_of_the_object(vector, 50)


    plt.figure(figsize=(8, 8))  # створює полотно в розмірі 8 на 8 дюймів
    plt.plot(heart[:, 0],  heart[:, 1], marker='o' )
    plt.plot(vector[:, 0],  vector[:, 1], marker='o' )
    plt.grid(True)  # будує розмірність на графіку
    plt.axis('equal')  # вирівнює
    plt.show()

if ask == 3:
    ask = input('x or y')
    if ask == "x" or ask == "X":
        reflection_x()
    if ask == "y" or ask == "Y":
        reflection_y()

    plt.plot(heart[:, 0], heart[:, 1], marker='o', label='Heart')
    plt.plot(vector[:, 0], vector[:, 1], marker='o', label='Vector')
    plt.grid(True)  # будує розмірність на графіку
    plt.axis('equal')  # вирівнює
    plt.show()




if ask == 2:
    scaling()
    plt.plot(heart[:, 0], heart[:, 1], marker='o', label='Heart')
    plt.plot(vector[:, 0], vector[:, 1], marker='o', label='Vector')
    plt.grid(True)  # будує розмірність на графіку
    plt.axis('equal')  # вирівнює
    plt.show()


    result_h = scaling_new(heart)
    result_v = scaling_new(vector)
    plt.plot(heart[:, 0], heart[:, 1], marker='o', label='Heart')
    plt.plot(vector[:, 0], vector[:, 1], marker='o', label='Vector')
    plt.grid(True)  # будує розмірність на графіку
    plt.axis('equal')  # вирівнює
    plt.show()




if ask == 4:
    chose = input('x or y')
    if chose == "y" or chose == "Y":

        rotated_heart = rotation_of_the_object_y(heart, 75)
        rotated_vector = rotation_of_the_object_y(vector, 75)
        plt.plot(rotated_heart[:, 0], rotated_heart[:, 1], marker='o', label='Rotated Heart')
        plt.plot(rotated_vector[:, 0], rotated_vector[:, 1], marker='o', label='Rotated Vector')
        plt.grid(True)  # будує розмірність на графіку
        plt.axis('equal')  # вирівнює
        plt.legend()
        plt.show()
    elif chose == "x" or chose == "X" :
        rotated_heart = rotation_of_the_object_x(heart, 75)
        rotated_vector = rotation_of_the_object_x(vector, 75)
        plt.plot(rotated_heart[:, 0], rotated_heart[:, 1], marker='o', label='Rotated Heart')
        plt.plot(rotated_vector[:, 0], rotated_vector[:, 1], marker='o', label='Rotated Vector')
        plt.grid(True)  # будує розмірність на графіку
        plt.axis('equal')  # вирівнює
        plt.legend()
        plt.show()


