import numpy as np
import matplotlib.pyplot as plt

# Vértices de un cubo unitario (cada fila representa un vértice).
vertices = np.array([
    [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
    [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]
], dtype=float)

# Pares de índices que definen las 12 aristas del cubo.
aristas = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# Parámetros que puede modificar el estudiante.
tx, ty, tz =  1, 6, 4
# Matriz homogénea de traslación (convención de vectores columna).
T = np.array([
    [1, 0, 0, tx],
    [0, 1, 0, ty],
    [0, 0, 1, tz],
    [0, 0, 0, 1]
], dtype=float)

# Añadir la coordenada homogénea 1 a cada vértice.
vertices_h = np.column_stack((vertices, np.ones(len(vertices))))

# Cada vértice se trata como columna; por eso se transpone la matriz.
transformados_h = (T @ vertices_h.T).T
vertices_trasladados = transformados_h[:, :3]


def dibujar_cubo(ax, puntos, color, etiqueta):
    for i, j in aristas:
        ax.plot(*puntos[[i, j]].T, color=color, linewidth=2)
    ax.scatter(*puntos.T, color=color, s=20, label=etiqueta)


fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection='3d')
dibujar_cubo(ax, vertices, 'royalblue', 'Original')
dibujar_cubo(ax, vertices_trasladados, 'lightgreen', 'Trasladado')

# Límites comunes y aspecto proporcional para evitar deformaciones visuales.
todos = np.vstack((vertices, vertices_trasladados))
centro = (todos.min(axis=0) + todos.max(axis=0)) / 2
radio = max((todos.max(axis=0) - todos.min(axis=0)).max() / 2, 0.75) * 1.15
ax.set_xlim(centro[0] - radio, centro[0] + radio)
ax.set_ylim(centro[1] - radio, centro[1] + radio)
ax.set_zlim(centro[2] - radio, centro[2] + radio)
ax.set_box_aspect((1, 1, 1))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f'Traslación 3D: ({tx:g}, {ty:g}, {tz:g})')
ax.legend()
plt.tight_layout()
plt.show()

print('Primer vértice original:', vertices[0])
print('Primer vértice trasladado:', vertices_trasladados[0])
