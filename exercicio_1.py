class Paciente:
    def __init__(self,id,nome,idade,telefone,sexo,cpf,endereco):
        self.__id = id
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.sexo = sexo
        self.__cpf = cpf
        self.__endereco = endereco

    def get_id(self):
        return f"ID: {self.__id}"

    def get_cpf(self):
        return f"CPF do paciente: {self.__cpf}"
    
    def get_endereco(self):
        return f"Endereço: {self.__endereco}"
    
    def __str__(self):
        print("Dados do paciente:")
        return f"ID: {self.__id}, nome: {self.nome}, idade: {self.idade}, telefone: {self.telefone}; sexo: {self.sexo}"
    
paciente1 = Paciente(1,"Sabrina Neves",21,11987763454,"feminino",44734589033,"Av. Maria Antônia")
print(paciente1)
print(paciente1.get_id())
print(paciente1.get_cpf())
print(paciente1.get_endereco())