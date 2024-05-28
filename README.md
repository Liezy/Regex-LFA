# Universidade Federal do Tocantins
## Curso de Bacharelado em Ciência da Computação
### Disciplina: Linguagens Formais e Autômatos
**Docente:** Alexandre Rossini  
**Discentes:** Daniel Reis Arruda Sales e Eliézer Alencar Moreira

---

## Trabalho 2: Implementação de Regex em Validações de Dados do Usuário

### Descrição
Este trabalho tem como objetivo implementar expressões regulares (Regex) para validação de diversos tipos de dados de usuários, incluindo nome, CPF, email e telefone.

### Arquivos do Projeto
- [Código em Python](./form.py)
- [Dados de Entrada](./form.txt)

---

### Detalhes da Implementação

#### Nome
- Deve conter apenas letras e espaços.
- **Exemplo de Regex:** `[a-zA-Z ]{1,50}`

#### CPF
- Deve seguir o formato brasileiro de CPF (###.###.###-##).
- **Exemplo de Regex:** `(\d{11}|\d{3}\.\d{3}\.\d{3}-\d{2})`

#### Email
- Deve seguir o padrão de emails válidos (e.g., user@example.com).
- **Exemplo de Regex:** `[\w\._]{2,}@[\w\._]{2,}\.[a-z]{3}`

#### Telefone
- Deve seguir o formato brasileiro de telefone, com ou sem código de área (e.g., (##) #####-#### ou #####-####).
- **Exemplo de Regex:** `(\d{11}|\(\d{2}\)\d{5}-\d{4})`

---

### Executando o Código
Para executar o código, utilize o seguinte comando no terminal:
```sh
python form.py
