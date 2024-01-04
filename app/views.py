from app import controllers
from app.utils import validar_senha, validar_email

def exibir_pagina_login():
    print("=== Página de Login ===")
    email = input("Digite o seu email: ")

    while not validar_email(email):
        print("E-mail inválido.")
        email = input("Digite um e-mail válido: ")

    senha = input("Digite a sua senha: ")

    usuario_logado = controllers.realizar_login(email, senha)

    if usuario_logado:
        print(f"Login realizado com sucesso!")

        manter_login_salvo = input("Deseja manter o login salvo? (S/N): ").lower()
        if manter_login_salvo == "s":
            print("Login salvo com sucesso!")

            if usuario_logado.tipo_perfil == 1:
                exibir_menu_comum(usuario_logado)
            elif usuario_logado.tipo_perfil == 2:
                exibir_menu_produtor(usuario_logado)
        else:
            if usuario_logado.tipo_perfil == 1:
                exibir_menu_comum(usuario_logado)
            elif usuario_logado.tipo_perfil == 2:
                exibir_menu_produtor(usuario_logado)

def exibir_pagina_registro_usuario():
    print("=== Registro de Novo Usuário ===")
    tipo_perfil = int(input("Tipo de perfil:\n[1] Comum\n[2] Produtor: "))
    nome = input("Nome: ")
    cpf = input("CPF: ")
    email = input("Email: ")

    for usuario in controllers.usuarios_db:
        if usuario.email == email:
            print(f"Já existe um cadastro com o e-mail {email}.")
            return

    senha = input("Senha: ")

    while not validar_senha(senha):
        print("A senha não atende aos requisitos de segurança.")
        senha = input("Digite uma senha válida: ")

    novo_usuario = controllers.registrar_novo_usuario(tipo_perfil, nome, cpf, email, senha)

    if novo_usuario:
        print(f"Usuário {novo_usuario.nome} registrado com sucesso!")

        realizar_login_opcao = input("Deseja realizar login agora? (S/N): ").lower()
        if realizar_login_opcao == "s":
            exibir_pagina_login()

def exibir_pagina_registro_evento():
    print("=== Registro de Novo Evento ===")
    titulo = input("Título do evento: ")

    while any(evento.titulo == titulo for evento in controllers.eventos_db):
        print(f"Já existe um evento com o título {titulo}. Escolha um nome diferente.")
        titulo = input("Digite um novo título para o evento: ")

    categoria = input("Categoria do evento: ")
    data = input("Data do evento (YYYY-MM-DD): ")
    horario = input("Horário do evento: ")
    local = input("Local do evento: ")
    imagem = input("Caminho da imagem do evento: ")
    

    if not (titulo and categoria and data and horario and local and imagem):
        if not imagem:
            print("É necessário fornecer o caminho da imagem para concluir o cadastro.")
            return None
        else:
            print("Todos os campos obrigatórios devem ser preenchidos para concluir o cadastro.")
            return None

    descricao = input("Descrição do evento: ")

    novo_evento = controllers.registrar_novo_evento(titulo, categoria, data, horario, local, imagem, descricao)

    if novo_evento:
        print(f"Evento {novo_evento.titulo} registrado com sucesso!")

def exibir_pagina_pesquisa_eventos():
    print("=== Pesquisa de Eventos ===")
    titulo = input("Digite o título do evento (ou deixe em branco): ").strip()
    categoria = input("Digite a categoria do evento (ou deixe em branco): ").strip()
    localidade = input("Digite a localidade do evento (ou deixe em branco): ").strip()

    eventos_encontrados = controllers.pesquisar_eventos_por_filtros(titulo, categoria, localidade)

    if eventos_encontrados:
        print("Eventos encontrados:")
        for evento in eventos_encontrados:
            print(f"- {evento.titulo} ({evento.data}, {evento.horario}, {evento.local})")
    else:
        print("Nenhum evento encontrado para os filtros selecionados.")

def exibir_menu_comum(usuario_logado):
    while True:
        print("=== Menu Comum ===")
        print("1 - Localizar eventos")
        print("2 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_pagina_pesquisa_eventos()
        elif opcao == "2":
            break
        else:
            print("Opção inválida. Tente novamente.")

def exibir_menu_produtor(usuario_logado):
    while True:
        print("=== Menu Produtor ===")
        print("1 - Cadastrar eventos")
        print("2 - Localizar eventos")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_pagina_registro_evento()
        elif opcao == "2":
            exibir_pagina_pesquisa_eventos()
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

def exibir_menu_principal():
    while True:
        print("=== Gerenciador de Eventos ===")
        print("1 - Realizar login")
        print("2 - Cadastrar-se")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuario_logado = exibir_pagina_login()
            if usuario_logado:
                if usuario_logado.tipo_perfil == 1:
                    exibir_menu_comum(usuario_logado)
                elif usuario_logado.tipo_perfil == 2:
                    exibir_menu_produtor(usuario_logado)
        elif opcao == "2":
            exibir_pagina_registro_usuario()
        elif opcao == "3":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

