# Atividade-py-semana-05
Finalização do Sistema de Análise de Dados em Python, aplicando os conceitos de manipulação de arquivos, expressões regulares (regex) e tratamento de exceções estudados na aula.

# Sistema de Análise e Validação de Dados em Python

Este projeto é a entrega da **Semana 05 (Desafio Sprint 5)**. Consiste em um script Python para processamento de arquivos CSV, aplicando expressões regulares (Regex) para validação de integridade e tratamento robusto de exceções.

## 🛠️ Tecnologias e Conceitos Utilizados
- **Manipulação de Arquivos**: Uso do `with open()` para leitura segura de dados CSV.
- **Regex (`re`)**: Validação criteriosa de padrões estruturais em strings (Raw Strings).
- **Tratamento de Exceções**: Utilização do fluxo completo `try/except/else/finally`.
- **Exceção Personalizada**: Criação da classe `FormatoInvalidoError` herdando de `Exception`.
- **f-strings**: Formatação semântica e alinhada para os outputs de relatório.

## 🛡️ Justificativa das Validações (Regex)
As expressões regulares foram construídas garantindo a consistência dos dados empresariais:
- **E-mail** (`r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"`): Garante a presença de caracteres alfanuméricos (incluindo `_`, `.`, `+`, `-`), seguidos de um `@`, um domínio e a extensão separada por ponto. As âncoras `^` e `$` garantem que não haja sujeira no início ou fim.
- **CPF** (`r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"`): Força estritamente o formato pontuado `XXX.XXX.XXX-XX`. Onde `\d` representa dígitos numéricos.
- **Telefone** (`r"^\(\d{2}\)\s\d{4,5}-\d{4}$"`): Permite DDDs entre parênteses, um espaço, e números com 8 ou 9 dígitos no formato `(XX) XXXXX-XXXX` ou `(XX) XXXX-XXXX`.
- **Data** (`r"^\d{2}/\d{2}/\d{4}$"`): Restringe a entrada ao formato brasileiro de barras `DD/MM/YYYY`.

## ⚠️ Exceções Tratadas
- `FileNotFoundError`: Captura o erro caso o arquivo `dados.csv` não seja encontrado no diretório, orientando o usuário a verificar o caminho.
- `KeyError`: Verifica o cabeçalho do CSV. Se uma coluna obrigatória (como 'cpf' ou 'email') foi excluída, o programa não avança e acusa o erro de estrutura.
- `FormatoInvalidoError` (Personalizada): Acionada especificamente quando o dado da linha não bate com o Regex, capturando o erro para a lista de "Registros Inválidos" sem interromper o loop principal.
- **else/finally**: O `else` foi utilizado para gerar o relatório *apenas* se o arquivo foi lido com sucesso. O `finally` avisa que os processos de memória/sistema foram finalizados.

## 🚀 Como Executar
1. Garanta que o Python 3.x esteja instalado.
2. Certifique-se de que os arquivos `analise_dados.py` e `dados.csv` estejam no mesmo diretório.
3. No terminal, rode o comando:
   ```bash
   python analise_dados.py
