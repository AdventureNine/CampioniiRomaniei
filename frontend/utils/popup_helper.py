from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


def create_simple_popup(title, message, button_text='OK', on_close=None, size_hint=(0.6, 0.3)):
    content = BoxLayout(orientation='vertical', padding=10, spacing=10)
    content.add_widget(Label(text=message, font_size="20sp"))

    popup = Popup(
        title=title,
        content=content,
        size_hint=size_hint
    )

    close_btn = Button(text=button_text, size_hint=(1, 0.3))

    def close_handler(instance):
        popup.dismiss()
        if on_close:
            on_close()

    close_btn.bind(on_press=close_handler)
    content.add_widget(close_btn)

    return popup


def create_completion_popup(message, button_text="Înapoi la regiuni", on_close=None, size_hint=(0.55, 0.55)):
    content = BoxLayout(orientation='vertical', padding=20, spacing=20)

    label = Label(
        text=message,
        font_size="26sp",
        halign="center",
        valign="middle"
    )

    close_btn = Button(
        text=button_text,
        size_hint=(1, 0.4),
        font_size="20sp",
        bold=True
    )

    content.add_widget(label)
    content.add_widget(close_btn)

    popup = Popup(
        title="Misiune Finalizată",
        content=content,
        size_hint=size_hint,
        auto_dismiss=False
    )

    def close_handler(instance):
        popup.dismiss()
        if on_close:
            on_close()

    close_btn.bind(on_press=close_handler)

    return popup


def create_answer_popup(is_correct, on_close=None):
    content = BoxLayout(orientation='vertical', padding=30, spacing=20)

    # Mesaj si culori
    if is_correct:
        title = "Corect!"
        message = "Bravo!\nRaspuns corect!"
        btn_color = (0.2, 0.7, 0.2, 1)
        btn_text = "Continua"
        title_color = (0.2, 0.7, 0.2, 1)
    else:
        title = "Gresit"
        message = "Mai incearca o data!"
        btn_color = (0.8, 0.2, 0.2, 1)
        btn_text = "OK"
        title_color = (0.8, 0.2, 0.2, 1)

    # Titlu mare
    title_label = Label(
        text=title,
        font_size="60sp",
        bold=True,
        size_hint=(1, 0.4),
        color=title_color
    )

    # Mesaj
    msg_label = Label(
        text=message,
        font_size="24sp",
        size_hint=(1, 0.3),
        halign="center",
        valign="middle"
    )

    # Buton
    btn = Button(
        text=btn_text,
        size_hint=(1, 0.3),
        font_size="20sp",
        bold=True,
        background_color=btn_color,
        color=(1, 1, 1, 1)
    )

    content.add_widget(title_label)
    content.add_widget(msg_label)
    content.add_widget(btn)

    popup = Popup(
        title="",
        content=content,
        size_hint=(0.5, 0.45),
        auto_dismiss=False,
        separator_height=0
    )

    def close_handler(instance):
        popup.dismiss()
        if on_close:
            on_close()

    btn.bind(on_press=close_handler)

    return popup