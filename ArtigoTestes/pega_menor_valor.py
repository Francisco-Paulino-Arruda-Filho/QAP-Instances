import os
import pandas as pd

# Pega o diretório onde o script está localizado
pasta_atual = os.path.dirname(os.path.abspath(__file__))

# Lista apenas os arquivos da própria pasta (sem subpastas)
arquivos = [
    f for f in os.listdir(pasta_atual)
    if f.startswith("resultados_") and f.endswith(".csv")
]

melhores = []

for arquivo in arquivos:
    caminho = os.path.join(pasta_atual, arquivo)

    # Detectar separador automaticamente
    with open(caminho, "r", encoding="utf-8") as f:
        primeira_linha = f.readline()
        sep = ";" if ";" in primeira_linha else ","

    try:
        df = pd.read_csv(caminho, sep=sep)
    except Exception as e:
        print(f"Erro lendo {arquivo}: {e}")
        continue

    # Padronizar nomes de colunas
    df.columns = [c.strip().lower() for c in df.columns]

    if "custo" not in df.columns:
        print(f"Coluna 'custo' não encontrada em {arquivo}")
        continue

    # Detectar algoritmo pelas colunas
    colunas = set(df.columns)
    if {"n_formigas", "alpha", "beta", "rho"}.issubset(colunas):
        algoritmo = "ACO"
    elif {"mu", "lambd", "taxa_mutacao"}.issubset(colunas):
        algoritmo = "ES_SA"
    else:
        algoritmo = "ES_VND"

    # Extrair instância do nome do arquivo
    nome = os.path.splitext(arquivo)[0]
    partes = nome.split("_")
    instancia = partes[1] if len(partes) > 1 else "?"

    menor_custo = df["custo"].min()

    melhores.append({
        "instancia": instancia,
        "algoritmo": algoritmo,
        "menor_custo": menor_custo
    })

# Gera e salva o CSV final na mesma pasta do script
resultado_df = pd.DataFrame(melhores)
resultado_df = resultado_df.sort_values(["instancia", "algoritmo"])
print(resultado_df.to_string(index=False))

saida_csv = os.path.join(pasta_atual, "melhores_resultados.csv")
resultado_df.to_csv(saida_csv, index=False)
print(f"\nArquivo salvo em: {saida_csv}")
