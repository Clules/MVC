from modelo.database import db
from modelo.Medico import Medico

class DoctorDAO:
    @staticmethod
    def ver():
        try:
            response = db.table("doctor").select("*").execute()
            return response.data
        except Exception as e:
            print(f"Error: {e}")
            return False
