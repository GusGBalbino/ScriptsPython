import zipfile
import os
#(Código utilizado para ler valores de vários arquivos dentro de um .zip e retorna-los todos dentro de um mesmo arquivo .txt)


#Path onde encontra-se o arquivo .zip
file_name = r"C:/Users/Gustavo/Documents/Paths/devkmbe-5511001_05-12-2022_00_20_09.zip"

#Open the zip file
with zipfile.ZipFile(file_name, 'r') as zip_ref:
    txt_dir = ''
    for file_name in zip_ref.namelist():
        if file_name.endswith('.txt'):
            txt_dir = os.path.dirname(file_name)
            break

#Path para salvar o arquivo txt + nome do arquivo
    merged_file = r"C:/Users/Gustavo/Documents/Paths/Logs.txt"

    with open(merged_file, 'w') as outfile:
        for file_name in zip_ref.namelist():
            if file_name.endswith('.txt'):
                with zip_ref.open(file_name) as infile:

                    outfile.write(infile.read().decode('utf-8') + '\n')

    print(f"The contents of the text files have been merged into {merged_file}.")