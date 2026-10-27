import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib

matplotlib.use("TkAgg")

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Transformaciones2D:
    def __init__(self):

        # Triángulo original

        self.figura = np.array([
            [0, 0],
            [2, 0],
            [1, 2],
            [0, 0]
        ], dtype=float)

        # Coordenadas homogéneas
        
        self.figura_h = np.column_stack((
            self.figura,
            np.ones(len(self.figura))
        ))

        self.matriz = np.eye(3)

    @staticmethod
    def traslacion(tx, ty):
        return np.array([
            [1, 0, tx],
            [0, 1, ty],
            [0, 0, 1]
        ], dtype=float)

    @staticmethod
    def escalamiento(sx, sy):
        return np.array([
            [sx, 0, 0],
            [0, sy, 0],
            [0, 0, 1]
        ], dtype=float)

    @staticmethod
    def rotacion(grados):
        rad = np.radians(grados)
        c, s = np.cos(rad), np.sin(rad)

        return np.array([
            [c, -s, 0],
            [s,  c, 0],
            [0,  0, 1]
        ], dtype=float)

    @staticmethod
    def reflexion_x():
        return np.array([
            [1,  0, 0],
            [0, -1, 0],
            [0,  0, 1]
        ], dtype=float)

    @staticmethod
    def reflexion_y():
        return np.array([
            [-1, 0, 0],
            [ 0, 1, 0],
            [ 0, 0, 1]
        ], dtype=float)

    @staticmethod
    def sesgado(kx, ky):
        return np.array([
            [1,  kx, 0],
            [ky, 1,  0],
            [0,  0,  1]
        ], dtype=float)

    @classmethod
    def rotacion_centro(cls, grados, cx, cy):
        return (
            cls.traslacion(cx, cy)
            @ cls.rotacion(grados)
            @ cls.traslacion(-cx, -cy)
        )

    def aplicar(self, nueva_matriz):

        # Permite componer varias transformaciones

        self.matriz = nueva_matriz @ self.matriz

    def reiniciar(self):
        self.matriz = np.eye(3)

    def figura_transformada(self):
        resultado = (self.matriz @ self.figura_h.T).T
        return resultado[:, :2]


class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Práctica 3 - Transformaciones 2D")
        self.ventana.geometry("1150x740")
        self.ventana.minsize(950, 620)

        self.modelo = Transformaciones2D()
        self._crear_interfaz()
        self._dibujar()

    def _crear_interfaz(self):
        contenedor = ttk.Frame(self.ventana, padding=10)
        contenedor.pack(fill="both", expand=True)

        # Panel de controles

        panel = ttk.Frame(contenedor, width=300)
        panel.pack(side="left", fill="y", padx=(0, 12))
        panel.pack_propagate(False)

        # Área de gráfica

        grafica_panel = ttk.Frame(contenedor)
        grafica_panel.pack(side="right", fill="both", expand=True)

        ttk.Label(
            panel,
            text="Transformaciones 2D",
            font=("Segoe UI", 15, "bold")
        ).pack(anchor="w", pady=(0, 8))

        # Traslación

        self._seccion(panel, "Traslación")
        self.tx = self._campo(panel, "Desplazamiento X (tx)", "2")
        self.ty = self._campo(panel, "Desplazamiento Y (ty)", "1")
        self._boton(
            panel, "Aplicar traslación",
            lambda: self.modelo.traslacion(
                self._numero(self.tx), self._numero(self.ty)
            )
        )

        # Escalamiento

        self._seccion(panel, "Escalamiento")
        self.sx = self._campo(panel, "Factor X (sx)", "1.5")
        self.sy = self._campo(panel, "Factor Y (sy)", "1.5")
        self._boton(
            panel, "Aplicar escalamiento",
            lambda: self.modelo.escalamiento(
                self._numero(self.sx), self._numero(self.sy)
            )
        )

        # Rotación sobre el origen

        self._seccion(panel, "Rotación respecto al origen")
        self.angulo = self._campo(panel, "Ángulo en grados", "45")
        self._boton(
            panel, "Aplicar rotación",
            lambda: self.modelo.rotacion(self._numero(self.angulo))
        )

        # Rotación sobre un punto arbitrario

        self._seccion(panel, "Rotación respecto a un punto")
        self.angulo_c = self._campo(panel, "Ángulo en grados", "45")
        self.cx = self._campo(panel, "Centro X (cx)", "1")
        self.cy = self._campo(panel, "Centro Y (cy)", "1")
        self._boton(
            panel, "Rotar respecto al punto",
            lambda: self.modelo.rotacion_centro(
                self._numero(self.angulo_c),
                self._numero(self.cx),
                self._numero(self.cy)
            )
        )

        # Sesgado

        self._seccion(panel, "Sesgado (shear)")
        self.kx = self._campo(panel, "Factor X (kx)", "0.5")
        self.ky = self._campo(panel, "Factor Y (ky)", "0")
        self._boton(
            panel, "Aplicar sesgado",
            lambda: self.modelo.sesgado(
                self._numero(self.kx), self._numero(self.ky)
            )
        )

        # Reflexiones

        self._seccion(panel, "Reflexión")
        self._boton(
            panel, "Reflejar sobre eje X",
            self.modelo.reflexion_x
        )
        self._boton(
            panel, "Reflejar sobre eje Y",
            self.modelo.reflexion_y
        )

        ttk.Separator(panel).pack(fill="x", pady=8)

        ttk.Button(
            panel,
            text="Mostrar matriz acumulada",
            command=self._mostrar_matriz
        ).pack(fill="x", pady=2)

        ttk.Button(
            panel,
            text="Reiniciar figura",
            command=self._reiniciar
        ).pack(fill="x", pady=2)

        self.estado = tk.StringVar(
            value="Selecciona una transformación."
        )
        ttk.Label(
            panel,
            textvariable=self.estado,
            wraplength=275
        ).pack(anchor="w", pady=8)

        # Gráfica de Matplotlib
        self.figura_mpl = Figure(figsize=(7, 6), dpi=100)
        self.eje = self.figura_mpl.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(
            self.figura_mpl,
            master=grafica_panel
        )
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    @staticmethod
    def _seccion(panel, texto):
        ttk.Label(
            panel,
            text=texto,
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w", pady=(5, 2))

    @staticmethod
    def _campo(panel, etiqueta, valor):
        ttk.Label(panel, text=etiqueta).pack(anchor="w")
        entrada = ttk.Entry(panel)
        entrada.insert(0, valor)
        entrada.pack(fill="x", pady=(0, 3))
        return entrada

    def _boton(self, panel, texto, operacion):
        ttk.Button(
            panel,
            text=texto,
            command=lambda: self._accion_segura(operacion)
        ).pack(fill="x", pady=(3, 6))

    @staticmethod
    def _numero(campo):
        return float(campo.get().strip())

    def _accion_segura(self, operacion):
        try:
            matriz = operacion()
            self.modelo.aplicar(matriz)
            self.estado.set("Transformación aplicada correctamente.")
            self._dibujar()
        except ValueError:
            messagebox.showerror(
                "Dato inválido",
                "Introduce valores numéricos válidos en los campos."
            )
        except Exception as error:
            messagebox.showerror(
                "Error",
                f"No se pudo aplicar la transformación:\n{error}"
            )

    def _reiniciar(self):
        self.modelo.reiniciar()
        self.estado.set("Figura y matriz reiniciadas.")
        self._dibujar()

    def _mostrar_matriz(self):
        texto = np.array2string(
            self.modelo.matriz,
            precision=3,
            suppress_small=True
        )
        messagebox.showinfo("Matriz acumulada 3x3", texto)

    def _dibujar(self):
        original = self.modelo.figura
        transformada = self.modelo.figura_transformada()

        self.eje.clear()

        self.eje.plot(
            original[:, 0], original[:, 1],
            "o-", color="blue", linewidth=2,
            label="Figura original"
        )

        self.eje.plot(
            transformada[:, 0], transformada[:, 1],
            "o-", color="red", linewidth=2,
            label="Figura transformada"
        )

        self.eje.axhline(0, color="black", linewidth=0.8)
        self.eje.axvline(0, color="black", linewidth=0.8)
        self.eje.grid(True, linestyle="--", alpha=0.5)
        self.eje.set_xlabel("X")
        self.eje.set_ylabel("Y")
        self.eje.set_title("Visualización de transformaciones 2D")
        self.eje.legend()
        self.eje.set_aspect("equal", adjustable="datalim")

        self.figura_mpl.tight_layout()
        self.canvas.draw()


if __name__ == "__main__":
    ventana = tk.Tk()
    app = Aplicacion(ventana)
    ventana.mainloop()