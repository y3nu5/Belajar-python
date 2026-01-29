# game = 3
# enemies = ["goblin", "troll", "dragon"]

# def enemy_selection():
#     # if, while, dll tidak membuat variabel menjadi lokal tetap global, kecuali dibuat fungsi
#     if game < 5:
#         enemy = enemies[0]
#         print("An enemy appears:", enemy)

# enemy_selection()
# enemies = 1

# def increase_enemies(enemies):
#     #membuat variabel baru di dalam fungsi
#     enemies = 2
#     print ("enemies is :", enemies)

# increase_enemies(enemies)
# print("enemies is :", enemies)


# enemies = 1

# def increase_enemies():
#     #tidak disarankan menggunakan global variable karena dapat membingungkan
#     global enemies
#     enemies += 1
#     print ("enemies is :", enemies)

# increase_enemies()
# print("enemies is :", enemies)

#alih alih menggunakan return value
# enemies = 1

# def increase_enemies(enemy):
#     return enemy + 1

# print(enemies)
# enemies = increase_enemies(enemies)
# print (f"jumlah musuh {enemies}")

#parameter argumen
def sapa(nama, umur):
    return (f"halo saya {nama}, umur {umur}")

print(sapa(nama = "Yunus",umur = 12))

#parameter kunci atau value
def sapa(nama = "Gunawan", pesan = "selamat hari raya idul fitri"):
    return (f"halo saya {nama}, mengucapkan {pesan}")

print(sapa())

#parameter *args (dengan inputan data bertipe tuple)
def sapa(*nama):
    return (f"halo {nama}")

print(sapa("Yunus", "Angga", "Izhar"))
    
#parameter  **kwargs (dengan inputan data bertipe dictionary)
# def sapa(**info):
#     for key, value in info.items():
#         return (f"yang merasa dipannggil maju kedepan {key} : {value}")

# print(sapa(nama="Yunus", umur=12, nomor_urut=1))

    
def sapa(**info):
    for key, value in info.items():
        print (f"{key} : {value}")

    print (f"yang merasa dipanggil maju kedepan {key} : {value}")

sapa(
    nama="Yunus", 
    umur=12, 
    nomor_urut=1
)


