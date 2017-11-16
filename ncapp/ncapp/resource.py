from enum import Enum

class ResponseNC(Enum):
    message = "message"
    status = "status"
    data = "data"

class StatusNC(Enum):
    ok = "ok"
    fail = "fail"
    data = "data"

MessageNC = {
    'vacio': 'No se encontraron datos', 
    'errorServidor': 'Se presentaron errores de comunicacion con el servidor'
}