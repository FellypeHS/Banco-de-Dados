import random
from datetime import datetime
import os

# Funções utilitárias
def geraData():
    return datetime.now().strftime("%d/%m/%Y")

def gera_id():
    return random.randint(1000, 9999)

def limpartela():
    os.system('cls' if os.name == 'nt' else 'clear')