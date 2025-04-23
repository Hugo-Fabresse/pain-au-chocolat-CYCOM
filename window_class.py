import tkinter as tk
from tkinter import messagebox

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Audit Web")
    
    def set_main(self):
        tk.Label(self.root, text="URL à auditer:").pack(pady=5)
        self.entry_url = tk.Entry(self.root, width=50)
        self.entry_url.pack(padx=10, pady=5)

        tk.Button(self.root, text="Lancer l'audit", command=self.launch_audit).pack(pady=10)
    
    def launch_audit(self):
        self.url = self.entry_url.get()
        if self.url:
            messagebox.showinfo("Audit", f"Lancement de l'audit sur : {self.url}")
        else:
            messagebox.showerror("Erreur", "Merci d’entrer une URL valide.")