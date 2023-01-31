import threading
from datetime import datetime
import time


def heure(heures, minutes, secondes):
    if format_12:
        if heures >= 12:
            return FORMAT_HEURE.format(heures - 12, minutes, secondes) + " PM"
        else:
            return FORMAT_HEURE.format(heures, minutes, secondes) + " AM"
    else:
        return FORMAT_HEURE.format(heures, minutes, secondes)


def h():
    affichage()


def affichage():
    print(heure(heure[0], heure[1], heure[2]))


def pause():
    global heure_active
    heure_active = False


def continuer():
    global heure_active
    heure_active = True


def changer_heure(heures, minutes, secondes):
    if (0 <= heures <= 23) and (0 <= minutes <= 59) and (0 <= secondes <= 59):
        global heure
        heure = [heures, minutes, secondes]
        print("Il est :", heure(heure[0], heure[1], heure[2]) + ".")
    else:
        print("Veuillez rentrer une commande valide")


def changer_alarme(heures, minutes, secondes):
    if (0 <= heures <= 23) and (0 <= minutes <= 59) and (0 <= secondes <= 59):
        global alarme
        alarme = [heures, minutes, secondes]
        afficher_alarme()
    else:
        print("Veuillez rentrer une commande valide")


def afficher_alarme():
    if alarme[0] != -1 and alarme[1] != -1 and alarme[2] != -1:
        print("Alarme est prévu pour:", heure(alarme[0], alarme[1], alarme[2]) + ".")
    else:
        print("Aucune alamre de prévu")


def al():
    afficher_alarme()


def liste():
    print(
        "\nListe des commandes valides:\n- liste()\n- affichage() | h()\n- changer_heure(HEURES, MINUTES, SECONDES)\n- afficher_alarme() | al()\n- changer_alarme(HEURES, MINUTES, SECONDES)\n- changer_format()\n- pause()\n- continuer()\n")


def changer_format():
    global format_12
    if format_12:
        format_12 = False
    else:
        format_12 = True


def alarme():
    if heure[0] == alarme[0] and heure[1] == alarme[1] and heure[2] == alarme[2]:
        return True
    else:
        return False


def actu():
    global heure
    heure[2] += 1
    if heure[2] >= 60 or heure[2] < 0:
        heure[2] = 0
        heure[1] += 1
    if heure[1] >= 60 or heure[1] < 0:
        heure[1] = 0
        heure[0] += 1
    if heure[0] >= 24 or heure[0] < 0:
        heure[0] = 0


def accept(cmd):
    for commande in commandes_valides:
        if cmd.startswith(commande + "("):
            return True
    return False


def thread_heure():
    global heure
    while True:
        if heure_active:
            alarme()
            if alarme():
                print("Il est l'heure !")
            time.sleep(1)
            actu()


heure = [datetime.now().hour, datetime.now().minute, datetime.now().second]
format_12 = False
FORMAT_HEURE = "{:02d}:{:02d}:{:02d}"
heure_active = True
alarme = [-1, -1, -1]
commandes_valides = ["liste", "affichage", "h", "changer_heure", "afficher_alarme", "al", "changer_alarme",
                     "changer_format", "pause", "continuer"]


def horloge():
    input_thread = threading.Thread(target=thread_heure, args=())
    input_thread.start()
    print(" Application : HORLOGE !\n Pour rentrez une commande en particulier, utilisez : \" liste() \".")
    while True:
        info = "Entrez une commande\n"
        if format_12:
            info = "Format: 12H.\t" + info
        else:
            info = "Format: 24H.\t" + info
        if heure_active:
            info = "État: ACTIVE.\t" + info
        else:
            info = "État: EN PAUSE.\t" + info
        info = "\n" + info
        cmd = input(info)
        if accept(cmd):
            try:
                cmd_compiled = compile(cmd, "horloge.py", "exec")
                exec(cmd_compiled)
            except Exception as e:
                print("La commande n'est pas valide")
        else:
            print("La commande n'est pas valide")


horloge()