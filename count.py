import os

# Obtém o diretório onde o script está localizado
pasta_atual = os.path.dirname(os.path.abspath(__file__))

# Lista todos os arquivos na pasta que terminam com .txt
arquivos_txt = [f for f in os.listdir(pasta_atual) if f.lower().endswith('.txt')]

# Conta e exibe o resultado
print(f"Quantidade de arquivos .txt na pasta: {len(arquivos_txt)}")
