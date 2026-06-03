import mysql.connector

# Objeto de conexão com o banco de dados MySQL
con = mysql.connector.connect(
    host="localhost",
    database="academia",
    user="root",
    password="1341408544"
)

# Verificar se a conexão foi estabelecida com sucesso
if con.is_connected():
    db_Info = con.get_server_info()
    print("Conexão com o banco de dados MySQL estabelecida com sucesso!")
    print(f'Informações do servidor: {db_Info}')
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print(f'Conectado ao banco de dados: {linha}')

# Fechar a conexão com o banco de dados
if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão com o banco de dados MySQL fechada.")