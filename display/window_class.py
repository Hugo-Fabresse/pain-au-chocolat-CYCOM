from urllib.parse import urlparse
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import requests

class Window:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.title("Audit Web")
        self.center_window()
        self.root.resizable(False, False)

        self.url = ""
        self.result = ""

        self.set_ask()

    def set_ask(self):
        ctk.CTkLabel(self.root, text="🌐 URL à auditer :", font=("Helvetica", 14)).pack(pady=10)

        self.entry_url = ctk.CTkEntry(self.root, width=300, placeholder_text="Ex: https://example.com")
        self.entry_url.pack(pady=10)

        self.entry_url.bind("<Return>", lambda event: self.launch_audit())
        ctk.CTkButton(self.root, text="🚀 Lancer l'audit", command=self.launch_audit).pack(pady=20)

    def launch_audit(self):
        self.result = ""
        self.url = self.entry_url.get()

        if self.url:
            if not self.url.startswith(("http://", "https://")):
                messagebox.showerror("Erreur", "L'URL doit commencer par http:// ou https://")
                return
            try:
                response = requests.get(self.url, timeout=3)
                if response.status_code == 200:
                    messagebox.showinfo("Audit", f"Lancement de l'audit sur : {self.url}")
                    self.display_error()
                else:
                    messagebox.showerror("Erreur", f"Site injoignable (code {response.status_code})")
            except requests.RequestException as e:
                messagebox.showerror("Erreur", f"URL invalide ou inaccessible.\n\nDétail : {e}")
        else:
            messagebox.showerror("Erreur", "Veuillez rentrer une URL.")

    def run(self):
        self.root.mainloop()

    def center_window(self, width=400, height=200):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - ((height // 2) * 2)

        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def display_error(self):
        self.root.resizable(True, True)

        if hasattr(self, "textbox"):
            self.textbox.delete("1.0", "end")
            self.textbox.insert("1.0", self.result)
            return

        self.text_frame = ctk.CTkFrame(self.root)
        self.text_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.textbox = ctk.CTkTextbox(self.text_frame, wrap="word", font=("Consolas", 12))
        self.textbox.pack(fill="both", expand=True, padx=5, pady=5)

        self.textbox.insert("1.0", self.result)
        self.textbox.configure(state="normal")

        self.center_window(height=400)



