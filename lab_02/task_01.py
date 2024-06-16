import numpy as np
import matplotlib.pyplot as plt





def eigenvalues_eigenvectors (matrix) :
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    print("Власні значення матриці:" , eigenvalues)

    print("Власні вектори матриці:")
    print(eigenvectors)



matrix = np.array([
        [4, 1],
        [2, 3]
    ])

eigenvalues_eigenvectors(matrix)