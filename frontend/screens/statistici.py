from kivymd.uix.screen import MDScreen

from backend.domain.entities.Player import Player

# MOCK DATA
player_test = Player(1, "Campionul")
player_test.set_quizzes_played(15)
player_test.set_quizzes_solved(12)
player_test.set_avg_play_time(4.5)
player_test.set_completion_percentage(35.0)
player_test.set_regions_unlocked(["Transilvania", "Moldova"])


class PaginaStatistici(MDScreen):
    def on_pre_enter(self, *args):
        curent_player = player_test

        stats = curent_player.get_statistics()

        self.ids.row_nume.valoare = str(curent_player.get_name())
        self.ids.row_credite.valoare = str(curent_player.get_credits())

        self.ids.row_jucate.valoare = str(stats["quizzes_played"])
        self.ids.row_rezolvate.valoare = str(stats["quizzes_solved"])
        self.ids.row_timp.valoare = f"{stats['avg_play_time']:.1f} min"

        nr_regiuni = len(stats["regions_unlocked"])
        self.ids.row_regiuni.valoare = f"{nr_regiuni}"

        self.ids.row_progres.valoare = f"{stats['completion_percentage']}%"