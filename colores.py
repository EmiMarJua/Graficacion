import matplotlib.pyplot as plt

colores = [("A", (255, 0 ,0)), 
           ("B", (0,255,0)), 
           ("C", (0,0,255)),
           ("D", (255,255,255)), 
           ("E", (0,0,0)), 
           ("F", (255,255,128))]

fig, ax = plt.subplots()

for i, (nombre, rgb) in enumerate(colores):
    #Matplotlib utiliza valores entre 0 y 1
    color = tuple(valor/255 for valor in rgb)

    ax.barh(i, 1, color = color)

    #elegimos color del texto para que sea visible

    texto = "white" if sum(rgb) < 300 else "black"

    ax.text(

        0.5, i,
        f"{nombre} = RGB{rgb}",
        ha = "center",
        va = "center",
        color = texto,
        fontsize = 12
        
    )

ax.set_xlim(0, 1)
ax.set_yticks([])
ax.set_xticks([])
ax.invert_yaxis()

plt.title("Asi son los colores?")
plt.show()
