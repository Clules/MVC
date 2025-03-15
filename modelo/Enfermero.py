from modelo.Usuario import Usuario

class Enfermero(Usuario):
    def __init__(self, id, nombre, rol, doctor_nombre):
        super().__init__(id, nombre, rol)
        self.doctor_nombre = doctor_nombre

    def actualizarEstadoCita(self):
        pass

    def registrarSignosVitales(self):
        pass
    

    