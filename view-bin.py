import pptk
import numpy as np

pc_bin = np.fromfile('binary_file.bin', '<f4')
pc_bin = np.reshape(pc_bin, (-1,4))

print(pc_bin.shape)

v = pptk.viewer(pc_bin[:, :3])

v.color_map('hsv', scale=[0,0,0,5])
v.color_map([[200, 0, 0], [1, 200, 1],[1, 200, 1], [1, 200, 1]])
