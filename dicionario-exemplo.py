usuario = {
    "nome" : "Natalia Neves",
    "idade" : 19,
    "cidade" : "Ferraz de Vasconcelos",
    "premium": True
} 

def exibir_perfil(dados_usuarios):
    print("\n=== PERFIL DO USUÁRIO ===")
    print(f"Nome: {dados_usuarios['nome']}")
    print(f"Idade: {dados_usuarios['idade']} anos")
    print(f"Cidade: {dados_usuarios['cidade']}")

    if dados_usuarios["premium"]:
        print("Status: Usuarios VIP ⭐")
    else:
        print("Status:Conta Gratuita")
    print("=========================\n")

exibir_perfil(usuario)

print("...Atualizando dados usuarios...")
usuario["cidade"] = "Belo Horizonte"
usuario["idade"] = 21
usuario["profissão"] = "Desenvolvedora"

exibir_perfil(usuario)
print(f"Profissao cadastrada: {usuario['profissão']}")

exibir_perfil(usuario)