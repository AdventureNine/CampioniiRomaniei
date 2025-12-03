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

