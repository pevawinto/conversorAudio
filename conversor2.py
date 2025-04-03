import os
import tkinter as tk
from tkinter import filedialog, messagebox
from ttkbootstrap import Style
from ttkbootstrap.widgets import Progressbar
from tkinter import ttk
from pydub import AudioSegment
from threading import Thread
import sys

# Descobrir o caminho do FFmpeg dentro da pasta do executável
if getattr(sys, 'frozen', False):  # Quando rodando como .exe
    ffmpeg_path = os.path.join(sys._MEIPASS, "ffmpeg_bin", "ffmpeg.exe")
else:  # Quando rodando como script normal
    ffmpeg_path = os.path.join(os.path.dirname(__file__), "ffmpeg_bin", "ffmpeg.exe")

AudioSegment.converter = ffmpeg_path
# Formatos suportados
FORMATOS = ["mp3", "wav", "flac", "ogg", "aac"]

class ConversorAudio:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Áudio by Pev")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        
        # Aplicando tema moderno
        self.style = Style(theme="flatly")
        
        # Rótulo de instrução
        tk.Label(root, text="Escolha seu arquivo:", font=("Arial", 12)).pack(pady=10)
        
        # Botão para selecionar um arquivo de áudio
        self.botao_arquivo = ttk.Button(root, text="Selecionar Arquivo", command=self.selecionar_arquivo)
        self.botao_arquivo.pack()
        
        # Label para exibir o nome do arquivo selecionado
        self.label_arquivo = tk.Label(root, text="", wraplength=300, fg="blue")
        self.label_arquivo.pack(pady=5)
        
        # Botão para selecionar pasta de destino
        self.botao_pasta = ttk.Button(root, text="Selecionar Pasta de Destino", command=self.selecionar_pasta)
        self.botao_pasta.pack()
        
        # Label para exibir a pasta selecionada
        self.label_pasta = tk.Label(root, text="", wraplength=300, fg="green")
        self.label_pasta.pack(pady=5)
        
        # Rótulo para escolher o formato de saída
        tk.Label(root, text="Formato de saída:", font=("Arial", 12)).pack()
        
        # Menu dropdown para escolher o formato de saída
        self.formato_var = tk.StringVar(value=FORMATOS[0])
        self.dropdown = ttk.Combobox(root, textvariable=self.formato_var, values=FORMATOS, state="readonly")
        self.dropdown.pack()
        
        # Botão de conversão
        self.botao_converter = ttk.Button(root, text="Converter", command=self.converter_audio)
        self.botao_converter.pack(pady=10)
        
        # Barra de progresso
        self.progress = Progressbar(root, mode="determinate", length=250)
        self.progress.pack(pady=10)
    
    def selecionar_arquivo(self):
        arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de áudio", "*.mp3 *.wav *.flac *.ogg *.aac")])
        if arquivo:
            self.arquivo_selecionado = arquivo
            self.label_arquivo.config(text=os.path.basename(arquivo))
    
    def selecionar_pasta(self):
        pasta = filedialog.askdirectory()
        if pasta:
            self.pasta_destino = pasta
            self.label_pasta.config(text=pasta)
    
    def converter_audio(self):
        if not hasattr(self, "arquivo_selecionado"):
            messagebox.showerror("Erro", "Nenhum arquivo selecionado!")
            return
        
        if not hasattr(self, "pasta_destino"):
            messagebox.showerror("Erro", "Nenhuma pasta de destino selecionada!")
            return
        
        formato_saida = self.formato_var.get()
        self.progress.start()
        
        Thread(target=self.processar_conversao, args=(self.arquivo_selecionado, self.pasta_destino, formato_saida)).start()
    
    def processar_conversao(self, arquivo, pasta_destino, formato_saida):
        try:
            audio = AudioSegment.from_file(arquivo)
            nome_arquivo = os.path.splitext(os.path.basename(arquivo))[0] + f".{formato_saida}"
            caminho_saida = os.path.join(pasta_destino, nome_arquivo)
            audio.export(caminho_saida, format=formato_saida)
            messagebox.showinfo("Sucesso", f"Arquivo convertido para {formato_saida} e salvo em:\n{caminho_saida}")
        except Exception as e:
            messagebox.showerror("Erro na conversão", str(e))
        finally:
            self.progress.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = ConversorAudio(root)
    root.mainloop()
