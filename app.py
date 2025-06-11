import tkinter as tk
from tkinter import messagebox, ttk
from typing import Self
from usuarioDAO import UsuarioDAO
from usuario import Usuario

class App:
    def __init__(self, root, tipo_usuario):
        self.tipo_usuario = tipo_usuario
        self.dao = UsuarioDAO()
        self.root = root
        self.root.title(f"AproximaTI - Área do {self.tipo_usuario.capitalize()}")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        # Define a cor do topo conforme o tipo de usuário
        cor_topo = "#3498db"  # azul padrão
        if self.tipo_usuario == "tecnico":
            cor_topo = "#27ae60"  # verde para técnico

        # Cabeçalho
        header_frame = tk.Frame(root, bg=cor_topo, height=80)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)
        
        tk.Label(header_frame, text=f"👤 Área do {self.tipo_usuario.capitalize()}", 
                font=("Arial", 18, "bold"), fg="white", bg=cor_topo).pack(pady=20)

        # Frame para abas/menu
        menu_frame = tk.Frame(root, bg="#e0e0e0", height=40)
        menu_frame.pack(fill="x")
        menu_frame.pack_propagate(False)

        # Botões do menu (simulando abas)
        tk.Button(menu_frame, text="📋 Meu Cadastro", bg="#d0d0d0", relief="flat", 
                 font=("Arial", 9), padx=15, pady=5).pack(side="left", padx=2, pady=5)
        
        if self.tipo_usuario == "cliente":
            tk.Button(menu_frame, text="🔍 Buscar Técnicos", bg="#e0e0e0", relief="flat", 
                     font=("Arial", 9), padx=15, pady=5).pack(side="left", padx=2, pady=5)
            tk.Button(menu_frame, text="⭐ Avaliar Técnico", bg="#e0e0e0", relief="flat", 
                     font=("Arial", 9), padx=15, pady=5).pack(side="left", padx=2, pady=5)

        # Frame principal com scroll
        main_frame = tk.Frame(root, bg="#f0f0f0")
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Frame do formulário de cadastro
        form_frame = tk.LabelFrame(main_frame, text=f"Cadastro do {self.tipo_usuario.capitalize()}", 
                                  font=("Arial", 12, "bold"), bg="#f0f0f0", padx=15, pady=10)
        form_frame.pack(fill="x", pady=10)

        # Campos do formulário em grid
        row = 0
        
        # Nome Completo
        tk.Label(form_frame, text="Nome Completo:", font=("Arial", 10), bg="#f0f0f0").grid(
            row=row, column=0, sticky="w", pady=5)
        self.entry_nome = tk.Entry(form_frame, width=50, font=("Arial", 10))
        self.entry_nome.grid(row=row, column=1, columnspan=2, sticky="ew", padx=(5, 0), pady=5)
        row += 1

        # Email
        tk.Label(form_frame, text="Email:", font=("Arial", 10), bg="#f0f0f0").grid(
            row=row, column=0, sticky="w", pady=5)
        self.entry_email = tk.Entry(form_frame, width=50, font=("Arial", 10))
        self.entry_email.grid(row=row, column=1, columnspan=2, sticky="ew", padx=(5, 0), pady=5)
        row += 1

        # Senha
        tk.Label(form_frame, text="Senha:", font=("Arial", 10), bg="#f0f0f0").grid(
            row=row, column=0, sticky="w", pady=5)
        self.entry_senha = tk.Entry(form_frame, width=50, font=("Arial", 10), show="*")
        self.entry_senha.grid(row=row, column=1, columnspan=2, sticky="ew", padx=(5, 0), pady=5)
        row += 1

        # Telefone
        tk.Label(form_frame, text="Telefone:", font=("Arial", 10), bg="#f0f0f0").grid(
            row=row, column=0, sticky="w", pady=5)
        self.entry_telefone = tk.Entry(form_frame, width=50, font=("Arial", 10))
        self.entry_telefone.grid(row=row, column=1, columnspan=2, sticky="ew", padx=(5, 0), pady=5)
        row += 1

        # Endereço
        tk.Label(form_frame, text="Endereço:", font=("Arial", 10), bg="#f0f0f0").grid(
            row=row, column=0, sticky="w", pady=5)
        self.entry_endereco = tk.Entry(form_frame, width=50, font=("Arial", 10))
        self.entry_endereco.grid(row=row, column=1, columnspan=2, sticky="ew", padx=(5, 0), pady=5)
        row += 1

        # Cidade e Estado na mesma linha
        tk.Label(form_frame, text="Cidade:", font=("Arial", 10), bg="#f0f0f0").grid(
            row=row, column=0, sticky="w", pady=5)
        self.entry_cidade = tk.Entry(form_frame, width=30, font=("Arial", 10))
        self.entry_cidade.grid(row=row, column=1, sticky="ew", padx=(5, 5), pady=5)
        
        tk.Label(form_frame, text="Estado:", font=("Arial", 10), bg="#f0f0f0").grid(
            row=row, column=2, sticky="w", padx=(10, 0), pady=5)
        self.entry_estado = tk.Entry(form_frame, width=5, font=("Arial", 10))
        self.entry_estado.grid(row=row, column=3, sticky="w", padx=(5, 0), pady=5)
        row += 1

        # ID para operações (oculto inicialmente)
        tk.Label(form_frame, text="ID (para atualizar/deletar):", font=("Arial", 10), bg="#f0f0f0").grid(
            row=row, column=0, sticky="w", pady=5)
        self.entry_id = tk.Entry(form_frame, width=10, font=("Arial", 10))
        self.entry_id.grid(row=row, column=1, sticky="w", padx=(5, 0), pady=5)
        row += 1

        # Configurar grid weights para responsividade
        form_frame.columnconfigure(1, weight=1)

        # Frame para botões
        btn_frame = tk.Frame(form_frame, bg="#f0f0f0")
        btn_frame.grid(row=row, column=0, columnspan=4, pady=15)

        # Botões de ação
        tk.Button(btn_frame, text="Cadastrar", bg="#3498db", fg="white", font=("Arial", 10, "bold"),
                 width=12, height=1, command=self.criar, relief="flat", cursor="hand2").pack(side="left", padx=5)
        
        tk.Button(btn_frame, text="Limpar", bg="#95a5a6", fg="white", font=("Arial", 10, "bold"),
                 width=12, height=1, command=self.limpar_campos, relief="flat", cursor="hand2").pack(side="left", padx=5)
        
        tk.Button(btn_frame, text="Atualizar", bg="#f39c12", fg="white", font=("Arial", 10, "bold"),
                 width=12, height=1, command=self.atualizar, relief="flat", cursor="hand2").pack(side="left", padx=5)
        
        tk.Button(btn_frame, text="Deletar", bg="#e74c3c", fg="white", font=("Arial", 10, "bold"),
                 width=12, height=1, command=self.deletar, relief="flat", cursor="hand2").pack(side="left", padx=5)
        
        tk.Button(btn_frame, text="Listar Todos", bg="#27ae60", fg="white", font=("Arial", 10, "bold"),
                 width=12, height=1, command=self.listar, relief="flat", cursor="hand2").pack(side="left", padx=5)

        # Área de resultado
        result_frame = tk.LabelFrame(main_frame, text="Usuários Cadastrados", 
                                   font=("Arial", 12, "bold"), bg="#f0f0f0", padx=15, pady=10)
        result_frame.pack(fill="both", expand=True, pady=10)

        # Text widget com scrollbar
        text_frame = tk.Frame(result_frame, bg="#f0f0f0")
        text_frame.pack(fill="both", expand=True)

        self.text_resultado = tk.Text(text_frame, height=8, font=("Arial", 10), wrap="word")
        scrollbar = tk.Scrollbar(text_frame, orient="vertical", command=self.text_resultado.yview)
        self.text_resultado.configure(yscrollcommand=scrollbar.set)
        
        self.text_resultado.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def criar(self):
        # Coleta todos os dados do formulário
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()
        senha = self.entry_senha.get().strip()
        telefone = self.entry_telefone.get().strip()
        endereco = self.entry_endereco.get().strip()
        cidade = self.entry_cidade.get().strip()
        estado = self.entry_estado.get().strip().upper()

        # Validação básica dos campos obrigatórios
        if not nome or not email or not senha:
            messagebox.showwarning("Erro!", "Nome, email e senha são obrigatórios!")
            return

        # Validação do estado (deve ter 2 caracteres)
        if estado and len(estado) != 2:
            messagebox.showwarning("Erro!", "Estado deve ter 2 letras (ex: SP, RJ)")
            return

        try:
            # Cria objeto usuario com todos os dados
            usuario = Usuario(nome=nome, email=email, senha=senha, tipo=self.tipo_usuario,
                            telefone=telefone, cidade=cidade, estado=estado)
            
            # Salva no banco de dados
            self.dao.criar(usuario)
            messagebox.showinfo("Sucesso!", f"{self.tipo_usuario.capitalize()} cadastrado com sucesso!")
            self.limpar_campos()
            
        except Exception as e:
            # Trata erros específicos
            if "Duplicate entry" in str(e):
                messagebox.showerror("Erro!", "Este email já está cadastrado!")
            else:
                messagebox.showerror("Erro!", f"Erro ao cadastrar: {str(e)}")

    def listar(self):
        # Busca todos os registros do banco
        registros = self.dao.listar()
        
        # Limpa a área de resultado
        self.text_resultado.delete("1.0", tk.END)
        
        if not registros:
            self.text_resultado.insert(tk.END, "Nenhum registro encontrado.\n")
            return
        
        # Exibe os registros formatados
        self.text_resultado.insert(tk.END, "=== USUÁRIOS CADASTRADOS ===\n\n")
        for r in registros:
            self.text_resultado.insert(tk.END, f"ID: {r[0]} | Nome: {r[1]} | Email: {r[2]}\n")
        self.text_resultado.insert(tk.END, f"\nTotal: {len(registros)} registros")

    def atualizar(self):
        # Coleta todos os dados incluindo ID
        id_usuario = self.entry_id.get().strip()
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()
        senha = self.entry_senha.get().strip()
        telefone = self.entry_telefone.get().strip()
        endereco = self.entry_endereco.get().strip()
        cidade = self.entry_cidade.get().strip()
        estado = self.entry_estado.get().strip().upper()

        # Validação dos campos obrigatórios
        if not id_usuario or not nome or not email or not senha:
            messagebox.showwarning("Erro!", "ID, nome, email e senha são obrigatórios para atualizar!")
            return

        # Validação do estado
        if estado and len(estado) != 2:
            messagebox.showwarning("Erro!", "Estado deve ter 2 letras (ex: SP, RJ)")
            return

        try:
            # Cria objeto usuario com ID para atualização
            usuario = Usuario(id=int(id_usuario), nome=nome, email=email, senha=senha, 
                            tipo=self.tipo_usuario, telefone=telefone, cidade=cidade, estado=estado)
            
            # Atualiza no banco
            self.dao.atualizar(usuario)
            messagebox.showinfo("Sucesso!", "Usuário atualizado com sucesso!")
            self.limpar_campos()
            
        except ValueError:
            messagebox.showerror("Erro!", "ID deve ser um número válido!")
        except Exception as e:
            if "Duplicate entry" in str(e):
                messagebox.showerror("Erro!", "Este email já está cadastrado!")
            else:
                messagebox.showerror("Erro!", f"Erro ao atualizar: {str(e)}")

    def deletar(self):
        # Coleta o ID para deletar
        id_usuario = self.entry_id.get().strip()
        
        if not id_usuario:
            messagebox.showwarning("Erro!", "Informe o ID do usuário para deletar!")
            return

        # Confirmação antes de deletar
        if messagebox.askyesno("Confirmar", f"Deseja realmente deletar o usuário ID {id_usuario}?"):
            try:
                self.dao.deletar(int(id_usuario))
                messagebox.showinfo("Sucesso!", "Usuário deletado com sucesso!")
                self.limpar_campos()
                
            except ValueError:
                messagebox.showerror("Erro!", "ID deve ser um número válido!")
            except Exception as e:
                messagebox.showerror("Erro!", f"Erro ao deletar: {str(e)}")

    def limpar_campos(self):
        # Limpa todos os campos do formulário
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)
        self.entry_endereco.delete(0, tk.END)
        self.entry_cidade.delete(0, tk.END)
        self.entry_estado.delete(0, tk.END)
        self.entry_id.delete(0, tk.END)
