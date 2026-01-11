import os

# aici vom inlocui cu path-ul din baza de date cand conectam cu backend-ul
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def image_path(filename):
    """
    Exemplu: image_path('menu/background.png')
    Returnează: C:/Users/.../CampioniiGeografiei/assets/images/menu/background.png
    """
    return os.path.join(BASE_DIR, 'frontend', 'assets', 'images', filename)

def font_path(filename):
    return os.path.join(BASE_DIR, 'frontend', 'assets', 'fonts', filename)

def sound_path(filename):
    return os.path.join(BASE_DIR, 'frontend', 'assets', 'sounds', filename)