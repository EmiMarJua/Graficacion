# ------------------------------------------------------------
# PRACTICA 5: DIBUJO DE OBJETOS EN 3D
# Nombre: Marcial Juarez Jose Emiliano, Fernando Garza Rodriguez, 
# Daniel Abisai Peralta Luevanos, Sayra Jeraldine Gomez Mares
# N. Control: 24130806 - 24130835 - 24130899 - 23130619
#
# Objetivo:
# Construir y visualizar un cubo y una esfera en 3D,
# utilizando vértices, aristas, caras y proyecciones
# (paralela y perspectiva), permitiendo rotar las figuras
# y comparar distintas resoluciones y tamaños.
# Materia: Graficacion
# Tema 3: Graficacion 3D
# ------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation


# ------------------------------------------------------------
# PARAMETROS MODIFICABLES
# ------------------------------------------------------------

TAMANO_CUBO = 1.5
RADIO_ESFERA = 1.0

# Resolución de la esfera
SEGMENTOS_U = 30
SEGMENTOS_V = 20


# ------------------------------------------------------------
# CONSTRUCCION DEL CUBO
# ------------------------------------------------------------

def construir_cubo(tamano):
    """
    Construye un cubo centrado en el origen.
    Devuelve: vértices (8,3), aristas (lista de tuplas), caras (lista de listas).
    """

    # Definición de los 8 vértices del cubo unitario
    vertices = np.array([
        [0, 0, 0],
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 1, 1]
    ], dtype=float)

    # Aplicar el tamaño indicado y centrar en el origen
    vertices = vertices * tamano
    vertices[:, 0] -= tamano / 2
    vertices[:, 1] -= tamano / 2
    vertices[:, 2] -= tamano / 2

    # Definición de las 12 aristas
    aristas = [
        (0, 1), (1, 2), (2, 3), (3, 0),   # cara inferior
        (4, 5), (5, 6), (6, 7), (7, 4),   # cara superior
        (0, 4), (1, 5), (2, 6), (3, 7)    # aristas verticales
    ]

    # Definición de las 6 caras
    caras = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [0, 1, 5, 4],
        [2, 3, 7, 6],
        [1, 2, 6, 5],
        [0, 3, 7, 4]
    ]

    return vertices, aristas, caras


# ------------------------------------------------------------
# DIBUJAR EL CUBO
# ------------------------------------------------------------

def dibujar_cubo(ax, vertices, aristas, caras,
                 color_caras='skyblue',
                 color_aristas='blue',
                 alpha=0.25):
    """Dibuja un cubo completo: caras, aristas y vértices."""

    # Caras
    caras_cubo = [vertices[indices] for indices in caras]
    coleccion = Poly3DCollection(
        caras_cubo,
        facecolors=color_caras,
        edgecolors=color_aristas,
        linewidths=1,
        alpha=alpha
    )
    ax.add_collection3d(coleccion)

    # Aristas
    for inicio, fin in aristas:
        ax.plot(
            *vertices[[inicio, fin]].T,
            color=color_aristas,
            linewidth=2
        )

    # Vértices
    ax.scatter(
        vertices[:, 0],
        vertices[:, 1],
        vertices[:, 2],
        color='darkblue',
        s=25
    )


# ------------------------------------------------------------
# CONSTRUCCION DE LA ESFERA (METODO PARAMETRICO)
# ------------------------------------------------------------

def construir_esfera(radio, segmentos_u, segmentos_v):
    """
    Construye una esfera usando coordenadas esféricas paramétricas.
    u: ángulo horizontal (0 a 2π)
    v: ángulo vertical (0 a π)
    """

    u = np.linspace(0, 2 * np.pi, segmentos_u)
    v = np.linspace(0, np.pi, segmentos_v)

    U, V = np.meshgrid(u, v)

    # Ecuaciones paramétricas de la esfera
    X = radio * np.cos(U) * np.sin(V)
    Y = radio * np.sin(U) * np.sin(V)
    Z = radio * np.cos(V)

    return X, Y, Z


# ------------------------------------------------------------
# DIBUJAR LA ESFERA
# ------------------------------------------------------------

def dibujar_esfera(ax, X, Y, Z, color='green', color_arista='darkred'):
    """Dibuja la superficie de la esfera."""

    ax.plot_surface(
        X, Y, Z,
        color=color,
        edgecolor=color_arista,
        linewidth=0.25,
        alpha=0.75,
        rstride=1,
        cstride=1
    )


# ------------------------------------------------------------
# CONFIGURAR LOS EJES
# ------------------------------------------------------------

def configurar_ejes(ax, tipo_proyeccion, titulo, focal_length=None):
    """
    Configura los ejes de una vista 3D.
    tipo_proyeccion: 'ortho' (paralela) o 'persp' (perspectiva).
    focal_length: solo aplica a 'persp'. Valores pequeños (0.2) → efecto fuerte.
    """

    if tipo_proyeccion == 'persp' and focal_length is not None:
        ax.set_proj_type('persp', focal_length=focal_length)
    else:
        ax.set_proj_type(tipo_proyeccion)

    ax.set_title(titulo)
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')

    # Límites de visualización (ampliados para que quepa la esfera desplazada)
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-2.0, 2.0)
    ax.set_zlim(-2.0, 2.0)

    # Proporciones iguales
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=20, azim=-60)


# ------------------------------------------------------------
# ANIMACION DE ROTACION (requisito: "permitir girar la figura")
# ------------------------------------------------------------

def animar_rotacion(fig, ax_list, frames=180, intervalo=50):
    """Rota las vistas alrededor del eje Z para verificar la estructura."""

    def update(frame):
        for ax in ax_list:
            ax.view_init(elev=20, azim=frame)
        return ax_list

    ani = FuncAnimation(
        fig, update,
        frames=np.arange(0, 360, 360 / frames),
        interval=intervalo,
        blit=False,
        repeat=True
    )
    return ani


# ------------------------------------------------------------
# FIGURA 1: COMPARACION DE PROYECCIONES
# ------------------------------------------------------------

def figura_proyecciones():
    """Muestra el cubo y la esfera con proyección paralela y perspectiva."""

    # Construir objetos
    vertices, aristas, caras = construir_cubo(TAMANO_CUBO)
    X, Y, Z = construir_esfera(RADIO_ESFERA, SEGMENTOS_U, SEGMENTOS_V)

    fig = plt.figure(figsize=(14, 7))

    ax1 = fig.add_subplot(121, projection='3d')  # Proyección paralela
    ax2 = fig.add_subplot(122, projection='3d')  # Proyección perspectiva

    for ax in [ax1, ax2]:
        dibujar_cubo(ax, vertices, aristas, caras)
        dibujar_esfera(ax, X + 1.7, Y, Z)

    # Paralela (ortográfica)
    configurar_ejes(ax1, 'ortho', 'Proyección Paralela')

    # Perspectiva con focal_length pequeño → efecto visible
    configurar_ejes(ax2, 'persp', 'Proyección en Perspectiva',
                    focal_length=0.2)

    fig.suptitle('PRACTICA 5: DIBUJO DE OBJETOS EN 3D',
                 fontsize=15)

    plt.tight_layout()

    # Animación de rotación para cumplir "permitir girar la figura"
    ani = animar_rotacion(fig, [ax1, ax2])

    plt.show()
    return ani


# ------------------------------------------------------------
# FIGURA 2: PRUEBAS (distintos tamaños y resoluciones)
# ------------------------------------------------------------

def figura_pruebas():
    """Cumple el punto 3 de la práctica:
       - Cubos de distintos tamaños
       - Esferas con distintas resoluciones
    """

    fig = plt.figure(figsize=(14, 7))

    # --- Cubos de distintos tamaños ---
    ax1 = fig.add_subplot(121, projection='3d')
    for tam, color in [(0.75, 'royalblue'), (2.0, 'crimson')]:
        v, a, c = construir_cubo(tam)
        dibujar_cubo(ax1, v, a, c, color_caras=color, color_aristas=color)
    ax1.set_title('Cubos de distintos tamaños')
    ax1.set_xlabel('X'); ax1.set_ylabel('Y'); ax1.set_zlabel('Z')
    ax1.set_xlim(-1.5, 1.5); ax1.set_ylim(-1.5, 1.5); ax1.set_zlim(-1.5, 1.5)
    ax1.set_box_aspect((1, 1, 1))

    # --- Esferas de distinta resolución ---
    ax2 = fig.add_subplot(122, projection='3d')
    for (su, sv, color) in [(6, 4, 'red'), (40, 30, 'green')]:
        X, Y, Z = construir_esfera(RADIO_ESFERA, su, sv)
        ax2.plot_surface(X, Y, Z, color=color, alpha=0.55,
                         edgecolor='black', linewidth=0.2)
    ax2.set_title('Esferas: baja (roja) vs alta (verde) resolución')
    ax2.set_xlabel('X'); ax2.set_ylabel('Y'); ax2.set_zlabel('Z')
    ax2.set_xlim(-1.2, 1.2); ax2.set_ylim(-1.2, 1.2); ax2.set_zlim(-1.2, 1.2)
    ax2.set_box_aspect((1, 1, 1))

    fig.suptitle('PRACTICA 5: PRUEBAS DE TAMAÑO Y RESOLUCIÓN',
                 fontsize=14)
    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------

def main():
    # Figura con comparación de proyecciones y rotación animada
    figura_proyecciones()

    # Figura con pruebas de tamaños y resoluciones
    figura_pruebas()

    # Información de los objetos
    vertices, aristas, caras = construir_cubo(TAMANO_CUBO)

    print("----- INFORMACION DEL CUBO -----")
    print("Cantidad de vértices:", len(vertices))
    print("Cantidad de aristas:", len(aristas))
    print("Cantidad de caras:", len(caras))

    print("\n----- INFORMACION DE LA ESFERA -----")
    print("Radio:", RADIO_ESFERA)
    print("Segmentos horizontales:", SEGMENTOS_U)
    print("Segmentos verticales:", SEGMENTOS_V)


# Ejecutar el programa principal
if __name__ == "__main__":
    main()