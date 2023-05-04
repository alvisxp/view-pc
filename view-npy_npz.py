import open3d as o3d
import numpy as np

point_clouds = np.load("train_points.npy") # path to your file

print(point_clouds.shape) 

for i in range(0, 98430, 10000): # modify/remove according to your file contents
    point_cloud = point_clouds[i]

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(point_cloud[:, :3])

    o3d.visualization.draw_geometries([pcd])
