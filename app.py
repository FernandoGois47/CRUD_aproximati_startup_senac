import tkinter as tk
from tkinter import messagebox, ttk
from typing import Self
from usuarioDAO import UsuarioDAO
from usuario import Usuario
from portfolioDAO import PortfolioDAO

class App:
    def __init__(self, root, tipo_usuario):
        self.tipo_usuario = tipo_usuario
        self.dao = UsuarioDAO()
        self.portfolio_dao = PortfolioDAO()
        self.root = root
        self.root.title(f"AproximaTI - Área do {self.tipo_usuario.capitalize()}")
        self.root.geometry("800x500")
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
        self.btn_cadastro = tk.Button(menu_frame, text="📋 Meu Cadastro", bg="#d0d0d0", relief="flat", 
                 font=("Arial", 9), padx=15, pady=5, command=self.mostrar_cadastro)
        self.btn_cadastro.pack(side="left", padx=2, pady=5)
        
        if self.tipo_usuario == "cliente":
            self.btn_buscar = tk.Button(menu_frame, text="🔍 Buscar Técnicos", bg="#e0e0e0", relief="flat", 
                     font=("Arial", 9), padx=15, pady=5, command=self.mostrar_busca_tecnicos)
            self.btn_buscar.pack(side="left", padx=2, pady=5)
            tk.Button(menu_frame, text="⭐ Avaliar Técnico", bg="#e0e0e0", relief="flat", 
                     font=("Arial", 9), padx=15, pady=5).pack(side="left", padx=2, pady=5)
        
        if self.tipo_usuario == "tecnico":
            self.btn_portfolio = tk.Button(menu_frame, text="📁 Meu Portfólio", bg="#e0e0e0", relief="flat", 
                     font=("Arial", 9), padx=15, pady=5, command=self.mostrar_portfolio)
            self.btn_portfolio.pack(side="left", padx=2, pady=5)
            tk.Button(menu_frame, text="⭐ Minhas Avaliações", bg="#e0e0e0", relief="flat", 
                     font=("Arial", 9), padx=15, pady=5).pack(side="left", padx=2, pady=5)

        # Frame principal
        self.main_frame = tk.Frame(root, bg="#f0f0f0")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Criar os frames para as diferentes seções
        self.criar_frame_cadastro()
        if self.tipo_usuario == "cliente":
            self.criar_frame_busca_tecnicos()
        if self.tipo_usuario == "tecnico":
            self.criar_frame_portfolio()
        
        # Mostrar a seção de cadastro inicialmente
        self.mostrar_cadastro()

    def criar_frame_cadastro(self):
        # Frame do formulário de cadastro
        self.frame_cadastro = tk.Frame(self.main_frame, bg="#f0f0f0")
        
        form_frame = tk.LabelFrame(self.frame_cadastro, text=f"Cadastro do {self.tipo_usuario.capitalize()}", 
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

    def criar_frame_busca_tecnicos(self):
        # Frame para busca de técnicos
        self.frame_busca = tk.Frame(self.main_frame, bg="#f0f0f0")
        
        # Seção de filtros
        filtros_frame = tk.LabelFrame(self.frame_busca, text="Filtros de Busca", 
                                     font=("Arial", 12, "bold"), bg="#f0f0f0", padx=15, pady=10)
        filtros_frame.pack(fill="x", pady=10)
        
        # Filtro por cidade
        tk.Label(filtros_frame, text="Cidade:", font=("Arial", 10), bg="#f0f0f0").grid(
            row=0, column=0, sticky="w", pady=5, padx=5)
        self.entry_filtro_cidade = tk.Entry(filtros_frame, width=20, font=("Arial", 10))
        self.entry_filtro_cidade.grid(row=0, column=1, padx=5, pady=5)
        
        # Filtro por estado
        tk.Label(filtros_frame, text="Estado:", font=("Arial", 10), bg="#f0f0f0").grid(
            row=0, column=2, sticky="w", pady=5, padx=5)
        self.entry_filtro_estado = tk.Entry(filtros_frame, width=5, font=("Arial", 10))
        self.entry_filtro_estado.grid(row=0, column=3, padx=5, pady=5)
        
        # Botão de buscar
        tk.Button(filtros_frame, text="🔍 Buscar Técnicos", bg="#27ae60", fg="white", 
                 font=("Arial", 10, "bold"), width=15, height=1, command=self.buscar_tecnicos,
                 relief="flat", cursor="hand2").grid(row=0, column=4, padx=15, pady=5)
        
        tk.Button(filtros_frame, text="Limpar Filtros", bg="#95a5a6", fg="white", 
                 font=("Arial", 10, "bold"), width=12, height=1, command=self.limpar_filtros,
                 relief="flat", cursor="hand2").grid(row=0, column=5, padx=5, pady=5)
        
        # Área de resultados dos técnicos
        result_frame = tk.LabelFrame(self.frame_busca, text="Técnicos Disponíveis", 
                                   font=("Arial", 12, "bold"), bg="#f0f0f0", padx=15, pady=10)
        result_frame.pack(fill="both", expand=True, pady=10)
        
        # Text widget com scrollbar para mostrar técnicos
        text_frame = tk.Frame(result_frame, bg="#f0f0f0")
        text_frame.pack(fill="both", expand=True)
        
        self.text_tecnicos = tk.Text(text_frame, height=12, font=("Arial", 10), wrap="word")
        scrollbar_tecnicos = tk.Scrollbar(text_frame, orient="vertical", command=self.text_tecnicos.yview)
        self.text_tecnicos.configure(yscrollcommand=scrollbar_tecnicos.set)
        
        self.text_tecnicos.pack(side="left", fill="both", expand=True)
        scrollbar_tecnicos.pack(side="right", fill="y")

    def criar_frame_portfolio(self):
        # Frame para o portfólio do técnico
        self.frame_portfolio = tk.Frame(self.main_frame, bg="#f0f0f0")
        
        # Seção do portfólio
        portfolio_frame = tk.LabelFrame(self.frame_portfolio, text="Descrição do Portfólio", 
                                       font=("Arial", 12, "bold"), bg="#f0f0f0", padx=25, pady=10)
        portfolio_frame.pack(fill="both", expand=True, pady=10)
        
        # ID do técnico
        tk.Label(portfolio_frame, text="ID do Técnico:", font=("Arial", 10), bg="#f0f0f0").pack(anchor="w", pady=5)
        self.entry_tecnico_id = tk.Entry(portfolio_frame, width=20, font=("Arial", 10))
        self.entry_tecnico_id.pack(anchor="w", pady=5)
        
        # Descrição do portfólio
        tk.Label(portfolio_frame, text="Descrição do Portfólio:", font=("Arial", 10), bg="#f0f0f0").pack(anchor="w", pady=(15, 5))
        
        # Frame para o text widget com scrollbar
        text_frame = tk.Frame(portfolio_frame, bg="#f0f0f0")
        text_frame.pack(fill="both", expand=True, pady=5)
        
        self.text_portfolio = tk.Text(text_frame, height=5, font=("Arial", 10), wrap="word")
        scrollbar_portfolio = tk.Scrollbar(text_frame, orient="vertical", command=self.text_portfolio.yview)
        self.text_portfolio.configure(yscrollcommand=scrollbar_portfolio.set)
        
        self.text_portfolio.pack(side="left", fill="both", expand=True)
        scrollbar_portfolio.pack(side="right", fill="y")
        
        # Frame para botões
        btn_frame = tk.Frame(portfolio_frame, bg="#f0f0f0")
        btn_frame.pack(pady=15)
        
        # Botões
        tk.Button(btn_frame, text="💾 Salvar Portfólio", bg="#3498db", fg="white", 
                 font=("Arial", 10, "bold"), width=15, height=1, command=self.salvar_portfolio,
                 relief="flat", cursor="hand2").pack(side="left", padx=5)
        
        tk.Button(btn_frame, text="📄 Carregar Portfólio", bg="#9b59b6", fg="white", 
                 font=("Arial", 10, "bold"), width=15, height=1, command=self.carregar_portfolio,
                 relief="flat", cursor="hand2").pack(side="left", padx=5)

    def mostrar_cadastro(self):
        # Esconde todos os frames
        if hasattr(self, 'frame_busca'):
            self.frame_busca.pack_forget()
        if hasattr(self, 'frame_portfolio'):
            self.frame_portfolio.pack_forget()
        
        # Mostra o frame de cadastro
        self.frame_cadastro.pack(fill="both", expand=True)
        
        # Atualiza cores dos botões
        self.btn_cadastro.configure(bg="#d0d0d0")
        if hasattr(self, 'btn_buscar'):
            self.btn_buscar.configure(bg="#e0e0e0")
        if hasattr(self, 'btn_portfolio'):
            self.btn_portfolio.configure(bg="#e0e0e0")

    def mostrar_busca_tecnicos(self):
        # Esconde todos os frames
        self.frame_cadastro.pack_forget()
        
        # Mostra o frame de busca
        self.frame_busca.pack(fill="both", expand=True)
        
        # Atualiza cores dos botões
        self.btn_cadastro.configure(bg="#e0e0e0")
        self.btn_buscar.configure(bg="#d0d0d0")
        
        # Carrega todos os técnicos automaticamente
        self.buscar_tecnicos()

    def mostrar_portfolio(self):
        # Esconde todos os frames
        self.frame_cadastro.pack_forget()
        
        # Mostra o frame de portfólio
        self.frame_portfolio.pack(fill="both", expand=True)
        
        # Atualiza cores dos botões
        self.btn_cadastro.configure(bg="#e0e0e0")
        self.btn_portfolio.configure(bg="#d0d0d0")

    def salvar_portfolio(self):
        tecnico_id = self.entry_tecnico_id.get().strip()
        descricao = self.text_portfolio.get("1.0", tk.END).strip()
        
        if not tecnico_id:
            messagebox.showwarning("Erro!", "Informe o ID do técnico!")
            return
            
        if not descricao:
            messagebox.showwarning("Erro!", "Digite sua experiência antes de salvar!")
            return
        
        try:
            self.portfolio_dao.salvar(int(tecnico_id), descricao)
            messagebox.showinfo("Sucesso!", "Portfólio salvo com sucesso!")
        except ValueError:
            messagebox.showerror("Erro!", "ID deve ser um número válido!")
        except Exception as e:
            messagebox.showerror("Erro!", f"Erro ao salvar portfólio: {str(e)}")

    def carregar_portfolio(self):
        tecnico_id = self.entry_tecnico_id.get().strip()
        
        if not tecnico_id:
            messagebox.showwarning("Erro!", "Informe o ID do técnico!")
            return
        
        try:
            portfolios = self.portfolio_dao.carregar_por_tecnico(int(tecnico_id))
            
            # Limpa o texto atual
            self.text_portfolio.delete("1.0", tk.END)
            
            if portfolios:
                # Carrega o portfólio mais recente
                self.text_portfolio.insert(tk.END, portfolios[0][0])
                messagebox.showinfo("Sucesso!", "Portfólio carregado com sucesso!")
            else:
                messagebox.showinfo("Informação", "Nenhum portfólio encontrado para este técnico.")
                
        except ValueError:
            messagebox.showerror("Erro!", "ID deve ser um número válido!")
        except Exception as e:
            messagebox.showerror("Erro!", f"Erro ao carregar portfólio: {str(e)}")

    def buscar_tecnicos(self):
        cidade_filtro = self.entry_filtro_cidade.get().strip()
        estado_filtro = self.entry_filtro_estado.get().strip().upper()
        
        # Busca técnicos no banco
        tecnicos = self.dao.buscar_tecnicos(cidade_filtro, estado_filtro)
        
        # Limpa a área de resultado
        self.text_tecnicos.delete("1.0", tk.END)
        
        if not tecnicos:
            self.text_tecnicos.insert(tk.END, "Nenhum técnico encontrado com os filtros informados.\n")
            return
        
        # Exibe os técnicos formatados
        self.text_tecnicos.insert(tk.END, "=== TÉCNICOS DISPONÍVEIS ===\n\n")
        for tecnico in tecnicos:
            self.text_tecnicos.insert(tk.END, f"📧 {tecnico[1]} - {tecnico[2]}\n")
            if tecnico[3]:  # telefone
                self.text_tecnicos.insert(tk.END, f"📞 {tecnico[3]}\n")
            if tecnico[4] and tecnico[5]:  # cidade e estado
                self.text_tecnicos.insert(tk.END, f"📍 {tecnico[4]}, {tecnico[5]}\n")
            self.text_tecnicos.insert(tk.END, "-" * 50 + "\n\n")
        
        self.text_tecnicos.insert(tk.END, f"Total: {len(tecnicos)} técnicos encontrados")

    def limpar_filtros(self):
        self.entry_filtro_cidade.delete(0, tk.END)
        self.entry_filtro_estado.delete(0, tk.END)
        self.buscar_tecnicos()  # Recarrega todos os técnicos

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
            messagebox.showwarning("Erro!", "Estado deve ter 2 letras (ex: PR, SC)")
            return

        try:
            # Cria objeto usuario com todos os dados
            usuario = Usuario(nome=nome, email=email, senha=senha, tipo=self.tipo_usuario,
                            telefone=telefone, cidade=cidade, estado=estado)

            # Salva no banco de dados e recupera o ID
            id_gerado = self.dao.criar(usuario)

            # Mostra mensagem com o ID
            messagebox.showinfo("Sucesso!", f"{self.tipo_usuario.capitalize()} cadastrado com sucesso!\nID: {id_gerado}")

            
        except Exception as e:
            # Trata erros específicos
            if "Duplicate entry" in str(e):
                messagebox.showerror("Erro!", "Este email já está cadastrado!")
            else:
                messagebox.showerror("Erro!", f"Erro ao cadastrar: {str(e)}")

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
