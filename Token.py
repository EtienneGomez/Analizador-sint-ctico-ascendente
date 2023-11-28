from TipoToken import TipoToken

class Token:
    def __init__(self, tipo, lexema, posicion=0):
        self.tipo = tipo
        self.lexema = lexema
        self.posicion = posicion

    def __eq__(self, otro):
        if not isinstance(otro, Token):
            return False
        return self.tipo == otro.tipo

    def __str__(self):
        return f"{self.tipo} {self.lexema} {self.posicion}"


# Ejemplo de cómo crear un token y imprimirlo
##token = Token(TipoToken.SELECT, "select", 1)
##print(token)  # Imprimirá: SELECT select 1
