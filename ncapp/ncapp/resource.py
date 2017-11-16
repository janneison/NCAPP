class ResponseNC:
    message = "message"
    status = "status"
    data = "data"

class StatusNC:
    ok = "ok"
    fail = "fail"
    data = "data"

MessageNC = {
    'vacio': 'No se encontraron datos', 
    'errorServidor': 'Se presentaron errores de comunicacion con el servidor'
}