import re

def validar_nome(nome):
    return bool(re.fullmatch(r"[a-zA-Z ]{1,50}", nome))

def validar_cpf(cpf):
    return bool(re.fullmatch(r"(\d{11}|\d{3}\.\d{3}\.\d{3}-\d{2})", cpf))

def validar_email(email):
    return bool(re.fullmatch(r"[\w\._]{2,}@[\w\._]{2,}\.[a-z]{3}", email))

def validar_telefone(telefone):
    return bool(re.fullmatch(r"(\d{11}|\(\d{2}\)\d{5}-\d{4})", telefone))

def validar_formulario(nome, cpf, email, telefone):
    return (validar_nome(nome) and
            validar_cpf(cpf) and
            validar_email(email) and
            validar_telefone(telefone))

def ler_dados_do_arquivo(caminho_arquivo):
    dados = {}
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        for linha in file:
            if ':' in linha:
                chave, valor = linha.split(':', 1)
                dados[chave.strip()] = valor.strip()
    return dados

caminho_arquivo = 'form.txt'
dados = ler_dados_do_arquivo(caminho_arquivo)

print("Dados lidos do arquivo:")
print(dados)

# TESTE para validar cada campo individualmente e imprimir o resultado
nome_valido = validar_nome(dados.get('nome', ''))
cpf_valido = validar_cpf(dados.get('cpf', ''))
email_valido = validar_email(dados.get('email', ''))
telefone_valido = validar_telefone(dados.get('telefone', ''))

print(f"Nome válido: {nome_valido}")
print(f"CPF válido: {cpf_valido}")
print(f"Email válido: {email_valido}")
print(f"Telefone válido: {telefone_valido}")

if nome_valido and cpf_valido and email_valido and telefone_valido:
    print("Formulário válido")
else:
    print("Formulário inválido")
