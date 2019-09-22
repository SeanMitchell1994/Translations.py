import numpy as np

class Trans:

    def __init__(self):
        self.exists = True

    def rotate_2d(self, theta):
        # rotates an axis in a 2d plane for a given angle theta
        # returns the rotation matrix for the given angle, theta
        rotation_matrix = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
        return rotation_matrix

    def rotate_x_3d(self, alpha):
        # rotates an axis in a 3d space for a given angle, alpha
        # returns the rotation matrix for the given angle, alpha
        rotation_matrix = np.array([[1, 0, 0], [0, np.cos(alpha), -np.sin(alpha)], [0, np.sin(alpha), np.cos(alpha)]])
        return rotation_matrix

    def rotate_y_3d(self, beta):
        # rotates an axis in a 3d space for a given angle, beta
        # returns the rotation matrix for a given angle, beta
        rotation_matrix = np.array([[np.cos(beta), 0, np.sin(beta)], [0, 1, 0], [-np.sin(beta), 0, np.cos(beta)]])
        return rotation_matrix

    def rotate_z_3d(self, gamma):
        # rotates an axis in a 3d space for a given angle, gamma
        # returns the rotation matrix for a given angle, gamma
        rotation_matrix = np.array([[np.cos(gamma), -np.sin(gamma), 0], [np.sin(gamma), np.cos(gamma), 0], [0, 0, 1]])
        return rotation_matrix

    def rotation_matrix(self, matrix_a, matrix_b):
        # Returns the matrix product of any two rotation matrices
        rotation_matrix = np.dot(matrix_a, matrix_b)
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