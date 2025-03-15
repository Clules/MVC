from modelo.database import db

class EnfermeroDAO:
    @staticmethod
    def ver():
        try:
            response = (
                db.from_("enfermero")
                .select("nombre, rol, doctor_nombre")
                .execute()
            )

            enfermeros = response.data  
            print("Datos obtenidos:", enfermeros) 
            return enfermeros
        except Exception as e:
            print(f"Error: {e}")
            return []