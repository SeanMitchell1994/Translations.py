import numpy as np

class Trans:

    def __init__(self):
        self.exists = True

    def rotate_x_2d(self, alpha):
        return 0

    def rotate_y_2d(self, beta):
        return 0

    def rotate_z_2d(self, gamma):
        return 0

    def rotate_x_3d(self, alpha):
        rotation_matrix = np.array([[1, 0, 0], [0, np.cos(alpha), -np.sin(alpha)], [0, np.sin(alpha), np.cos(alpha)]])
        return rotation_matrix

    def rotate_y_3d(self, beta):
        rotation_matrix = np.array([[np.cos(beta), 0, np.sin(beta)], [0, 1, 0], [-np.sin(beta), 0, np.cos(beta)]])
        return rotation_matrix

    def rotate_z_3d(self, gamma):
        rotation_matrix = np.array([[np.cos(gamma), -np.sin(gamma), 0], [np.sin(gamma), np.cos(gamma), 0], [0, 0, 1]])
        return rotation_matrix

    def create_translation_matrix_3d(self, x = 0, y = 0, z = 0):
        #print("x: %s, y: %s, z: %s" % (str(x), str(y), str(z)))
        displacement_vector = np.array([[x], [y], [z]])
        #print(displacement_vector)
        return displacement_vector

    #def translate(self, translation, matrix):
    #    translated_matrix = np.dot(translation, matrix)
    #    #return 0
    #    return translated_matrix

    def homogenous_transform(rotation, translation):
        return 0