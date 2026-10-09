import csv
import re
import os

class FormatoInvalidoError(Exception):
    def __init__(self, campo, valor, mensagem="Formato inválido"):
        self.campo = campo
        self.valor = valor
        self.mensagem = f"{mensagem} para o campo '{campo}': {valor}"
        super().__init__(self.mensagem)

def validar_email(email):
    padrao = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(padrao, email):
        raise FormatoInvalidoError("E-mail", email)

def validar_cpf(cpf):
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    if not re.match(padrao, cpf):
        raise FormatoInvalidoError("CPF", cpf, "O CPF deve estar no formato XXX.XXX.XXX-XX")

def validar_telefone(telefone):
    padrao = r"^\(\d{2}\)\s\d{4,5}-\d{4}$"
    if not re.match(padrao, telefone):
        raise FormatoInvalidoError("Telefone", telefone, "Formato esperado: (XX) XXXXX-XXXX")

def validar_data(data):
    padrao = r"^\d{2}/\d{2}/\d{4}$"
    if not re.match(padrao, data):
        raise FormatoInvalidoError("Data de Nascimento", data, "Formato esperado: DD/MM/YYYY")

def gerar_relatorio(total, validos, invalidos):
    print("\n" + "="*50)
    print("      RELATÓRIO DE ANÁLISE DE DADOS      ")
    print("="*50)
    
    print(f"\n📊 ESTATÍSTICAS:")
    print(f"- Total de registros analisados: {total}")
    print(f"- Registros VÁLIDOS: {len(validos)}")
    print(f"- Registros INVÁLIDOS: {len(invalidos)}")
    
    if validos:
        print("\n✅ REGISTROS APROVADOS:")
        for reg in validos:
            print(f"  - {reg['nome']} | {reg['email']} | {reg['cpf']}")
            
    if invalidos:
        print("\n❌ REGISTROS COM ERRO:")
        for erro in invalidos:
            print(f"  - Linha {erro['linha']} ({erro['nome']}): {erro['motivo']}")
    
    print("\n" + "="*50)

def processar_arquivo(caminho_arquivo):
    registros_validos = []
    registros_invalidos = []
    total_linhas = 0

    try:
        print(f"[Sistema] Iniciando leitura do arquivo: {caminho_arquivo}...")
        with open(caminho_arquivo, mode='r', encoding='utf-8') as file:
            leitor_csv = csv.DictReader(file)

            colunas_obrigatorias = ['nome', 'email', 'cpf', 'telefone', 'data_nascimento']
            for coluna in colunas_obrigatorias:
                if coluna not in leitor_csv.fieldnames:
                    raise KeyError(f"A coluna obrigatória '{coluna}' não foi encontrada no arquivo CSV.")

            for linha_num, linha in enumerate(leitor_csv, start=2): 
                total_linhas += 1
                try:
                    validar_email(linha['email'])
                    validar_cpf(linha['cpf'])
                    validar_telefone(linha['telefone'])
                    validar_data(linha['data_nascimento'])
                    
                    registros_validos.append(linha)
                    
                except FormatoInvalidoError as erro:
                    registros_invalidos.append({
                        'linha': linha_num,
                        'nome': linha.get('nome', 'Desconhecido'),
                        'motivo': erro.mensagem
                    })
                except ValueError as erro:
                    registros_invalidos.append({
                        'linha': linha_num,
                        'nome': linha.get('nome', 'Desconhecido'),
                        'motivo': f"Erro de valor: {erro}"
                    })

    except FileNotFoundError:
        print(f"\n[ERRO CRÍTICO] O arquivo '{caminho_arquivo}' não foi encontrado.")
        print("Verifique se o nome está correto e se ele está na mesma pasta do script.")
    except KeyError as erro:
        print(f"\n[ERRO DE ESTRUTURA] {erro}")
    except Exception as erro:
        print(f"\n[ERRO INESPERADO] Ocorreu um erro não mapeado: {erro}")
    
    else:
        gerar_relatorio(total_linhas, registros_validos, registros_invalidos)
    
    finally:
        print("\n[Sistema] O processamento foi encerrado.")

if __name__ == "__main__":
    arquivo = "dados.csv"
    processar_arquivo(arquivo)