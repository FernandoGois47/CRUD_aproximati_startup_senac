import tkinter as tk
from app import App

def escolher_usuario(root_principal):
    escolha = tk.Toplevel(root_principal)
    escolha.title("AproximaTI - Sistema de Conectividade")
    escolha.geometry("500x400")
    escolha.configure(bg="#2c3e50")
    escolha.resizable(False, False)
    
    # Quando fechar a janela de escolha, fecha tudo
    escolha.protocol("WM_DELETE_WINDOW", root_principal.quit)

    def abrir_cliente():
        escolha.destroy()
        abrir_crud("cliente", root_principal)

    def abrir_tecnico():
        escolha.destroy()
        abrir_crud("tecnico", root_principal)

    # Ícone e título
    frame_header = tk.Frame(escolha, bg="#2c3e50")
    frame_header.pack(pady=40)
    
    tk.Label(frame_header, text="🔧 AproximaTI", font=("Arial", 28, "bold"), 
             fg="white", bg="#2c3e50").pack()
    
    tk.Label(frame_header, text="Conectando Clientes e Técnicos de TI", 
             font=("Arial", 14), fg="#bdc3c7", bg="#2c3e50").pack(pady=(10, 0))

    # Frame para botões
    frame_botoes = tk.Frame(escolha, bg="#2c3e50")
    frame_botoes.pack(pady=5)

    # Botão Cliente
    btn_cliente = tk.Button(frame_botoes, text="👤 Sou Cliente\n(Buscar Técnicos)", 
                           font=("Arial", 16, "bold"), fg="white", bg="#3498db",
                           width=20, height=3, command=abrir_cliente,
                           relief="flat", cursor="hand2")
    btn_cliente.pack(pady=10)

    # Botão Técnico
    btn_tecnico = tk.Button(frame_botoes, text="🛠️ Sou Técnico\n(Oferecer Serviços)", 
                           font=("Arial", 16, "bold"), fg="white", bg="#27ae60",
                           width=20, height=3, command=abrir_tecnico,
                           relief="flat", cursor="hand2")
    btn_tecnico.pack(pady=10)

def abrir_crud(tipo_usuario, root_principal):
    crud_window = tk.Toplevel(root_principal)
    # Quando fechar a janela do CRUD, volta para escolha
    crud_window.protocol("WM_DELETE_WINDOW", lambda: [crud_window.destroy(), escolher_usuario(root_principal)])
    App(crud_window, tipo_usuario)
