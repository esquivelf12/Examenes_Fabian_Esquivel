class Persona:
    def __init__(self, nombre, saldo=0):
        self.nombre = nombre
        self.saldo = saldo

    def consultar_saldo(self):
        """Muestra y devuelve el saldo actual."""
        print(f"Saldo de {self.nombre}: S/ {self.saldo:.2f}")
        return self.saldo

    def transferir(self, destino, monto):
        """Transfiere 'monto' de esta persona a 'destino'.
        Devuelve True si se realizó, False si fue rechazada."""

        # 1) El destinatario debe ser una Persona
        if not isinstance(destino, Persona):
            print("Transferencia rechazada: el destinatario no es válido.")
            return False

        # 2) El monto debe ser numérico (bool cuenta como int en Python, lo excluimos)
        if isinstance(monto, bool) or not isinstance(monto, (int, float)):
            print("Transferencia rechazada: el monto debe ser un número.")
            return False

        # 3) El monto debe ser mayor que cero
        if monto <= 0:
            print("Transferencia rechazada: el monto debe ser mayor que cero.")
            return False

        # 4) El monto no puede superar el saldo disponible
        if monto > self.saldo:
            print(f"Transferencia rechazada: saldo insuficiente "
                  f"({self.nombre} tiene S/ {self.saldo:.2f}).")
            return False

        # Si pasó todas las validaciones, se ejecuta la operación
        self.saldo -= monto
        destino.saldo += monto
        print(f"Transferencia exitosa: {self.nombre} envió "
              f"S/ {monto:.2f} a {destino.nombre}.")
        return True


carlos = Persona("Carlos", 4500)
airon = Persona("Airon", 2200)

print("--- Saldos iniciales ---")
carlos.consultar_saldo()
airon.consultar_saldo()

print("\n--- Transferencia válida ---")
carlos.transferir(airon, 900)

print("\n--- Transferencia rechazada (supera el saldo) ---")
carlos.transferir(airon, 3800)

print("\n--- Otros intentos rechazados ---")
carlos.transferir(airon, "abc")
carlos.transferir(airon, -210)
carlos.transferir(airon, 0)

print("\n--- Saldos finales ---")
carlos.consultar_saldo()
airon.consultar_saldo()