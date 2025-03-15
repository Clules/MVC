from flask import request
from DAO.enfermeroDAO import EnfermeroDAO

def verEnfermero():
    enfermeros = EnfermeroDAO.ver()
    if enfermeros:
        return enfermeros
    else:
        return [{"error":"No se encontraron enfermeros"}]
