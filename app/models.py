class Usuario:
    def __init__(self, tipo_perfil, nome, cpf, email, senha):
        self.tipo_perfil = tipo_perfil
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.senha = senha

class Evento:
    def __init__(self, titulo, categoria, data, horario, local, descricao, imagem):
        self.titulo = titulo
        self.categoria = categoria
        self.data = data
        self.horario = horario
        self.local = local
        self.descricao = descricao
        self.imagem = imagem