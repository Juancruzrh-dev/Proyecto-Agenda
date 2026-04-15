import json


def Carga():
    try:
        with open("Agenda.diaria.json", "r") as descarga:
            return json.load(descarga)
    except FileNotFoundError:
        return {}

def Descarga(disc):
    with open("Agenda.diaria.json", "w") as carga:
        json.dump(disc, carga)




    

