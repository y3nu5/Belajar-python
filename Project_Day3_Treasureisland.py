print("===Welcome to Treasure Island.Your mission is to find the treasure===")

arah_jalan = input("ada dua arah mau kiri apa kanan?")

if arah_jalan == "kiri":
    print("anda memasuki danau")
    
    tindakan_danau = input("mau menunggu atau berenang")
    if tindakan_danau == "menunggu":
        print("anda menunggu di tepi danau")
    else :
        print("diserang ikan trout, game over")


    labirin = input("ada tiga pintu, mau pilih yang mana? merah, kuning atau biru?")
    if labirin == "merah":
        print ("Burned by fire.Game Over")
    elif labirin == "biru":
        print("Eaten by beasts.Game Over")
    elif labirin == "kuning":
        print("You found the treasure! You Win!")
    else :
        print("game over")
else:
    print("anda masuk ke dalam lubang, game over")

