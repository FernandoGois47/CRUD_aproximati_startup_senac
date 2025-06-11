import tkinter as tk
from tela_usuario import escolher_usuario

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    root.protocol("WM_DELETE_WINDOW", root.quit)  # Força saída completa
    escolher_usuario(root)
    root.mainloop()
    root.destroy()  # Garante fechamento da janela
