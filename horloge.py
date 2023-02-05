import time

current_time = None
alarm_time = None

def set_time(hour, minute, second):
    global current_time
    current_time = (hour, minute, second)
    print("Heure réglée pour ", hour, ":", minute, ":", second)

def set_alarm(hour, minute, second):
    global alarm_time
    alarm_time = (hour, minute, second)
    print("Alarme réglée pour ", hour, ":", minute, ":", second)

def afficher_heure():
    global current_time
    if current_time is None:
        current_time = time.localtime()
    hour, minute, second = current_time[3], current_time[4], current_time[5]
    print("{:02d}:{:02d}:{:02d}".format(hour, minute, second))
    if alarm_time is not None and (hour, minute, second) == alarm_time:
        print("Alarme !")

while True:
    afficher_heure()
    time.sleep(1)
