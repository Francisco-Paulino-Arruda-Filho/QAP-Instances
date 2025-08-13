import os

pasta_atual = os.path.dirname(os.path.abspath(__file__))

arquivos_txt = [f for f in os.listdir(pasta_atual) if f.lower().endswith('.txt')]

print(f"Quantidade de arquivos .txt na pasta: {len(arquivos_txt)}")
