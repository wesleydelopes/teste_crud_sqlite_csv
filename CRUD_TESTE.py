import sqlite3
from faker import Faker
import csv


# Criando dados fakes

fake = Faker()
nome = fake.name()
endereco = fake.address()
telefone = fake.phone_number()

# Se o arquivo nao existir, cria e conecta. Se nao só conecta

con = sqlite3.connect('example.db')
cur = con.cursor()

# Cria a tabela no banco de dados caso ela nao existir
cur.execute('''
            CREATE TABLE IF NOT EXISTS pessoas
            (nome TEXT, 
            endereço TEXT,
            telefone INT);
            ''' )


cur.execute(f'''INSERT INTO pessoas VALUES ('{nome}',
                '{endereco}',
                '{telefone}')''')



# valida as alteraçoes feitas
con.commit()

# Seleciona os dados da tabela do banco de dados e imprime na tela
#for row in cur.execute('SELECT * FROM pessoas'):
#    print(row[0])
#    print(row[1])
#    print(row[2])

   
# Obter os resultados da consulta
cur.execute('SELECT * FROM pessoas')
resultados = cur.fetchall()

# Obter os nomes das colunas
nomes_colunas = [descricao[0] for descricao in cur.description]

# Fechar a conexão com o banco de dados
con.close()

# Escrever os resultados em um arquivo CSV
with open('saida.csv', 'w', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    
    # Escrever os nomes das colunas como o cabeçalho
    writer.writerow(nomes_colunas)
    
    # Escrever os dados
    writer.writerows(resultados)

print("Dados exportados com sucesso para 'saida.csv'.")