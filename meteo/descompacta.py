import zipfile
import os

# Caminho para o arquivo ZIP e pasta de destino
zip_file_path = r'C:\Users\Back\OneDrive - Ensino Lusófona\Apps\Documents\Universidade\2_ano\2_semestre\PW\pratica\icons_ipma_weather.zip'
destination_path = 'static/meteo'

# Certifique-se de que a pasta de destino existe
os.makedirs(destination_path, exist_ok=True)

# Descompactar o arquivo ZIP
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(destination_path)

print(f"Arquivos descompactados em {destination_path}")
