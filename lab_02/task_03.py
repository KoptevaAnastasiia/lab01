import numpy as np


def encrypt_message(message, key_matrix):
    message_vector = np.array([ord(char) for char in message])
    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)
    diagonalized_key_matrix = np.dot(np.dot(eigenvectors, np.diag(eigenvalues)), np.linalg.inv(eigenvectors))
    encrypted_vector = np.dot(diagonalized_key_matrix, message_vector[:len(key_matrix)])
    return encrypted_vector


massage = input("Enter message: ")
key_matrix = np.random.randint(0, 256, (len(massage), (len(massage))))


encrypted_vector = encrypt_message(massage, key_matrix)
print("Encrypted vector:", encrypted_vector)

