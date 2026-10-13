
import tkinter as tk


ventana = tk.Tk()
ventana.title("Calculadora")

posicion = 0

entrada_texto = tk.Entry(
    ventana,
    font=("Calibri", 20)
)
entrada_texto.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=5,
    pady=5
)


def insertar_valor(valor):
    global posicion

    entrada_texto.insert(posicion, valor)
    posicion += len(str(valor))


def borrar():
    global posicion

    entrada_texto.delete(0, tk.END)
    posicion = 0


def calcular():
    global posicion

    ecuacion = entrada_texto.get()

    try:
        resultado = eval(ecuacion)

        entrada_texto.delete(0, tk.END)
        entrada_texto.insert(0, str(resultado))
        posicion = len(str(resultado))

    except (SyntaxError, ZeroDivisionError, NameError, TypeError):
        entrada_texto.delete(0, tk.END)
        entrada_texto.insert(0, "Error")
        posicion = 5


# Botones numéricos
boton_9 = tk.Button(
    ventana, text="9", width=5, height=2,
    command=lambda: insertar_valor(9)
)
boton_8 = tk.Button(
    ventana, text="8", width=5, height=2,
    command=lambda: insertar_valor(8)
)
boton_7 = tk.Button(
    ventana, text="7", width=5, height=2,
    command=lambda: insertar_valor(7)
)
boton_6 = tk.Button(
    ventana, text="6", width=5, height=2,
    command=lambda: insertar_valor(6)
)
boton_5 = tk.Button(
    ventana, text="5", width=5, height=2,
    command=lambda: insertar_valor(5)
)
boton_4 = tk.Button(
    ventana, text="4", width=5, height=2,
    command=lambda: insertar_valor(4)
)
boton_3 = tk.Button(
    ventana, text="3", width=5, height=2,
    command=lambda: insertar_valor(3)
)
boton_2 = tk.Button(
    ventana, text="2", width=5, height=2,
    command=lambda: insertar_valor(2)
)
boton_1 = tk.Button(
    ventana, text="1", width=5, height=2,
    command=lambda: insertar_valor(1)
)
boton_0 = tk.Button(
    ventana, text="0", width=13, height=2,
    command=lambda: insertar_valor(0)
)

# Botones de operaciones
boton_igual = tk.Button(
    ventana, text="=", width=5, height=2,
    command=calcular
)
boton_borrar = tk.Button(
    ventana, text="AC", width=5, height=2,
    command=borrar
)
boton_parentesis_1 = tk.Button(
    ventana, text="(", width=5, height=2,
    command=lambda: insertar_valor("(")
)
boton_parentesis_2 = tk.Button(
    ventana, text=")", width=5, height=2,
    command=lambda: insertar_valor(")")
)
boton_punto = tk.Button(
    ventana, text=".", width=5, height=2,
    command=lambda: insertar_valor(".")
)
boton_suma = tk.Button(
    ventana, text="+", width=5, height=2,
    command=lambda: insertar_valor("+")
)
boton_resta = tk.Button(
    ventana, text="-", width=5, height=2,
    command=lambda: insertar_valor("-")
)
boton_multiplicacion = tk.Button(
    ventana, text="*", width=5, height=2,
    command=lambda: insertar_valor("*")
)
boton_division = tk.Button(
    ventana, text="/", width=5, height=2,
    command=lambda: insertar_valor("/")
)

# Ubicación de los botones
boton_borrar.grid(row=1, column=0, padx=5, pady=2)
boton_parentesis_1.grid(row=1, column=1, padx=5, pady=2)
boton_parentesis_2.grid(row=1, column=2, padx=5, pady=2)
boton_division.grid(row=1, column=3, padx=5, pady=2)

boton_7.grid(row=2, column=0, padx=5, pady=2)
boton_8.grid(row=2, column=1, padx=5, pady=2)
boton_9.grid(row=2, column=2, padx=5, pady=2)
boton_multiplicacion.grid(row=2, column=3, padx=5, pady=2)

boton_4.grid(row=3, column=0, padx=5, pady=2)
boton_5.grid(row=3, column=1, padx=5, pady=2)
boton_6.grid(row=3, column=2, padx=5, pady=2)
boton_resta.grid(row=3, column=3, padx=5, pady=2)

boton_1.grid(row=4, column=0, padx=5, pady=2)
boton_2.grid(row=4, column=1, padx=5, pady=2)
boton_3.grid(row=4, column=2, padx=5, pady=2)
boton_suma.grid(row=4, column=3, padx=5, pady=2)

boton_0.grid(
    row=5, column=0, columnspan=2,
    padx=13, pady=2
)
boton_punto.grid(row=5, column=2, padx=5, pady=2)
boton_igual.grid(row=5, column=3, padx=5, pady=2)


ventana.mainloop()
