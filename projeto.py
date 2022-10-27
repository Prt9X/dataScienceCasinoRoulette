
import mysql.connector
from mysql.connector import errorcode
import json
from datetime import date


class Connection():

	dbConnection=""

	def getFileJson(self, arquivo):
		with open(arquivo) as file: 
			arquivo = json.load(file)

		atividade = arquivo
		return atividade

	def db(self):
		dataConnection= self.getFileJson('dadosConexao.json')
		try:
			#print("Database connection made!")
			self.dbConnection = mysql.connector.connect(host='localhost', user= dataConnection['username'], password= dataConnection['password'], database= dataConnection['dbname'])
			return
		except mysql.connector.Error as error:
			if error.errno == errorcode.ER_BAD_DB_ERROR:
				print("Database doesn't exist")
			elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("User name or password is wrong")
			else:
				print(error)
		else:
			self.dbConnection.close()

    
	def dbClose(self):
		return self.dbConnection.close()

	
	

"""
connections= Connection()

#connections.db()

conexao= connections.dbConnection
cursor = conexao.cursor()

sql = "INSERT INTO logscasino (numero_aposta, valor_aposta, resultado) VALUES (%s, %s, %s)"
values = (20, 220, 0)
cursor.execute(sql, values)



cursor.close()
conexao.commit()
conexao.close()

"""