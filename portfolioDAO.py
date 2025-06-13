# from database import Database

# class PortfolioDAO:
#     def salvar(self, id_tecnico, descricao):
#         conn = Database.conectar()
#         cursor = conn.cursor()
#         sql = "INSERT INTO portfolio (id_tecnico, descricao) VALUES (%s, %s)"
#         cursor.execute(sql, (id_tecnico, descricao))
#         conn.commit()
#         cursor.close()
#         conn.close()

#     def carregar_por_tecnico(self, id_tecnico):
#         conn = Database.conectar()
#         cursor = conn.cursor()
#         sql = "SELECT descricao FROM portfolio WHERE id_tecnico = %s ORDER BY data_envio DESC"
#         cursor.execute(sql, (id_tecnico,))
#         resultados = cursor.fetchall()
#         cursor.close()
#         conn.close()
#         return resultados
