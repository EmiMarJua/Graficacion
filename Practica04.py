import numpy as np
import matplotlib.pyplot as plt


# 1. DEFINICIÓN DE LA FUENTE
# Cada caracter es una lista de trazos. Cada trazo es una lista
# de puntos (x, y) en coordenadas normalizadas (alto = 1).

ANCHO = 0.6      # ancho de cada letra
ESPACIO = 0.85   # distancia entre el inicio de una letra y la siguiente

GLYPHS = {
    "H": [
        [(0, 0), (0, 1)],
        [(ANCHO, 0), (ANCHO, 1)],
        [(0, 0.5), (ANCHO, 0.5)],
    ],
    "O": [
        [(0.15, 0), (0.45, 0), (ANCHO, 0.15), (ANCHO, 0.85),
         (0.45, 1), (0.15, 1), (0, 0.85), (0, 0.15), (0.15, 0)],
    ],
    "L": [
        [(0, 1), (0, 0), (ANCHO, 0)],
    ],
    "A": [
        [(0, 0), (0.3, 1), (ANCHO, 0)],
        [(0.12, 0.4), (0.48, 0.4)],
    ],
    "E": [
        [(ANCHO, 0), (0, 0), (0, 1), (ANCHO, 1)],
        [(0, 0.5), (0.45, 0.5)],
    ],
}


# 2. MATRICES DE TRANSFORMACION (coordenadas homogeneas)
# Se usa la convención [x, y, 1] · T

def trasladar(tx, ty):
    return np.array([[1, 0, 0],
                     [0, 1, 0],
                     [tx, ty, 1]], dtype=float)

def escalar(sx, sy=None):
    sy = sx if sy is None else sy
    return np.array([[sx, 0, 0],
                     [0, sy, 0],
                     [0, 0, 1]], dtype=float)

def rotar(grados):
    t = np.radians(grados)
    c, s = np.cos(t), np.sin(t)
    return np.array([[c, s, 0],
                     [-s, c, 0],
                     [0, 0, 1]], dtype=float)

def reflejar_x():
    """Espejo respecto al eje X."""
    return escalar(1, -1)

def reflejar_y():
    """Espejo respecto al eje Y."""
    return escalar(-1, 1)

def alrededor_de(T, px, py):
    """Aplica la transformacion T respecto al punto (px, py)."""
    return trasladar(-px, -py) @ T @ trasladar(px, py)

def aplicar(puntos, T):
    """Multiplica una lista de puntos (x, y) por la matriz T."""
    p = np.array(puntos, dtype=float)
    p = np.hstack([p, np.ones((len(p), 1))])
    return (p @ T)[:, :2]


# 3. FUNCIONES DE DIBUJO

def dibujar_caracter(ax, ch, x=0, y=0, escala=1.0, angulo=0,
                     color="black", lw=2, T_local=None):
    """Dibuja un caracter en (x, y), con escala y rotacion sobre su centro."""
    cx, cy = ANCHO / 2, 0.5                 # centro de la letra
    if T_local is None:
        T_local = np.eye(3)

    # Orden: transformacion local -> rotar sobre su centro -> escalar -> trasladar
    T = (T_local
         @ alrededor_de(rotar(angulo), cx, cy)
         @ escalar(escala)
         @ trasladar(x, y))

    for trazo in GLYPHS[ch]:
        pts = aplicar(trazo, T)
        ax.plot(pts[:, 0], pts[:, 1], color=color, linewidth=lw,
                solid_capstyle="round", solid_joinstyle="round")

def dibujar_palabra(ax, texto, x=0, y=0, escala=1.0, angulo=0,
                    color="black", lw=2, T_local=None):
    """Dibuja una palabra completa, separando las letras segun ESPACIO."""
    for i, ch in enumerate(texto.upper()):
        dibujar_caracter(ax, ch, x + i * ESPACIO * escala, y,
                         escala, angulo, color, lw, T_local)

def preparar_ax(ax, titulo):
    ax.set_title(titulo)
    ax.set_aspect("equal")
    ax.set_xlim(-0.5, 9)
    ax.set_ylim(-1, 3)
    ax.grid(True, alpha=0.3)


# 4. DEMOSTRACION DE TRANSFORMACIONES

if __name__ == "__main__":
    fig, ejes = plt.subplots(2, 3, figsize=(14, 8))
    ejes = ejes.flatten()

    configuraciones = [
        ("Original", dict()),
        ("Escala x2", dict(escala=2, color="red")),
        ("Escala x0.5", dict(escala=0.5, color="blue")),
        ("Rotada 45° (sobre su centro)", dict(angulo=45, color="green")),
        ("Reflejada (espejo en Y)",
         dict(T_local=alrededor_de(reflejar_y(), ANCHO / 2, 0.5),
              color="orange")),
        ("Trasladada y grosor 5",
         dict(x=0.5, y=0.5, color="purple", lw=5)),
    ]

    for ax, (titulo, opciones) in zip(ejes, configuraciones):
        preparar_ax(ax, titulo)
        dibujar_palabra(ax, "HOLA", **opciones)

    plt.tight_layout()
    plt.show()