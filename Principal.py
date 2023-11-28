from Scanner import Scanner
from ASA import ASA

class Principal:
    existen_errores = False

    @staticmethod
    def main():
        Principal.ejecutar_prompt()

    @staticmethod
    def ejecutar_prompt():
        while True:
            linea = input(">>> ")
            if not linea:  # Salir con Ctrl+D o Ctrl+Z en Windows
                break
            Principal.ejecutar(linea)
            Principal.existen_errores = False

    @staticmethod
    def ejecutar(source):
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()

        # Descomenta para imprimir los tokens
        # for token in tokens:
        #     print(token)

        parser = ASA(tokens)
        parser.parse()

    @staticmethod
    def error(linea, mensaje):
        Principal.reportar(linea, "", mensaje)

    @staticmethod
    def reportar(linea, donde, mensaje):
        print(f"[linea {linea}] Error {donde}: {mensaje}", file=sys.stderr)
        Principal.existen_errores = True

# Ejecución del programa
if __name__ == "__main__":
    Principal.main()
