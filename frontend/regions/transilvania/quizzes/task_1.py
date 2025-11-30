from .task_base import TaskScreenBase
from frontend.regions.transilvania.colors import TASK_BG_COLORS

QUESTIONS = {
    'USOR': [
        ("Muntii din jurul Transilvaniei se numesc ?", "Carpati"),
        ("Muntii sunt colorati pe harta cu culoarea ?", "Maro"),
        ("Muntii din vestul Transilvaniei se numesc ?", "Apuseni"),
        ("In Carpati cresc multe __ si brazi.", "Paduri"),
        ("Pe varful muntilor creste doar __.", "Iarba"),
        ("In muntii Carpati traieste __.", "Ursul"),
    ],
    'MEDIU': [
        ("Care sunt cei mai inalti munti din jurul Transilvaniei?", "Carpatii Meridionali"),
        ("In ce munti se afla Lacul Rosu?", "Carpatii Orientali"),
        ("Ce animal mare traieste in padurile de munte?", "Ursul"),
        ("In Muntii Apuseni sunt multe __.", "Pesteri"),
        ("Pe munti iarna cade multa __.", "Zapada"),
        ("In Carpati cresc __ de brad si molid.", "Paduri"),
    ],
    'DIFICIL': [
        ("Care este cel mai inalt varf din Romania?", "Varful Moldoveanu"),
        ("In ce munti sunt lacuri glaciare?", "Carpatii Meridionali"),
        ("De ce sunt modelati Muntii inafara de vant?", "Apa"),
        ("Muntii inalti sunt colorati cu maro __.", "Inchis"),
        ("Muntii Retezat au multe __ la altitudine mare.", "Lacuri"),
        ("Stancile din munti sunt taiate de __.", "Chei"),
    ]
}


class Task1Screen(TaskScreenBase):
    def __init__(self, **kwargs):
        super().__init__(QUESTIONS, TASK_BG_COLORS['task_1'], 1, name='task_1', **kwargs)
