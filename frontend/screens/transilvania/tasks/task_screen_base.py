from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty, ListProperty

from frontend.regions.transilvania.tasks.task_logic import TaskLogic
from frontend.utils.popup_helper import create_simple_popup, create_answer_popup


class TaskScreenBase(Screen):
    # Proprietati
    timer = NumericProperty(180)
    question = StringProperty('')
    difficulty = StringProperty('')
    progress = StringProperty('1/5')
    bg_color = ListProperty([1, 1, 1, 1])

    def __init__(self, questions, bg_color, task_number, name=None, **kwargs):
        if name:
            kwargs['name'] = name
        super().__init__(**kwargs)
        self.bg_color = bg_color
        self.logic = TaskLogic(questions, task_number)
        self.timer_event = None
        self.answer_checked = False

    # Lifecycle
    def on_pre_enter(self):
        # Reseteaza task-ul si porneste timer-ul
        self.logic.reset_task()
        self.timer = 180
        if self.timer_event:
            self.timer_event.cancel()
        self.setup_question()
        self.timer_event = Clock.schedule_interval(self.update_timer, 1)

    # Setup intrebare
    def setup_question(self):
        # Configureaza intrebarea curenta
        q_data = self.logic.get_current_question()
        if not q_data:
            return

        self.difficulty = q_data['difficulty']
        self.question = q_data['question']
        self.progress = self.logic.get_progress()
        self.answer_checked = False

        # Creaza input pentru raspuns
        answer_container = self.ids.answer_container
        answer_container.clear_widgets()

        text_input = TextInput(
            multiline=False,
            font_size='22sp',
            size_hint=(1, None),
            height=70,
            hint_text='Introdu raspunsul...'
        )
        text_input.bind(on_text_validate=self.on_submit_answer)
        answer_container.add_widget(text_input)

        # Buton submit
        submit_btn = Button(
            text='Trimite Raspuns',
            size_hint=(1, None),
            height=60,
            font_size='20sp',
            background_color=(0.2, 0.5, 0.8, 1),
            color=(1, 1, 1, 1)
        )
        submit_btn.bind(on_press=self.on_submit_answer)
        answer_container.add_widget(submit_btn)

        # Actualizeaza butoanele de navigare
        self.ids.next_btn.disabled = True
        is_last = not self.logic.has_more_questions()
        self.ids.finish_btn.disabled = not is_last

    # Gestionare raspuns
    def on_submit_answer(self, instance):
        # Verifica raspunsul utilizatorului
        if self.answer_checked:
            return

        # Gaseste raspunsul din TextInput
        answer_container = self.ids.answer_container
        user_answer = None
        for child in answer_container.children:
            if isinstance(child, TextInput):
                user_answer = child.text
                break

        # Valideaza raspunsul
        if not user_answer or not user_answer.strip():
            popup = create_simple_popup(
                title="Raspuns Lipsa",
                message="Te rog introdu un raspuns!",
                button_text='OK'
            )
            popup.open()
            return

        # Verifica corectitudinea
        is_correct = self.logic.check_answer(user_answer)
        self.answer_checked = True

        if is_correct:
            self.show_correct_answer_popup()
        else:
            self.show_wrong_answer_popup()

    def show_correct_answer_popup(self):
        # Afiseaza popup pentru raspuns corect
        def on_close():
            self.ids.next_btn.disabled = False
            if not self.logic.has_more_questions():
                self.ids.finish_btn.disabled = False

        popup = create_answer_popup(
            is_correct=True,
            on_close=on_close
        )
        popup.open()

    def show_wrong_answer_popup(self):
        # Afiseaza popup pentru raspuns gresit
        def on_close():
            self.answer_checked = False

        popup = create_answer_popup(
            is_correct=False,
            on_close=on_close
        )
        popup.open()

    # Navigare intrebari
    def next_question(self):
        # Trece la urmatoarea intrebare
        self.logic.next_question()
        if self.logic.has_more_questions():
            self.setup_question()
        else:
            self.ids.next_btn.disabled = True
            self.ids.finish_btn.disabled = False

    # Timer
    def update_timer(self, dt):
        # Actualizeaza timer-ul
        self.timer -= 1
        if self.timer <= 0:
            self.time_up()

    def time_up(self):
        # Opreste task-ul cand expira timpul
        if self.timer_event:
            self.timer_event.cancel()
        popup = create_simple_popup(
            title="Timp expirat!",
            message="Ai ramas fara timp. Incearca din nou!",
            button_text='OK',
            on_close=lambda: self.quit_task()
        )
        popup.open()

    # Finalizare task
    def finish_task(self):
        # Finalizeaza task-ul si deblocheaza urmatorul
        if self.timer_event:
            self.timer_event.cancel()

        if self.logic.is_task_complete():
            prev_screen = self.manager.get_screen("transilvania")

            if self.logic.is_final_task():
                prev_screen.show_completion_popup()
            else:
                prev_screen.unlock_next_task(self.logic.task_number)

            self.manager.current = "transilvania"
        else:
            popup = create_simple_popup(
                title="Task incomplet",
                message="Trebuie sa raspunzi corect la toate intrebarile!",
                button_text='OK'
            )
            popup.open()

    def quit_task(self):
        # Paraseste task-ul si revine la ecranul principal
        if self.timer_event:
            self.timer_event.cancel()
        self.manager.current = "transilvania"