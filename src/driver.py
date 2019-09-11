from trans import Trans

rotate_obj = Trans()
print("2d rotation:")
print(rotate_obj.rotate_2d(30))
print("\n3d rotation (x):")
print(rotate_obj.rotate_x_3d(45))
print("\n3d rotation (y):")
print(rotate_obj.rotate_y_3d(45))
print("\n3d rotation (z):")
print(rotate_obj.rotate_z_3d(45))