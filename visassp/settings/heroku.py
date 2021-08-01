#importar a biblioteca environ
import environ

#Importar os arquivos do arquivo base.py
from visassp.settings.base import *

#Criando uma instância da classe env
env = environ.Env()

#Quatro atribuições de valores para quatro variáveis, que já estão no arquivo base, porém
#neste Heroku.py ele modifica para poder acessar online, quando for usar localmente ele
#utiliza este arquivo.
DEBUG = env.bool("DEBUG", False)
#estamos configurando um valor padrão de false. Transforma em booleano


SECRET_KEY = env("SECRET_KEY")


ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
    "default": env.db(),
}