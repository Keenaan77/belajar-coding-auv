kedalaman = 35.0
batas_maks = 40.0
baterai = 18.0
batas_baterai = 20.0
kedalaman_aman = kedalaman <= batas_maks
print(f"Kedalaman aman: {kedalaman_aman}")
baterai_lemah = baterai < batas_baterai
print(f"Baterai lemah: {baterai_lemah}")