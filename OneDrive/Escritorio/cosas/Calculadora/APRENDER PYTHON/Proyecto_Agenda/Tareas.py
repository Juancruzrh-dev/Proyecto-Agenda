

class TareaMalIndexada(Exception):
    def __init__(self, tarea):
        self.tarea = tarea
        super().__init__("La nueva tarea ingresada debe tener al menos 3 caracteres")

class TareaRepetida(Exception):
    def __init__(self, tarea):
        self.tarea = tarea
        super().__init__("La nueva tarea ingresada ya se encuentra en el registro")

class TareaNoExistente(Exception):
    def __init__(self, tarea):
        self.tarea = tarea
        super().__init__("La taraa que buscas no existe")



class Agenda_Tareas:

    def __init__(self):
        self.disc = {}
  

    def CrearTareaNueva(self, tarea, fecha, **kwargs):
        if len(tarea) < 3:
            raise TareaMalIndexada(tarea)
        if tarea in self.disc:
            raise TareaRepetida(tarea)
         
        self.disc[tarea] = {"Estado:": "Incompleta", "Tiempo limite de:": fecha,}
       
        for clave, valor in kwargs.items():
            self.disc[tarea][clave] = valor
        
        print (f"La tarea {tarea} fue agregada.")

    def MarcarComoCompletada(self, tarea):
        if tarea not in self.disc:
            raise TareaNoExistente(tarea)
        
        self.disc[tarea]["Estado:"] = "Completada"
        
        print (f"La tarea {tarea} fue completada con exito.")

    def BorrarTarea(self, tarea):
        if tarea not in self.disc:
            raise TareaNoExistente(tarea)

        self.disc.pop(tarea)
        
        print (f"La tarea {tarea} fue borrada con exito.")

    def MosrarAgendaCompleta(self):
        for clave, valor in self.disc.items():
            if "descripcion" in valor:
                print (f"{clave} - {valor["Estado:"]} - {valor["Tiempo limite de:"]} - {valor["descripcion"]}")
            else:
                print (f"{clave} - {valor["Estado:"]} - {valor["Tiempo limite de:"]}")
            
