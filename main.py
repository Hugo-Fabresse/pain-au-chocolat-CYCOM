#! /usr/bin/env python3
import tkinter as tk
from tkinter import messagebox

def lancer_audit():
    url = entry_url.get()
    if url:
        messagebox.showinfo("Audit", f"Lancement de l'audit sur : {url}")
    else:
        messagebox.showerror("Erreur", "Merci d’entrer une URL valide.")

root = tk.Tk()
root.title("Audit Web")

tk.Label(root, text="URL à auditer:").pack(pady=5)

entry_url = tk.Entry(root, width=50)
entry_url.pack(padx=10, pady=5)

tk.Button(root, text="Lancer l'audit", command=lancer_audit).pack(pady=10)

root.mainloop()
