import random
from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors import DragBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock
from kivy.app import App
from frontend.components.common import FeedbackPopup

PAIRS_DATA = [
    # Set 1
    {
        "Mihai Viteazul": "A realizat Unirea din 1600",
        "Alexandru Ioan Cuza": "A realizat Unirea Principatelor din 1859",
        "Ștefan cel Mare": "A fost domnitorul Moldovei în jurul anului 1500",
        "Basarab I": "Este întemeietorul Țării Românești",
        "Vlad Țepeș": "A atestat documentar Bucureștiul în 1459"
    },
    # Set 2
    {
        "Delta Dunării": "Este cea mai joasă unitate de relief",
        "Vârful Moldoveanu": "Este cel mai înalt vârf din România",
        "Lacul Sfânta Ana": "Este singurul lac vulcanic din România",
        "Munții Apuseni": "Sunt munți cunoscuți pentru multele peșteri",
        "Lacul Roșu": "S-a format prin alunecare de teren"
    },
    # Set 3
    {
        "Cluj-Napoca": "Este traversat de râul Someș",
        "București": "Este traversat de râul Dâmbovița",
        "Granița de Sud a României": "Este formată de fluviul Dunărea",
        "Bacău": "Este traversat de râul Bistrița",
        "Granița de Est a României": "Este formată de râul Prut"
    },
    # Set 4
    {
        "Podișul Târnavelor": "Este cunoscut pentru vița-de-vie",
        "Delta Dunării": "Ocupația principală este pescuitul",
        "Munții Carpați": "Au multe păduri de brad și molid",
        "Maramureș": "Este renumit pentru porțile din lemn",
        "Turda": "Locul de unde se extrage sarea"
    },
    # Set 5
    {
        "Timișoara": "Orașul unde a început Revoluția din 1989",
        "Dobrogea": "Are ieșire la Marea Neagră",
        "Crișana": "Se află lângă granița cu Ungaria",
        "Transilvania": "Are relief de podiș în centru",
        "Suceava": "A devenit capitală în timpul lui Petru I Mușat"
    },
    # Set 6
    {
        "Monumentul istoric de la Adamclisi": "Tropaeum Traiani",
        "Cartofii cresc cel mai bine": "În locuri răcoroase",
        "Cheile Bicazului": "S-au format prin eroziunea râului Bicaz",
        "Iași": "Orașul unde a fost înființată prima universitate modernă",
        "Cetatea Histria": "O cetate antică grecească din Dobrogea"
    }
]


# --- LOGICA WIDGET-URILOR ---

class DraggableAnswer(DragBehavior, Widget):
    text = StringProperty("")
    current_slot = ObjectProperty(None)
    app_ref = ObjectProperty(None)
    state = StringProperty('normal')

    # Pentru a ține minte unde era înainte de drag
    original_pos = (0, 0)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.state = 'down'
            self.original_pos = self.pos

            # Când începem să tragem, mutăm widget-ul temporar pe fereastra principală (root)
            # pentru a nu fi tăiat de limitele ScrollView-ului sau ale rândului
            if self.parent:
                self.parent.remove_widget(self)
                App.get_running_app().root.add_widget(self)
                self.center = touch.pos

            return super().on_touch_down(touch)
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if self.state == 'down':
            self.state = 'normal'

            # Căutăm ecranul jocului pentru a găsi sloturile
            app = App.get_running_app()
            # NOTĂ: Asigură-te că numele ecranului în main.py este 'pairs_game'
            game_screen = app.sm.get_screen('pairs_game')

            found_slot = False

            if game_screen:
                # Iterăm prin toate rândurile pentru a vedea dacă am dat drumul deasupra unui slot
                for row in game_screen.ids.rows_container.children:
                    slot = row.ids.slot
                    # Verificăm coliziunea
                    if slot.collide_point(*self.center):
                        self.move_to_slot(slot)
                        found_slot = True
                        break

            if not found_slot:
                # Dacă nu a nimerit niciun slot, se întoarce la slotul anterior
                self.move_to_slot(self.current_slot)

        return super().on_touch_up(touch)

    def move_to_slot(self, target_slot):
        """
        Mută acest răspuns într-un slot.
        Dacă slotul este ocupat, face schimb (swap) cu celălalt răspuns.
        """
        occupant = None
        if target_slot.children:
            occupant = target_slot.children[0]

        # Ne scoatem de pe părintele curent (root sau alt slot)
        if self.parent:
            self.parent.remove_widget(self)

        # LOGICA DE SCHIMB (SWAP)
        if occupant and occupant != self:
            # Scoatem ocupantul din slotul țintă
            target_slot.remove_widget(occupant)

            # Îl mutăm în slotul nostru vechi (dacă există)
            if self.current_slot:
                self.current_slot.add_widget(occupant)
                occupant.current_slot = self.current_slot
                # Resetăm poziția ocupantului
                occupant.pos = self.current_slot.pos
                occupant.size = self.current_slot.size

        # Ne adăugăm pe noi în slotul țintă
        target_slot.add_widget(self)
        self.current_slot = target_slot

        # Resetăm poziția și dimensiunea relativ la noul părinte
        self.pos = target_slot.pos
        self.size = target_slot.size


class AnswerSlot(Widget):
    pass


class GameRow(BoxLayout):
    question_text = StringProperty("")

    def __init__(self, question, **kwargs):
        super().__init__(**kwargs)
        self.question_text = question


class PairsGameScreen(Screen):
    current_data = {}  # Dicționarul curent {Întrebare: Răspuns Corect}

    def on_enter(self):
        # Se apelează automat când intrăm pe ecran
        self.start_new_game()

    def start_new_game(self):
        container = self.ids.rows_container
        container.clear_widgets()

        # 1. Alegem un set random direct din lista constantă PAIRS_DATA
        self.current_data = random.choice(PAIRS_DATA)

        questions = list(self.current_data.keys())
        correct_answers = list(self.current_data.values())

        # 2. Amestecăm răspunsurile pentru a fi afișate dezordonat
        shuffled_answers = correct_answers.copy()
        random.shuffle(shuffled_answers)

        # 3. Generăm rândurile în interfață
        for i, question in enumerate(questions):
            # Creăm rândul cu întrebarea fixă
            row = GameRow(question=question)
            container.add_widget(row)

            # Creăm răspunsul (care e amestecat, deci probabil nu corespunde întrebării din stânga)
            ans_text = shuffled_answers[i]
            ans_widget = DraggableAnswer(text=ans_text)

            # Îl punem în slotul din dreapta
            slot = row.ids.slot
            slot.add_widget(ans_widget)
            ans_widget.current_slot = slot

            # Un mic hack cu Clock pentru a ne asigura că poziția se actualizează corect după randare
            Clock.schedule_once(lambda dt, w=ans_widget, s=slot: setattr(w, 'pos', s.pos), 0.1)
            Clock.schedule_once(lambda dt, w=ans_widget, s=slot: setattr(w, 'size', s.size), 0.1)

    def check_win_condition(self):
        correct_count = 0
        total = len(self.current_data)
        rows = self.ids.rows_container.children

        # Verificăm fiecare rând
        for row in rows:
            question = row.question_text
            slot = row.ids.slot

            # Dacă există un răspuns în slot
            if slot.children:
                answer_widget = slot.children[0]
                given_answer = answer_widget.text
                correct_answer = self.current_data.get(question)

                if given_answer == correct_answer:
                    correct_count += 1

        # Afișăm Popup-ul de Feedback (folosind common.py)
        if correct_count == total:
            # SUCCES
            popup = FeedbackPopup(
                type='success',
                title_text="FELICITĂRI!",
                message_text=f"Ai asociat corect toate cele {total} perechi!",
                button_text="Continua"
            )
            # Când închide popup-ul, ne întoarcem la meniu (sau reîncepem)
            popup.bind(on_dismiss=lambda x: self.go_back())
            popup.open()

            # Actualizare scor (opțional)
            app = App.get_running_app()
            if hasattr(app, 'score'):
                app.score += 50
        else:
            # EȘEC
            popup = FeedbackPopup(
                type='fail',
                title_text="MAI ÎNCEARCĂ!",
                message_text=f"Ai nimerit doar {correct_count} din {total}. Nu renunța!",
                button_text="Încearcă din nou"
            )
            popup.open()

    def go_back(self):
        app = App.get_running_app()
        if hasattr(app, 'clouds'):
            app.clouds.change_screen('region_dashboard')
        else:
            app.sm.current = 'menu'