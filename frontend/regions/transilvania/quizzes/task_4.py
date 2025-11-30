from .task_base import TaskScreenBase
from frontend.regions.transilvania.colors import TASK_BG_COLORS

QUESTIONS = {
    'USOR': [
        ("Ce cereale cresc pe camp?", "Porumb / Grau"),
        ("Ce animale pasc pe dealuri?", "Oi / Vaci"),
        ("Ce se face din vita-de-vie?", "Vin"),
        ("Pe campuri cresc __.", "Plante"),
        ("Pe dealuri se cultiva __.", "Vie"),
        ("Oamenii cresc animale si __.", "Plante"),
    ],
    'MEDIU': [
        ("Ce cereale se cultiva pe camp?", "Grau si Porumb"),
        ("Unde pasc animalele vara?", "Pe pasuni"),
        ("Cum sunt iernile in Transilvania?", "Reci"),
        ("Pe dealuri cresc bine __.", "Pomii"),
        ("De la vite luam __ si carne.", "Lapte"),
        ("Cartofii cresc in locuri __.", "Racoroase"),
    ],
    'DIFICIL': [
        ("Pentru ce este bun Podisul Tarnavelor?", "Vita-de-vie"),
        ("Ce clima are Transilvania?", "Temperata"),
        ("Ce fel de plante sunt cartofii si cerealele?", "Agricole"),
        ("Vita-de-vie creste pe dealuri __.", "Insorite"),
        ("In podisuri se cresc multe __.", "Animale"),
        ("In Transilvania se cresc vite, porci si __.", "Pasari"),
    ]
}


class Task4Screen(TaskScreenBase):
    def __init__(self, **kwargs):
        super().__init__(QUESTIONS, TASK_BG_COLORS['task_4'], 4, name='task_4', **kwargs)
