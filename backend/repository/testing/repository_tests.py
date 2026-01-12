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

    repoQuestions.save(Question(-1,"Cine este considerat întemeietorul Țării Românești?","Basarab I, Mircea cel Bătrân, Vlad Țepeș, Mihai Viteazul".split(", ")),13)
    repoQuestions.save(Question(-1,"Care este cea mai joasă formă de relief din zonă?","Câmpia Română, Podișul Getic, Subcarpații, Munții Bucegi".split(", ")),13)
    repoQuestions.save(Question(-1,"Ce râu traversează Bucureștiul?","Dâmbovița, Dunărea, Argeș, Olt".split(", ")),13)

    repoQuestions.save(Question(-1,"Ce domnitor a luptat la Rovine în 1395?","Mircea cel Bătrân, Ștefan cel Mare, Vlad Țepeș, Cuza".split(", ")),14)
    repoQuestions.save(Question(-1,"În timpul cui a fost atestat documentar Bucureștiul (1459)?","Vlad Țepeș, Basarab I, Mihai Viteazul, Matei Basarab".split(", ")),14)
    repoQuestions.save(Question(-1,"Ce mare unire a realizat Mihai Viteazul în 1600?","Unirea celor 3 țări, Mica Unire, Unirea cu Dobrogea, Unirea cu Banatul".split(", ")),14)

    repoQuestions.save(Question(-1,"Ce resurse se extrag din Podișul Getic?","Petrol și Gaze, Aur și Argint, Uraniu, Diamante".split(", ")),15)
    repoQuestions.save(Question(-1,"De ce s-a dezvoltat agricultura în Câmpia Română?","Soluri fertile, Multe păduri, Multe dealuri, Climă rece".split(", ")),15)
    repoQuestions.save(Question(-1,"Unde se află Vârful Omu?","Munții Bucegi, Munții Făgăraș, Munții Retezat, Munții Apuseni".split(", ")),15)

    repoQuestions.save(Question(-1,"Ce reformă importantă a făcut Cuza?","Legea învățământului, A construit metroul, A fondat Bucureștiul, A cucerit Turcia".split(", ")),16)
    repoQuestions.save(Question(-1,"De ce este Bucureștiul un nod de comunicație?","Are multe legături rutiere și feroviare, Are port la mare, Este la munte, Nu este nod".split(", ")),16)
    repoQuestions.save(Question(-1,"Curtea de Argeș este cunoscută pentru...","Mănăstirea Meșterului Manole, Turnul Chindiei, Podul lui Saligny, Castelul Peleș".split(", ")),16)

    repoQuestions.save(Question(-1,"Unde se află \"Coloana Infinitului\"?","Târgu Jiu, Craiova, Pitești, Ploiești".split(", ")),17)
    repoQuestions.save(Question(-1,"Barajul Vidraru se află pe râul...","Argeș, Olt, Dâmbovița, Ialomița".split(", ")),17)
    repoQuestions.save(Question(-1,"Cine a sculptat \"Poarta Sărutului\"?","Brâncuși, Grigorescu, Enescu, Tonitza".split(", ")),17)

    repoQuestions.save(Question(-1,"În ce an a avut loc Bătălia de la Posada?","1330, 1475, 1600, 1859".split(", ")),18)
    repoQuestions.save(Question(-1,"Care este principala bogăție a solului în zona Ploiești?","Petrol, Aur, Fier, Cupru".split(", ")),18)
    repoQuestions.save(Question(-1,"Câmpia Română este...","Grânarul țării, Zona minieră, Zona muntoasă, Delta".split(", ")),18)

    repoQuestions.save(Question(-1,"Care este cea mai joasă unitate de relief din România?","Delta Dunării, Câmpia de Vest, Podișul Getic, Lunca Siretului".split(", ")),19)
    repoQuestions.save(Question(-1,"Ce mare mărginește Dobrogea la est?","Marea Neagră, Marea Mediterană, Marea Roșie, Marea Caspică".split(", ")),19)
    repoQuestions.save(Question(-1,"Care sunt brațele Dunării?","\"Chilia, Sulina, Sf. Gheorghe\"; \"Olt, Mureș, Siret\"; \"Borcea, Măcin, Vâlciu\"; \"Niciunul\"".split("; ")),19)

    repoQuestions.save(Question(-1,"Cine este considerat întemeietorul statului medieval Dobrogea?","Dobrotici, Mircea cel Bătrân, Burebista, Decebal".split(", ")),20)
    repoQuestions.save(Question(-1,"Numiți o colonie grecească antică din Dobrogea.","Histria, Sarmizegetusa, Apulum, Potaissa".split(", ")),20)
    repoQuestions.save(Question(-1,"Cărui imperiu a fost cedată Dobrogea în 1417?","Imperiul Otoman, Imperiul Roman, Imperiul Austro-Ungar, Imperiul Rus".split(", ")),20)

    repoQuestions.save(Question(-1,"Ce popor minoritar a influențat Dobrogea?","Turcii/Tătarii, Ungurii, Sârbii, Polonezii".split(", ")),21)
    repoQuestions.save(Question(-1,"În ce an a revenit Dobrogea la România (Războiul de Independență)?","1878, 1918, 1600, 1417".split(", ")),21)
    repoQuestions.save(Question(-1,"Ce tip de vegetație este specific Podișului Dobrogei?","Stepa, Pădurea de brad, Tundra, Savana".split(", ")),21)

    repoQuestions.save(Question(-1,"De ce este Delta Dunării rezervație naturală?","Pentru biodiversitate (păsări, pești); Pentru petrol; Pentru industrie; Pentru agricultură".split("; ")),22)
    repoQuestions.save(Question(-1,"Care sunt cei mai vechi munți din România, aflați în Dobrogea?","Munții Măcinului, Munții Bucegi, Munții Făgăraș, Munții Retezat".split(", ")),22)
    repoQuestions.save(Question(-1,"Podul de la Cernavodă a fost construit de...","Anghel Saligny, Henri Coandă, Ana Aslan, Aurel Vlaicu".split(", ")),22)

    repoQuestions.save(Question(-1,"Care braț al Dunării este cel mai scurt și folosit pentru navigație?","Sulina, Chilia, Sf. Gheorghe, Peța".split(", ")),23)
    repoQuestions.save(Question(-1,"Portul principal al României la Marea Neagră este...","Constanța, Mangalia, Tulcea, Sulina".split(", ")),23)
    repoQuestions.save(Question(-1,"Lacul Razim este un lac...","Lagună (fost golf), Vulcanic, Glaciar, De acumulare".split(", ")),23)

    repoQuestions.save(Question(-1,"Peștera Sfântului Andrei se află în...","Dobrogea, Moldova, Banat, Oltenia".split(", ")),24)
    repoQuestions.save(Question(-1,"Care braț al Dunării transportă cea mai mare cantitate de apă?","Chilia, Sulina, Sf. Gheorghe, Niciunul".split(", ")),24)
    repoQuestions.save(Question(-1,"Dobrogea este o zonă cu climă...","Secetoasă și caldă, Umedă și rece, Polară, Tropicală".split(", ")),24)

    repoQuestions.save(Question(-1,"În ce oraș a început Revoluția din 1989?","Timișoara, București, Cluj, Iași".split(", ")),25)
    repoQuestions.save(Question(-1,"Capitala județului Timiș este...","Timișoara, Arad, Lugoj, Reșița".split(", ")),25)
    repoQuestions.save(Question(-1,"Banatul se află în partea de ... a țării.","Sud-Vest, Est, Nord, Sud-Est".split(", ")),25)

    repoQuestions.save(Question(-1,"Care este cel mai important oraș din Crișana?","Oradea, Satu Mare, Zalău, Baia Mare".split(", ")),26)
    repoQuestions.save(Question(-1,"Crișana se învecinează la vest cu...","Ungaria, Ucraina, Serbia, Bulgaria".split(", ")),26)
    repoQuestions.save(Question(-1,"De câte râuri \"Criș\" este străbătută Crișana?","Trei (Alb, Negru, Repede); Unul; Două; Patru".split("; ")),26)

    repoQuestions.save(Question(-1,"Maramureșul este faimos pentru...","Porțile din lemn, Castele de nisip, Zgârie-nori, Podgorii".split(", ")),27)
    repoQuestions.save(Question(-1,"Ce lanț muntos se află în Maramureș?","Carpații Maramureșului și Bucovinei, Munții Banatului, Făgăraș, Bucegi".split(", ")),27)
    repoQuestions.save(Question(-1,"Unde este situat Maramureșul?","Nordul României, Sudul României, Estul României, Vestul României".split(", ")),27)

    repoQuestions.save(Question(-1,"Ce resurse importante se găseau în Munții Apuseni (zona auriferă)?","Aur și Argint, Sare, Petrol, Cărbune".split(", ")),28)
    repoQuestions.save(Question(-1,"Ce au trimis provinciile (Crișana, Maramureș) la Alba Iulia în 1918?","Delegați pentru Unire, Soldați, Bani, Mâncare".split(", ")),28)
    repoQuestions.save(Question(-1,"Memorialul Victimelor Comunismului se află la...","Sighetu Marmației, Baia Mare, Satu Mare, Arad".split(", ")),28)

    repoQuestions.save(Question(-1,"Castelul Corvinilor (Huniade) este aproape de Banat, în...","Hunedoara, Timișoara, Arad, Deva".split(", ")),29)
    repoQuestions.save(Question(-1,"Cascada Bigăr se află în regiunea...","Banat, Dobrogea, Moldova, Muntenia".split(", ")),29)
    repoQuestions.save(Question(-1,"Cetatea Aradului este construită în stil...","Vauban (stea), Gotic, Modern, Dacic".split(", ")),29)

    repoQuestions.save(Question(-1,"Fluviul Dunărea intră în țară prin regiunea...","Banat (Baziaș), Dobrogea, Moldova, Crișana".split(", ")),30)
    repoQuestions.save(Question(-1,"Bisericile de lemn din Maramureș sunt în patrimoniul...","UNESCO, NATO, UE, ONU".split(", ")),30)
    repoQuestions.save(Question(-1,"Care este un oraș important din județul Arad?","Lipova, Mangalia, Făgăraș, Sighișoara".split(", ")),30)

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

    repoFillins.save(FillInStatement(-1,["Fluviul care formează limita de sud a țării este ____."],["dunărea"]),13)
    repoFillins.save(FillInStatement(-1,["Capitala României se află în orașul ____."],["bucurești"]),13)

    repoFillins.save(FillInStatement(-1,["Bătălia de la Posada (1330) a asigurat ____ "," țării."],["independența"]),14)
    repoFillins.save(FillInStatement(-1,["Alexandru Ioan Cuza a realizat Mica ____ "," în 1859."],["unire"]),14)

    repoFillins.save(FillInStatement(-1,["Între Carpați și Câmpia Română se află Podișul ____."],["getic"]),15)
    repoFillins.save(FillInStatement(-1,["Ocupația principală la sate este ____."],["agricultura"]),15)

    repoFillins.save(FillInStatement(-1,["Vlad Țepeș era cunoscut pentru severitate și ____."],["dreptate"]),16)
    repoFillins.save(FillInStatement(-1,["Cel mai mare port la Dunăre din această regiune este ____."],["giurgiu"]),16)

    repoFillins.save(FillInStatement(-1,["Reședința domnească a lui Vlad Țepeș a fost la Târgoviște, unde vedem Turnul ____."],["chindiei"]),17)
    repoFillins.save(FillInStatement(-1,["Cunoscuta stațiune de pe Valea Prahovei este ____."],["sinaia"]),17)

    repoFillins.save(FillInStatement(-1,["Râul Olt trece prin defileul Turnu ____."],["roșu"]),18)
    repoFillins.save(FillInStatement(-1,["Mihai Viteazul a fost domn al Țării ____."],["românești"]),18)

    repoFillins.save(FillInStatement(-1,["Porțiunile de uscat din Deltă formate din mâl se numesc ____."],["grinduri"]),19)
    repoFillins.save(FillInStatement(-1,["Orașul-port la vărsarea brațului mijlociu este ____."],["sulina"]),19)

    repoFillins.save(FillInStatement(-1,["Vechiul nume al orașului Constanța este ____."],["tomis"]),20)
    repoFillins.save(FillInStatement(-1,["Monumentul Tropaeum Traiani se află la ____."],["adamclisi"]),20)

    repoFillins.save(FillInStatement(-1,["Pentru irigații, în Dobrogea este nevoie de multă ____."],["apă"]),21)
    repoFillins.save(FillInStatement(-1,["Litoralul este renumit pentru stațiunile ____."],["turistice"]),21)

    repoFillins.save(FillInStatement(-1,["Ocupația principală a oamenilor din Deltă este ____."],["pescuitul"]),22)
    repoFillins.save(FillInStatement(-1,["Pasărea simbol a Deltei Dunării este ____."],["pelicanul"]),22)

    repoFillins.save(FillInStatement(-1,["Orașul Tulcea este poarta de intrare în ____."],["delta dunarii"]),23)
    repoFillins.save(FillInStatement(-1,["Vânturile din Dobrogea, numite Crivăț, sunt foarte ____."],["reci"]),23)

    repoFillins.save(FillInStatement(-1,["Centrala nucleară de la Cernavodă produce ____."],["energie"]),24)
    repoFillins.save(FillInStatement(-1,["Insula Popina se află în lacul ____."],["razim"]),24)

    repoFillins.save(FillInStatement(-1,["Râul care trece prin Timișoara (canal navigabil) este ____."],["bega"]),25)
    repoFillins.save(FillInStatement(-1,["Banatul a revenit României după anul ____."],["1918"]),25)

    repoFillins.save(FillInStatement(-1,["Forma de relief predominantă la granița de vest este ____."],["câmpia de vest"]),26)
    repoFillins.save(FillInStatement(-1,["La Oradea se află stațiunea Băile ____."],["felix"]),26)

    repoFillins.save(FillInStatement(-1,["Cimitirul Vesel se află în localitatea ____."],["săpânța"]),27)
    repoFillins.save(FillInStatement(-1,["Trenul cu aburi de pe Valea Vaserului se numește ____."],["mocănița"]),27)

    repoFillins.save(FillInStatement(-1,["Zona tradițională din nord se numește Țara ____."],["maramureșului"]),28)
    repoFillins.save(FillInStatement(-1,["Râul Tisa formează granița cu țara numită ____."],["ucraina"]),28)

    repoFillins.save(FillInStatement(-1,["Orașul Baia Mare este reședința județului ____."],["maramureș"]),29)
    repoFillins.save(FillInStatement(-1,["Cea mai mare câmpie din vestul țării este Câmpia de ____."],["vest"]),29)

    repoFillins.save(FillInStatement(-1,["Cele trei râuri Criș sunt: Repede, Negru și ____."],["alb"]),30)
    repoFillins.save(FillInStatement(-1,["Mânăstirea Bârsana se află în ____."],["maramureș"]),30)

def insert_quizzes(repoQuizzes: QuizzRepository) -> None:
    for i in range(5):
        repoQuizzes.save(Quizz(-1,[],[],[],Difficulty[0]),1)
        # repoQuizzes.save(Quizz(1,[],[],[],Difficulty[0]),1)
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