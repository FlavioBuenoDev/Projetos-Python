import contas
import pessoas

class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[pessoas.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None,
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []
    
    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False
    
    def _checa_cliente(self, clientes):
        if clientes 
        return True
    
    def _checa_conta(self, conta):
        return True

    def autenticar(self, cliente. conta):
        return True
