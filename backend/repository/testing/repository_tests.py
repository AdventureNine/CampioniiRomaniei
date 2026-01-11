import sqlite3
from backend.domain.entities.FillInStatement import FillInStatement
from backend.domain.entities.Player import Player
from backend.domain.entities.Question import Question
from backend.domain.entities.Quizz import Quizz
from backend.domain.utils.Difficulty import Difficulty
from backend.repository.FillInStatementRepository import FillInStatementRepository
from backend.repository.PlayerRepository import PlayerRepository
from backend.repository.QuestionRepository import QuestionRepository
from backend.repository.QuizzRepository import QuizzRepository
from backend.repository.QuizzTaskRepository import QuizzTaskRepository

def insert_questions(repoQuestions: QuestionRepository) -> None:
    repoQuestions.save(Question(-1,"Munții din jurul Transilvaniei se numesc...",["Carpați","Balcani","Alpi","Himalaya"]),1)
    # repoQuestions.save(Question(1,"Munții din jurul Transilvaniei se numesc...",["Carpați", "Balcani","Alpi", "Himalaya"]),1)
    repoQuestions.save(Question(-1,"Munții sunt colorați pe hartă cu culoarea...",["Maro", "Verde", "Albastru", "Galben"]),1)
    repoQuestions.save(Question(-1,"Munții din vestul Transilvaniei se numesc...",["Apuseni", "Meridionali", "Orientali", "Banatului"]),1)

    repoQuestions.save(Question(-1,"Ce fel de relief este în centrul Transilvaniei?",["Podiș", "Câmpie", "Delta", "Munte"]), 2)
    repoQuestions.save(Question(-1,"Ce oraș mare este în Transilvania?",["Cluj", "Iași", "Constanța", "Craiova"]), 2)
    repoQuestions.save(Question(-1,"La Turda se scoate din pământ...",["Sare", "Aur", "Cărbune", "Petrol"]), 2)

    repoQuestions.save(Question(-1,"Care este cel mai lung râu din Transilvania?",["Mureș", "Olt", "Siret", "Prut"]), 3)
    repoQuestions.save(Question(-1,"Ce râu trece prin orașul Cluj-Napoca?",["Someș", "Bega", "Jiu", "Argeș"]), 3)
    repoQuestions.save(Question(-1,"Lacul Sfânta Ana este un lac...",["Vulcanic", "Glaciar", "Sărat", "Artificial"]), 3)

    repoQuestions.save(Question(-1,"Ce se face din vița-de-vie?",["Vin", "Ulei", "Făină", "Zahăr"]), 4)
    repoQuestions.save(Question(-1,"Cartofii cresc în locuri...",["Răcoroase", "Secetoase", "Foarte calde", "Mlaștinoase"]), 4)
    repoQuestions.save(Question(-1,"Pentru ce plantă este cunoscut Podișul Târnavelor?",["Vița-de-vie", "Porumb", "Floarea soarelui", "Orez"]), 4)

    repoQuestions.save(Question(-1,"Care este cel mai înalt vârf din România?",["Moldoveanu", "Omu", "Negoiu", "Pietrosu"]),5)
    repoQuestions.save(Question(-1,"Cum s-a format Lacul Roșu?",["Alunecare de teren", "Vulcan", "Baraj", "Meteorit"]),5)
    repoQuestions.save(Question(-1,"Ce râu a săpat Cheile Turzii?",["Hășdate", "Arieș", "Ampoi", "Mureș"]),5)

    repoQuestions.save(Question(-1,"Lângă ce munți este orașul Brașov?",["Carpați", "Măcin", "Apuseni", "Rodnei"]),6)
    repoQuestions.save(Question(-1,"În ce munți se află Lacul Roșu?",["Orientali", "Meridionali", "Occidentali", "Banatului"]),6)
    repoQuestions.save(Question(-1,"În munții Apuseni sunt multe...",["Peșteri", "Vulcani", "Deșerturi", "Delte"]),6)

    repoQuestions.save(Question(-1,"Ce râu trece prin orașul Iași?",["Bahlui", "Siret", "Prut", "Bistrița"]),7)
    repoQuestions.save(Question(-1,"Cetatea de Scaun a Moldovei se află la...",["Suceava", "Iași", "Neamț", "Soroca"]),7)
    repoQuestions.save(Question(-1,"Ion Creangă s-a născut la...",["Humulești", "Ipotești", "Mircești", "Botoșani"]),7)

    repoQuestions.save(Question(-1,"Care este fluviul care formează granița de est a României?",["Prutul", "Dunărea", "Siretul", "Mureșul"]),8)
    repoQuestions.save(Question(-1,"Cum se numește fluviul care se varsă în Marea Neagră și trece prin sudul Moldovei?",["Dunărea", "Olt", "Argeș", "Tisa"]),8)
    repoQuestions.save(Question(-1,"Din ce regiune face parte muntele Ceahlău?",["Moldova", "Banat", "Dobrogea", "Transilvania"]),8)

    repoQuestions.save(Question(-1,"Cine a fost domnitorul Moldovei în jurul anului 1500?",["Ștefan cel Mare", "Mihai Viteazul", "Vlad Țepeș", "Mircea cel Bătrân"]), 9)
    repoQuestions.save(Question(-1,"Ce domnitor a mutat capitala la Suceava?",["Petru I Mușat", "Alexandru cel Bun", "Dragoș Vodă", "Ieremia Movilă"]), 9)
    repoQuestions.save(Question(-1,"În ce oraș din Moldova a fost înființată prima universitate modernă?",["Iași", "Suceava", "Bacău", "Galați"]), 9)

    repoQuestions.save(Question(-1,"Ce rol avea Cetatea Neamț în vremea lui Ștefan cel Mare?",["Apărare", "Vacanță", "Comerț", "Religios"]), 10)
    repoQuestions.save(Question(-1,"Ce fenomen a format Cheile Bicazului?",["Eroziunea apei", "Cutremur", "Vulcan", "Vânt"]), 10)
    repoQuestions.save(Question(-1,"Ce ramură economică e specifică Bucovinei?",["Prelucrarea lemnului", "Pescuitul", "Petrolul", "Mineritul"]), 10)

    repoQuestions.save(Question(-1,"Mănăstirea Putna a fost ctitorită de...",["Ștefan cel Mare", "Mircea cel Bătrân", "Petru Rareș", "Alexandru Lăpușneanu"]), 11)
    repoQuestions.save(Question(-1,"Ce scriitor celebru s-a născut la Ipotești?",["Mihai Eminescu", "Ion Creangă", "Vasile Alecsandri", "George Bacovia"]), 11)
    repoQuestions.save(Question(-1,"Moldova se află în partea de ... a României.",["Est", "Vest", "Sud", "Nord-Vest"]), 11)

    repoQuestions.save(Question(-1,"Ce lac de acumulare se află pe râul Bistrița?",["Izvorul Muntelui", "Vidraru", "Sfânta Ana", "Bâlea"]), 12)
    repoQuestions.save(Question(-1,"Câte cetăți de scaun a avut Moldova?",["Două (Suceava și Iași)", "Una", "Trei", "Niciuna"]), 12)
    repoQuestions.save(Question(-1,"„Perla Moldovei” este stațiunea...",["Slănic Moldova", "Vatra Dornei", "Sovata", "Sinaia"]), 12)

def insert_fillins(repoFillins: FillInStatementRepository) -> None:
    repoFillins.save(FillInStatement(-1,["Pe vârful munților crește doar ____."],["iarbă"]), 1)
    #repoFillins.save(FillInStatement(37,["Pe vârful munților crește doar ____."],["iarba"]), 1)
    repoFillins.save(FillInStatement(-1,["În munții Carpați trăiește animalul numit ____."],["urs"]), 1)

    repoFillins.save(FillInStatement(-1,["Orașul Sibiu este un oraș foarte ____."],["vechi"]), 2)
    repoFillins.save(FillInStatement(-1,["Ce oraș a fost capitala Transilvaniei?"],["alba iulia"]), 2)

    repoFillins.save(FillInStatement(-1,["Râurile curg prin ____."],["văi"]), 3)
    repoFillins.save(FillInStatement(-1,["Râul Olt curge spre punctul cardinal ____."],["sud"]), 3)

    repoFillins.save(FillInStatement(-1,["De la vite oamenii iau carne și ____."],["lapte"]), 4)
    repoFillins.save(FillInStatement(-1,["Vara, animalele pasc pe ____."],["pășuni"]), 4)

    repoFillins.save(FillInStatement(-1,["Văile înguste dintre munți se numesc ____."],["chei"]), 5)
    repoFillins.save(FillInStatement(-1,["Munții foarte înalți sunt colorați pe hartă cu maro ____."],["închis"]), 5)

    repoFillins.save(FillInStatement(-1,["Râurile din Transilvania se varsă până la urmă în fluviul ____."],["dunăre"]), 6)
    repoFillins.save(FillInStatement(-1,["În Transilvania sunt multe ____ ", " vechi construite pentru apărare."],["cetăți"]), 6)

    repoFillins.save(FillInStatement(-1,["Mănăstirea albastră din Bucovina se numește _______."],["voroneț"]), 7)
    repoFillins.save(FillInStatement(-1,["Capitala județului Iași este municipiul ____."],["iași"]), 7)

    repoFillins.save(FillInStatement(-1,["Râul important care trece prin Bacău se numește ____."],["bistrița"]), 8)
    repoFillins.save(FillInStatement(-1,["Cel mai înalt vârf din Carpații Orientali este Pietrosul ____."],["rodnei"]), 8)

    repoFillins.save(FillInStatement(-1,["Regiunea istorică din estul Carpaților se numește ____."],["moldova"]), 9)
    repoFillins.save(FillInStatement(-1,["Râul care trece pe lângă Cetatea Neamțului este ____."],["ozana"]), 9)

    repoFillins.save(FillInStatement(-1,["Unirea Principatelor (Moldova și Țara Românească) a avut loc în anul ____."],["1859"]), 10)
    repoFillins.save(FillInStatement(-1,["Vecinul de la est al Moldovei este Republica ____."],["moldova"]), 10)

    repoFillins.save(FillInStatement(-1,["Cetatea Soroca se află pe malul râului ____."],["nistru"]), 11)
    repoFillins.save(FillInStatement(-1,["Ștefan cel Mare a câștigat o mare bătălie la Podul ____."],["înalt"]), 11)

    repoFillins.save(FillInStatement(-1,["Bucovina este renumită pentru mănăstrile ____."],["pictate"]), 12)
    repoFillins.save(FillInStatement(-1,["Orașul Iași se află pe cele 7 ____."],["coline"]), 12)

def insert_quizzes(repoQuizzes: QuizzRepository) -> None:
    repoQuizzes.save(Quizz(-1,[],[],[],Difficulty[0]),1)
    # repoQuizzes.save(Quizz(1,[],[],[],Difficulty[0]),1)
    repoQuizzes.save(Quizz(-1,[],[],[],Difficulty[0]),1)
    repoQuizzes.save(Quizz(-1,[],[],[],Difficulty[1]),1)
    repoQuizzes.save(Quizz(-1,[],[],[],Difficulty[1]),1)
    repoQuizzes.save(Quizz(-1,[],[],[],Difficulty[2]),1)
    repoQuizzes.save(Quizz(-1,[],[],[],Difficulty[2]),1)
    repoQuizzes.save(Quizz(-1,[],[],[],Difficulty[0]),1)
    repoQuizzes.save(Quizz(-1,[],[],[],Difficulty[0]),1)
    repoQuizzes.save(Quizz(-1,[],[],[],Difficulty[1]),1)
    repoQuizzes.save(Quizz(-1,[],[],[],Difficulty[1]),1)
    repoQuizzes.save(Quizz(-1,[],[],[],Difficulty[2]),1)
    repoQuizzes.save(Quizz(-1,[],[],[],Difficulty[2]),1)

def test_repository() -> bool:
    con = sqlite3.connect("../../domain/data.db")

    repoPlayers = PlayerRepository(con)
    repoPlayers.delete(1)
    print(">--------------( Player deleted! )---------------<\n")
    con.cursor().execute("DELETE FROM answers where true")
    con.cursor().execute("DELETE FROM minigames where true")
    con.cursor().execute("DELETE FROM quizz_tasks where true")
    con.cursor().execute("DELETE FROM quizzes where true")
    con.cursor().execute("DELETE FROM sqlite_sequence WHERE name=?", ("answers",))
    con.cursor().execute("DELETE FROM sqlite_sequence WHERE name=?", ("minigames",))
    con.cursor().execute("DELETE FROM sqlite_sequence WHERE name=?", ("quizz_tasks",))
    con.cursor().execute("DELETE FROM sqlite_sequence WHERE name=?", ("quizzes",))
    con.commit()

    repoPlayers.save(Player(-1,"test"))
    print(repoPlayers.get())
    print(">--------------( Player inserted! )---------------<\n")

    # the update is functional
    # player = Player(1, "test")
    # player.set_regions_state({"Transilvania": 3, "Moldova": 1, "Țara Românească": 2, "Dobrogea": 1, "Banat": 1})
    # repoPlayers.save(player)
    # print(">--------------( Player updated! )---------------<\n")

    repoQuizzes = QuizzRepository(con)
    insert_quizzes(repoQuizzes)
    print(repoQuizzes.get_by_id(1))
    print(">--------------( Quizzes inserted! )---------------<\n")

    repoQuestions = QuestionRepository(con)
    insert_questions(repoQuestions)
    print(repoQuestions.get_by_id(1))
    print(">--------------( Questions inserted! )---------------<\n")

    repoFillins = FillInStatementRepository(con)
    insert_fillins(repoFillins)
    print(repoFillins.get_by_id(39))
    print(">--------------( Fill-ins inserted! )---------------<\n")

    repoQuizzTasks = QuizzTaskRepository(con)
    print(repoQuizzTasks.get_all()[10])
    print(f">--------------( {len(repoQuizzTasks.get_all())} quizz tasks! )---------------<\n")

    con.close()
    return True

def run_tests() -> None: # TODO: putem popula baza de date cu aceasta functie!
    print(">--------------( Start repository tests )---------------<\n")
    if test_repository(): print("\n>--------------( All tests passed! )---------------<")
    else: print("\n>--------------( Some tests failed! )---------------<")

run_tests()