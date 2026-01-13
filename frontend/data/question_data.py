# frontend/data/questions_data.py

# Structura: { REGION_ID: { LEVEL_ID: [ Exercițiu1, Exercițiu2, ... ] } }
# Pe moment hardcodat, dar la un moment dat aici o sa facem legatura cu back end
# frontend/data/questions_data.py

QUESTIONS_DATA = {
    # --- TRANSILVANIA (ID: 1) ---
    1: {
        # NIVEL 1: Munți și Relief General (Ușor)
        1: [
            {
                "type": "quiz",
                "question": "Munții din jurul Transilvaniei se numesc...",
                "options": ["Alpi", "Carpați", "Himalaya", "Balcani"],
                "correct": "Carpați"
            },
            {
                "type": "quiz",
                "question": "Munții sunt colorați pe hartă cu culoarea...",
                "options": ["Verde", "Albastru", "Maro", "Galben"],
                "correct": "Maro"
            },
            {
                "type": "quiz",
                "question": "Munții din vestul Transilvaniei se numesc...",
                "options": ["Apuseni", "Meridionali", "Orientali", "Banatului"],
                "correct": "Apuseni"
            },
            {
                "type": "fill",
                "question": "Pe vârful munților crește doar ____.",
                "correct": ["iarba", "iarbă"]
            },
            {
                "type": "fill",
                "question": "În munții Carpați trăiește animalul numit ____.",
                "correct": ["urs", "ursul"]
            },
            {
                "type": "puzzle",
                "image": "puzzle1.jpg",
                "question": "Rezolvă puzzle-ul!"
            }
        ],

        # NIVEL 2: Dealuri, Podișuri și Orașe (Ușor/Mediu)
        2: [
            {
                "type": "quiz",
                "question": "Ce fel de relief este în centrul Transilvaniei?",
                "options": ["Câmpie", "Podiș", "Delta", "Munte"],
                "correct": "Podiș"
            },
            {
                "type": "quiz",
                "question": "Ce oraș mare este în Transilvania?",
                "options": ["Iași", "Constanța", "Cluj", "Craiova"],
                "correct": "Cluj"
            },
            {
                "type": "quiz",
                "question": "La Turda se scoate din pământ...",
                "options": ["Aur", "Sare", "Cărbune", "Petrol"],
                "correct": "Sare"
            },
            {
                "type": "fill",
                "question": "Orașul Sibiu este un oraș foarte ____.",
                "correct": ["vechi"]
            },
            {
                "type": "fill",
                "question": "Ce oraș a fost capitala Transilvaniei?",
                "correct": ["alba iulia"]
            }
        ],

        # NIVEL 3: Ape și Hidrografie (Mediu)
        3: [
            {
                "type": "quiz",
                "question": "Care este cel mai lung râu din Transilvania?",
                "options": ["Olt", "Mureș", "Siret", "Prut"],
                "correct": "Mureș"
            },
            {
                "type": "quiz",
                "question": "Ce râu trece prin orașul Cluj-Napoca?",
                "options": ["Someș", "Bega", "Jiu", "Argeș"],
                "correct": "Someș"
            },
            {
                "type": "quiz",
                "question": "Lacul Sfânta Ana este un lac...",
                "options": ["Glaciar", "Vulcanic", "Sărat", "Artificial"],
                "correct": "Vulcanic"
            },
            {
                "type": "fill",
                "question": "Râurile curg prin ____.",
                "correct": ["vai", "văi"]
            },
            {
                "type": "fill",
                "question": "Râul Olt curge spre punctul cardinal ____.",
                "correct": ["sud"]
            }
        ],

        # NIVEL 4: Agricultură și Resurse (Mediu/Greu)
        4: [
            {
                "type": "quiz",
                "question": "Ce se face din vița-de-vie?",
                "options": ["Ulei", "Vin", "Făină", "Zahăr"],
                "correct": "Vin"
            },
            {
                "type": "quiz",
                "question": "Cartofii cresc în locuri...",
                "options": ["Secetoase", "Foarte calde", "Răcoroase", "Mlaștinoase"],
                "correct": "Răcoroase"
            },
            {
                "type": "quiz",
                "question": "Pentru ce plantă este cunoscut Podișul Târnavelor?",
                "options": ["Porumb", "Vița-de-vie", "Floarea soarelui", "Orez"],
                "correct": "Vița-de-vie"
            },
            {
                "type": "fill",
                "question": "De la vite oamenii iau carne și ____.",
                "correct": ["lapte"]
            },
            {
                "type": "fill",
                "question": "Vara, animalele pasc pe ____.",
                "correct": ["pasuni", "pășuni"]
            }
        ],

        # NIVEL 5: Geografie Avansată (Greu)
        5: [
            {
                "type": "quiz",
                "question": "Care este cel mai înalt vârf din România?",
                "options": ["Omu", "Moldoveanu", "Negoiu", "Pietrosu"],
                "correct": "Moldoveanu"
            },
            {
                "type": "quiz",
                "question": "Cum s-a format Lacul Roșu?",
                "options": ["Vulcan", "Alunecare de teren", "Baraj", "Meteorit"],
                "correct": "Alunecare de teren"
            },
            {
                "type": "quiz",
                "question": "Ce râu a săpat Cheile Turzii?",
                "options": ["Arieș", "Hășdate", "Ampoi", "Mureș"],
                "correct": "Hășdate"
            },
            {
                "type": "fill",
                "question": "Văile înguste dintre munți se numesc ____.",
                "correct": ["chei"]
            },
            {
                "type": "fill",
                "question": "Munții înalți sunt colorați pe hartă cu maro ____.",
                "correct": ["inchis", "închis"]
            }
        ],

        # NIVEL 6: Recapitulare
        6: [
            {
                "type": "quiz",
                "question": "Lângă ce munți este orașul Brașov?",
                "options": ["Măcin", "Carpați", "Apuseni", "Rodnei"],
                "correct": "Carpați"
            },
            {
                "type": "quiz",
                "question": "În ce munți se află Lacul Roșu?",
                "options": ["Meridionali", "Orientali", "Occidentali", "Banatului"],
                "correct": "Orientali"
            },
            {
                "type": "quiz",
                "question": "În munții Apuseni sunt multe...",
                "options": ["Vulcani", "Peșteri", "Deșerturi", "Delte"],
                "correct": "Peșteri"
            },
            {
                "type": "fill",
                "question": "Râurile din Transilvania se varsă până la urmă în fluviul ____.",
                "correct": ["dunare", "dunăre"]
            },
            {
                "type": "fill",
                "question": "În Transilvania sunt multe ____ vechi construite pentru apărare.",
                "correct": ["cetati", "cetăți"]
            }
        ]
    },

    # --- MOLDOVA (ID: 2) ---
    2: {
        # NIVEL 1: General (Ușor)
        1: [
            {
                "type": "quiz",
                "question": "Ce râu trece prin orașul Iași?",
                "options": ["Bahlui", "Siret", "Prut", "Bistrița"],
                "correct": "Bahlui"
            },
            {
                "type": "quiz",
                "question": "Cetatea de Scaun a Moldovei se află la...",
                "options": ["Suceava", "Iași", "Neamț", "Soroca"],
                "correct": "Suceava"
            },
            {
                "type": "quiz",
                "question": "Ion Creangă s-a născut la...",
                "options": ["Humulești", "Ipotești", "Mircești", "Botoșani"],
                "correct": "Humulești"
            },
            {
                "type": "fill",
                "question": "Mănăstirea albastră din Bucovina se numește _______.",
                "correct": ["voronet", "voroneț"]
            },
            {
                "type": "fill",
                "question": "Capitala județului Iași este municipiul ____.",
                "correct": ["iasi", "iași"]
            }
        ],

        # NIVEL 2: Ape și Relief (Ușor/Mediu)
        2: [
            {
                "type": "quiz",
                "question": "Care este fluviul care formează granița de est a României?",
                "options": ["Dunărea", "Prutul", "Siretul", "Mureșul"],
                "correct": "Prutul"
            },
            {
                "type": "quiz",
                "question": "Cum se numește fluviul care se varsă în Marea Neagră și trece prin sudul Moldovei?",
                "options": ["Dunărea", "Olt", "Argeș", "Tisa"],
                "correct": "Dunărea"
            },
            {
                "type": "quiz",
                "question": "Din ce regiune face parte muntele Ceahlău?",
                "options": ["Banat", "Dobrogea", "Moldova", "Transilvania"],
                "correct": "Moldova"
            },
            {
                "type": "fill",
                "question": "Râul important care trece prin Bacău se numește ____.",
                "correct": ["bistrita", "bistrița"]
            },
            {
                "type": "fill",
                "question": "Cel mai înalt vârf din Carpații Orientali este Pietrosul ____.",
                "correct": ["rodnei"]
            }
        ],

        # NIVEL 3: Istorie și Cultură (Mediu)
        3: [
            {
                "type": "quiz",
                "question": "Cine a fost domnitorul Moldovei în jurul anului 1500?",
                "options": ["Mihai Viteazul", "Ștefan cel Mare", "Vlad Țepeș", "Mircea cel Bătrân"],
                "correct": "Ștefan cel Mare"
            },
            {
                "type": "quiz",
                "question": "Ce domnitor a mutat capitala la Suceava?",
                "options": ["Alexandru cel Bun", "Petru I Mușat", "Dragoș Vodă", "Ieremia Movilă"],
                "correct": "Petru I Mușat"
            },
            {
                "type": "quiz",
                "question": "În ce oraș din Moldova a fost înființată prima universitate modernă?",
                "options": ["Suceava", "Bacău", "Galați", "Iași"],
                "correct": "Iași"
            },
            {
                "type": "fill",
                "question": "Regiunea istorică din estul Carpaților se numește ____.",
                "correct": ["moldova"]
            },
            {
                "type": "fill",
                "question": "Râul care trece pe lângă Cetatea Neamțului este ____.",
                "correct": ["ozana"]
            }
        ],

        # NIVEL 4: Geografie Avansată (Greu)
        4: [
            {
                "type": "quiz",
                "question": "Ce rol avea Cetatea Neamț în vremea lui Ștefan cel Mare?",
                "options": ["Vacanță", "Comerț", "Apărare", "Religios"],
                "correct": "Apărare"
            },
            {
                "type": "quiz",
                "question": "Ce fenomen a format Cheile Bicazului?",
                "options": ["Cutremur", "Eroziunea apei", "Vulcan", "Vânt"],
                "correct": "Eroziunea apei"
            },
            {
                "type": "quiz",
                "question": "Ce ramură economică e specifică Bucovinei?",
                "options": ["Pescuitul", "Petrolul", "Prelucrarea lemnului", "Mineritul"],
                "correct": "Prelucrarea lemnului"
            },
            {
                "type": "fill",
                "question": "Unirea Principatelor (Moldova și Țara Românească) a avut loc în anul ____.",
                "correct": ["1859"]
            },
            {
                "type": "fill",
                "question": "Vecinul de la est al Moldovei este Republica ____.",
                "correct": ["moldova"]
            }
        ],

        # NIVEL 5: Mix
        5: [
            {
                "type": "quiz",
                "question": "Mănăstirea Putna a fost ctitorită de...",
                "options": ["Mircea cel Bătrân", "Ștefan cel Mare", "Petru Rareș", "Alexandru Lăpușneanu"],
                "correct": "Ștefan cel Mare"
            },
            {
                "type": "quiz",
                "question": "Ce scriitor celebru s-a născut la Ipotești?",
                "options": ["Ion Creangă", "Mihai Eminescu", "Vasile Alecsandri", "George Bacovia"],
                "correct": "Mihai Eminescu"
            },
            {
                "type": "quiz",
                "question": "Moldova se află în partea de ... a României.",
                "options": ["Vest", "Sud", "Est", "Nord-Vest"],
                "correct": "Est"
            },
            {
                "type": "fill",
                "question": "Cetatea Soroca se află pe malul râului ____.",
                "correct": ["nistru"]
            },
            {
                "type": "fill",
                "question": "Ștefan cel Mare a câștigat o mare bătălie la Podul ____.",
                "correct": ["inalt", "înalt"]
            }
        ],

        # NIVEL 6: Recapitulare
        6: [
            {
                "type": "quiz",
                "question": "Ce lac de acumulare se află pe râul Bistrița?",
                "options": ["Vidraru", "Izvorul Muntelui", "Sfânta Ana", "Bâlea"],
                "correct": "Izvorul Muntelui"
            },
            {
                "type": "quiz",
                "question": "Câte cetăți de scaun a avut Moldova?",
                "options": ["Una", "Două (Suceava și Iași)", "Trei", "Niciuna"],
                "correct": "Două (Suceava și Iași)"
            },
            {
                "type": "quiz",
                "question": "„Perla Moldovei” este stațiunea...",
                "options": ["Slănic Moldova", "Vatra Dornei", "Sovata", "Sinaia"],
                "correct": "Slănic Moldova"
            },
            {
                "type": "fill",
                "question": "Bucovina este renumită pentru mănăstrile ____.",
                "correct": ["pictate"]
            },
            {
                "type": "fill",
                "question": "Orașul Iași se află pe cele 7 ____.",
                "correct": ["coline"]
            }
        ]
    },

    # --- ȚARA ROMÂNEASCĂ (ID: 3) ---
    3: {
        # NIVEL 1: Istorie și Relief (Ușor)
        1: [
            {
                "type": "quiz",
                "question": "Cine este considerat întemeietorul Țării Românești?",
                "options": ["Mircea cel Bătrân", "Basarab I", "Vlad Țepeș", "Mihai Viteazul"],
                "correct": "Basarab I"
            },
            {
                "type": "quiz",
                "question": "Care este cea mai joasă formă de relief din zonă?",
                "options": ["Câmpia Română", "Podișul Getic", "Subcarpații", "Munții Bucegi"],
                "correct": "Câmpia Română"
            },
            {
                "type": "quiz",
                "question": "Ce râu traversează Bucureștiul?",
                "options": ["Dunărea", "Argeș", "Dâmbovița", "Olt"],
                "correct": "Dâmbovița"
            },
            {
                "type": "fill",
                "question": "Fluviul care formează limita de sud a țării este ____.",
                "correct": ["dunarea", "dunărea"]
            },
            {
                "type": "fill",
                "question": "Capitala României se află în orașul ____.",
                "correct": ["bucuresti", "bucurești"]
            }
        ],
        # NIVEL 2: Domnitori și Evenimente (Mediu)
        2: [
            {
                "type": "quiz",
                "question": "Ce domnitor a luptat la Rovine în 1395?",
                "options": ["Ștefan cel Mare", "Mircea cel Bătrân", "Vlad Țepeș", "Cuza"],
                "correct": "Mircea cel Bătrân"
            },
            {
                "type": "quiz",
                "question": "În timpul cui a fost atestat documentar Bucureștiul (1459)?",
                "options": ["Basarab I", "Vlad Țepeș", "Mihai Viteazul", "Matei Basarab"],
                "correct": "Vlad Țepeș"
            },
            {
                "type": "quiz",
                "question": "Ce mare unire a realizat Mihai Viteazul în 1600?",
                "options": ["Mica Unire", "Unirea celor 3 țări", "Unirea cu Dobrogea", "Unirea cu Banatul"],
                "correct": "Unirea celor 3 țări"
            },
            {
                "type": "fill",
                "question": "Bătălia de la Posada (1330) a asigurat ____ țării.",
                "correct": ["independenta", "independența"]
            },
            {
                "type": "fill",
                "question": "Alexandru Ioan Cuza a realizat Mica ____ în 1859.",
                "correct": ["unire"]
            }
        ],
        # NIVEL 3: Geografie și Economie (Mediu)
        3: [
            {
                "type": "quiz",
                "question": "Ce resurse se extrag din Podișul Getic?",
                "options": ["Aur și Argint", "Petrol și Gaze", "Uraniu", "Diamante"],
                "correct": "Petrol și Gaze"
            },
            {
                "type": "quiz",
                "question": "De ce s-a dezvoltat agricultura în Câmpia Română?",
                "options": ["Soluri fertile", "Multe păduri", "Multe dealuri", "Climă rece"],
                "correct": "Soluri fertile"
            },
            {
                "type": "quiz",
                "question": "Unde se află Vârful Omu?",
                "options": ["Munții Bucegi", "Munții Făgăraș", "Munții Retezat", "Munții Apuseni"],
                "correct": "Munții Bucegi"
            },
            {
                "type": "fill",
                "question": "Între Carpați și Câmpia Română se află Podișul ____.",
                "correct": ["getic"]
            },
            {
                "type": "fill",
                "question": "Ocupația principală la sate este ____.",
                "correct": ["agricultura"]
            }
        ],
        # NIVEL 4: Mix Istorie-Geografie (Greu)
        4: [
            {
                "type": "quiz",
                "question": "Ce reformă importantă a făcut Cuza?",
                "options": ["A construit metroul", "Legea învățământului", "A fondat Bucureștiul", "A cucerit Turcia"],
                "correct": "Legea învățământului"
            },
            {
                "type": "quiz",
                "question": "De ce este Bucureștiul un nod de comunicație?",
                "options": ["Are port la mare", "Are multe legături rutiere și feroviare", "Este la munte", "Nu este nod"],
                "correct": "Are multe legături rutiere și feroviare"
            },
            {
                "type": "quiz",
                "question": "Curtea de Argeș este cunoscută pentru...",
                "options": ["Mănăstirea Meșterului Manole", "Turnul Chindiei", "Podul lui Saligny", "Castelul Peleș"],
                "correct": "Mănăstirea Meșterului Manole"
            },
            {
                "type": "fill",
                "question": "Vlad Țepeș era cunoscut pentru severitate și ____.",
                "correct": ["dreptate"]
            },
            {
                "type": "fill",
                "question": "Cel mai mare port la Dunăre din această regiune este ____.",
                "correct": ["giurgiu"]
            }
        ],
        # NIVEL 5: Curiozități
        5: [
            {
                "type": "quiz",
                "question": "Unde se află 'Coloana Infinitului'?",
                "options": ["Târgu Jiu", "Craiova", "Pitești", "Ploiești"],
                "correct": "Târgu Jiu"
            },
            {
                "type": "quiz",
                "question": "Barajul Vidraru se află pe râul...",
                "options": ["Olt", "Argeș", "Dâmbovița", "Ialomița"],
                "correct": "Argeș"
            },
            {
                "type": "quiz",
                "question": "Cine a sculptat 'Poarta Sărutului'?",
                "options": ["Brâncuși", "Grigorescu", "Enescu", "Tonitza"],
                "correct": "Brâncuși"
            },
            {
                "type": "fill",
                "question": "Reședința domnească a lui Vlad Țepeș a fost la Târgoviște, unde vedem Turnul ____.",
                "correct": ["chindiei"]
            },
            {
                "type": "fill",
                "question": "Cunoscuta stațiune de pe Valea Prahovei este ____.",
                "correct": ["sinaia"]
            }
        ],
        # NIVEL 6: Recapitulare
        6: [
            {
                "type": "quiz",
                "question": "În ce an a avut loc Bătălia de la Posada?",
                "options": ["1330", "1475", "1600", "1859"],
                "correct": "1330"
            },
            {
                "type": "quiz",
                "question": "Care este principala bogăție a solului în zona Ploiești?",
                "options": ["Aur", "Petrol", "Fier", "Cupru"],
                "correct": "Petrol"
            },
            {
                "type": "quiz",
                "question": "Câmpia Română este...",
                "options": ["Grânarul țării", "Zona minieră", "Zona muntoasă", "Delta"],
                "correct": "Grânarul țării"
            },
            {
                "type": "fill",
                "question": "Râul Olt trece prin defileul Turnu ____.",
                "correct": ["rosu", "roșu"]
            },
            {
                "type": "fill",
                "question": "Mihai Viteazul a fost domn al Țării ____.",
                "correct": ["romanesti", "românești"]
            }
        ]
    },

    # --- DOBROGEA (ID: 4) ---
    4: {
        # NIVEL 1: Geografie Fizică (Ușor)
        1: [
            {
                "type": "quiz",
                "question": "Care este cea mai joasă unitate de relief din România?",
                "options": ["Câmpia de Vest", "Delta Dunării", "Podișul Getic", "Lunca Siretului"],
                "correct": "Delta Dunării"
            },
            {
                "type": "quiz",
                "question": "Ce mare mărginește Dobrogea la est?",
                "options": ["Marea Mediterană", "Marea Neagră", "Marea Roșie", "Marea Caspică"],
                "correct": "Marea Neagră"
            },
            {
                "type": "quiz",
                "question": "Care sunt brațele Dunării?",
                "options": ["Chilia, Sulina, Sf. Gheorghe", "Olt, Mureș, Siret", "Borcea, Măcin, Vâlciu", "Niciunul"],
                "correct": "Chilia, Sulina, Sf. Gheorghe"
            },
            {
                "type": "fill",
                "question": "Porțiunile de uscat din Deltă formate din mâl se numesc ____.",
                "correct": ["grinduri"]
            },
            {
                "type": "fill",
                "question": "Orașul-port la vărsarea brațului mijlociu este ____.",
                "correct": ["sulina"]
            }
        ],
        # NIVEL 2: Istorie Antică și Medievală (Mediu)
        2: [
            {
                "type": "quiz",
                "question": "Cine este considerat întemeietorul statului medieval Dobrogea?",
                "options": ["Mircea cel Bătrân", "Dobrotici", "Burebista", "Decebal"],
                "correct": "Dobrotici"
            },
            {
                "type": "quiz",
                "question": "Numiți o colonie grecească antică din Dobrogea.",
                "options": ["Histria", "Sarmizegetusa", "Apulum", "Potaissa"],
                "correct": "Histria"
            },
            {
                "type": "quiz",
                "question": "Cărui imperiu a fost cedată Dobrogea în 1417?",
                "options": ["Imperiul Roman", "Imperiul Otoman", "Imperiul Austro-Ungar", "Imperiul Rus"],
                "correct": "Imperiul Otoman"
            },
            {
                "type": "fill",
                "question": "Vechiul nume al orașului Constanța este ____.",
                "correct": ["tomis"]
            },
            {
                "type": "fill",
                "question": "Monumentul Tropaeum Traiani se află la ____.",
                "correct": ["adamclisi"]
            }
        ],
        # NIVEL 3: Geografie Umană și Modernă (Mediu)
        3: [
            {
                "type": "quiz",
                "question": "Ce popor minoritar a influențat Dobrogea?",
                "options": ["Turcii/Tătarii", "Ungurii", "Sârbii", "Polonezii"],
                "correct": "Turcii/Tătarii"
            },
            {
                "type": "quiz",
                "question": "În ce an a revenit Dobrogea la România (Războiul de Independență)?",
                "options": ["1878", "1918", "1600", "1417"],
                "correct": "1878"
            },
            {
                "type": "quiz",
                "question": "Ce tip de vegetație este specific Podișului Dobrogei?",
                "options": ["Pădurea de brad", "Stepa", "Tundra", "Savana"],
                "correct": "Stepa"
            },
            {
                "type": "fill",
                "question": "Pentru irigații, în Dobrogea este nevoie de multă ____.",
                "correct": ["apa", "apă"]
            },
            {
                "type": "fill",
                "question": "Litoralul este renumit pentru stațiunile ____.",
                "correct": ["turistice"]
            }
        ],
        # NIVEL 4: Curiozități (Greu)
        4: [
            {
                "type": "quiz",
                "question": "De ce este Delta Dunării rezervație naturală?",
                "options": ["Pentru petrol", "Pentru biodiversitate (păsări, pești)", "Pentru industrie", "Pentru agricultură"],
                "correct": "Pentru biodiversitate (păsări, pești)"
            },
            {
                "type": "quiz",
                "question": "Care sunt cei mai vechi munți din România, aflați în Dobrogea?",
                "options": ["Munții Măcinului", "Munții Bucegi", "Munții Făgăraș", "Munții Retezat"],
                "correct": "Munții Măcinului"
            },
            {
                "type": "quiz",
                "question": "Podul de la Cernavodă a fost construit de...",
                "options": ["Anghel Saligny", "Henri Coandă", "Ana Aslan", "Aurel Vlaicu"],
                "correct": "Anghel Saligny"
            },
            {
                "type": "fill",
                "question": "Ocupația principală a oamenilor din Deltă este ____.",
                "correct": ["pescuitul"]
            },
            {
                "type": "fill",
                "question": "Pasărea simbol a Deltei Dunării este ____.",
                "correct": ["pelicanul"]
            }
        ],
        # NIVEL 5: Mix
        5: [
            {
                "type": "quiz",
                "question": "Care braț al Dunării este cel mai scurt și folosit pentru navigație?",
                "options": ["Chilia", "Sulina", "Sf. Gheorghe", "Borcea"],
                "correct": "Sulina"
            },
            {
                "type": "quiz",
                "question": "Portul principal al României la Marea Neagră este...",
                "options": ["Mangalia", "Constanța", "Tulcea", "Sulina"],
                "correct": "Constanța"
            },
            {
                "type": "quiz",
                "question": "Lacul Razim este un lac...",
                "options": ["Vulcanic", "Lagună (fost golf)", "Glaciar", "De acumulare"],
                "correct": "Lagună (fost golf)"
            },
            {
                "type": "fill",
                "question": "Orașul Tulcea este poarta de intrare în ____.",
                "correct": ["delta", "delta dunarii"]
            },
            {
                "type": "fill",
                "question": "Vânturile din Dobrogea, numite Crivăț, sunt foarte ____.",
                "correct": ["puternice", "reci"]
            }
        ],
        # NIVEL 6: Recapitulare
        6: [
            {
                "type": "quiz",
                "question": "Peștera Sfântului Andrei se află în...",
                "options": ["Dobrogea", "Moldova", "Banat", "Oltenia"],
                "correct": "Dobrogea"
            },
            {
                "type": "quiz",
                "question": "Care braț al Dunării transportă cea mai mare cantitate de apă?",
                "options": ["Chilia", "Sulina", "Sf. Gheorghe", "Niciunul"],
                "correct": "Chilia"
            },
            {
                "type": "quiz",
                "question": "Dobrogea este o zonă cu climă...",
                "options": ["Umedă și rece", "Secetoasă și caldă", "Polară", "Tropicală"],
                "correct": "Secetoasă și caldă"
            },
            {
                "type": "fill",
                "question": "Centrala nucleară de la Cernavodă produce ____.",
                "correct": ["electricitate", "curent", "energie"]
            },
            {
                "type": "fill",
                "question": "Insula Popina se află în lacul ____.",
                "correct": ["razim"]
            }
        ]
    },

    # --- BANAT - CRIȘANA - MARAMUREȘ (ID: 5) ---
    5: {
        # NIVEL 1: Banat și Revoluție (Ușor)
        1: [
            {
                "type": "quiz",
                "question": "În ce oraș a început Revoluția din 1989?",
                "options": ["București", "Cluj", "Timișoara", "Iași"],
                "correct": "Timișoara"
            },
            {
                "type": "quiz",
                "question": "Capitala județului Timiș este...",
                "options": ["Arad", "Timișoara", "Lugoj", "Reșița"],
                "correct": "Timișoara"
            },
            {
                "type": "quiz",
                "question": "Banatul se află în partea de ... a țării.",
                "options": ["Est", "Sud-Vest", "Nord", "Sud-Est"],
                "correct": "Sud-Vest"
            },
            {
                "type": "fill",
                "question": "Râul care trece prin Timișoara (canal navigabil) este ____.",
                "correct": ["bega"]
            },
            {
                "type": "fill",
                "question": "Banatul a revenit României după anul ____.",
                "correct": ["1918"]
            }
        ],
        # NIVEL 2: Crișana și Vecinii (Mediu)
        2: [
            {
                "type": "quiz",
                "question": "Care este cel mai important oraș din Crișana?",
                "options": ["Oradea", "Satu Mare", "Zalău", "Baia Mare"],
                "correct": "Oradea"
            },
            {
                "type": "quiz",
                "question": "Crișana se învecinează la vest cu...",
                "options": ["Ucraina", "Ungaria", "Serbia", "Bulgaria"],
                "correct": "Ungaria"
            },
            {
                "type": "quiz",
                "question": "De câte râuri 'Criș' este străbătută Crișana?",
                "options": ["Unul", "Două", "Trei (Alb, Negru, Repede)", "Patru"],
                "correct": "Trei (Alb, Negru, Repede)"
            },
            {
                "type": "fill",
                "question": "Forma de relief predominantă la granița de vest este ____.",
                "correct": ["campia", "câmpia", "câmpia de vest"]
            },
            {
                "type": "fill",
                "question": "La Oradea se află stațiunea Băile ____.",
                "correct": ["felix"]
            }
        ],
        # NIVEL 3: Maramureș și Tradiții (Mediu)
        3: [
            {
                "type": "quiz",
                "question": "Maramureșul este faimos pentru...",
                "options": ["Porțile din lemn", "Castele de nisip", "Zgârie-nori", "Podgorii"],
                "correct": "Porțile din lemn"
            },
            {
                "type": "quiz",
                "question": "Ce lanț muntos se află în Maramureș?",
                "options": ["Carpații Maramureșului și Bucovinei", "Munții Banatului", "Făgăraș", "Bucegi"],
                "correct": "Carpații Maramureșului și Bucovinei"
            },
            {
                "type": "quiz",
                "question": "Unde este situat Maramureșul?",
                "options": ["Nordul României", "Sudul României", "Estul României", "Vestul României"],
                "correct": "Nordul României"
            },
            {
                "type": "fill",
                "question": "Cimitirul Vesel se află în localitatea ____.",
                "correct": ["sapanta", "săpânța"]
            },
            {
                "type": "fill",
                "question": "Trenul cu aburi de pe Valea Vaserului se numește ____.",
                "correct": ["mocanita", "mocănița"]
            }
        ],
        # NIVEL 4: Resurse și Istorie (Greu)
        4: [
            {
                "type": "quiz",
                "question": "Ce resurse importante se găseau în Munții Apuseni (zona auriferă)?",
                "options": ["Aur și Argint", "Sare", "Petrol", "Cărbune"],
                "correct": "Aur și Argint"
            },
            {
                "type": "quiz",
                "question": "Ce au trimis provinciile (Crișana, Maramureș) la Alba Iulia în 1918?",
                "options": ["Soldați", "Delegați pentru Unire", "Bani", "Mâncare"],
                "correct": "Delegați pentru Unire"
            },
            {
                "type": "quiz",
                "question": "Memorialul Victimelor Comunismului se află la...",
                "options": ["Sighetu Marmației", "Baia Mare", "Satu Mare", "Arad"],
                "correct": "Sighetu Marmației"
            },
            {
                "type": "fill",
                "question": "Zona tradițională din nord se numește Țara ____.",
                "correct": ["maramuresului", "maramureșului"]
            },
            {
                "type": "fill",
                "question": "Râul Tisa formează granița cu țara numită ____.",
                "correct": ["ucraina"]
            }
        ],
        # NIVEL 5: Mix
        5: [
            {
                "type": "quiz",
                "question": "Castelul Corvinilor (Huniade) este aproape de Banat, în...",
                "options": ["Hunedoara", "Timișoara", "Arad", "Deva"],
                "correct": "Hunedoara"
            },
            {
                "type": "quiz",
                "question": "Cascada Bigăr se află în regiunea...",
                "options": ["Banat", "Dobrogea", "Moldova", "Muntenia"],
                "correct": "Banat"
            },
            {
                "type": "quiz",
                "question": "Cetatea Aradului este construită în stil...",
                "options": ["Vauban (stea)", "Gotic", "Modern", "Dacic"],
                "correct": "Vauban (stea)"
            },
            {
                "type": "fill",
                "question": "Orașul Baia Mare este reședința județului ____.",
                "correct": ["maramures", "maramureș"]
            },
            {
                "type": "fill",
                "question": "Cea mai mare câmpie din vestul țării este Câmpia de ____.",
                "correct": ["vest"]
            }
        ],
        # NIVEL 6: Recapitulare
        6: [
            {
                "type": "quiz",
                "question": "Fluviul Dunărea intră în țară prin regiunea...",
                "options": ["Banat (Baziaș)", "Dobrogea", "Moldova", "Crișana"],
                "correct": "Banat (Baziaș)"
            },
            {
                "type": "quiz",
                "question": "Bisericile de lemn din Maramureș sunt în patrimoniul...",
                "options": ["UNESCO", "NATO", "UE", "ONU"],
                "correct": "UNESCO"
            },
            {
                "type": "quiz",
                "question": "Care este un oraș important din județul Arad?",
                "options": ["Lipova", "Mangalia", "Făgăraș", "Sighișoara"],
                "correct": "Lipova"
            },
            {
                "type": "fill",
                "question": "Cele trei râuri Criș sunt: Repede, Negru și ____.",
                "correct": ["alb"]
            },
            {
                "type": "fill",
                "question": "Mânăstirea Bârsana se află în ____.",
                "correct": ["maramures", "maramureș"]
            }
        ]
    }
}