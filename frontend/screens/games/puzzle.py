import random

from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, ColorProperty
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage

from frontend.components.common import FeedbackPopup
from frontend.utils.assets import image_path
from frontend.utils.colors import AppColors


class PuzzleTile(ButtonBehavior, RelativeLayout):
    original_index = NumericProperty(0)
    current_index = NumericProperty(0)
    is_empty = False


class PuzzleGameScreen(Screen):
    bg_image = StringProperty("")
    game_grid = ObjectProperty(None)

    header_color = ColorProperty(AppColors.PRIMARY)
    region_id = NumericProperty(0)
    primary_color = ColorProperty(AppColors.PRIMARY)

    rows = 3
    cols = 3
    tiles = []
    empty_index = 0

    def set_theme_color(self):
        colors_map = {
            1: AppColors.TRANSILVANIA,
            2: AppColors.MOLDOVA,
            3: AppColors.TARA_ROMANEASCA,
            4: AppColors.DOBROGEA,
            5: AppColors.BANAT
        }
        color = colors_map.get(self.region_id, AppColors.ACCENT)
        self.header_color = color

    def load_data(self, data, step_number):
        if self.game_grid:
            self.game_grid.clear_widgets()
        self.tiles = []
        self.empty_index = (self.rows * self.cols) - 1

        full_path = ""

        if 'puzzle' in data:
            minigame_entity = data['puzzle']
            raw_path = minigame_entity.get_image_path()

            if raw_path:
                full_path = raw_path
            else:
                print("Eroare: Entitatea Puzzle nu are cale setată.")
                return
        else:
            print("Eroare: Nu s-a găsit sursa imaginii pentru Puzzle.")
            return

        self.set_theme_color()

        try:
            texture = CoreImage(full_path).texture
        except Exception as e:
            print(f"Nu s-a putut încărca textura: {e}")
            return

        tile_w = texture.width / self.cols
        tile_h = texture.height / self.rows

        for i in range(self.rows * self.cols):
            row = i // self.cols
            col = i % self.cols

            tex_x = col * tile_w
            tex_y = (self.rows - 1 - row) * tile_h

            tile_texture = texture.get_region(tex_x, tex_y, tile_w, tile_h)

            tile = PuzzleTile()
            tile.original_index = i
            tile.current_index = i

            img = Image(texture=tile_texture, fit_mode="fill")
            img.size_hint = (1, 1)
            img.pos_hint = {'x': 0, 'y': 0}

            tile.add_widget(img)
            tile.bind(on_release=self.on_tile_click)

            if i == (self.rows * self.cols) - 1:
                tile.is_empty = True
                tile.opacity = 0
                self.empty_index = i

            self.tiles.append(tile)
            self.game_grid.add_widget(tile)

        self.shuffle_puzzle()

    def shuffle_puzzle(self):
        moves = 20
        last_moved = -1

        for _ in range(moves):
            neighbors = self.get_valid_moves(self.empty_index)
            if last_moved in neighbors and len(neighbors) > 1:
                neighbors.remove(last_moved)

            target = random.choice(neighbors)
            self.swap_tiles(self.empty_index, target)
            last_moved = self.empty_index
            self.empty_index = target

    def get_valid_moves(self, empty_idx):
        moves = []
        row = empty_idx // self.cols
        col = empty_idx % self.cols

        if row > 0: moves.append(empty_idx - self.cols)  # Sus
        if row < self.rows - 1: moves.append(empty_idx + self.cols)  # Jos
        if col > 0: moves.append(empty_idx - 1)  # Stânga
        if col < self.cols - 1: moves.append(empty_idx + 1)  # Dreapta

        return moves

    def on_tile_click(self, tile):
        if tile.is_empty: return

        idx = self.tiles.index(tile)
        if idx in self.get_valid_moves(self.empty_index):
            self.swap_tiles(self.empty_index, idx)
            self.empty_index = idx

            self.check_win()

    def swap_tiles(self, idx1, idx2):
        self.tiles[idx1], self.tiles[idx2] = self.tiles[idx2], self.tiles[idx1]

        self.game_grid.clear_widgets()
        for tile in self.tiles:
            self.game_grid.add_widget(tile)

    def check_win(self):
        for i, tile in enumerate(self.tiles):
            if tile.original_index != i:
                return False

        self.tiles[-1].opacity = 1

        popup = FeedbackPopup(
            type='success',
            title_text="Puzzle Complet!",
            message_text="Ai reconstituit imaginea!",
            button_text="Continuă"
        )
        popup.bind(on_dismiss=self.go_next)
        popup.open()
        return True

    def go_next(self, instance):
        app = App.get_running_app()
        dashboard = app.sm.get_screen('region_dashboard')
        dashboard.load_next_step()