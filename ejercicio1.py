import tkinter as tk

def seleccionar():
    selection = opcion.get()
    label.config(text="Seleccionado: "+  (selection))

def reset():
    opcion.set(None)
    label.config(text="")

root = tk.Tk()
root.title("Lista de RadioButton")

opcion = tk.StringVar()
opcion.set(None)

boton1 = tk.Radiobutton(root, text="comer", variable=opcion, value='comer', command=seleccionar)
boton1.pack()

boton2 = tk.Radiobutton(root, text="dormir", variable=opcion, value='dormir', command=seleccionar)
boton2.pack()

boton3 = tk.Radiobutton(root, text="jugar", variable=opcion, value='jugar', command=seleccionar)
boton3.pack()

boton4 = tk.Radiobutton(root, text="leer", variable=opcion, value='leer', command=seleccionar)
boton4.pack()

boton_reinicio = tk.Button(root, text="Reiniciar", command=reset)
boton_reinicio.pack()

label = tk.Label(root)
label.pack()

root.mainloop()
