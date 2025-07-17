from ics import Calendar, Event
from datetime import datetime, timedelta

cal = Calendar()

e = Event()
e.name = "Séance vélo seuil"
e.begin = datetime(2025, 7, 20, 18, 0)  # 20 juillet à 18h
e.duration = timedelta(hours=1)
e.description = "20 min échauffement\n3x10 min à 85% FTP avec 5 min récup\n10 min retour au calme"
cal.events.add(e)

with open("entrainement.ics", "w") as f:
    f.writelines(cal)