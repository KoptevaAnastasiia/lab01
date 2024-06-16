import numpy as np


def encrypt_message(message, key_matrix):
    message_vector = np.array([ord(char) for char in message])
    print(message_vector)
    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)                        #обернена матриця власних значень
    diagonalized_key_matrix = np.dot(np.dot(eigenvectors, np.diag(eigenvalues)), np.linalg.inv(eigenvectors))
    encrypted_vector = np.dot(diagonalized_key_matrix, message_vector[:len(key_matrix)])
    return encrypted_vector, eigenvalues, eigenvectors


def decrypt_message(encrypted_vector, key_matrix, eigenvalues, eigenvectors):

                            #оберненої матриця власних векторів:
    inv_eigenvectors = np.linalg.inv(eigenvectors)

#  діагоналізованої матриці, щоб її відновити треба помножити вл в   на діагон м вл в на обернену матрицю вл в
    diagonalized_key_matrix = np.dot(np.dot(eigenvectors, np.diag(eigenvalues)), inv_eigenvectors)


    diagonalized_key_matrix = np.linalg.inv(diagonalized_key_matrix)


    decrypted_vector = np.dot(diagonalized_key_matrix, encrypted_vector)

#Конвертація розшифрованого вектора назад в рядок
    decrypted_message = ''.join(chr(int(np.round(num.real))) for num in decrypted_vector)
    return decrypted_message
# таблиця ASCII


message = input("Input: ")
key_matrix = np.random.randint(0, 256, (len(message), len(message)))

encrypted_vector, eigenvalues, eigenvectors = encrypt_message(message, key_matrix)
print("Encrypted vector:", encrypted_vector)

decrypted_message = decrypt_message(encrypted_vector, key_matrix, eigenvalues, eigenvectors)
print("Decrypted message:", decrypted_message)
