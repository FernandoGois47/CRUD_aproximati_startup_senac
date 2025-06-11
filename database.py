import mysql.connector

class Database:
    @staticmethod
    def conectar():
        try:
            return mysql.connector.connect(
                host="localhost",
                user="root",  # Altere para seu usuário MySQL
                password="",  # Altere para sua senha MySQL
                database="aproximati"
            )
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao banco: {e}")
            raise
