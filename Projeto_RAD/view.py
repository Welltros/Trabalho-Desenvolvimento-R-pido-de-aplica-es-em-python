# Importando banco de dados
import sqlite3 as lite
#Criando conexão  com o banco
con = lite.connect('dados.db')

#CRUD

#Inserir dado no banco
def inserir_form(i):
   with con:
    cur = con.cursor()
    query = "INSERT INTO inventario(nome,local, descricao, marca, data_da_compra,valor_da_compra, serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
    cur.execute(query,i)    #Executa a query que salva os valores no banco de dados na tabela iventario

atualizar_dados = ['vaso','cozinha', 'vaso que comprei ao lado','Marca chinesa','27/08/2024','100','seriexxccsx','c:imagens',1]

#Atualizar dado no banco
def atualizar_form(i):
  with con:
    cur = con.cursor()
    query = "UPDATE inventario SET nome=?,local=?, descricao=?, marca=?, data_da_compra=?,valor_da_compra=?, serie=?, imagem=? WHERE id=? "
    cur.execute(query,i)   

#Apagar dados no banco
def deletar_form(i):
  with con:
    cur = con.cursor()
    query = "DELETE FROM inventario WHERE id=?" 
    cur.execute(query,i)

#Ver dados no banco
def ver_form():
  ver_dados =[]
  with con:
    cur = con.cursor()
    query = "SELECT * FROM inventario" #Seleciona tudo da tabela inventario
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
      ver_dados.append(row)
  return ver_dados



#Ver dados individual no banco
def ver_item(id):
  ver_dados_inidividual =[]
  with con:
    cur = con.cursor()
    query = "SELECT * FROM inventario Where id=?" 
    cur.execute(query,id)

    rows = cur.fetchall()
    for row in rows:
      ver_dados_inidividual.append(row)
  print(ver_form)
