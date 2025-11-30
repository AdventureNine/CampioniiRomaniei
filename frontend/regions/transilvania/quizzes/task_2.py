from .task_base import TaskScreenBase
from frontend.regions.transilvania.colors import TASK_BG_COLORS

QUESTIONS = {
    'USOR': [
        ("Ce fel de relief este in centrul Transilvaniei?", "Podis"),
        ("Cu ce culoare este colorat podisul pe harta?", "Galben"),
        ("Ce oras mare este in Transilvania?", "Cluj"),
        ("La Turda se scoate __ din pamant.", "Sare"),
        ("Pe dealuri oamenii planteaza __ fructiferi.", "Pomi"),
        ("Sibiu este un oras __.", "Vechi"),
    ],
    'MEDIU': [
        ("Ce oras a fost capitala Transilvaniei?", "Alba Iulia"),
        ("Intre ce rauri se afla Podisul Transilvaniei?", "Mures si Olt"),
        ("Langa ce munti este orasul Brasov?", "Carpati"),
        ("Pe dealuri cresc __ si vie.", "Pomi"),
        ("Pe dealuri sunt multe __.", "Sate"),
        ("Sibiu este in zona de __.", "Podis"),
    ],
    'DIFICIL': [
        ("Ce zona este in centrul tarii plina de sate si orase?", "Podisul Transilvaniei"),
        ("Pentru ce planta este cunoscut Podisul Tarnavelor?", "Vita-de-vie"),
        ("La ce fel de altitudine este orasul Predeal?", "Mare"),
        ("Podisul are multe culturi __.", "Agricole"),
        ("Dealurile sunt bune pentru cultivarea de __.", "Pomi"),
        ("In Transilvania sunt multe __ vechi.", "Cetati"),
    ]
}


class Task2Screen(TaskScreenBase):
    def __init__(self, **kwargs):
        super().__init__(QUESTIONS, TASK_BG_COLORS['task_2'], 2, name='task_2', **kwargs)
