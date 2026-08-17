import flet as ft

def main(page: ft.Page):
    page.title = "Mi primera app con Flet"
    
    mensaje = ft.Text("Aquí va un mensaje")
    nombre = ft.TextField(label="Escribe tu nombre", autofocus=True)
    def saludar(e):
        if nombre.value == "":
                mensaje.value = "hola desconocido"
        else:
            mensaje.value = ("Hola, " + nombre.value)
            #page.update()
    
    
    page.add(
    
        ft.Text("Hola, Andrés!"),
        ft.Button("Click aquí", on_click = saludar),
        mensaje,
        nombre
    )
ft.run(main)