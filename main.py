from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.toolbar import MDTopAppBar
import webbrowser
from urllib.parse import quote

class DeliveryApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"  # Delivery jaisa color
        self.theme_cls.theme_style = "Dark"        # Battery bachane ke liye
        
        screen = MDScreen()
        
        # Layout
        layout = MDBoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # Top Bar
        toolbar = MDTopAppBar(title="Delivery Route Tool")
        toolbar.elevation = 10
        layout.add_widget(toolbar)
        
        # Input Field
        self.address_input = MDTextField(
            hint_text="Parcel Address Likho",
            mode="rectangle",
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.address_input)
        
        # Add Button
        add_btn = MDRaisedButton(
            text="ADD PARCEL",
            size_hint=(1, None),
            height=50,
            on_release=self.add_address
        )
        layout.add_widget(add_btn)
        
        # List of Parcels (Scrollable)
        scroll = MDScrollView()
        self.list_view = MDList()
        scroll.add_widget(self.list_view)
        layout.add_widget(scroll)
        
        # Start Route Button (Bottom)
        route_btn = MDRaisedButton(
            text="🚀 START GOOGLE MAPS ROUTE",
            md_bg_color=(0, 1, 0, 1), # Green Color
            size_hint=(1, None),
            height=60,
            on_release=self.open_google_maps
        )
        layout.add_widget(route_btn)
        
        screen.add_widget(layout)
        self.parcel_addresses = []
        return screen

    def add_address(self, obj):
        addr = self.address_input.text
        if addr:
            self.parcel_addresses.append(addr)
            # List mein dikhao
            item = OneLineListItem(text=f"{len(self.parcel_addresses)}. {addr}")
            self.list_view.add_widget(item)
            self.address_input.text = "" # Clear box

    def open_google_maps(self, obj):
        if not self.parcel_addresses:
            return
            
        # Google Maps URL banana (Magic Trick)
        base_url = "https://www.google.com/maps/dir/"
        
        # Saare address ko URL safe format mein badalna
        formatted_addresses = [quote(addr) for addr in self.parcel_addresses]
        
        # "Your Location" se shuru karke saare stops jodna
        full_url = base_url + "Current+Location/" + "/".join(formatted_addresses)
        
        # Browser/Map open karna
        webbrowser.open(full_url)

DeliveryApp().run()
