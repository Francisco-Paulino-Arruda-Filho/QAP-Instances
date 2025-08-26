import os
import pandas as pd

pasta_atual = os.path.dirname(os.path.abspath(__file__))

arquivos_txt = [f for f in os.listdir(pasta_atual) if f.lower().endswith('.txt')]

print(f"Quantidade de arquivos .txt na pasta: {len(arquivos_txt)}")

arquivos_csv = [f for f in os.listdir(pasta_atual) if f.lower().endswith('.csv')]
print(f"Quantidade de arquivos .csv na pasta: {len(arquivos_csv)}")

# Caminhos
csv_path = "solutions.csv"   # seu CSV padronizado
txt_folder = "."  # pasta com os arquivos .txt

# 1. Carrega o dataset
df = pd.read_csv(csv_path, sep=";")

# 2. Pega os nomes do dataset
dataset_names = set(df["name"].str.strip())

# 3. Lista todos os arquivos txt na pasta
txt_files = [f for f in os.listdir(txt_folder) if f.endswith(".txt")]

# 4. Extrai só os nomes sem extensão
txt_names = set(os.path.splitext(f)[0] for f in txt_files)

# 5. Verifica o que tem nos txt mas não no dataset
missing_in_dataset = txt_names - dataset_names

# 6. Mostra resultados
if missing_in_dataset:
    print("Arquivos TXT que não estão no dataset:")
    for name in sorted(missing_in_dataset):
        print(name)
else:
    print("Todos os arquivos TXT estão no dataset.")
