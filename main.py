import json
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

# Configuración de tamaño para simular móvil
Window.size = (400, 600)

KV = """
WindowManager:
    MenuInicio:
    MenuCategorias:
    MenuProductos:

<MenuInicio>:
    name: "inicio"
    BoxLayout:
        orientation: 'vertical'
        padding: 50
        spacing: 20
        canvas.before:
            Color:
                rgba: 0.1, 0.1, 0.1, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: "Restaurante Oliver Avila "
            font_size: '26sp'
            bold: True
            color: 1, 0.8, 0, 1
        Label:
            text: "Computacion en la nube \\nOliver Claudio Avila Castillo"
            halign: 'center'
            font_size: '14sp'
        Button:
            text: "VER MENÚ"
            size_hint_y: None
            height: '50dp'
            background_color: 0.2, 0.6, 1, 1
            on_release: app.root.current = "categorias"

<MenuCategorias>:
    name: "categorias"
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        Label:
            text: "CATEGORÍAS"
            size_hint_y: 0.1
            font_size: '22sp'
            bold: True
        ScrollView:
            BoxLayout:
                id: container_cat
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                spacing: 10
        Button:
            text: "VOLVER"
            size_hint_y: 0.1
            on_release: app.root.current = "inicio"

<MenuProductos>:
    name: "productos"
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        Label:
            id: titulo_categoria
            text: ""
            size_hint_y: 0.1
            font_size: '22sp'
            color: 0.2, 0.8, 0.2, 1
        ScrollView:
            BoxLayout:
                id: container_prod
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                spacing: 10
        Button:
            text: "VOLVER A CATEGORÍAS"
            size_hint_y: 0.1
            on_release: app.root.current = "categorias"
"""

class MenuInicio(Screen):
    pass

class MenuCategorias(Screen):
    def on_enter(self):
        self.ids.container_cat.clear_widgets()
        try:
            with open('menu.json', 'r', encoding='utf-8') as f:
                datos = json.load(f)
            
            for cat in datos.keys():
                btn = Button(text=cat, size_hint_y=None, height='70dp')
                # Usamos una función que capture el valor actual de 'cat'
                btn.bind(on_release=lambda instance, c=cat: self.ir_a_productos(c))
                self.ids.container_cat.add_widget(btn)
        except Exception as e:
            print(f"Error cargando JSON: {e}")

    def ir_a_productos(self, categoria):
        app = App.get_running_app()
        app.root.get_screen('productos').categoria_actual = categoria
        app.root.current = 'productos'

class MenuProductos(Screen):
    categoria_actual = ""

    def on_enter(self):
        self.ids.titulo_categoria.text = self.categoria_actual
        self.ids.container_prod.clear_widgets()
        
        with open('menu.json', 'r', encoding='utf-8') as f:
            datos = json.load(f)
        
        productos = datos.get(self.categoria_actual, [])
        for p in productos:
            # Mostramos nombre y precio
            lbl = Label(
                text=f"{p['nombre']} - {p['precio']}", 
                size_hint_y=None, 
                height='50dp',
                font_size='16sp'
            )
            self.ids.container_prod.add_widget(lbl)

class WindowManager(ScreenManager):
    pass

class MenuApp(App):
    def build(self):
        self.title = "App Menú - Oliver Avila"
        return Builder.load_string(KV)

if __name__ == '__main__':
    MenuApp().run()