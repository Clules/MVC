from modelo.Usuario import Usuario

class Medico(Usuario):
    def __init__(self, id, nombre, rol, horario):
        super().__init__(id, nombre, rol)
        self.horario = horario

    def revisarCitas(self):
        pass

    def aceptarCitas(self):
        pass

    def actualizarEstadoConsulta(self):
        pass
