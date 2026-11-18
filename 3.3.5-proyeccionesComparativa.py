import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# Utilidades de transformación
# ------------------------------
def rotX(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[1,0,0],
                     [0,c,-s],
                     [0,s, c]])

def rotY(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[ c,0,s],
                     [ 0,1,0],
                     [-s,0,c]])

def project_ortho(P):
    """Proyección ortográfica (paralela): descarta z."""
    return P[:, :2]

def project_persp(P, f=2.0, eps=1e-6):
    """Proyección pinhole: (x', y') = (f*x/z, f*y/z)."""
    z = P[:,2] + eps
    return np.column_stack([f * (P[:,0]/z), f * (P[:,1]/z)])

# ------------------------------
# Geometría: cubo + rejilla
# ------------------------------
cube = np.array([
    [0,0,0],[1,0,0],[1,1,0],[0,1,0],   # base
    [0,0,1],[1,0,1],[1,1,1],[0,1,1]    # tapa
])
edges = [(0,1),(1,2),(2,3),(3,0),
         (4,5),(5,6),(6,7),(7,4),
         (0,4),(1,5),(2,6),(3,7)]

# Rejilla en el plano z=0 (suelo)
g = np.linspace(-3, 3, 13)
grid_segments = []
for x in g:
    grid_segments.append(np.array([[x,-0.001,-3],[x,-0.001, 3]]))
for z in g:
    grid_segments.append(np.array([[-3,-0.001,z],[ 3,-0.001, z]]))

# ----------------------------------------
# "Colocamos" la escena frente a la cámara
# ----------------------------------------
R = rotY(np.radians(30)) @ rotX(np.radians(-25))  # orienta la escena
T = np.array([-0.5, -0.5, 6.0])                   # traslada (z>0)

cube_cam = (cube @ R.T) + T
grid_cam = [ (seg @ R.T) + T for seg in grid_segments ]

# ------------------------------
# Proyecciones
# ------------------------------
focal = 2.2
# cube_ortho = project_ortho(cube_cam)
# grid_ortho = [ project_ortho(seg) for seg in grid_cam ]

cube_ortho = 0.6 * project_ortho(cube_cam)
grid_ortho = [project_ortho(seg) for seg in grid_cam]


cube_persp = project_persp(cube_cam, f=focal)
grid_persp = [ project_persp(seg, f=focal) for seg in grid_cam ]

# ------------------------------
# Dibujo lado a lado
# ------------------------------
fig, axs = plt.subplots(1, 2, figsize=(11,5))
titles = ["Proyección ortográfica (paralela)", "Proyección en perspectiva (pinhole)"]

for ax, cube2d, grid2d, title in [
    (axs[0], cube_ortho, grid_ortho, titles[0]),
    (axs[1], cube_persp, grid_persp, titles[1])
]:
    # rejilla
    for seg in grid2d:
        ax.plot(seg[:,0], seg[:,1], linewidth=0.7, alpha=0.6)
    # cubo (aristas)
    for a,b in edges:
        ax.plot([cube2d[a,0], cube2d[b,0]],
                [cube2d[a,1], cube2d[b,1]],
                'r-', linewidth=2)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title(title)
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.set_xlabel("x'")
    ax.set_ylabel("y'")

# Opcional: mismos límites aproximados para comparar mejor
all_pts = np.vstack([cube_ortho, *grid_ortho, cube_persp, *grid_persp])
m = np.percentile(all_pts, [2, 98], axis=0)  # evita outliers
for ax in axs:
    ax.set_xlim(m[0,0], m[1,0])
    ax.set_ylim(m[0,1], m[1,1])

plt.tight_layout()
plt.show()
