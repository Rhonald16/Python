

#*Longigtud entre 6 y 20 caracteres
#*Debe contener al menos 1 numero 
#*Debe contener al menos 2 numeros
#*Debe contener al menos un caracter especial
#*No puede contener espacios


import re


class Usuario:
    def __init__(self):
        self.usuario = None
        self.pas = None

    def set_usuario(self, usuario):
        self.usuario = usuario

    def set_pas(self, pas):
        valida_pass = self.validar_pass(pas)
        if valida_pass:
            self.pas=pas
            print("Se ha actualizado la contraseña")
            
        else:
            print("Contraseña incorrecta!!!")
            

    def get_usuario(self):
        return self.usuario
    
    def get_pas(self):
        return self.pas


    def validar_pass(self, pas):
        # Validar Longigtud entre 6 y 20 caracteres
        if not (6 <= len(pas.replace('  ', '')) <= 20):
            return False

        # Validar contener al menos 1 numero
        any_number_regex = "[0-9]"
        if not re.search(any_number_regex, pas):
            return False

        # Validar contener al menos 2 Mayusculas
        any_capital_letter = "[A-Z]"
        capital_letter = re.findall(any_capital_letter, pas)
        if not len(capital_letter) >= 2:
            return False

        # Validar contener al menos 1 caracter espacial
        spacial_ch_regex = "[$#%&/()=!<>]"
        if not re.search(spacial_ch_regex, pas):
            return False

        # Validar contener al menos 1 caracter espacial
        blank_space_regex = "[\s]"
        if re.search(blank_space_regex, pas):
            return False

        return True


user1 = Usuario()

user1.set_usuario("Userprueba")
user1.set_pas("Hola$coMoteva9")
