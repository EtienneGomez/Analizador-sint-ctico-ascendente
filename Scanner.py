from enum import Enum

class TipoToken(Enum):
    IDENTIFICADOR = "IDENTIFICADOR"
    SELECT = "SELECT"
    FROM = "FROM"
    DISTINCT = "DISTINCT"
    COMA = "COMA"
    PUNTO = "PUNTO"
    ASTERISCO = "ASTERISCO"
    EOF = "EOF"


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


class Scanner:
    palabras_reservadas = {
        "select": TipoToken.SELECT,
        "from": TipoToken.FROM,
        "distinct": TipoToken.DISTINCT,
    }

    def __init__(self, source):
        self.source = source + " "
        self.tokens = []

    def scan_tokens(self):
        estado = 0
        lexema = ""
        inicio_lexema = 0

        for i, caracter in enumerate(self.source):
            if estado == 0:
                if caracter == '*':
                    self.tokens.append(Token(TipoToken.ASTERISCO, "*", i + 1))
                elif caracter == ',':
                    self.tokens.append(Token(TipoToken.COMA, ",", i + 1))
                elif caracter == '.':
                    self.tokens.append(Token(TipoToken.PUNTO, ".", i + 1))
                elif caracter.isalpha():
                    estado = 1
                    lexema = lexema + caracter
                    inicio_lexema = i
            elif estado == 1:
                if caracter.isalpha() or caracter.isdigit():
                    lexema += caracter
                else:
                    tt = self.palabras_reservadas.get(lexema, TipoToken.IDENTIFICADOR)
                    self.tokens.append(Token(tt, lexema, inicio_lexema + 1))
                    estado = 0
                    i -= 1
                    lexema = ""
                    inicio_lexema = 0

        self.tokens.append(Token(TipoToken.EOF, "", len(self.source)))
        return self.tokens
