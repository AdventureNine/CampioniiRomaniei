# Structura: { REGION_ID: { LEVEL_ID: [ Exercițiu1, Exercițiu2, ... ] } }
# Pe moment hardcodat, dar la un moment dat aici o sa facem legatura cu back end
# frontend/data/questions_data.py

QUESTIONS_DATA = {
    # --- TRANSILVANIA (ID: 1) ---
    1: {
        # NIVEL 1: Munți și Relief General (Ușor)
        1: [
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
    # Sursa: Document "Set Intrebari Regiuni", Secțiunea IV [cite: 188]
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
    }
}