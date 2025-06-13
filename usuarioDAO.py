from database import Database
from usuario import Usuario

class UsuarioDAO:
    def criar(self, usuario: Usuario):
        try:
            conn = Database.conectar()
            cursor = conn.cursor()
            # SQL para inserir usuário com todos os campos
            sql = """
            INSERT INTO usuarios (nome, email, senha, tipo, telefone, cidade, estado)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                usuario.nome,
                usuario.email,
                usuario.senha,
                usuario.tipo,
                usuario.telefone or "",  # Se vazio, insere string vazia
                usuario.cidade or "",
                usuario.estado or ""
            )
            cursor.execute(sql, valores)
            conn.commit()
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")
            raise  # Repassa o erro para a interface tratar
        finally:
            # Sempre fecha conexão
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def listar(self):
        try:
            conn = Database.conectar()
            cursor = conn.cursor()
            # Busca apenas os campos principais para listagem
            cursor.execute("SELECT id, nome, email FROM usuarios ORDER BY nome")
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Erro ao listar usuários: {e}")
            return []  # Retorna lista vazia em caso de erro
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def buscar_tecnicos(self, cidade_filtro="", estado_filtro=""):
        try:
            conn = Database.conectar()
            cursor = conn.cursor()
            
            # SQL base para buscar apenas técnicos
            sql = "SELECT id, nome, email, telefone, cidade, estado FROM usuarios WHERE tipo = 'tecnico'"
            valores = []
            
            # Adiciona filtros se informados
            if cidade_filtro:
                sql += " AND cidade LIKE %s"
                valores.append(f"%{cidade_filtro}%")
            
            if estado_filtro:
                sql += " AND estado = %s"
                valores.append(estado_filtro)
            
            sql += " ORDER BY nome"
            
            cursor.execute(sql, valores)
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Erro ao buscar técnicos: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def atualizar(self, usuario: Usuario):
        try:
            conn = Database.conectar()
            cursor = conn.cursor()
            # SQL para atualizar todos os campos editáveis
            sql = """
            UPDATE usuarios SET nome=%s, email=%s, senha=%s, tipo=%s, telefone=%s, cidade=%s, estado=%s 
            WHERE id=%s
            """
            valores = (
                usuario.nome,
                usuario.email,
                usuario.senha,
                usuario.tipo,
                usuario.telefone or "",
                usuario.cidade or "",
                usuario.estado or "",
                usuario.id
            )
            cursor.execute(sql, valores)
            conn.commit()
            
            # Verifica se algum registro foi afetado
            if cursor.rowcount == 0:
                raise Exception("Usuário não encontrado com este ID")
                
        except Exception as e:
            print(f"Erro ao atualizar usuário: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def deletar(self, id_usuario):
        try:
            conn = Database.conectar()
            cursor = conn.cursor()
            # Deleta usuário pelo ID
            cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_usuario,))
            conn.commit()
            
            # Verifica se algum registro foi deletado
            if cursor.rowcount == 0:
                raise Exception("Usuário não encontrado com este ID")
                
        except Exception as e:
            print(f"Erro ao deletar usuário: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
