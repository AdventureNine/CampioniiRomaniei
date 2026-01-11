from kivy.utils import get_color_from_hex

class AppColors:
    # --- Culori Interfață Generală ---
    PRIMARY = get_color_from_hex('#1565C0')    # Albastru închis (Header, Meniu)
    ACCENT = get_color_from_hex('#FF9800')     # Portocaliu (Butoane principale)
    BACKGROUND = get_color_from_hex('#E3F2FD') # Albastru deschis (Fundal ecrane)
    TEXT_PRIMARY = get_color_from_hex('#212121') # Negru/Gri închis (Text)
    WHITE = get_color_from_hex('#FFFFFF')

    # --- Culori Feedback ---
    SUCCESS = get_color_from_hex('#4CAF50')    # Verde (Răspuns corect)
    ERROR = get_color_from_hex('#F44336')      # Roșu (Răspuns greșit)
    INFO = get_color_from_hex('#2196F3')       # Albastru (Info)

    # --- Culori Specifice Regiunilor ---
    # Folosite pentru butoanele de pe hartă sau tematica paginii
    TRANSILVANIA = get_color_from_hex('#795548') # Maro (Munți)
    MOLDOVA = get_color_from_hex('#4CAF50')      # Verde (Dealuri)
    TARA_ROMANEASCA = get_color_from_hex('#FFC107') # Galben (Câmpie)
    DOBROGEA = get_color_from_hex('#03A9F4')     # Albastru (Mare)
    BANAT = get_color_from_hex('#009688')        # Turcoaz/Verde închis