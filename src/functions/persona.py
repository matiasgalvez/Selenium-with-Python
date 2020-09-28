class Persona:

    def __init__(self, nombre, apellido, dni, email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email

    def mostrar_valores(self):
        print(f"El nombre de la personas es: {self.nombre}")
        print(f"El apellido de la personas es: {self.apellido}")
        print(f"El dni de la personas es: {self.dni}")
        print(f"El email de la personas es: {self.email}")


persona1 = Persona("Matias", "Galvez", "37500685", "aosnfaojfnajofn")
persona2 = Persona("Pamela", "Quintana", "37100917", "pqblablabla@gmail.com")
persona1.mostrar_valores()
persona2.mostrar_valores()

