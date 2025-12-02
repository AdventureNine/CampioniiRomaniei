REGIONS_DATA = {
    1: {"name": "Transilvania", "mission": "Misiune: Relieful de poveste", "companion": "Geo"},
    2: {"name": "Moldova", "mission": "Misiune: Aventura Apelor", "companion": "Rio"},
    3: {"name": "Țara Românească", "mission": "Misiune: Drumul spre Dunăre", "companion": "Busu"},
    4: {"name": "Dobrogea", "mission": "Misiune: Vecinii României", "companion": "Busu"},
    5: {"name": "Banat-Crișana-Maramureș", "mission": "Misiune: România unită", "companion": "Toți"}
}

# Date dinamice (Progresul jucatorului)
# Cheia este ID-ul regiunii, Valoarea este lista de nivele deblocate [True, False, ...]
# Initial, doar primul nivel e deblocat peste tot.
USER_PROGRESS = {
    1: [True, False, False, False, False, False],
    2: [True, False, False, False, False, False],
    3: [True, False, False, False, False, False],
    4: [True, False, False, False, False, False],
    5: [True, False, False, False, False, False],
}