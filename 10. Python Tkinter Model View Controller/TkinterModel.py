import re

class Model:
    def __init__(self, email):
        self.email= email

    @property # getter
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f"Endereço de Email Inválido: {value}")
        
    def save(self):
        with open(r'G:\Users\Bruno\Desktop\email.txt', "a") as f:  # a: append | Adiciona emails ao arquivo emails.txt, sem apagar os anteriores
            f.write(self.email + "\n")