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

# Ejemplo de uso:
# print(TipoToken.SELECT)  # Imprimirá: TipoToken.SELECT
# print(TipoToken.SELECT.value)  # Imprimirá: SELECT
