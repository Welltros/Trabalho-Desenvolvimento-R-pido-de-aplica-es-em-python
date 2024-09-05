import sqlite3 as conector

def conectar_banco():
    conexao = conector.connect('academia.db')
    cursor = conexao.cursor()
    # Aqui você pode adicionar uma instrução SQL se desejar consultar dados
    # cursor.execute("SELECT * FROM cadastro")
    # registros = cursor.fetchall()  # Obtém todos os registros retornados
    conexao.commit()  # Necessário apenas para operações que alteram o banco
    cursor.close()
    conexao.close()
    print('Abrindo uma conexão de BD')

def criar_tabela():
    conexao = conector.connect('academia.db')
    cursor = conexao.cursor()
    
    sql = "DROP TABLE IF EXISTS cadastro"  # Use DROP TABLE IF EXISTS para evitar erro se a tabela não existir
    cursor.execute(sql)
    
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Abra a pasta do programa e veja se o arquivo está lá")
    print("Fim do programa")

# Chamada das funções
conectar_banco()
criar_tabela()
