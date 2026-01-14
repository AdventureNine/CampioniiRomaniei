import os
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty, StringProperty, ObjectProperty
from kivy.clock import Clock

from frontend.utils.assets import image_path


class CosmeticCard(BoxLayout):
    item_id = StringProperty("")
    item_name = StringProperty("")
    price = StringProperty("0")
    source = StringProperty("")
    is_owned = BooleanProperty(False)
    is_equipped = BooleanProperty(False)


class CosmeticsScreen(Screen):
    def on_pre_enter(self):
        Clock.schedule_once(self.refresh_store, 0.1)

    def refresh_store(self, dt=None):
        if 'cosmetics_grid' not in self.ids:
            return

        grid = self.ids.cosmetics_grid
        grid.clear_widgets()

        app = App.get_running_app()
        # Preluăm datele jucătorului prin Service
        player_stats = app.service.get_player_stats()

        if not player_stats:
            print("Eroare: Nu s-au putut prelua statisticile jucătorului.")
            return

        purchased_paths = player_stats["cosmetics_owned"]
        current_equipped = player_stats["equipped_cosmetic"]

        base_path = image_path("cosmetics")

        if not os.path.exists(base_path):
            print(f"Eroare: Calea {base_path} nu există!")
            return

        cosmetic_files = [f for f in os.listdir(base_path) if f.endswith('.png')]

        for filename in cosmetic_files:
            item_id = filename
            display_name = filename.replace('.png', '').capitalize()

            # Logică preț: Ken e 500, restul 300
            item_price = 500 if display_name.lower() == "ken" else 300
            if filename == "default.png":
                item_price = 0

            # Calea completă folosită pentru identificare în Service/DB
            full_path = f"backend/domain/assets/images/cosmetics/{filename}"

            card = CosmeticCard()
            card.item_id = item_id  # Păstrăm numele fișierului ca ID intern al cardului
            card.item_name = display_name
            card.price = str(item_price)
            card.source = os.path.join(base_path, filename)

            # Verificăm proprietatea folosind lista de căi din Service
            card.is_owned = full_path in purchased_paths or item_price == 0
            card.is_equipped = (current_equipped == full_path)

            grid.add_widget(card)

    def handle_action(self, card):
        app = App.get_running_app()
        # Construim calea formatată pentru Service
        full_path = f"backend/domain/assets/images/cosmetics/{card.item_id}"
        item_price = int(card.price)

        if not card.is_owned:
            # Utilizăm Service pentru achiziție
            if app.service.purchase_cosmetic(full_path, item_price):
                # Actualizăm scorul vizual în App (care este legat de UI în main.py)
                app.score = app.service.get_player().get_credits()
                self.refresh_store()
            else:
                print("Achiziție eșuată: Credite insuficiente sau obiect deja deținut.")
        else:
            # Utilizăm Service pentru echipare
            if app.service.equip_cosmetic(full_path):
                self.refresh_store()
            else:
                print("Echipare eșuată: Obiectul nu este deținut.")