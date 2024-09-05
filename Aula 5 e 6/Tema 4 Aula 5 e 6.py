import sqlite3 as conector 
def conectar_banco():
    conexao = conector.connect('academia.db')
#aquisição de um cursor
    cursor = conexao.cursor()
#execução de comandos SQL
#cursor.execute("instrução SQL")
    cursor.fetchall() #todos os registros retornados
#efetivação do comando (para atualizar)
    conexao.commit()
#fechamento do ponteiro e da conexão
    cursor.close()
    conexao.close()
#chamada da função
    print('Abrindo uma conexão de BD')
conectar_banco()
#encerrando
print('Encerrando a conexão')

