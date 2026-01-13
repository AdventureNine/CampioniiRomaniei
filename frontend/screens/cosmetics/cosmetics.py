import os
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty, StringProperty, ObjectProperty
from kivy.clock import Clock

# Importă datele (asigură-te că fișierul există în backend/domain/utils/)
from backend.domain.utils.cosmetics_data import COSMETICS_STORE
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
        # Folosim Clock pentru a ne asigura că layout-ul este gata
        Clock.schedule_once(self.refresh_store, 0.1)

    def refresh_store(self, dt=None):
        if 'cosmetics_grid' not in self.ids:
            return

        grid = self.ids.cosmetics_grid
        grid.clear_widgets()

        app = App.get_running_app()
        # Verificăm dacă player-ul există în App (trebuie să îl ai în DidacticApp)
        player = getattr(app, 'player', None)

        purchased_ids = []
        current_equipped = ""

        if player:
            purchased_ids = player.get_cosmetics_purchased()
            current_equipped = player.get_cosmetic()
        else:
            print("AVERTISMENT: Obiectul 'player' nu a fost găsit în App. Se afișează modul previzualizare.")

        for item in COSMETICS_STORE:
            card = CosmeticCard()
            card.item_id = item['id']
            card.item_name = item['name']
            card.price = str(item['price'])
            card.is_owned = item['id'] in purchased_ids or item['price'] == 0

            # Construim calea imaginii
            img_filename = f"cosmetics/{item['image']}"
            try:
                card.source = image_path(img_filename)
            except:
                card.source = image_path("default.png")

            # Verificăm dacă este echipat
            target_path = f"backend/domain/assets/images/cosmetics/{item['image']}"
            card.is_equipped = (current_equipped == target_path)

            grid.add_widget(card)

    def handle_action(self, card):
        app = App.get_running_app()
        player = getattr(app, 'player', None)

        if not player:
            print("Eroare critică: Jucătorul nu a fost încărcat în App!")
            return

        item_data = next(i for i in COSMETICS_STORE if i['id'] == card.item_id)

        if not card.is_owned:
            # Folosim app.score pentru a verifica balanța curentă
            if app.score >= item_data['price']:
                # 1. Scădem din balanța vizuală
                app.score -= item_data['price']

                # 2. Actualizăm obiectul Player
                player.set_credits(app.score)
                new_list = player.get_cosmetics_purchased()
                new_list.append(card.item_id)
                player.set_cosmetics_purchased(new_list)

                # 3. Salvăm în baza de date
                app.player_repo.save(player)

                self.refresh_store()
                print(f"Ai cumpărat {item_data['name']}!")
            else:
                print("Nu ai destule credite!")
        else:
            img_path = f"backend/domain/assets/images/cosmetics/{item_data['image']}"
            player.set_cosmetic(img_path)
            # app.player_repo.save(player)
            self.refresh_store()