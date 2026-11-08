bocor = False
kedalaman_aman = True
baterai_lemah = True
boleh_menyelam = kedalaman_aman and not bocor
print(f"Boleh menyelam: {boleh_menyelam}")
perlu_surfacing = bocor or baterai_lemah
print(f"Perlu surfacing: {perlu_surfacing}")