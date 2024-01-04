from app.models import Usuario, Evento
from app import utils
from app import views

usuarios_db = []
eventos_db = [] 

def registrar_novo_usuario(tipo_perfil, nome, cpf, email, senha):
    if not utils.validar_senha(senha):
        print("A senha não atende aos requisitos de segurança.")
        return None

    novo_usuario = Usuario(tipo_perfil, nome, cpf, email, senha)
    usuarios_db.append(novo_usuario)
    return novo_usuario

def realizar_login(email, senha):
    usuario_encontrado = None
    for usuario in usuarios_db:
        if usuario.email == email:
            usuario_encontrado = usuario
            break

    if usuario_encontrado is None:
        print("Não há perfil cadastrado com o e-mail informado.")
        cadastrar_novo_usuario = input("Deseja realizar o cadastro? (S/N): ").lower()
        if cadastrar_novo_usuario == "s":
            views.exibir_pagina_registro_usuario()
        return None

    if not usuario_encontrado.senha == senha:
        print("Email ou senha incorretos.")
        return None

    return usuario_encontrado

def registrar_novo_evento(titulo, categoria, data, horario, local, imagem, descricao):
    novo_evento = Evento(titulo, categoria, data, horario, local, imagem, descricao)
    eventos_db.append(novo_evento)

    return novo_evento

def pesquisar_eventos_por_filtros(titulo=None, localidade=None, categoria=None):
    eventos_encontrados = []

    for evento in eventos_db:
        if titulo and titulo.lower() not in evento.titulo.lower():
            continue

        if localidade and localidade.lower() not in evento.local.lower():
            continue

        if categoria and categoria.lower() not in evento.categoria.lower():
            continue

        eventos_encontrados.append(evento)

    return eventos_encontrados