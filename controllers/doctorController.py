from DAO.doctorDAO import DoctorDAO
from flask import request

def verDoctor():
    doctores = DoctorDAO.ver()
    if doctores:
        return doctores
    else:
        return [{"error": "No se encontraron doctores"}]
