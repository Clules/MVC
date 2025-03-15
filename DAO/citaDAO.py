from modelo.database import db
from modelo.Cita import Cita

class CitaDAO:
    @staticmethod
    def crear(cita: Cita):
        try:
            response = db.table("cita").insert(cita.to_dict()).execute()
            print(response)
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    @staticmethod
    def verCitas():
        try:
            response = db.table("cita").select("*").execute()
            return response.data
        except Exception as e:
            print(f"Error: {e}")
            return False