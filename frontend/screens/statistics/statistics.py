from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class PaginaStatistici(MDScreen):
    def on_pre_enter(self, *args):
        app = MDApp.get_running_app()
        if not hasattr(app, 'service'):
            return

        stats = app.service.get_player_stats()

        if stats:
            # 1. Credite
            self.ids.row_credite.valoare = str(stats.get("credits", 0))

            # 2. Quiz-uri Jucate
            self.ids.row_jucate.valoare = str(stats.get("quizzes_played", 0))

            # 3. Quiz-uri Rezolvate
            self.ids.row_rezolvate.valoare = str(stats.get("quizzes_solved", 0))

            # 4. Timp mediu
            avg_time = stats.get('avg_play_time', 0.0)
            self.ids.row_timp.valoare = f"{avg_time:.1f} min"

            # 5. Quiz-uri Deblocate (Total nivele)
            regions_state = stats.get("regions_state", {})

            total_levels_unlocked = sum(regions_state.values())

            if total_levels_unlocked == 0:
                total_levels_unlocked = 5

            # Sunt 5 regiuni * 6 nivele = 30 nivele totale
            self.ids.row_regiuni.valoare = f"{total_levels_unlocked} / 30"

            # 6. Cosmetice deținute
            cosmetics = stats.get("cosmetics_owned", [])
            nr_cosmetics = len(cosmetics)
            self.ids.row_cosmetici.valoare = str(nr_cosmetics)

            # 7. Progres Total
            completion = (total_levels_unlocked / 30) * 100
            self.ids.row_progres.valoare = f"{completion:.1f}%"