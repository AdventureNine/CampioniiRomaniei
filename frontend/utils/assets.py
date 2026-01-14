import os
import unicodedata

# aici vom inlocui cu path-ul din baza de date cand conectam cu backend-ul
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def image_path(filename):
    """
    Exemplu: image_path('menu/background.png')
    Returnează: C:/Users/.../CampioniiGeografiei/assets/images/menu/background.png
    """
    filename = filename.replace('/', os.sep)
    return os.path.join(BASE_DIR, 'backend', 'domain', 'assets', 'images', filename)

def font_path(filename):
    filename = filename.replace('/', os.sep)
    return os.path.join(BASE_DIR, 'backend', 'domain', 'assets', 'fonts', filename)

def sound_path(filename):
    filename = filename.replace('/', os.sep)
    return os.path.join(BASE_DIR, 'backend', 'domain', 'assets', 'sounds', filename)

def remove_diacritics(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')