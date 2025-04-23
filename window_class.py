import customtkinter as ctk
from tkinter import messagebox
import requests

class Window:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.title("Audit Web")
        self.root.geometry("400x200")
        self.root.resizable(False, False)

        self.url = ""

        self.set_ask()

    def set_ask(self):
        ctk.CTkLabel(self.root, text="🌐 URL à auditer :", font=("Helvetica", 14)).pack(pady=10)

        self.entry_url = ctk.CTkEntry(self.root, width=300, placeholder_text="Ex: https://example.com")
        self.entry_url.pack(pady=10)

        ctk.CTkButton(self.root, text="🚀 Lancer l'audit", command=self.launch_audit).pack(pady=20)

    def launch_audit(self):
        self.url = self.entry_url.get()

        if self.url:
            try:
                response = requests.get(self.url, timeout=3)
                if response.status_code == 200:
                    messagebox.showinfo("Audit", f"Lancement de l'audit sur : {self.url}")
                else:
                    messagebox.showerror("Erreur", f"Site injoignable (code {response.status_code})")
            except requests.RequestException as e:
                messagebox.showerror("Erreur", f"URL invalide ou inaccessible.\n\nDétail : {e}")
        else:
            messagebox.showerror("Erreur", "Veuillez rentrer une URL.")

    def run(self):
        self.root.mainloop()
