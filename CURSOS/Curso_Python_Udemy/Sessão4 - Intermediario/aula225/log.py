# Abstração
# Herança - é um 
# Log
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o metodo log')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')

# classe abstrata
        
# Adicionar funcionalidades na herança multipla (em outras classes)
class LogFileMixin(Log):
    # esse trexo abaixo é chamado de assinatura do método
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print("Salvando no log")
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.white('\n')


# Adicionar funcionalidades na herança multipla (em outras classes)
class LogPrintMixin(Log):
    # esse trexo abaixo é chamado de assinatura do método
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')



# Verifica se o metodo esta executando no metodo main
if __name__ == '__main__':
    lp = LogFileMixin()
    lp.log_error('Qualquer coisa')
    lp.log_success('Que Legal')

    lf = LogPrintMixin()
    lf.log_error('Qualquer coisa')
    lf.log_success('Que Legal')