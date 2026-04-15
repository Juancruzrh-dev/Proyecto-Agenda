import Tareas
import Json

class Menu:
    
    def Mostrar_Opciones(self):
        print ("Hola esta es tu agenda diaria")
        print ("Que quieres hacer hoy...")
        print ("Opcion 1: Agregar nueva tarea ")
        print ("Opcion 2: Marcar una tarea como realizada")
        print ("Opcion 3: Borrar tarea especifica")
        print ("Opcion 4: Mostrar la lista de tareas")
        print ("Opcion 5: Salir")

        return int(input("Que opcion elegirar..."))

    
    def Desiciones(self, t):
        while True:
            opcion = self.Mostrar_Opciones()
    
            if opcion == 1:
                tarea = input("Cual es el nombre de la tarea a agregar")
                fecha = input("Cuantos dias te quieres poner como maximo para completarla")
                descripcion = input("Quieres agregar alguna descripcion? Si no solo apreta enter")
                if descripcion:
                    t.CrearTareaNueva(tarea, fecha, descripcion=descripcion)
                else:
                    t.CrearTareaNueva(tarea, fecha)
        
            elif opcion == 2:
                tarea = input("Cual es el nombre de la tarea a marcar como completada")
                t.MarcarComoCompletada(tarea)

            elif opcion == 3:
                tarea = input("Cual es el nombre de la tarea a borrar")
                t.BorrarTarea(tarea)


            elif opcion == 4:
                t.MosrarAgendaCompleta()

            elif opcion == 5:
                break

            else:
                print ("Accion mal indexada")

t = Tareas.Agenda_Tareas()
t.disc = Json.Carga()

m = Menu()
m.Desiciones(t)

Json.Descarga(t.disc)









