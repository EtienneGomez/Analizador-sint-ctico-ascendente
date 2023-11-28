from Scanner import TipoToken

class ASA:
    def __init__(self, tokens):
        self.i = 0
        self.tokens = tokens
        self.preanalisis = tokens[self.i]
        self.pila = [0]
        self.hay_errores = False
        self.salir = False

    def parse(self):
        while not self.hay_errores and not self.salir:
            estado = self.pila[-1]
            tipo_token_actual = self.preanalisis.tipo
            # Imprimir el estado actual y el token actual
            print(f"Estado actual: {estado}, Token actual: {self.preanalisis}")
            if estado == 0:
                if tipo_token_actual == TipoToken.SELECT:
                    self.pila.append(2)
                    self.avanzar_token()
                else:
                    self.hay_errores = True
            elif estado == 1:
                if tipo_token_actual == TipoToken.EOF:
                    self.salir = True
                else:
                    self.hay_errores = True
            elif estado == 2:
                if tipo_token_actual == TipoToken.IDENTIFICADOR:
                    self.pila.append(9)
                    self.avanzar_token()
                elif tipo_token_actual == TipoToken.ASTERISCO:
                    self.pila.append(6)
                    self.avanzar_token()
                elif tipo_token_actual == TipoToken.DISTINCT:
                    self.pila.append(4)
                    self.avanzar_token()
                else:
                    self.hay_errores = True
            elif estado == 3:
                if tipo_token_actual == TipoToken.FROM:
                        self.pila.append(10)
                        self.avanzar_token()
                else:
                        self.hay_errores = True
            elif estado == 4:
                    if tipo_token_actual == TipoToken.IDENTIFICADOR:
                        self.pila.append(9)
                        self.avanzar_token()
                    elif tipo_token_actual == TipoToken.ASTERISCO:
                        self.pila.append(6)
                        self.avanzar_token()
                    else:
                        self.hay_errores = True
            elif estado == 5:
                    if tipo_token_actual == TipoToken.FROM:
                        self.pila.pop()
                    if self.pila[-1] == 2:
                            self.pila.append(3)
                    else:
                            self.hay_errores = True
            elif estado == 6:
                if tipo_token_actual == TipoToken.FROM:
                    self.pila.pop()
                    if self.pila[-1] == 2:
                        self.pila.append(5)
                    elif self.pila[-1] == 4:
                        self.pila.append(18)
                    else:
                        self.hay_errores = True
                else:
                    self.hay_errores = True
            elif estado == 7:
                if tipo_token_actual == TipoToken.COMA:
                    self.pila.append(22)
                    self.avanzar_token()
                elif tipo_token_actual == TipoToken.FROM:
                    self.pila.pop()
                    if self.pila[-1] == 2:
                        self.pila.append(5)
                    elif self.pila[-1] == 4:
                        self.pila.append(18)
                    else:
                        self.hay_errores = True
                else:
                    self.hay_errores = True
            elif estado == 8:
                if tipo_token_actual in [TipoToken.COMA, TipoToken.FROM]:
                    self.pila.pop()
                    if self.pila[-1] == 2 or self.pila[-1] == 4:
                        self.pila.append(7)
                    else:
                        self.hay_errores = True
                else:
                    self.hay_errores = True
            elif estado == 9:
                    if tipo_token_actual == TipoToken.PUNTO:
                        self.pila.append(20)
                        self.avanzar_token()
                    elif tipo_token_actual in [TipoToken.COMA, TipoToken.FROM]:
                        self.pila.append(19)
                    else:
                        self.hay_errores = True
            elif estado == 10:
                if tipo_token_actual == TipoToken.IDENTIFICADOR:
                    self.pila.append(13)
                    self.avanzar_token()
                else:
                    self.hay_errores = True
            elif estado == 11:
                if tipo_token_actual == TipoToken.COMA:
                    self.pila.append(14)
                    self.avanzar_token()
                elif tipo_token_actual == TipoToken.EOF:
                    # Reducción de 1 (Q -> select D from T)
                    self.pila.pop()  # Elimina 4 elementos de la pila para emparejar con la producción
                    self.pila.pop()
                    self.pila.pop()
                    self.pila.pop()
                    if self.pila[-1] == 0:
                        self.pila.append(1)
                    else:
                        self.hay_errores = True
                else:
                    self.hay_errores = True
            elif estado == 12:
                if tipo_token_actual in [TipoToken.COMA, TipoToken.EOF]:
                    # Reducción de 12 (T -> T1)
                    self.pila.pop()
                    if self.pila[-1] == 10:
                        self.pila.append(11)
                    else:
                        self.hay_errores = True
                else:
                    self.hay_errores = True
            elif estado == 13:
                if tipo_token_actual == TipoToken.IDENTIFICADOR:
                    self.pila.append(17)
                    self.avanzar_token()
                elif tipo_token_actual in [TipoToken.COMA, TipoToken.EOF]:
                    # Reducción de 15 (T2 -> Epsilon)
                    self.pila.append(16)
                else:
                    self.hay_errores = True
            elif estado == 14:
                if tipo_token_actual == TipoToken.IDENTIFICADOR:
                    self.pila.append(13)
                    self.avanzar_token()
                else:
                    self.hay_errores = True
            elif estado == 15:
                if tipo_token_actual in [TipoToken.COMA, TipoToken.EOF]:
                    # Reducción de 11 (T -> T, T1)
                    self.pila.pop()
                    self.pila.pop()
                    self.pila.pop()
                    if self.pila[-1] == 10:
                        self.pila.append(11)
                    else:
                        self.hay_errores = True
                else:
                    self.hay_errores = True
            elif estado == 16:
                if tipo_token_actual in [TipoToken.COMA, TipoToken.EOF]:
                    # Reducción de 13 (T1 -> id T2)
                    self.pila.pop()
                    self.pila.pop()
                    if self.pila[-1] == 10:
                        self.pila.append(12)
                    elif self.pila[-1] == 14:
                        self.pila.append(15)
                    else:
                        self.hay_errores = True
                else:
                    self.hay_errores = True
            elif estado == 17:
                if tipo_token_actual in [TipoToken.COMA, TipoToken.EOF]:
                    # Reducción de 14 (T2 -> id)
                    self.pila.pop()
                    if self.pila[-1] == 13:
                        self.pila.append(16)
                    else:
                        self.hay_errores = True
                else:
                    self.hay_errores = True
            elif estado == 18:
                if tipo_token_actual == TipoToken.FROM:
                    # Reducción de 2 (D -> distinct P)
                    self.pila.pop()
                    self.pila.pop()
                    if self.pila[-1] == 2:
                        self.pila.append(3)
                    else:
                        self.hay_errores = True
                else:
                    self.hay_errores = True
            elif estado == 19:
                if tipo_token_actual in [TipoToken.COMA, TipoToken.FROM]:
                    # Reducción de 8 (A1 -> id A2)
                    self.pila.pop()
                    self.pila.pop()
                    if self.pila[-1] in [2, 4]:
                        self.pila.append(8)
                    elif self.pila[-1] == 22:
                        self.pila.append(23)
                    else:
                        self.hay_errores = True
                else:
                    self.hay_errores = True
            elif estado == 20:
                if tipo_token_actual == TipoToken.IDENTIFICADOR:
                    self.pila.append(21)
                    self.avanzar_token()
                else:
                    self.hay_errores = True

            elif estado == 21:
                if tipo_token_actual in [TipoToken.COMA, TipoToken.FROM]:
                    # Reducción de 9 (A2 -> . id)
                    self.pila.pop()
                    self.pila.pop()
                    if self.pila[-1] == 9:
                        self.pila.append(19)
                    else:
                        self.hay_errores = True
                else:
                    self.hay_errores = True
            elif estado == 22:
                if tipo_token_actual == TipoToken.IDENTIFICADOR:
                    self.pila.append(9)
                    self.avanzar_token()
                else:
                    self.hay_errores = True
            elif estado == 23:
                if tipo_token_actual in [TipoToken.COMA, TipoToken.FROM]:
                    # Reducción de 6 (A -> A, A1)
                    self.pila.pop()
                    self.pila.pop()
                    self.pila.pop()
                    if self.pila[-1] in [2, 4]:
                        self.pila.append(7)
                    else:
                        self.hay_errores = True
                else:
                    self.hay_errores = True
            print(f"Estado de la pila: {self.pila}")
            # Continuar con los demás casos del 'switch'...
                
        if self.hay_errores:
            print("Consulta inválida")
            return False
        else:
            print("Consulta correcta")
            return True

    def avanzar_token(self):
        self.i += 1
        if self.i < len(self.tokens):
            self.preanalisis = self.tokens[self.i]
        else:
            self.preanalisis = None  # O manejar el final de los tokens de alguna manera

# Suponiendo que 'tokens' es una lista de objetos Token
# analizador = ASA(tokens)
# analizador.parse()
