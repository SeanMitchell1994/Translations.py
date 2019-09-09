from trans import Trans
import numpy as np

rotate_obj = Trans()
#print(rotate_obj.rotate_y_3d(30))
t =  np.array([[1, 2, 3]])
m = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
np.dot(m,t)

#print(Trans.translate(t, m))
