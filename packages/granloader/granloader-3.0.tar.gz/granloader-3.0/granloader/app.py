import os
import sys
import re
import subprocess
import threading
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from queue import Queue

from .utils import install_dependencies, get_video_id, start_download

class YouTubeDownloaderApp:
    def __init__(self, master):
        self.master = master
        master.title("Fast Downloads")
        master.geometry("400x500")
        master.configure(bg='#f5f5f7')

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.configure_styles()

        self.frame = ttk.Frame(master, style='Main.TFrame')
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.title_label = ttk.Label(self.frame, text="Fast Downloads", style='Title.TLabel')
        self.title_label.pack(pady=(0, 20))

        self.link_frame = ttk.Frame(self.frame, style='Link.TFrame')
        self.link_frame.pack(fill=tk.X, pady=(0, 20))

        self.link_entry = ttk.Entry(self.link_frame, style='Link.TEntry')
        self.link_entry.pack(side=tk.LEFT, expand=True, fill=tk.X)
        self.link_entry.insert(0, "Cole o link do YouTube aqui")
        self.link_entry.bind("<FocusIn>", self.clear_placeholder)
        self.link_entry.bind("<FocusOut>", self.restore_placeholder)

        self.button_frame = ttk.Frame(self.link_frame, style='Button.TFrame')
        self.button_frame.pack(side=tk.RIGHT, padx=(10, 0))

        self.download_button = tk.Button(self.button_frame, text="⬇", command=self.add_to_queue, 
                                         bg='#0071e3', fg='white', relief=tk.FLAT, 
                                         width=3, height=1)
        self.download_button.pack(expand=True, fill=tk.BOTH)
        self.download_button.bind("<Enter>", self.on_enter)
        self.download_button.bind("<Leave>", self.on_leave)

        self.queue_label = ttk.Label(self.frame, text="Fila de Downloads: 0", style='Info.TLabel')
        self.queue_label.pack(pady=(0, 10))

        self.info_frame = ttk.Frame(self.frame, style='Info.TFrame')
        self.info_frame.pack(fill=tk.X, pady=(0, 20))

        self.title_var = tk.StringVar()
        self.title_label = ttk.Label(self.info_frame, textvariable=self.title_var, style='Info.TLabel', wraplength=360)
        self.title_label.pack(anchor='w')

        self.resolution_var = tk.StringVar()
        self.resolution_label = ttk.Label(self.info_frame, textvariable=self.resolution_var, style='Info.TLabel')
        self.resolution_label.pack(anchor='w')

        self.status_var = tk.StringVar()
        self.status_label = ttk.Label(self.info_frame, textvariable=self.status_var, style='Info.TLabel')
        self.status_label.pack(anchor='w')

        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.frame, variable=self.progress_var, maximum=100, style='TProgressbar')
        self.progress_bar.pack(fill=tk.X, pady=(0, 10))

        self.eta_var = tk.StringVar()
        self.eta_label = ttk.Label(self.frame, textvariable=self.eta_var, style='Eta.TLabel')
        self.eta_label.pack(anchor='e')

        self.download_queue = Queue()
        self.is_downloading = False

    def configure_styles(self):
        self.style.configure('Main.TFrame', background='#f5f5f7')
        self.style.configure('Link.TFrame', background='#f5f5f7')
        self.style.configure('Info.TFrame', background='#f5f5f7')
        self.style.configure('Button.TFrame', background='#f5f5f7')
        
        self.style.configure('Title.TLabel', font=('SF Pro Display', 24, 'bold'), background='#f5f5f7', foreground='#1d1d1f')
        self.style.configure('Info.TLabel', font=('SF Pro Text', 12), background='#f5f5f7', foreground='#1d1d1f')
        self.style.configure('Eta.TLabel', font=('SF Pro Text', 10), background='#f5f5f7', foreground='#86868b')
        
        self.style.configure('Link.TEntry', font=('SF Pro Text', 12), padding=10, relief='flat', borderwidth=0)
        self.style.map('Link.TEntry', fieldbackground=[('focus', '#ffffff'), ('!focus', '#ffffff')])
        
        self.style.configure('TProgressbar', thickness=6, background='#0071e3', troughcolor='#e0e0e0', bordercolor='#f5f5f7', lightcolor='#0071e3', darkcolor='#0071e3')

    def on_enter(self, e):
        self.download_button['background'] = '#0077ED'

    def on_leave(self, e):
        self.download_button['background'] = '#0071e3'

    def clear_placeholder(self, event):
        if self.link_entry.get() == "Cole o link do YouTube aqui":
            self.link_entry.delete(0, tk.END)

    def restore_placeholder(self, event):
        if not self.link_entry.get():
            self.link_entry.insert(0, "Cole o link do YouTube aqui")

    def add_to_queue(self):
        link = self.link_entry.get()
        if link == "Cole o link do YouTube aqui":
            messagebox.showerror("Erro", "Por favor, insira um link do YouTube.")
            return

        if get_video_id(link):
            self.download_queue.put(link)
            self.queue_label.config(text=f"Fila de Downloads: {self.download_queue.qsize()}")
            self.link_entry.delete(0, tk.END)
            self.link_entry.insert(0, "Cole o link do YouTube aqui")
            if not self.is_downloading:
                self.process_queue()
        else:
            messagebox.showerror("Erro", "Link inválido. Por favor, insira um link válido do YouTube.")

    def process_queue(self):
        if not self.download_queue.empty() and not self.is_downloading:
            self.is_downloading = True
            link = self.download_queue.get()
            date_folder = datetime.now().strftime("%Y-%m-%d")
            folder_path = os.path.join(os.path.expanduser("~"), "Downloads", "FastDownloads", date_folder)
            os.makedirs(folder_path, exist_ok=True)
            
            self.progress_var.set(0)
            self.title_var.set("")
            self.resolution_var.set("")
            self.eta_var.set("")
            threading.Thread(target=self.download_thread, args=(link, folder_path), daemon=True).start()
        else:
            self.is_downloading = False

    def download_thread(self, link, folder_path):
        start_download(link, folder_path, self.status_var, self.progress_var, self.title_var, self.resolution_var, self.eta_var)
        self.master.after(0, self.download_complete)

    def download_complete(self):
        self.is_downloading = False
        self.queue_label.config(text=f"Fila de Downloads: {self.download_queue.qsize()}")
        self.process_queue()

def main():
    if not install_dependencies():
        print("Não foi possível encontrar as dependências necessárias. Por favor, execute o script setup_env.bat.")
        sys.exit(1)

    root = tk.Tk()
    app = YouTubeDownloaderApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
