import open3d as o3d
import numpy as np

bin_file = "kitti_file.bin" #path to your bin file

lidar_data = np.fromfile(bin_file, dtype=np.float32).reshape(-1, 4)

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(lidar_data[:, :3])

pcd_file = "kitti_pcd.pcd" #path to save pcd file

o3d.io.write_point_cloud(pcd_file, pcd, write_ascii=True)

