# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
         #setter
        self.user = user
        
    def set_password(self, password):
        #setter
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(msg):
        print('Log: ',msg)
    
#c1 = Connection()
c1 = Connection.create_with_auth('Flavio', '123')
#c1.set_user('Flavio')
#c1.set_password('123')
print(c1.user)
print(c1.password)
print(Connection.log('Essa é a mensagem de log'))

""" qualquer method que precisar usar self, esse methodo é um metodo de instancia """
""" diferença entre metodo normal e classmethod é que o classmethod recebe cls(classe) e o normal recebe self """