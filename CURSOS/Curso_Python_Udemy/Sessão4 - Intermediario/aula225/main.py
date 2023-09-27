# from log import LogFileMixin, LogPrintMixin

# lp = LogFileMixin()
# lp.log_error('Qualquer coisa')
# lp.log_success('Que Legal')

# lf = LogPrintMixin()
# lf.log_error('Qualquer coisa')
# lf.log_success('Que Legal')


from aula228_eletronico import Smartphone

galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('Iphone')

galaxy_s.ligar()
iphone.desligar()
