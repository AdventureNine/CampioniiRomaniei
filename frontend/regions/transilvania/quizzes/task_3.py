from .task_base import TaskScreenBase
from frontend.regions.transilvania.colors import TASK_BG_COLORS

QUESTIONS = {
    'USOR': [
        ("Care este cel mai lung rau din Transilvania?", "Mures"),
        ("Ce rau trece prin orasul Cluj?", "Somes"),
        ("Unde curge raul Olt?", "Sud"),
        ("Lacul Sfanta Ana este un lac __.", "Vulcanic"),
        ("Raurile curg prin __.", "Vai"),
        ("Multe rauri se varsa in raul __.", "Mures"),
    ],
    'MEDIU': [
        ("Incotro face cot raul Olt?", "Sud"),
        ("Cum se numesc cele doua brate ale Somesului?", "Somesul Mare si Somesul Mic"),
        ("Cum s-a format Lacul Rosu?", "Prin alunecare de pamant"),
        ("O vale ingusta intre munti se numeste __.", "Cheie"),
        ("Raurile se aduna intr-un __ hidrografic.", "Bazin"),
        ("Valea este intre __.", "Munti"),
    ],
    'DIFICIL': [
        ("Ce rau a sapat Cheile Turzii?", "Hasdate"),
        ("In ce munti se afla Lacul Sfanta Ana?", "Carpatii Orientali"),
        ("Cum s-a format Lacul Rosu?", "Alunecare"),
        ("Vaile inguste se numesc __.", "Chei"),
        ("Raurile din Transilvania se varsa in __.", "Dunare"),
        ("Pe rauri se construiesc __.", "Hidrocentrale"),
    ]
}


class Task3Screen(TaskScreenBase):
    def __init__(self, **kwargs):
        super().__init__(QUESTIONS, TASK_BG_COLORS['task_3'], 3, name='task_3', **kwargs)
