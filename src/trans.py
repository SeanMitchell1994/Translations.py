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
        rotation_matrix = np.array([[1, 0, 0], [0, np.cos(alpha), -np.sin(alpha)], [0, np.sin(alpha), np.cos(alpha)]])
        return rotation_matrix

    def rotate_y_3d(self, beta):
        rotation_matrix = np.array([[np.cos(beta), 0, np.sin(beta)], [0, 1, 0], [-np.sin(beta), 0, np.cos(beta)]])
        return rotation_matrix

    def rotate_z_3d(self, gamma):
        rotation_matrix = np.array([[np.cos(gamma), -np.sin(gamma), 0], [np.sin(gamma), np.cos(gamma), 0], [0, 0, 1]])
        return rotation_matrix

    def rotation_matrix(self, matrix_a, matrix_b):
        # Returns the matrix product of any two rotation matrices
        rotation_matrix = np.dot(matrix_a, matrix_b)
        return rotation_matrix

    def translate_x(b):
        return 0

    def translate_y(b):
        return 0

    def translate_z(b):
        return 0

    def homogenous_transform(rotation, translation):
        return 0