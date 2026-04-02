# %%
# Fully working Jupyter-friendly Open3D point cloud loader
import open3d as o3d
import os
from tkinter import Tk, filedialog

# -------------------------------
# 1️⃣ Define the function FIRST
# -------------------------------
def load_point_cloud(file_path):
    """
    Load a point cloud from supported formats: PLY, PCD, XYZ
    Returns Open3D point cloud object or None if failed
    """
    if not os.path.exists(file_path):
        print("❌ File not found:", file_path)
        return None

    # Attempt to read the point cloud
    try:
        pcd = o3d.io.read_point_cloud(file_path)
    except Exception as e:
        print("❌ Error loading point cloud:", e)
        return None

    if pcd.is_empty():
        print("❌ Point cloud is empty or format not supported")
        return None

    print(f"✅ Loaded {len(pcd.points)} points from {file_path}")
    return pcd

# -------------------------------
# 2️⃣ Pick the file interactively
# -------------------------------
Tk().withdraw()  # Hide the Tkinter root window
file_path = filedialog.askopenfilename(
    title="Select your point cloud file",
    filetypes=[("Point Cloud Files", "*.ply *.pcd *.xyz *.txt"), ("All Files", "*.*")]
)

if not file_path:
    print("❌ No file selected")
else:
    # -------------------------------
    # 3️⃣ Load the point cloud
    # -------------------------------
    pcd = load_point_cloud(file_path)

    # -------------------------------
    # 4️⃣ Visualize (Jupyter inline)
    # -------------------------------
    if pcd is not None:
        o3d.visualization.draw_plotly([pcd])

# %%
import open3d as o3d
import numpy as np
from tkinter import Tk, filedialog

# Pick the file ONLY .txt
Tk().withdraw()
file_path = filedialog.askopenfilename(
    title="Select your TXT point cloud file",
    filetypes=[("Text files", "*.txt")]
)

if not file_path:
    print("❌ No file selected")
else:
    try:
        # Load the TXT as a NumPy array
        points = np.loadtxt(file_path)  # expects columns: X Y Z

        # Check shape
        if points.shape[1] < 3:
            raise ValueError("File must have at least 3 columns (X Y Z)")

        # Create Open3D PointCloud
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(points[:, :3])

        print(f"✅ Loaded {len(pcd.points)} points from {file_path}")

        # Visualize inline in Jupyter
        o3d.visualization.draw_plotly([pcd])

    except Exception as e:
        print("❌ Failed to load point cloud:", e)


