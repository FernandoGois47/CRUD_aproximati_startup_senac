from database import Database

class PortfolioDAO:
    def salvar(self, tecnico_id, descricao):
        conn = Database.conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO portfolio (tecnico_id, descricao) VALUES (%s, %s)"
        cursor.execute(sql, (tecnico_id, descricao))
        conn.commit()
        cursor.close()
        conn.close()

    def carregar_por_tecnico(self, tecnico_id):
        conn = Database.conectar()
        cursor = conn.cursor()
        sql = "SELECT descricao FROM portfolio WHERE tecnico_id = %s ORDER BY data_envio DESC"
        cursor.execute(sql, (tecnico_id,))
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultados
