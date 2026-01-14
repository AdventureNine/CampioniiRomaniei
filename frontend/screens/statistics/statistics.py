from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class PaginaStatistici(MDScreen):
    def on_pre_enter(self, *args):
        app = MDApp.get_running_app()
        if not hasattr(app, 'service'):
            return

        stats = app.service.get_player_stats()

        if stats:
            # Nume Jucător
            self.ids.row_nume.valoare = str(stats["name"])

            # Credite
            self.ids.row_credite.valoare = str(stats["credits"])

            # Quiz-uri
            self.ids.row_jucate.valoare = str(stats["quizzes_played"])
            self.ids.row_rezolvate.valoare = str(stats["quizzes_solved"])

            # Timp mediu
            avg_time = stats.get('avg_play_time', 0.0)
            self.ids.row_timp.valoare = f"{avg_time:.1f} min"

            # Regiuni deblocate
            regions_state = stats.get("regions_state", {})
            nr_regiuni_deblocate = len(regions_state)
            self.ids.row_regiuni.valoare = f"{nr_regiuni_deblocate} / 5"

            # Cosmetice deținute
            cosmetics = stats.get("cosmetics_owned", [])
            nr_cosmetics = len(cosmetics)
            self.ids.row_cosmetici.valoare = str(nr_cosmetics)

            # Progres Total
            completion = stats.get("completion_percentage", 0.0)
            self.ids.row_progres.valoare = f"{completion}%"