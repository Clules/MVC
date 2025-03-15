
class Cita:
    def __init__(self, nombre, fecha, hora, motivo, estado):
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.estado = estado
    
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "fecha": self.fecha,
            "hora": self.hora,
            "motivo": self.motivo,
            "estado": self.estado
        }