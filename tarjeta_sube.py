#exepciones
class EstadoNoExistenteException(Exception):
    pass

class UsuarioDesactivadoException(Exception):
    pass

class NoHaySaldoException(Exception):
    pass

#contantes
PRIMARIO = "primario"
SECUNDARIO = "secundario"
UNIVERSITARIO = "universitario"
JUBILADO = "jubilado"
DESACTIVADO = "desactivado"
ACTIVADO = "activado"
PRECIO_TICKET = 70



DESCUENTOS = {
    PRIMARIO: 50,
    SECUNDARIO: 40,
    UNIVERSITARIO: 30,
    JUBILADO: 25,
}

class Sube():
    def __init__(self):
        self.saldo = 0
        self.estado = ACTIVADO
        self.grupo_beneficiario = None

    def obtener_precio_ticket(self):
        precio_total = PRECIO_TICKET
        if self.grupo_beneficiario is not None:
            precio_total = PRECIO_TICKET
            descuento = DESCUENTOS[self.grupo_beneficiario]
            precio_total = PRECIO_TICKET - ((PRECIO_TICKET* descuento)/100)    
        return precio_total
    
    def cambiar_estado(self,estado_cambio):
       self.estado = estado_cambio
       if self.estado != ACTIVADO and self.estado != DESACTIVADO:
           raise EstadoNoExistenteException()

    def pagar_pasaje(self):
        descuento = self.obtener_precio_ticket()
        if self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException()
        elif self.saldo < descuento:
            raise NoHaySaldoException()
        else:
            self.saldo = self.saldo - descuento
            return self.saldo    
            