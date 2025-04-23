#! /usr/bin/env python3

import tkinter as tk
from tkinter import messagebox
from window_class import Window

def main():
    window = Window()
    window.set_main()
    window.root.mainloop()

if __name__ == "__main__":
    main()