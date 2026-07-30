class cuentaBancaria:
    def __init__(self,Titular, Saldo):
        self._Saldo = Saldo
        self.Titular = Titular

cuenta = cuentaBancaria("Prado", 1_000_000)
print(f"{cuenta._Saldo:,.0f}")